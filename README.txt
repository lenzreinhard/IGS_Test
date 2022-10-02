Install Python 3.10 at https://www.python.org/downloads/

Navigate until the directory of the project by cmd and execute the following commands:

(It's neessary that python and its subdirectory Scripts are set in enviroment variable of the windows)

>> pip install virtualenv
>> virtualenv IGS_Test
>> IGS_Test\Scripts\activate
>> pip install django
>> cd IGS_DTApp
>> pip install djangorestframework
>> python manage.py runserver

After that everything is configured and now you can see the project by the browser at:

http://localhost:8000/admin - Django Panel
user: IGSAppTest
password: IGSAppTest

So there you can add, edit, select and delete the employees and departments data

The API endpoints are:

http://localhost:8000/api/employee
http://localhost:8000/api/employee/<int:pk>
http://localhost:8000/api/employee/create
http://localhost:8000/api/employee/delete/<int:pk>

http://localhost:8000/api/department
http://localhost:8000/api/department/<int:pk>
http://localhost:8000/api/department/create
http://localhost:8000/api/department/delete/<int:pk>

The webpages listing deparmtents and employees are

http://localhost:8000/employees
http://localhost:8000/departments