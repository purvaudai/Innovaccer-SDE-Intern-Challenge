# Entry Management Web App - 
# Innovaccer SDE Intern Challenge

Submission for Innovaccer Summer Internship 2020.

## Tech Stack
1. Django
2. Docker
3. Gunicorn Server
4. Nginx for reverse proxy in third option

## Prerequisites
Ensure Python 3 is installed, and venv is working (normally is is installed along with Python3).
Also ensure docker and docker-compose is installed.

## Why are there three folders above?
I have provided three different ways to access the program:
1. Running it on local machine like most Django Application
2. Dockerized above set-up and switched to PostgreSQL to provide flexibility given by containerisation.
3. Dockerized using a production-grade Gunicorn Server backed up with Nginx for reverse-proxy, along side PostgreSQL for database.

## Setting Required API Keys
Depending on which method you prefer to use, enter the twilio api keys and admin email id in var.env or in variables.env

If you plan on using the Twilio keys already provided in the project, that is a trial account which only allows sending SMS to phones numbers which are registered in the Twilio account. Also, messages can only be sent from 9 A.M. TO 9 P.M. IST in trail account.

To register your number in the given account, or any other account:
Go to [Twilio](https://www.twilio.com/).
Login with Email[purvaudai99@gmail.com], password[TingooPingoo123].
Now go visit [here](https://www.twilio.com/console/phone-numbers/verified) and add Host Phone No.


## Accounts Already Present in Database(In Non-dockerized Version):
### Admins:
1. Username: admin <br>
   Password: admin 

### Hosts:
1. Username: purvaudai <br>
   Password: welcomep<br>
   Email: purvaudai99@gmail.com
   
2. Username: namant <br>
   Password: welcomen <br>
   Email: 17uec077@lnmiit.ac.in

## Setting up server
Move to directory of your choice till the folder which has manage.py, this is the project root.
Then, run, 

```bash
./start.sh
```
Enter user password, if prompted. (Since I do not know your docker configuration, I have set start.sh to use sudo for the dockerized projects.

If you are using Docker version, you will need to do the following to start the app since the database will be empty on running the app for the first time on a new system, due to Postgre Docker Image, where persisted data is made with permissions of the originating docker build.

1. Run 
```bash
docker ps
```
2. Obtain Container ID of dockerized_entry_local_web
3. Run, after replacing correct Container ID
```bash
docker exec -it c0c20a45003a /bin/bash
```
4. Run
```bash
python manage.py makemigrations
```
5. Run
```bash
python manage.py migrate
```
6. Run, and add admin account.
```bash
python manage.py createsuperuser
```
7. Welcome to app. Now you have a empty database to begin populating. Proceed to add new hosts by method below.

# Using Web App
 ## Visit [localhost:8000](localhost:8000)

 <img src = "https://raw.githubusercontent.com/purvaudai/Innovaccer-SDE-Intern-Challenge/master/PicturesForREADME/1.png" width="500px">

 ## Adding new Hosts
 1. Log into admin account (Username: admin, Password: admin)

 <img src = "https://raw.githubusercontent.com/purvaudai/Innovaccer-SDE-Intern-Challenge/master/PicturesForREADME/2.png" width="500px">

 2. Now click on add user.

 <img src = "https://raw.githubusercontent.com/purvaudai/Innovaccer-SDE-Intern-Challenge/master/PicturesForREADME/3.png" width="500px">

 3. Fill in details (NOTE: phone number must have country code) and click save and continue editing

 <img src = "https://raw.githubusercontent.com/purvaudai/Innovaccer-SDE-Intern-Challenge/master/PicturesForREADME/4.png" width="500px">

 4. Fill in remaining details and click save and logout

 <img src = "https://raw.githubusercontent.com/purvaudai/Innovaccer-SDE-Intern-Challenge/master/PicturesForREADME/5.png" width="500px">

 ## Visitor Check In

 1. Fill in details and click on go to meeting

 <img src = "https://raw.githubusercontent.com/purvaudai/Innovaccer-SDE-Intern-Challenge/master/PicturesForREADME/7.png" width="500px">

 2. Host will now receive Email and SMS

 ## Visitor Check Out
 1. Fill in details

 <img src = "https://raw.githubusercontent.com/purvaudai/Innovaccer-SDE-Intern-Challenge/master/PicturesForREADME/8.png" width="500px">

 2. Guest will now receive Email

 ## View Visitor History For any Host
 1. Fill in information

 <img src = "https://raw.githubusercontent.com/purvaudai/Innovaccer-SDE-Intern-Challenge/master/PicturesForREADME/9.png" width="500px">

 2. View Log

 <img src = "https://raw.githubusercontent.com/purvaudai/Innovaccer-SDE-Intern-Challenge/master/PicturesForREADME/10.png" width="500px">

 ### To stopp server
 1. If using non-dockerized version, just use Ctrl+C
 2. Else,
 ```bash
docker-compose down
```



# Future Improvements
1. If server hardware is know, deploy to Kubernetes.
2. Improve FrontEnd.
3. Improve Error Handling
