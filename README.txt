After Installing python3 on it's website please run these commands on cmd of the windows (C:\users\$username$)

>> mkdir App
>> cd App
>> pip install virtualenv
>> virtualenv IGS_Django_Test_App
>> IGS_Django_Test_App\Scripts\activate
>> pip install django
>> django-admin startproject IGS_DTApp
>> cd IGS_DTApp
>> python manage.py migrate
>> python manage.py createsuperuser (Placing username, email and password)
>> django-admin startapp CRUD
>> pip install djangorestframework
>> python manage.py makemigrations
>> python manage.py migrate
>> python manage.py runserver