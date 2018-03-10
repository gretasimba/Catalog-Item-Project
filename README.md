# Catalog-Item-Project
#About Project:
Adopt Center allows user to review available pets to adopt. It uses Google for autorization and authetication. Logged user is allowed to create/edit/delete animal group and also create/edit and delete animals in the the group user owns.
Some of the technologies used to build this application include Flask, Bootsrap, Jinja2, and SQLite.

#Getting Started:
Install Vagrant and VirtualBox
Clone the Vagrantfile from the Udacity Repo
Clone this repo into the fullsta found in the Vagrant directory
Run vagrant up to run the virtual machine, then vagrant ssh to login to the VM
from the main directory run sudo pip install -r requirements
run application with python application.py from within its directory
go to http://localhost:5000/adoptCenter/ to access the application

#Project contents
This project consists for the following files in the adoptCenter directory:
application.py - The main Python script that serves the website. If no database is found, one is created and populated by populate_database.py.
client_secrets.json - Client secrets for Google OAuth login.
README.md - This read me file.
STATIC - Folder contains CSS 
Templates -Folder contains the HTML templates used in the website
auth.py - Handles the login and logout of users using OAuth.
database_setup.py - Defines the database classes and creates an empty database.
database_insert_data.py - Inserts a selection of animals into the database.


#Run the Project
Download the project zip file to you computer and unzip the file. Or clone this repository to your desktop.
Open the text-based interface for your operating system (e.g. the terminal window in Linux, the command prompt in Windows).
Navigate to the project directory and then enter the vagrant directory.
Bringing the VM up: vagrant up
Log into the VM with the following command:vagrant ssh
Navigate to the tournament directory with this command:

cd /vagrant/[you path to adoptcenter]

OAuth setup
In order to log in to the web app, you will need to get Google+ OAuth app ID and secret. For Google, go to the Google Developers Console.

Once you have your credentials, put the IDs and secrets in the client_secrets.json.

Now run application.py: python application.py

It then starts a web server that serves the application. To view the application, go to the following address using a browser on the host system:
http://localhost:5000/adoptCenter/

You should see the 6 latest animals that were added to the database. Go ahead and explore the web site. To add an animal, you'll need to log in first with either a Google account.
 

#Author Olga Novgorodsky
