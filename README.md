Here’s the **updated README** with the new project name **`openstack-clouds-yaml-to-terraform-workspace-vars`** and refined details for clarity and consistency. 🚀  

---

# **OpenStack Clouds.yaml to Terraform Workspace Vars**  
📡 **Automatically extract OpenStack authentication details from `clouds.yaml` and upload them as environment variables to a Terraform Cloud workspace.**  

## **Overview**  
This tool reads OpenStack authentication details from a `clouds.yaml` file and securely uploads them as **environment variables** to Terraform Cloud.  
This eliminates the need to manually enter credentials and ensures **secure, automated authentication** for Terraform Cloud workspaces.  

### **Features**  
✅ **Extracts OpenStack credentials** dynamically from `clouds.yaml`  
✅ **Ensures `region_name` is present** before proceeding  
✅ **Automatically retrieves Terraform Cloud workspace ID**  
✅ **Marks `OS_PASSWORD` as sensitive** for security 🔒  
✅ **Provides detailed error handling** and logs API responses  

---

## **Prerequisites**  
### **1. Terraform Cloud API Token**  
Before running the script, set up your Terraform Cloud API token:  
```bash
export TFC_API_TOKEN="your-terraform-cloud-token"
```
💡 **Using CI/CD?** Store the token as a **GitHub Secret** or in your CI/CD environment variables.  

### **2. OpenStack `clouds.yaml` Configuration**  
Ensure your OpenStack credentials are defined in `~/.config/openstack/clouds.yaml`.  
Here’s an example:  

```yaml
clouds:
  cleura-fra1:
    auth:
      auth_url: https://fra1.citycloud.com:5000
      username: your-username
      password: your-password
      project_name: Demo-Project
      project_domain_name: PROJECT_DEMO_DOMAIN_NAME
      user_domain_name: USER_DOMAIN_NAME
    identity_api_version: 3
    interface: public
    region_name: Fra1
```
**Each cloud entry must have a `region_name`, otherwise the script will exit with an error.**  

---

## **Installation**  
Ensure Python 3 is installed, then install the required dependencies:  
```bash
pip install requests pyyaml
```

---

## **Usage**  
### **Upload credentials for a specific OpenStack region**  
Run the script and specify the cloud profile (e.g., `cleura-kna1`):  
```bash
python3 upload_openstack_vars.py cleura-kna1
```
The script will:  
1️⃣ Extract OpenStack authentication details from `clouds.yaml`  
2️⃣ Validate that `region_name` is present  
3️⃣ Retrieve the **Terraform Cloud workspace ID**  
4️⃣ Upload the following environment variables:  
   - `OS_AUTH_URL`  
   - `OS_USERNAME`  
   - `OS_PASSWORD` (marked as sensitive)  
   - `OS_PROJECT_NAME`  
   - `OS_USER_DOMAIN_NAME`  
   - `OS_PROJECT_DOMAIN_NAME`  
   - `OS_REGION_NAME`  

### **Expected Output**
```bash
🌍 Region Name: Kna1
🔄 Uploading OpenStack credentials to Terraform Cloud workspace: Terraform-OpenStack-Docker
📡 Sending OS_AUTH_URL: https://kna1.citycloud.com:5000
✅ Variable OS_AUTH_URL uploaded!
📡 Sending OS_USERNAME: your-username
✅ Variable OS_USERNAME uploaded!
📡 Sending OS_PASSWORD: *********
✅ Variable OS_PASSWORD uploaded (marked as sensitive)!
...
```

---

## **Error Handling**  
| **Error** | **Cause** | **Solution** |
|-----------|----------|-------------|
| `❌ File clouds.yaml not found!` | `clouds.yaml` is missing | Ensure it's located at `~/.config/openstack/clouds.yaml` |
| `❌ Cloud '<cloud_name>' not found in clouds.yaml!` | Incorrect cloud name | Run `cat ~/.config/openstack/clouds.yaml` and verify the correct name |
| `❌ No region_name found!` | `region_name` is missing | Ensure each cloud entry has `region_name` |
| `❌ Failed to fetch Terraform Cloud workspace ID` | Incorrect workspace or org | Verify Terraform Cloud settings |
| `❌ Terraform Cloud API returned 500 Internal Server Error` | Terraform Cloud issue | Check https://status.hashicorp.com/ |

---

## **Automating in CI/CD**  
### **GitHub Actions**
To integrate this script in **GitHub Actions**, add the following step:  
```yaml
- name: Upload OpenStack credentials to Terraform Cloud
  run: python3 upload_openstack_vars.py cleura-kna1
  env:
    TFC_API_TOKEN: ${{ secrets.TFC_API_TOKEN }}
```

### **GitLab CI/CD**
For **GitLab CI/CD**, add this step to `.gitlab-ci.yml`:  
```yaml
upload-openstack-vars:
  script:
    - python3 upload_openstack_vars.py cleura-kna1
  variables:
    TFC_API_TOKEN: $TFC_API_TOKEN
```

---

## **Contributing**  
We welcome contributions! To contribute:  
1. **Fork the repo**  
2. **Create a feature branch**  
3. **Submit a pull request**  

---

## **License**  
This script is open-source and licensed under the **MIT License**.  

---

### **🌍 Secure & Automate OpenStack Authentication in Terraform Cloud! 🚀**  
No more manual variable entry—let this tool handle your OpenStack-to-Terraform Cloud integration. 


