# PFM_Python_Shcool

## 🔗 Lien de video : https://youtu.be/msiY9NEyEyU

## ⚙️ Instructions d'installation

### 1. Cloner le projet
```bash
git clone https://github.com/HamzaSAlyaacoubi/PFM_Python_Shcool
cd PFM_Python_Shcool
```
#### 2. Créer un environnement virtuel
```bash
python -m venv env
source env/bin/activate  # Linux / Mac
env\Scripts\activate     # Windows
```
### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```
### 4. Configurer la base de données
```bash
python manage.py makemigrations
python manage.py migrate
```
### 5. Lancer le serveur
```bash
python manage.py runserver
http://127.0.0.1:8000/
```
## Initialisation des données avec fixtures
Après les migrations :

```bash
python manage.py loaddata data
```

