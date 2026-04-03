# PFM_Python_Shcool

## ⚙️ Instructions d'installation

### 1. Cloner le projet
```bash
git clone https://github.com/HamzaSAlyaacoubi/PFM_Python_Shcool
cd PFM_Python_Shcool
python -m venv env
source env/bin/activate  # Linux / Mac
env\Scripts\activate     # Windows
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
http://127.0.0.1:8000/
