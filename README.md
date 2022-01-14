
<img src="https://github.com/PaulBowden673/Projects-MP-MP3/blob/main/static/documents/simplyfood.png" width="100%" alt="SimplyFood Recipe website">

<a href="https://simply-food-project.herokuapp.com/" rel="nofollow" target="_blank">Click  here</a> to access the site.


## UX ##
**The main purpose of this full-stack MongoDB-based Flask project is to create a database of recipes that allows users to create, read, update and delete (CRUD) recipes. "Simply Food" gives an access to all the recipes in the database for non-registered users. At the same time, it gives the opportunity to create an account and benifit from having convenient access to all features of the website. Registered users can add new recipes, edit and delete their own ones, as well as edit their username and password or delete account.
Simply Food is a simple way to view, create and store your recipes!
Sign in, get inspired, contribute, cook and enjoy!**


  
**USER STORIES**

As a user, I want/expect:

- to view all the recipes without having to register
- to view all recipe details (including cooking time, servings, list of ingredients and directions)
- to create my own account
- to add new recipes
- to edit my recipes
- to delete my recipes
- to log out any time and have the session terminated
- to delete all recipes I've created
- to use the website from any device (laptop, tablet, mobile)
## Design
   
   I wanted to keep the site simple and encourage less adventurous cooks to find recipes that were simple to make with few ingredients  
   
   ### Colour Scheme
   - The 2 main colours used on the site are #fff White, #f0f8ff Aliceblue which keep the site looking fresh.
   ### Typography
   - The Roboto font is the main font used throughout the whole site, with sans-serif as fallback in case the font does not load correctly. It is frequently used and easy to read. 

   
   ### Imagery

- Background image taken from Unslpash.com. Photo by Gaelle Marcel


## Wireframe Mock-ups 
These can be found at the following links 

- [Wireframe 3 screen sizes](/https://github.com/PaulBowden673/Projects-MP-MP3/blob/main/static/documents/MileStone%203%20Project%20.pdf)

## Flowchart
- [Flowchart](/https://github.com/PaulBowden673/Projects-MP-MP3/blob/main/static/documents/flowchartMS3.drawio)

## Features

- Responsive on all screen sizes
- Interactive elements
- Links to social media pages
- Navigation links on all pages, limited options for non registered users 

### [Home Page](Https://github.com/PaulBowden673/Projects-MP-MP3/index.html)


- Catergory cards linking to recipes by category.

#### Home
<img src="https://github.com/PaulBowden673/Projects-MP-MP2-Quiz/blob/main/assets/documents/readme-images/home-page.png" alt="Home page" width="100%">

#### Login
<img src="https://github.com/PaulBowden673/Projects-MP-MP2-Quiz/blob/main/assets/documents/readme-images/rules-page.png" alt="Rules Page" width="100%">

#### Register
<img src="https://github.com/PaulBowden673/Projects-MP-MP2-Quiz/blob/main/assets/documents/readme-images/highscores-page.png" alt="Highscores Page" width="100%">

#### Profile
<img src="https://github.com/PaulBowden673/Projects-MP-MP2-Quiz/blob/main/assets/documents/readme-images/contact-page.png" alt="Contact Page" width="100%">

### Recipes

### Single Recipe 

### Add Recipe


#### Edit Recipe
<img src="https://github.com/PaulBowden673/Projects-MP-MP2-Quiz/blob/main/assets/documents/readme-images/quiz404.png" alt="404 Page" width="100%">

## Technologies Used

GitPod - an online IDE for developing this project.
Git - for version control.
GitHub - for remotely storing project's code.
PIP - for installation of necessary tools.
Am I Responsive - for creation of the images in the readme file and checking responsiveness.

Front-End
HTML - to build the foundation of the project.
CSS - to create custom styles.
Back-End
Python 3.8.2 - back-end programming language used in this project.
Flask 1.1.2 - microframework for building and rendering pages.
MongoDB Atlas - NoSQL database for storing back-end data.
PyMongo - for Python to get access the MongoDB database.
WTForms 2.2.1 - for creating forms with validation.
Werkzeug 0.16.1 - to generate and verify password hashing.
Jinja 2.10.1 - templating language for Python, to display back-end data in HTML.
Heroku - to host the project.
Libraries
Bootstrap 5 - main responsive modern front-end framework used for grid and responsivesness.
Google Fonts - to import fonts.
FontAwesome - to provide icons used across the project.
JQuery 3.5.0 - to simplify DOM manipulation and to initialize Materialize functions.

## Future updates

- Update recipe datebase to hold arrays to give more scope to size of recipes - struggled to be able to impliment this at this time.
- Add favourite recipes to profile page - ran out of time to impliment
- Add way for users to add own recipe pictures
- Add functionality to add more categories

## Testing
All recipes and single recipe display
When I click on "Recipe page", I can see recipe cards displayed. In that view, I can see image and  recipe name. Clicking on the recipe card redirects me to the single recipe page, where I can see all the detailed information about the recipe. I tested this functionality as a non-logged in (guest) user and a logged in user and it perfectly worked in both cases.

Create a new user account
I created my main account, as well as a few test accounts to test this functionality. Clicking on the "Register" button in the navbar opens the form, where I can put username and password to create a new account. I tried to input an existing username, not matching passwords in "password" and "confirm password" fields, and input less then 3 or more then 15 charachters. In all cases I got a corresponding flash error message. As well as that, I tried to leave an empty field and submit the form, but got an error message again asking to fill the field. When the form was successfully submitted, I was redirected to the home page, seeing a message that my new account was created. I also checked the link to the Login page at the bottom of the form, which worked well.

Login
Clicking on the "Login" button in the navbar opens the form, allowing me to login to my account. I tried to leave empty fields or input incorrect details, but I was not able to submit the form if something was entered incorrectly. After a successful login I was redirected to the home page, seeing the message that I was logged in. I also checked the link to the Register page at the bottom of the form, which worked well.

Delete Account
I deleted some testing accounts to test the functionality. Followed by clicking the "Delete account" button on the Account Settings page, the modal opens and I am asked to confirm the deletion by entering my password. I tried to put the wrong password, but got an error flash message. When I input the correct password, I am redirected to the home page and see the message that my account was deleted. Then, I checked the database to make sure that the account as well as all the recipes created by this user were removed.

Add New Recipe
I added plenty of test recipes to check the functionality throughout the development. If I leave some of the required fields empty, I will not be able to submit the form. THe functionality to add a photo of the recipe was not added at this stage and the recipe image displays a placeholder rather than an image ( images were added to test recipes when building the app, but ran out of time to impliment a way of users adding own recipe photos) 

Edit Recipe
If I am logged, I can see the buttons "Edit" and "Delete" in the single_recipe page.  I also tried to change the link manually in the browser to edit other's recipe. However, I was not able to open the form and got the message, that I can only edit my own recipes, which means defensive design works well against brute forcing. Being the creator of the recipe, {I can view the form with pre-populated fields and can change anything that I want. If all fields are valid, I can see the changes I made in a  Recipe Page after the submission. I tried to edit a number of recipes and edit different fields, everything worked correctly.}

Delete Recipe
I deleted some dummy testing recipes to test the functionality. After clicking the "delete" button,  I was redirected to the home page and saw the message about the succsessful deletion.
Then I checked the database to make sure, that the recipe was removed and found an issue that the recipe was not removed from the app or the database

#### Devices

- Samsung S9
- Samsung S6 Lte Tablet
- Ipad 
- Iphone 6/7/8
- Desktop with 4K 2056px Monitor
- Dell Inspiron 5405 Laptop 

#### Browsers

- Microsoft Edge
- Chrome
- Firefox
- Safari 

## Issues/Bugs

- Issue with recipe cards not displaying inline on All recipes page. Not sure how to fix
- Issue with delete recipe not removing recipe from DB but showing Flash message 
- Issue with add recipe not picking up category select option and writing to DB 

### Validation

All files passed validation testing at 

 ###### HTML index.html page

  ![HTML Validation](https://github.com/PaulBowden673/Projects-MP-MP2-Quiz/blob/main/assets/documents/validation/w3%20HTML%20Validation%20index.html.png)
  
  ###### HTML 404.html page
  
  ![HTML Validation](https://github.com/PaulBowden673/Projects-MP-MP2-Quiz/blob/main/assets/documents/validation/w3%20HTML%20Validation%20quiz404.html.png)

- [CSS] - Issue with validating with Bootstrap. When validated as Direct Input no issues were found

 #### CSS Style.css 
 
 ###### By URL
 
  ![CSS Validation style.css](https://github.com/PaulBowden673/Projects-MP-MP2-Quiz/blob/main/assets/documents/validation/w3%20CSS%20validator%20style.css.png)
  
  ###### By Direct Input
  
  ![CSS Validation Direct Input](https://github.com/PaulBowden673/Projects-MP-MP2-Quiz/blob/main/assets/documents/validation/w3%20CSS%20validator%20style.css%20Direct%20Input.png)

  #### CSS 404Style.css
  
  ###### By URL
  
  ![CSS Validation quiz404.css](https://github.com/PaulBowden673/Projects-MP-MP2-Quiz/blob/main/assets/documents/validation/w3%20CSS%20validator%20style404.css.png)

  ###### By Direct Input
 
  ![CSS Validation Direct Input](https://github.com/PaulBowden673/Projects-MP-MP2-Quiz/blob/main/assets/documents/validation/w3%20CSS%20validator%20style404.css%20Direct%20Input.png)

- [Lighthouse]

 ###### Lighthouse Validation Desktop
 
![Lighthouse Validation Desktop](https://github.com/PaulBowden673/Projects-MP-MP2-Quiz/blob/main/assets/documents/validation/Lightouse%20Report%20Desktop%20MP2%20Quiz.png)

###### Lighthouse Validation Mobile

![Lighthouse Validation Mobile](https://github.com/PaulBowden673/Projects-MP-MP2-Quiz/blob/main/assets/documents/validation/Lighthouse%20Report%20Mobile%20MP2%20Quiz.png)

- [JSHint]

###### Script.js

![jsHint Validation Report](https://github.com/PaulBowden673/Projects-MP-MP2-Quiz/blob/main/assets/documents/validation/JSHint%20validation%20script.js.png)

###### EmailJS.js

![jsHint Validation Report EmailJS.js](https://github.com/PaulBowden673/Projects-MP-MP2-Quiz/blob/main/assets/documents/validation/JSHint%20validation%20emailJS.js.png)
## Deployment
### Local Deployment
To be able to run this project, the following tools have to be installed:
- An IDE  (I used [GitPod](https://www.gitpod.io/) online IDE for creating this project)
- [MongoDB Atlas](https://www.mongodb.com/) (for creation your database)
- [Git](https://git-scm.com/)
- [PIP](https://pip.pypa.io/en/stable/installing/) 
- [Python](https://www.python.org/)   
#### Directions
1. You can clone this repository directly into the editor of your choice by pasting the following command into the terminal:   
`git clone https://github.com/irinatu17/MyCookBook`    
Alternatively, you can save a copy of this repository by clicking the green button "Clone or download" , then "Download Zip" button, and after extract the Zip file to your folder.
2. In the terminal window change directory (CD) to the correct file location (directory that you have just created).
3. Set up environment variables:
    - Create **.env** file in the root directory.
    - On the top of the file add `import os` to set the environment variables in the operating system.
    - Set the connection to your MongoDB database(MONGO_URI) and a SECRET_KEY with the following syntax:
    `os.environ["SECRET_KEY"] = "YourSecretKey"`   
    `os.environ["MONGO_URI"] = "YourMongoURI"`  
    .
4. Install all requirements from the **requirements.txt** file putting this command into your terminal:   
`pip3 install -r requirements.txt`  
*Note: GitPod does not require `sudo`, so if you use another IDE, you will need to include `sudo` in the beginning of the command: `sudo pip3 install -r requirements.txt`.*
5. Create a new Database called "MyCookBook" in [MongoDB Atlas](https://www.mongodb.com/).   
*You can sign up for free account, if you do not have one.*
6. In "MyCookBook" database create five following collections:
###### Cuisines
```
_id: <ObjectId>
cuisine_type: <String>
```
###### Meals
```
_id: <ObjectId>
meal_type: <String>
```
###### Diets
```
_id: <ObjectId>
diet_type: <String>
```
###### Users
```
_id: <ObjectId>
username: <String>
password: <String>
user_recipes: <Array>
```
###### Recipes
```
_id: <ObjectId>
recipe_name: <String>
description: <String>
cuisine_type: <String>
meal_type: <String>
cooking_time: <String>
diet_type: <String>
servings: <String>
ingredients: <Array>
directions: <Array>
author: <ObjectId>
image: <String>
```
7. You will now be able to run the application using the following command `python3 run.py`.   

### Heroku Deployment
To deploy the project to [Heroku](https://heroku.com/) the following steps need to be completed:
1. Create a **requirement.txt** file, which contains a list of the dependencies, using the following command in the terminal:  
`pip3 freeze > requirements.txt`
2. Create a **Procfile**, in order to tell Heroku how to run the project, using the following command in the terminal:   
`echo web: python run.py > Procfile`
3. `git add`, `git commit` and `git push` these files to GitHub repository
4. Create a **new app** in Heroku, assigning a name (must be unique) and set a region (for my project I set Europe)
5. From the Heroku dashboard link the new Heroku app to your GitHub repository:    
    - "Deploy" -> "Deployment method" -> "GitHub"
    - then "Enable automatic deployment"
6. To start the web process, put the following command into the terminal: `heroku ps:scale web=1` to scale dynos
7. In the **Settings** tab of the new Heroku app, click on "Reveal Config Vars" and set the following config vars:
    - **IP** : 0.0.0.0
    - **PORT** : 8080
    - **MONGO_URI** : `<link to your MongoDB database>`
    - **SECRET_KEY** : `<your secret key>`
    - **DEBUG**: **FALSE**  
*Note: your MONGO_URI and SECRET_KEY must match the ones you entered in .env.py file*

8. The app will be deployed and ready to run. Click "Open App" to view the app.   

**Note**: if you have not linked GitHub and Heroku following step N.5, alternatively as the last step of deployment, you can put the following command into your terminal:   
 `heroku login`, after a successful log in `git push heroku master` - to push the app to Heroku, and finally click "Open App" in Heroku dashboard to view the app.

## Credits

### Content

I have borrowed code ideas and inspiration from the following sources during this project. This helped me to write my code and make my project work.

- https://www.youtube.com/watch?v=f4fB9Xg2JEY&amp;t=3763s&amp;ab_channel=BrianDesignBrianDesign

- https://github.com/jamesqquick/Build-A-Quiz-App-With-HTML-CSS-and-JavaScript

- https://www.lcn.com/blog/beginners-guide-custom-404-pages/

- https://medium.com/nerd-for-tech/javascript-build-quiz-application-f6ee0a235417

- https://codereview.stackexchange.com/questions/189399/quiz-app-from-a-json-file

- CodeInstitute 

### Media

- Background image - www.Pexels.com. (Photo by Ash @ModernAfflatus)

- 404 page image - www.flaticon.com


## Acknowledgements

- [Code Institute](https://www.codeinstitute.net/)
- Newcastle College
- Bootstrap framework
