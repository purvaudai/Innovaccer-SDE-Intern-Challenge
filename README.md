# Entry Management Web App - Innovaccer SDE Intern Challenge

Submission for Innovaccer Summer Internship 2020.

## Tech Stack
1. Django
2. Docker
3. Gunicorn Server
4. Nginx for reverse proxy in third option

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
I
## Accounts Already Present in Database:
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

# Future Improvements
1. If server hardware is know, deply to Kubernetes.
2. Improve FrontEnd.
3. Improve Error Handling
