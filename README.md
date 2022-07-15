# Toolbox Project

[GitHub Link](https://github.com/amos-kibet/toolbox-project)

``Toolbox Project``is a personal productivity software for daily routine tasks, like task planning, time management, calendar scheduling, and saving favourite websites.
``Toolbox project`` idea struck me after I realized that in the course my browsing, I often come across useful resources on the internet, that are worth remembering. A common way to save these resources/websites is to bookmark them.
However, bookmarking is not always convenient, as you may find yourself using more than one browser. With bookmarking, you would be forced to create folders for your favourites websites.
This is too much work already, and your favourite resources would be scattered, and probably repeated on every browser.

With ``Toolbox Project``, there will be a single bookmarking and 'storage' tool for your favourite websites. You will be able to have all your favourite resources in one place.
This tool is called Aggregator.

Other tools under Toolbox Project include:
- ``Task Planner``: A CRUD-powered tool that allows you plan out your daily activities. At the simplest, it is just a task planner. However, other features will be incorporated later, like sending a notification when a particular task is almost due, or automatically scheduling your tasks in your calendar.
- ``Timer:`` A tool that helps you manage your time by allowing you to set time for particular task and notify you when the time is about to elapse, and when the time elapses.

## Task Planner

This is a Django app that let's you add tasks that you want to do. 

Tasks are identified by their level of priority. There are 3 levels, which are:

- High -- Tasks are coloured `RED`
- Medium -- Tasks are coloured `YELLOW`
- Low -- Tasks are coloured `GREEN`
## API Endpoints
Task Planner has two endpoints at the moment. Other endpoints will be added later.

They are:
- `GET /tasks/task/` => Returns the Homepage, where all tasks are listed.
- `POST /tasks/task/add/` => Enables addition of tasks either in the UI (client app) or from a REST API test environment.

## Setup

- Clone this project in your preferred working space (Desktop, etc).
- Navigate to the project folder.
- Create & activate a Python virtual environment.
  - `sudo apt install virtualenv`
  - `virtualenv env` `env` is the name of your virtual environment. You can give it any name you want.
  - `source env/bin/activate` Replace `env` with your preferred name.
- To run the app, run this in the terminal
  - `python manage.py runserver`
- Open your browser and navigate to `localhost:8000`

## Technologies Used
```commandline
asgiref==3.5.2
backports.zoneinfo==0.2.1
Django==4.0.5
pip==22.1.2
psycopg2-binary==2.9.3
setuptools==62.3.4
sqlparse==0.4.2
wheel==0.37.1
```
Check out requirements.txt.

For the database, I used PostgreSQL. You can use the default database that Django ships with, which is SQLite3.
