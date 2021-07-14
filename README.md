# Django Instagram Clone
## This is a Djnago Instagram Clone application where users can can post pictures, follow other users, commmnet on photos and like photos
 
 ## Author
## By **[JOSEPHAT OTIENO](https://github.com/josphat-otieno)**

## User Stories
These are the behaviours/features that the application implements for use by a user and writer.

* User loads the application using the url provided
* User signs for the application and taken to login page
* User logs n using the his/her credentials
* User views photos posted by other users
* user posts new  photos
* user likes a photo
* user commnets on a photo
* user clicks on profile to view profile info



## Behaviour Driven Development
## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| users loads the application | *On page load* | login page is loaded |
| user chooses to sign up if does not have an already created sccount | *On  click* | on successful sign up, the user is taken to login page|
| user logs in using the correct credentials | *on page load* | home page is loaded and the user sees various photos on the page |
| user clicks on profile| *On page load* | profile info is loaded showing user info such as username, profile photo, email and phone numbber |
| user clicks on logout  | *on page load* | user is logged out of the application and taken login page |



## Prerequisites
* Python3.8

## Setup/Installation Requirements
* Clone [this repository]( https://github.com/josphat-otieno/instagram.git)  using the following commamnd  in the terminal: `git clone  https://github.com/josphat-otieno/instagram.git`. 
* Note:<em>You will need  git installed in your machine. You can install using the following comman: `$ sudo apt-get install git.`</em>
* After cloning, navigate to the folder where the repo was cloned and open it with your favorite code editor. 
* Create a vitual environment using the following command `python3 -m venv --without-pip virtual`
* Activate the virtual environment using the following command `source virtual/bin/activate`
* set up your Database in psql
* run `python3.8 manage.py migrate` followed by `python3.8 manage.py makemigrations gallery` and finally `python3.8 manage.py migrate` 

* create a super `python3.8 manage.py createsuperuser` to start adding your own photos
*  Run thefollowing command  to interact with the application `$python3.8 manage.py runserver`
* Log in using the credentials for super user or create a new account
* Run tests units using the following command `$python3.8 manage.py test`

## Known Bugs

No known bugs

## Technologies Used
- Python3.8
- Django
- Heroku

## Contacts
# Tel: +254717878813
Email: josephat.otieno@student.moringaschool.com