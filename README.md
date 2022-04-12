# Gencrud - free software for creating web projects

Gencrud is the platform for creating simple sites, corporate sites, internet-shop, or blogs. 
The platform is easy to expand and customize, which will create a project of any complexity.


## Install for Ubuntu
```
git clone https://github.com/gencrud/gencrud.git
cd gencrud
. install.sh
```
Congratulations! Open browser - [localhost:8000](http://localhost:8000).


## Install for Windows
>*TODO: fix the description*
>Install git
>Install python
>Install virtualenv, activate
> Run migrations
> run project


### Installation Description
1. [Downolad](https://github.com/gencrud/gencrud) or [clone](https://github.com/gencrud/gencrud.git) a repo **gencrud**.

2. Open a console into the root (`gencrud`) and type `ll`. You must see the next structure folders and files:
```
gencrud/
.git/
.gitignore
install.sh
README.md
```

3. Next, we will install and run the project. This script will install a virtual environment, set a DB (SQLite by default), add a default theme.
```
$ . install.sh
```

**Congratulations!** Open browser - [localhost:8000](http://localhost:8000)
The welcome page should displays. 
Next, you need to fill **general settings** to see the Home page with your content. 
This should take about a minute!


### Structure project (after install)
+ **app/** - 	frontend folder (css, js, images, ...)
+ **gencrud/** - backand folder / core
+ **theme/** - 	theme folder (html, media, ...)
+ **venv/** -  	virtual environment folder
+ README.md
+ install.sh
+ .gitignore


## Upgrade project
*todo: fix description of this section*
*todo: ssh_key copy from `general/gen/settings.py`*
*todo: fix using DB `general/gen/settings_db.py`*

The `upgrade.zip` archive must exist into the root.
```
cd <PROJECT_NAME>
. gencrud/gencrud/sh/upgrade.sh -h  # check command
. gencrud/gencrud/sh/upgrade.sh core
```
Next, fix `settings_db.sql`.
```
python gencrud/manage.py makemigrations
python gencrud/manage.py collectstatic --noinput
python gencrud/manage.py migrate
```



### Useful comands:
> All next commands run from the root `project_name` folder. 
Go to the root `project_name` folder.


**Create a supers user:**
```
python gencrud/manage.py createsuperuser
```

**Run project:**
```
python gencrud/manage.py runserver
```

**Run tests:**
```
cd gencrud
python manage.py test
```


##### Techologies
* Python 3.6
* Django 2.2
* Postgres, MySQL, SQLite
* Bootstrap 4
