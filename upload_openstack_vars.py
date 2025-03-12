import requests
import yaml
import os
import sys

# === KONFIGURERA DITT TERRAFORM CLOUD ACCOUNT ===
TFC_ORG = "OpenSTack-Cluera-kna1"  # Byt till din Terraform Cloud-organisation
TFC_WORKSPACE = "Terraform-OpenStack-Docker"  # Byt till ditt workspace
TFC_API_TOKEN = os.getenv("TFC_API_TOKEN")  # Terraform Cloud API Token

# === FILSÖKVÄG TILL clouds.yaml ===
CLOUDS_FILE = os.path.expanduser("~/.config/openstack/clouds.yaml")

# === LÄS IN credentials från clouds.yaml ===
def load_cloud_config(cloud_name):
    """Läser in OpenStack `clouds.yaml` och hämtar auth-info för `cloud_name`."""
    if not os.path.exists(CLOUDS_FILE):
        print(f"❌ Filen {CLOUDS_FILE} hittades inte!")
        sys.exit(1)

    with open(CLOUDS_FILE, "r") as file:
        clouds = yaml.safe_load(file)

    if "clouds" not in clouds or cloud_name not in clouds["clouds"]:
        print(f"❌ Cloud '{cloud_name}' hittades inte i clouds.yaml!")
        sys.exit(1)

    return clouds["clouds"][cloud_name]

# === KONVERTERA OPENSTACK-CONFIG TILL MILJÖVARIABLER ===
def convert_to_env_vars(cloud_config):
    """Konverterar cloud-konfigurationen till Terraform Cloud-miljövariabler."""
    return {
        "OS_AUTH_URL": cloud_config["auth"]["auth_url"],
        "OS_USERNAME": cloud_config["auth"]["username"],
        "OS_PASSWORD": cloud_config["auth"]["password"],  # OBS! Märks som sensitive i TFC
        "OS_PROJECT_NAME": cloud_config["auth"]["project_name"],
        "OS_USER_DOMAIN_NAME": cloud_config["auth"].get("user_domain_name", "Default"),
        "OS_PROJECT_DOMAIN_NAME": cloud_config["auth"].get("project_domain_name", "Default"),
         "OS_REGION_NAME": cloud_config["region_name"], 
    }

# === HÄMTA WORKSPACE ID ===
def get_workspace_id():
    """Hämtar workspace-ID från Terraform Cloud"""
    workspace_url = f"https://app.terraform.io/api/v2/organizations/{TFC_ORG}/workspaces/{TFC_WORKSPACE}"
    headers = {"Authorization": f"Bearer {TFC_API_TOKEN}"}
    response = requests.get(workspace_url, headers=headers)

    if response.status_code == 200:
        return response.json()["data"]["id"]
    else:
        print(f"❌ Misslyckades att hämta workspace ID: {response.text}")
        sys.exit(1)

# === LÄGG TILL VARIABLER I TERRAFORM CLOUD ===
def upload_to_terraform_cloud(variables):
    """Laddar upp OpenStack-miljövariabler till Terraform Cloud workspace."""
    workspace_id = get_workspace_id()
    api_url = f"https://app.terraform.io/api/v2/workspaces/{workspace_id}/vars"

    headers = {
        "Authorization": f"Bearer {TFC_API_TOKEN}",
        "Content-Type": "application/vnd.api+json",
    }

    for key, value in variables.items():
        data = {
            "data": {
                "type": "vars",
                "attributes": {
                    "key": key,
                    "value": value,
                    "category": "env",
                    "sensitive": True if key == "OS_PASSWORD" else False
                }
            }
        }

        response = requests.post(api_url, json=data, headers=headers)
        
        # Debug-logga responsen
        print(f"📡 Skickar {key}: {value}")
        print(f"🔹 API Response: {response.status_code} - {response.text}")

        if response.status_code == 201:
            print(f"✅ Variabel {key} uppladdad!")
        else:
            print(f"❌ Misslyckades med {key}: {response.text}")

# === HUVUDFUNKTION ===
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Ange OpenStack cloud-namn (ex: python upload_openstack_vars.py cleura-kna1)")
        sys.exit(1)

    if not TFC_API_TOKEN:
        print("❌ Terraform Cloud API-token saknas! Sätt den med 'export TFC_API_TOKEN=din-token-här'")
        sys.exit(1)

    cloud_name = sys.argv[1]
    cloud_config = load_cloud_config(cloud_name)
    env_vars = convert_to_env_vars(cloud_config)

    print(f"🔄 Laddar upp OpenStack-credentials till Terraform Cloud workspace: {TFC_WORKSPACE}")
    upload_to_terraform_cloud(env_vars)

    print("✅ Klar!")