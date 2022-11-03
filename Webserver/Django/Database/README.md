# **Django databases**

## 1. models.py

* After creating a server with a web server and app edit models.py under <app_name> directory


## 2. Migrate
```
python manage.py makemigrations
```
* This is to specify what changes that need to be applied to the database 

## 3. To apply the migration to the database
```
python manage.py migrate
```

## 4. To apply the migration to the database
```
python manage.py migrate
```
## 5. To go into Django shell
```
python manage.py shell
>>> from flights.models import Flight
>>> f = Flight(origin="New York", destination="London",duration=415)
>>> f.save()
```
* **Shell Line 1**
    * flights = <app_name>
    * .models = models.py
    * Flight = <app_name> class under models.py

* **Shell Line 2**
    * Instead of using Sqlite to add to database you can use python to add to the table

* **Shell Line 3**
    * To save it to the database

## 6. To Query the data
```
>>> Flight.objects.all()
<QuerySet [<Flight: Flight object (1)>]>
```

## 7. Make it look Cleaner
* Under models.py under the Flight class introduce the __str__ function
```
def __str__(self):
    return f"{self.id}: {self.origin} t0 {self.destination}
```
## Shell:
```
>>> from flights.models import Flight
>>> flights = Flight.objects.all()
>>> flights
<QuerySet [<Flight: 1: New York to London>]>
>>>
```
## Sample of what Python can do

```
>>> flight = flights.first()
>>> flight
<Flight: 1: New York to London>
>>> flight.id
1
>>> flight.origin
New York
>>> flight.destination
London
>>> flight.duration
415
>>> flight.delete()
```
## 8. Froeign Key

* In order to link multiple tables together you would need to change the charater representation of each columns in to a foreign key like this:
**Character Representaion**
```
class Flight(models.Model)
    origin = models.CharField(max_length = 64)
```

**Foreign Key**
```
from django.db import models
class Airport(models.Model):
    code = models.CharField(max_length =3)
    city = models.CharField(max_length =64)


    def __str__(self):
        return f"{self.city} {self.code}"


class Flight(models.Model)
    origin = models.ForeignKey(Airport, on_delete = models.CASCADE, related_name = "departures")
```

* Next is to update the database by using:
```
python manage.py makemigrations
python manage.py migrate
```

## 9. Admin
* To use built in applications that Django as preloaded
```
python manage.py createsuperuser
Username (leave blank to use <'workspace'>): <Your_name>
Email address: <email>
Password: <makeup a password>
Superuser created successfully.
```
* Django has created a super user account for this applicatiom, this lets you have access to the admin app to manipulate these preinstalled models.
* Takes classes in models.py and add it to admin.py under the <app_name> directory
    * Import the classes to admin.py adn edit the file:
    ```
    admin.site.register(<class_name>)
    ```
* Then run server
* Go into the webpage and add the tag /admin to the link and login with the above login information



