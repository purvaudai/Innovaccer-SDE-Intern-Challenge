# Entry Management Web App - Innovaccer SDE Intern Challenge

Submission for Innovaccer Summer Internship 2020.

## Why are there three folders above?
I have provided three different ways to access the program:
1. Running it on local machine like most Django Application
2. Dockerized above set-up and switched to PostgreSQL to provide flexibility given by containerisation.
3. Dockerized using a production-grade Gunicorn Server backed up with Nginx for reverse-proxy, along side PostgreSQL for database.

## Setting Required API Keys
Depending on which method you prefer to use, enter the api keys in var.env or in variables.env

## Setting up server
Move to directory of your choice till the folder which has manage.py, this is the project root.
Then, run, 

```bash
./start.sh
```
Enter user password, if prompted. (Since I do not know your docker configuration, I have set start.sh to use sudo for the dockerized projects.

# Using Web App
 ## Visit [localhost:8000](localhost:8000)
 <img src=">https://raw.githubusercontent.com/purvaudai/Innovaccer-SDE-Intern-Challenge/master/PicturesForREADME/1.png" align="right" width="500px">
![Home Page](https://raw.githubusercontent.com/purvaudai/Innovaccer-SDE-Intern-Challenge/master/PicturesForREADME/1.png)
 ## Adding new Hosts
 1. Log into admin account (Username: admin, Password: admin)
 ![Home Page](https://raw.githubusercontent.com/purvaudai/Innovaccer-SDE-Intern-Challenge/master/PicturesForREADME/2.png)
 2. Now click on add user.
 ![Admin Front Page](https://raw.githubusercontent.com/purvaudai/Innovaccer-SDE-Intern-Challenge/master/PicturesForREADME/3.png)
 3. Fill in details (NOTE: phone number must have country code) and click save and continue editing
 ![Add New User 1](https://raw.githubusercontent.com/purvaudai/Innovaccer-SDE-Intern-Challenge/master/PicturesForREADME/4.png)
 4. Fill in remaining details and click save and logout
 ![Add new user 2](https://raw.githubusercontent.com/purvaudai/Innovaccer-SDE-Intern-Challenge/master/PicturesForREADME/5.png)

 ## Visitor Check In
 1. Fill in details and click on go to meeting
 ![Visitor Check-In](https://raw.githubusercontent.com/purvaudai/Innovaccer-SDE-Intern-Challenge/master/PicturesForREADME/7.png)
 2. Host will now receive Email and SMS

 ## Visitor Check Out
 1. Fill in details
 ![Visitor Check-Out](https://raw.githubusercontent.com/purvaudai/Innovaccer-SDE-Intern-Challenge/master/PicturesForREADME/8.png)
 2. Guest will now receive Email

 ## View Visitor History For any Host
 1. Fill in information
 ![Host Visitor Log](https://raw.githubusercontent.com/purvaudai/Innovaccer-SDE-Intern-Challenge/master/PicturesForREADME/9.png)
 2. View Log
 ![Log](https://raw.githubusercontent.com/purvaudai/Innovaccer-SDE-Intern-Challenge/master/PicturesForREADME/10.png)




```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)