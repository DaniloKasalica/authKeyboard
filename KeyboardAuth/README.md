# cleanbear


1. pip install virtualenv (aka ga nemate, provjera virtualenv --version) 
2. virtualenv venv 
3. source venv/bin/activate (za windows venv/scripts/activate ) nakon ove komande treba da vidite (venv) lijevo od imena 
4. pip install -r requirements.txt 
5. python manage.py makemigrations 
6. python manage.py migrate  
7. python manage.py loaddata fixtures/initial_data.json
8. python manage.py runserver
