# Welcome to [CIRCECO](https://circeco-contribuite.herokuapp.com/)!

![circdata](static/img/mockup-mobile.jpg)


Do you wanna contribuite to a sustaianble future? 
Circeco is the platform for circular economy where to find shops that sell and accept recycled and reuse stuff or also where you can repair your own stuff! 
You can search for second hand shops for music, books, clothes, electronics and home stuff with the scope of give good hints on what good sustainable initiatives are available out there! 
You can also add unlimited circular initiatives to share with the community and contribuiting to build a circular ecosystem! 


## Table of Contents
1. [**UX**](#ux)
    - [**Project Goal**](#project-goal)
    - [**Site Owner Goal**](#site-owner-goal)
    - [**User Stories**](#user-stories)
    - [**User Expectation**](#user-expectation)
2. [**Design**](#ux)
    - [**Fonts**](#fonts)
    - [**Icons**](#Icons)
    - [**Colors**](#colors)
3. [**Features**](#features)
    - [**Existing**](#existing)
    - [**Left to Implemtent**](#left-to-implement)
4. [**Technologies Used**](#technologies-used)
    - [**Front End Technologies**](#front-end-technologies)
    - [**Back End Technologies**](#back-end-technologies)
5. [**Database Schema**](#Database-schema)
6. [**Testing**](#testing)
7. [**Deployment**](#deployment)
8. [**Credits**](#credits)
#


## 1. UX 

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

---
## 2. Design 
Sleak, clean and straighforward user interface with focus on sustaianbility themes and important key words. 
The use of colors is kept at minimum with lots of use of neutral black and white to mantain focus on key elements and to generate a crisp design. 

### External Dependency
[Materialize 1.0.2](https://materializecss.com/) I enjoyed using Materialize modern and professional-looking layout as a framework and the documentation was simple and clear for implementation with the ready-to-use codes.

### Fonts 
[Google Font](https://fonts.google.com/) the font-family used have lettersforms that are dynamic, designed for a modular system with a good balancing and that avoide repetitiviness. Their styles are suatable for headlines, short paragraphs or single word, which is what this site is mostly made of 
  - [Khand](https://fonts.google.com/specimen/Khand?query=khand) 
  - [Bebas Neue](https://fonts.google.com/?query=Bebas+Neue)

### Icons 
[Font Awesome 5.8.1](https://fontawesome.com/) Social Icon in the footer cannot be found in Materialize so Font Awesome can provide icons for more specific needs 

### Colors 
The eye-catching use of colors aim to highlight important reoccuring key words with the red. The red color is also a call for action for the emergency related to the state of the environmental. 
Sustainability themes are represented with shades of greens as this is recognised to be a color associate with nature and sustainability. 
Different shades of green are also commonly recognised in the field with different levels of sustaiability, stronger sustainability with deeper green while weaker susteainbiltiy towards a lighther green. 
The custom logo created is also a reminder of the sustainability theme with different shades of green. 
The colors employed together with the font create a specific custom theme recognizable among any other website. 

- ![#FF5252](https://placehold.it/15/FF5252/000000?text=+) Primary: #FF5252; "Fringy Flower" - This pastel green colour provides an elegant & efficient contrast for the strong brown colour.
- ![#FF5252](https://placehold.it/15/FF5252/000000?text=+) Primary: #FF5252; "Fringy Flower" - This pastel green colour provides an elegant & efficient contrast for the strong brown colour.
- ![#FF5252](https://placehold.it/15/FF5252/000000?text=+) Primary: #FF5252; "Fringy Flower" - This pastel green colour provides an elegant & efficient contrast for the strong brown colour.
- ![#FF5252](https://placehold.it/15/FF5252/000000?text=+) Primary: #FF5252; "Fringy Flower" - This pastel green colour provides an elegant & efficient contrast for the strong brown colour.
- ![#FF5252](https://placehold.it/15/FF5252/000000?text=+) Primary: #FF5252; "Fringy Flower" - This pastel green colour provides an elegant & efficient contrast for the strong brown colour.

### Wireframes 
I have not used any program to make my wireframe but I have rather made a hand sketch [here](https://github.com/circeco/circdata/blob/master/static/img/circdata-sketch.jpg).


---
## 4. Technology Used

### Languages 
* HTML 
* CSS 
* JavaScript 
* JSON
* Python


### Frameworks 
* [Flask 1.0.2](http://flask.pocoo.org/)
This microframework is used to render the back-end Python with the Front-End Materialize.

* [jQuery 3.2.1](https://code.jquery.com/jquery/)
This framework is very useful to keep the JS coding at minimum so can be used as fundation of my scripts. 


### 



## 3. Features



## 5. Database Schema 


## 6. Testing 

[![Build Status](https://travis-ci.org/circeco/circeco_django.svg?branch=master)](https://travis-ci.org/circeco/circeco_django) 
