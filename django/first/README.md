# Django Web Server

#
## Commands: to exit server – Ctrl+C

1. Install:
  1. pip3 install Django
2. Create a Django project:
  1. Django-admin startproject \<project\_name\>
  2. ![](RackMultipart20221023-1-670eiy_html_a744299856fa87bb.png)
  3. manage.py – to be able to execute commands on the Django file
  4. setting.py – contains settings for the Django application
  5. urls.py – a table of contents for our application, which consists a number of different URLs or routes that can you can visit
3. Running web sever:
  1. python manage.py runserver
    1. goes and actually runs this web server
    2. ![](RackMultipart20221023-1-670eiy_html_d97fcb6f34b54bf1.png)
  2. This is to contain multiple applications under one web server, typically one web application has multiple applications running – Like for google for example has google search, google images, google maps all different apps under one server.
4. Create app:
  1. Python manage.py startapp \<app\_name\>
  2. Creates a new directory with the app\_name
  3. views.py lets us describe what the user sees when they visit a particular route.
5. To install app into webserver:
  1. Go into the project\_name directory and into settings.py
  2. Scroll down to INSTALLED\_APPS[] and add '\<app\_name\>'
6. To edit the app:
  1. Go into views.py under the \<app\_name\> directory
  2. Look at – file link
  3. Then create urls.py under the same directory to specify when to use the views.py and edit the urls.py like this – file link
  4. Then do under the urls.py under the \<project\_name\> directory and edit it like this – file link
  5. Run the web server not the app
  6. Go into the web address and edit the link to contain /hello tag at the end
7. In case of TemplateDoesNotExsit at \<app\_name\> error:
  1. Go into views.py under the \<project name\> directory
  2. Then go into settings.py then find TEMPLATES[]
  3. Then do into DIRS:[] and add the path to the Template Dir like starting with r'\<template\_dir\>'
  4.