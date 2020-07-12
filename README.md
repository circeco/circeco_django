# Welcome to [CIRCECO](https://circeco-django.herokuapp.com/)!

![cireco tour](/static/img/demo/circeco.gif)

Do you wanna contribuite to a sustaianble future? 
Circeco is the platform for circular economy where to find shops that sell and accept recycled and reuse stuff or also where you can repair your own stuff! 
You can search for second hand shops for music, books, clothes, electronics and home stuff with the scope of give good hints on what good sustainable initiatives are available out there! 
You can also add unlimited circular initiatives to share with the community and contribuiting to build a circular ecosystem! 

---
---

## Table of Contents

1. [**UX**](#ux)
    - [**Project Goal**](#project-goal)
    - [**Site Owner Goal**](#site-owner-goal)
    - [**User Stories**](#user-stories)
    - [**User Expectation**](#user-expectation)
2. [**Design**](#design)
    - [**Design Dependency**](#design-dependency)
    - [**Fonts**](#fonts)
    - [**Colors**](#colors)
    - [**Wireframe**](#wireframe)
3. [**Technologies Used**](#technologies-used)
    - [**Front-End**](#front-end)
    - [**Back-End**](#back-end)
4. [**Features**](#features)
    - [**Existing**](#existing)
    - [**Left to Implement**](#left-to-implement)
5. [**Testing**](#testing)
6. [**Deployment**](#deployment)
7. [**Credits**](#credits)


---

## UX 

### Project Goal
CIRCECO aim to create a "Circular Ecosystem" through a platform for sustatainable consumption that collects suggestion and alternatives ideas to the common wasteful take-make-dispose consumption of products and services. 
My great interest and knowledge in sustaianblity lead me over the years came accross several sustainable alternatives to consumption that often are not evident, easy to find and actually sustaianble. 
The platform collects real alternatives for sustainable consumption and promote sustainability through promoting circular economic/production systems. 
Main project goal is also to give access and usability of the platform through visually appealing design and navigability on any device whether mobile, tablet or desktop. 

### Site Owner Goal
This project is a **Full Stack Frameworks with Django Milestone Project** part of my study in Full Stack Software Development at [Code Institute](https://codeinstitute.net/).
The goal is to build a Django project backend by a relational database to create a website that allows users to store and manipulate data records within this domain through also a relational database.
Ultimately, my goal is to promote a network of circular initiative that offer solutions alternative to the wasteful take-make-disposal model, inspire consumers action towards circular initiative 
and support circular business models that reduce environmental impact from resource use and waste creation. 

### User Goal 
Users on CIRCECO will be able to create an account, save cards as their favourites, select a voucer/donation for circular shopping, pay for the voucher/donation and view their favourites and shopping in their user profile page. 
Specificly users on CIRCECO would be able to: 
* Read info and better understand about Circular Ecosystem, Circular Economy and the Sustainability related to it
* Subscribe to receive latest and updates of the website
* Browse among various circular initiatives in a structured and informative way 
* Support circular ecosystem by buying a voucher to spend in shops that offer circular sustainble alternatives 
* Create an account where to save/pin favorites circular initiatives and to view purchased vouchers via user profile dashboard 

### User Stories 
User one is a university student that is looking for affordable second hand furniture for his student room so is using CIRCECO on his phone while on the bus to find local second hand and cool vintage home furniture and appliance shop. 

User two is an enviromental aware person commited to a sustainable life-style, he/she would want to browse all best options for sustainble consumption whether that is regaridng home, music, book, clothes or bikes. 
By creating a profile he/she can always have access and save favorites circualr initiatives. 

User three is not so much into second hand shops but her/his best friend loves to get lost into those place to find lost books and music so he/she will use the site to gift a voucher for his/her frined. 

User four is a fashionista and thanks to CIRCECO, has discover that there is a shop in the centre district that rent luxury bags promoting sharing and so circular economy. 

User five did not know much about sustainabiltiy or circular economy but thanks to CIRCECO many information are now more clear and concrete understanding how is a circular ecosystem in action. 

### User expectation 
User can feel safe to purchase a voucher safely using an authentication system and a secure payment gateways (in this case Stripe). 
No sensitive user information are stored by the webApp but only an email, username and passowrd. 
If the user want can save/pin favorites circualr initiatives and have them stored and associated with his user profile. 
That would be the only other information stored by the webApp. 
The user is not necessarly expected to create an account to freely browse and explore the webApp. 
However, it is required registration for more interaction like saving favorite initiatives or buying a voucher. 
Finally, the webApp can be navigate and consumed from any device and browser. 


##### back to [top](#table-of-contents)

---
## Design 
Sleak, clean and straighforward user interface with focus on sustaianbility themes and important key words. 
The use of colors is kept at minimum with lots of use of neutral black and white to mantain focus on key elements and to generate a crisp design. 

### Design Dependency
[Materialize 1.0.2](https://materializecss.com/) I enjoyed using Materialize modern and professional-looking layout as a framework and the documentation was simple and clear for implementation with the ready-to-use codes.
Icons are also from Materialize. 

### Fonts 
[Google Font](https://fonts.google.com/) the font-family used have lettersforms that are dynamic, designed for a modular system with a good balancing and that avoide repetitiviness. Their styles are suatable for headlines, short paragraphs or single word, which is what this site is mostly made of 
  - [Khand](https://fonts.google.com/specimen/Khand?query=khand) 
  - [Bebas Neue](https://fonts.google.com/?query=Bebas+Neue)
  - [Chathura](https://fonts.google.com/specimen/Chathura?selection.family=Itim&sidebar.open)
  - [Economica](https://fonts.google.com/specimen/Economica)

### Colors 
The eye-catching use of colors aim to highlight important reoccuring key words with the red. The red color is also a call for action for the emergency related to the state of the environmental. 
Sustainability themes are represented with shades of greens as this is recognised to be a color associate with nature and sustainability. 
Different shades of green are also commonly recognised in the field with different levels of sustaiability, stronger sustainability with deeper green while weaker susteainbiltiy towards a lighther green. 
The custom logo created is also a reminder of the sustainability theme with different shades of green. 
The colors employed together with the font create a specific custom theme recognizable among any other website. 

- ![#FFFFFF](https://placehold.it/15/FFFFFF/000000?text=+) Primary: #FFFFFF; "Simply White" - White is the colur of clarity and semplicity to contrast any colour.
- ![#000000](https://placehold.it/15/000000/000000?text=+) Primary: #000000; "Black" - Elegant and efficient. 

- ![#006064](https://placehold.it/15/006064/000000?text=+) Primary: #006064; "Dark Cyan" - This custom dark green-blue colour is extensively used in the website in various shades and variation, it represents the theme of the web app as well as is the main colours theme of the logo.
- ![#FF5252](https://placehold.it/15/FF5252/000000?text=+) Secondary: #FF5252; "Light Red" - The light red highlights important key words and concept, as well as giving some contrast with other colours for some more design-appealing details. 


### Wireframe 
I have started sketching simply with a pencil and a paper and once satisfied I moved into using Keynote because it has all features, colour and styles that I needed for this sketch. 
With Keynote I could build my muckup concept wireframe well also because I could sketch different part of the app and different pages on different slides. 
[Here](https://db7001a1-0fdb-499d-83ae-5262fe3c1549.ws-eu01.gitpod.io/files/download/?id=81f6bae9-0f16-4813-ab88-4cc87dbc085f) you can find my mockup.


##### back to [top](#table-of-contents)

---
## Technologies Used

### Front-End

* [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)

* [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)

* [jQuery 3.4.1](https://code.jquery.com/jquery/) - This framework is very useful to keep the JS coding at minimum so can be used as fundation of my scripts.

* [Materialize 1.0.0](https://materializecss.com/) - Used as the front-end framework for layout and design.

* [Flask 1.0.2](http://flask.pocoo.org/) - This microframework is used to render the back-end Python with the Front-End Materialize.

* [Stripe API](https://stripe.com/docs/api?lang=python) - Used to make payments.

* [QR code](https://www.qrcode-monkey.com/qr-code-api-with-logo) - Provides API for the creation of QR codes. 

* [Amazon AWS S3](https://aws.amazon.com/) - Mainly used to store staticfiles.


### Back-End

* [Python 3.6.7](https://www.python.org/) - Used as the back-end programming language.

* [Heroku](https://www.heroku.com) - Used for app hosting.

* [PostgreSQL 11.4](https://www.postgresql.org/) - This was usefull for relational SQL database plugin via Heroku.

* [Django 1.11.29](https://www.djangoproject.com/download/) The free open-source framework is being used to render Python back-end codes with Materialize front-end codes. 
The project was developed using an older version of Django following the lessions, despite Django 3+ being the current version. 
An upgrade in this sense will come soon. 

Further details on all Python packages used on this project can be found in the [requirements.txt](/circeco_django/requirements.txt) file.


##### back to [top](#table-of-contents)

---
---
## Features

### Existing
**Browse for circular shops**
- The User can browse through a list of circular shops, read about them and find their weblink.

**Search for circular shops**
- Through the search box the user can filter by word the shops of his/her interest. 

**Create a profile** 
- The user can create a profile so to save favourite shops and buy a voucher.

**Save and unsave favourite circular shop**
- The registered user can save and unsave favourite circular shops that would be visible on his profile page. 
At any time when the user can save or unsave favourite shops. 
If the user is looged in would be always visible if a shop is favourite or not. 

**Buy a voucher**
- Users that have a profile can also buy a voucher to use in circular shops.

**Store non sensitive user info**
- The user profile page will store the list of favourite circular shops and the vouchers purchased by the user. 


---
## Left to Implement
**Change passowrd**
- The users would be able to update their passwords from their profile page through reciving an email with instructions on how to reset the password.

**Receive voucher on the user's email address**
- The user would receive the purchased voucher on the user's email address 

**Filter bittons**
- Search by filtering for specific object or their use, also a button to reverse and view them all

**Subscribe for news**
- Introducing the otpion for user who register and non to subscribe with their email and receive news about circular shops


##### back to [top](#table-of-contents)

---
---
## Testing  
**PLEASE NOTE**: 
DO NOT insert your real card deatails to test this app but rather use the info in the img below
![CARD-DETAIL](/static/img/demo/card-example.png)
This project is been through a series of automated and manual testing. 
Furthermore, validation sites have been used as well as compatibilitieschecks across major modern browser and devices. 

### Validators 

**HTML** [W3C HTML Validator](https://validator.w3.org)

**CSS** [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

**JavaScript** [JShint](https://jshint.com/)

**Python** [PEP8 Online](http://pep8online.com/)


### Compatibility

- :white_check_mark: Responsive webdesign for different devices and screen size
- :white_check_mark: Crossbrowser testing


### Automated testing

[![Build Status](https://travis-ci.org/circeco/circeco_django.svg?branch=master)](https://travis-ci.org/circeco/circeco_django) 
This project uses [Travis-CI](https://travis-ci.org/) to test Continuous Integration. 


##### back to [top](#table-of-contents)

---
## Deployment 

In order to run Circeco_django locally you are adviced to follow the steps below. 

Before starting make sure you have the following:

- [Python3](https://www.python.org/downloads) to run the application.
- [GIT](https://www.atlassian.com/git/tutorials/install-git) for cloning and version control.
- [Microsoft Visual Studio Code](https://code.visualstudio.com) (or any suitable IDE) to develop your project.
- [PIP](https://pip.pypa.io/en/stable/installing) to install all requirements for the app.

Also, You will <strong>need to</strong> create accounts with the following online services in order to run this project.
- [Stripe](https://stripe.com/en-se) for the payment service.
- [QRcodeMonkey](https://www.qrcode-monkey.com) for the QR code creation for the voucher. 


## Instructions:

WARNING: You may need to follow a different guide based on the OS you are using, read more [here](https://python.readthedocs.io/en/latest/library/venv.html")


* 1: <strong>Clone</strong> circeco_django repository by either downloading from <a href="https://github.com/Circeco/circeco_django">here</a> or type the following command into your terminal.
```bash
git clone https://github.com/circeco/circeco_django
```
* 2: <strong>Navigate</strong> to this folder in your terminal.
* 3: <strong>Enter</strong> the following command into your terminal.
```bash
python3 -m .venv venv
```
* 4: <strong>Initialize</strong> the environment by using the following command.
```bash
.venv\bin\activate
```

* 5: <strong>Install</strong> the requirements and dependancies from the requirements.txt file
```bash
pip3 -r requirements.txt
```

* 6: Within your IDE now <strong>create</strong> a file where you can store your secret information for the app, I used vscodes settings.json however you can just create an env.py file if you wish.

```bash
{
    "python.pythonPath": "/usr/local/bin/python3",
    "python.terminal.activateEnvironment": true,
    "python.linting.enabled": true,
    "files.autoSave": "onFocusChange",
    "files.useExperimentalFileWatcher": true,
    "terminal.integrated.env.osx": {
      "SECRET_KEY": "<your_secret_key_here>",
      "DEV": "1",
      "STRIPE_PUBLISHABLE": "<your_stripe_publishable_key_here>",
      "STRIPE_SECRET": "<your_stripe_secret_key_here>",
      "DATABASE_URL": "<your_database_url_here>",
}
```

* 7: <strong>Enter</strong> the following command into the terminal to migrate models into database.
```bash
python3 manage.py migrate
```

* 8: Then you need to <strong>Create</strong> a 'superuser' for the project using the terminal, enter the following command.
```bash
python3 manage.py createsuperuser
```

Once the database migrations and superuser have been successfully completed, Django should migrate the existing *migrations.py* files from each app to configure a relational schema.

* 9: The app can now be ran locally using the following command.
```bash
python3 manage.py runserver
```

Congratulations, CIRCECO is now running locally!

### Deploying CIRCECO to Heroku:

* 1: <strong>Create</strong> a requirements.txt file using the following command.
```bash
pip3 freeze > requirements.txt
```

* 2: <strong>Create</strong> a procfile with the following command.
```bash
echo web: python3 app.py > Procfile
```
* 3: Push these newly created files to your repository.
* 4: Create a new app for this project on the Heroku Dashboard.
* 5: Select your deployment method by clicking on the deployment method button and select GitHub.
* 6: On the dashboard, set the following config variables:

**Key**|**Value**
:-----:|:-----:
DATABASE\_URL|<your\_database\_url>
SECRET\_KEY|<your\_secret\_key>
STRIPE\_PUBLISHABLE|<your\_stripe\_publishable\_key>
STRIPE\_SECRET|<your\_stripe\_secret\_key>

* 7: <strong>Click</strong> the deploy button on the heroku Dashboard.
* 8: Wait for the build to finish and click the view project link once it has!

Congratulations, CIRCECO is now hosted on Heroku and is live!


##### back to [top](#table-of-contents)

---
## Credits
Styles and logos are custom made or in-line referenced. 
Circeco.org holds the copyright for the business idea, content and codes of this repository. 

### Authors and Acknowledgment:
- **Autor**: Author **Piero Grilli** can be contacted at grilli.piero@circeco.org
- **Acknowledgment**: Code Institute Slack, Code Institute Tutor Support and mentors. 
- Massive thanks to [Andreas Nyberg](https://github.com/middlewareman) my local mentor, tutor and one of mine greatest supporter!

##### back to [top](#table-of-contents)
