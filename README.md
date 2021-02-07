# Test_Technique_Mehdi_Jrebi

## Introduction

This project is a technical test for Voguel consulting.

Template is written with django 3.1.6 and python 3 in mind.

![Default Home View](__screenshots/capture1.PNG?raw=true "Title")
![Default Home View](__screenshots/capture2.PNG?raw=true "Title")

### Main features

* Add a level(category), subject(sub-category) and a chapter(sub-sub-category).

* Upload a PDF file with the same name as the chapter

* If the file already exists, add (1) at the end of its name

* Show the list of the inserted data and sort them by date      

# myapp

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/mehdijrebi/Test_Technique_Mehdi_Jrebi.git
    $ cd {{ project_name }}
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install django-widget-tweaks
    $ pip install django-filter
        
    
Then simply apply the migrations:

    $ python manage.py makemigrations myapp
    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver
