# openstack-clouds-yaml-to-terraform-workspace-vars
A tool to convert OpenStack clouds.yaml authentication details into Terraform Cloud workspace environment variables.


## **📌 Steps to Create & Set Up the Repository**  

### **1️⃣ Create the GitHub Repository**
Go to **[GitHub](https://github.com/new)** and set up the repo:  
- **Organization:** `development-toolbox`  
- **Repository Name:** `terraform-openstack-cloud-uploader` (or any preferred name)  
- **Description:** `A tool to upload OpenStack credentials from clouds.yaml to Terraform Cloud.`  
- **Visibility:** **Public** (recommended for open-source) or **Private**  
- **Initialize with:**  
  ✅ `README.md`  
  ✅ `.gitignore` → Choose **Python**  
  ✅ `LICENSE` → Choose **MIT**  

---

### **2️⃣ Clone the Repository Locally**
Once the repository is created, clone it to your local machine:  
```bash
git clone https://github.com/development-toolbox/terraform-openstack-cloud-uploader.git
cd terraform-openstack-cloud-uploader
```

---

### **3️⃣ Add the Python Script**
Move the `upload_openstack_vars.py` script into the repository:  
```bash
mv /path/to/upload_openstack_vars.py .
```

---

### **4️⃣ Add the README**
Copy and paste the **README** (from my previous message) into a new file:  
```bash
nano README.md
```
Paste the content, then save and exit (`CTRL+X`, then `Y`, then `Enter`).

---

### **5️⃣ Commit and Push the Code**
Run the following commands to commit and push the script to GitHub:  
```bash
git add .
git commit -m "Initial commit - Add OpenStack credential uploader script"
git push origin main
```

---

### **6️⃣ Enable Issues & Discussions (Optional)**
- Go to the **GitHub repo → Settings**  
- Enable **Issues** for tracking bugs/feature requests  
- Enable **Discussions** for community feedback  

---

### **7️⃣ Add CI/CD (Optional)**
To automate testing, we can add a **GitHub Action** for linting the script:  

📌 **Create `.github/workflows/lint.yml`**  
```yaml
name: Lint Python Code

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v3
        with:
          python-version: "3.9"

      - name: Install dependencies
        run: pip install flake8

      - name: Run linter
        run: flake8 upload_openstack_vars.py --max-line-length=100
```
Commit & push this to enable automatic **Python linting**!

---

## **🔹 Next Steps**
1️⃣ **Create the repo on GitHub**  
2️⃣ **Push the script & README**  
3️⃣ **Enable Issues & Discussions**  
4️⃣ **Set up CI/CD (optional)**  

Once done, **share the GitHub link** so we can refine & improve the repo! 🚀🔥