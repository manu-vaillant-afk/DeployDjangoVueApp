# Todo list - Django Vue

Todo list utilisant une api rest django en backend et vue.js en frontend.

## Installation du backend :

### 1) Créer un envi virtuel :
```python
python -m venv env 
```
### 2) Activer l'environnement:
```python
env\Scripts\activate
```
### 3) Installer dépendances : 
```python
pip install -r requirements.txt
```
### 4) Effectuer les migrations :
```python
python manage.py makemigrations
python manage.py migrate
```
### 5) Créer un user :
```python
python manage.py createsuperuser
```

### 6 bis) Si erreur "no such table: TodoBase_myuser"
```python
a) python manage.py migrate --run-syncdb
b) créer un user
```

### 7) Lancer le serveur :
```python
python manage.py runserver
```

## Installation du frontend :

### 1) Installer les dépencances :
```
npm install
```

### 2) Toujours plus de dépendances :
```
npm install axios vue-router vuex sass sass-loader
```

