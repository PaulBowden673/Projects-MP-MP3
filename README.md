<img src="https://github.com/PaulBowden673/Projects-MP-MP2-Quiz/blob/main/assets/documents/readme-images/quiz-responsive-image.png" width="100%" alt="Health & Safety Quiz">


<a href="https://paulbowden673.github.io/Projects-MP-MP2-Quiz/" rel="nofollow" target="_blank">Click  here</a> to access the site.

**I built this website to give users a fun and enjoyable game to play. I based the game on Health & Safety questions so it can also be used for training**
## UX ##
**The main purpose of this full-stack MongoDB-based Flask project is to create a database of recipes that allows users to create, read, update and delete (CRUD) recipes. "Simply Food" gives an access to all the recipes in the database for non-registered users. At the same time, it gives the opportunity to create an account and benifit from having convenient access to all features of the website. Registered users can add new recipes, edit and delete their own ones, as well as edit their username and password or delete account.
Simply Food is a simple way to view, create and store your recipes!
Sign in, get inspired, contribute, cook and enjoy!**






**I incorporated the following things in order for the target audience to have a great experience when visiting my website,**

- A Home page with buttons to start the game and also view the game rules.
- A rules section so users can learn how to play the game.
- A highscores section so users can keep track of thier scores and complete against other users for the highest score.
- A Contact form so users can contact me with feedback via EmailJS.
 
  
**USER STORIES**

As a user, I want/expect:

to view all the recipes without having to register
to view all recipe details (including cuisine, meal and diet types, cooking time, servings, list of ingredients and directions)
to see how many recipes are on the website
to create my own account
to add new recipes
to edit my recipes
to view a list of my recipes on a separate page and see how many recipes I've created
to delete my recipes
to log out any time and have the session terminated
to change my current username
to change my current password
to delete my account and all recipes I've created
to use the website from any device (laptop, tablet, mobile)
## Design
    
   ### Colour Scheme
   - The 3 main colours used on the site are Black, #571ce0 Blue and Red which are appropriate.
   ### Typography
   - The Roboto font is the main font used throughout the whole site, with sans-serif as fallback in case the font does not load correctly. It is frequently used and easy to read. 
   - The Merriweather Sans font is used for headings throughout the site, with sans-serif fallback in case the font does not load correctly, it is optimised for a bold display on modern web browsers. 
   
   ### Imagery

- Background image taken from Pexels.com. Photo by Ash @ModernAfflatus
- 404 page image taken from flaticon.com


## Wireframe Mock-ups 
These can be found at the following links 

- [Wireframe 3 screen sizes](/https://paulbowden673.github.io/Projects-MP-MP2-Quiz/assets/documents/wireframes/milestoneProject2Quiz.pdf)

## Features

- Responsive on all screen sizes
- Interactive elements 

### [Home Page](Https://github.com/PaulBowden673/Projects-MP-MP2/index.html)

- Navigation links for the Home page and Contact page.
- Buttons to view the rules and highscores, restart the game and clear the high scores list.
- Contact button to allow users to send feedback via EmailJS API

#### Home
<img src="https://github.com/PaulBowden673/Projects-MP-MP2-Quiz/blob/main/assets/documents/readme-images/home-page.png" alt="Home page" width="100%">

#### Rules
<img src="https://github.com/PaulBowden673/Projects-MP-MP2-Quiz/blob/main/assets/documents/readme-images/rules-page.png" alt="Rules Page" width="100%">

#### Highscores
<img src="https://github.com/PaulBowden673/Projects-MP-MP2-Quiz/blob/main/assets/documents/readme-images/highscores-page.png" alt="Highscores Page" width="100%">

#### Contact
<img src="https://github.com/PaulBowden673/Projects-MP-MP2-Quiz/blob/main/assets/documents/readme-images/contact-page.png" alt="Contact Page" width="100%">


### [404 Page](Https://github.com/PaulBowden673/Projects-MP-MP2/quiz404.html)

- 404 Error page to direct user back to the home page.
- Links to social media pages

#### 404 Page
<img src="https://github.com/PaulBowden673/Projects-MP-MP2-Quiz/blob/main/assets/documents/readme-images/quiz404.png" alt="404 Page" width="100%">

## Technologies Used

GitPod - an online IDE for developing this project.
Git - for version control.
GitHub - for remotely storing project's code.
PIP - for installation of necessary tools.
GIMP2 - for editing, compressing and resizing images.
Am I Responsive - for creation of the images in the readme file and checking responsiveness.
Ezgit - to create gifs for README
Imgur - to host gifs
ImgBB - to host images used in README
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
Materialize 1.0.0 - main responsive modern front-end framework used for grid and responsivesness.
Google Fonts - to import fonts.
FontAwesome - to provide icons used across the project.
Adorable Avatars - to create user avatars.
JQuery 3.5.0 - to simplify DOM manipulation and to initialize Materialize functions.

## Future updates

- Fetch questions from JSON file to allow questions to be changed without changing the code - struggled to be able to impliment this at this time.
- Change the qustions so the answers are in a random order to avoid regular users knowing where the answers will be
- Add more questions in  random order to give a better experience for returning users
- Add futher sets of questions to make the game more challenging, such as Food Safety, Fire Safety, Licensing.

## Testing
 I have thoroughly tested this website and was unable to find any broken links within it. I have also tried to submit blank contact forms and forms with incorrect email addresses which gave me an error message by way of alert box when thhe emial was sent.
 
 ### Testing User Stories from UX section

User stories from the UX section were tested to ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals. 

 #### First Time visitor

1. As a first time Visitor, I want to easily understand the purpose of the site and how to play the game.
    1. On entering the site, the user is presented with a clean website detailing the purpose of the site and giving instructions on how to play the game after clicking on the rules button.  
2. As a first time visitor, I want to find the game enjoyable and challenging.
    1. . On entering the website the user is presented with several buttons - Play, Rules, Highscores and Contact. THe user can then easily choose to play or to review the other options presented.
 
 #### Returning Visitor

1.  As a returning visitor, I want to still find the game enjoyable and challenging. 
    1.  The questions are displayed in a random order everytime the game is started.
2.  As a returning visitor, I want to be able to give feedback to the website owner and suggest improvements or ideas.
    1. The contact button takes the user from the home screen to blank email form for them to complete with name, email address and message. Upon clicking send email, the email is sent via EmailJS to the site owner.

#### Frequent Visitor

1. As a frequent visitor,  I want to still find the game enjoyable and challenging.
    1. The questions are presented in a random order everytime the game is played.
2. As a frequent visitor,  I want to be able to try to beat the highest scores.
    1. The user can display the current table of high scores ( the scores are only saved locally on the same device previously used)
3. As a frequent visitor, I want to be able to give feedback on the quiz.
    1. The contact button takes the user from the home screen to blank email form for them to complete with name, email address and message. Upon clicking send email, the email is sent via EmailJS to the site owner.
    
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

- The score was showing the previous game score rather than the current game score. After investigation, I identified that the issue was in the script.js file. Once the game had ended the score was set to the local storage. The finalScore variable was then set to get the score from the local storage, this was getting the wrong score. To resolve the issue, I put the finalScore variable in the function that increments the score during the quiz and set it to return that score.After testing this more the issue was resolved.

- During testing I identified an issue in the main Quiz Game section. In the script.js file, any correct or incorrect answers selected by the user would have the relevant style class applied to change the colour, once the answer was selected, the answer button did not change to the relevant colour, instead the surrounding area in between the buttons would have the style class applied to change the colour. I identified that the style class was being applied to the parent element of the answer button which is the div containing all the answer buttons. The style class was applied to the div rather than the answer buttons. To fix the issue, I changed the code in the script.js to ensure the style class is applied to the answer buttons. Further testing was completed, and the answer buttons now correctly have the style applied.

- An additional issue was identified within the main Quiz Game section. The answer buttons have a hover style applied, once the user selects the answer and the new class style is applied for correct or incorrect answer, the hover style was still in effect. if the user was still hovering over the answer button, they were not able to see whether the answer was correct or incorrect. This affected the UX of the quiz. To resolve the issue, I added additional style classes to separate the answer buttons from the other buttons. Then I added additional code in the script.js, when the user selects the answer the hover style would be removed from the button and the correct/incorrect style class applied. The hover style is now removed, and they are able to view whether the answer is correct or incorrect.

- During testing an issue was found with the finish quiz modal that pops up once user has finished the game. The default behaviour for a modal is to close if mouse is clicked outside of the modal or if 'esc' is pressed on keyboard. This was causing an issue as the user was able to close the finish quiz modal and return back to the quiz game section. However, they would not be able to view the finish quiz modal again, and all the progress would be lost. The only way to exit the game would be to reload the webpage or select the 'Quit Game' button and return to the Home page. This identified issue would reduce the UX and functionality of the end game section. To resolve this issue, I added additional code to the script.js for the finish quiz modal as well as confirmation modals. This has improved the overall UX of the quiz game. Once the user is presented with the finish quiz modal, they can no longer close this without selecting one of the provided buttons. The user is also not able to close the additional confirmation modal without selecting one of the options. 

- On mobile devices, a UX issue was identified with the hover style. Once the user clicked the button to select their answer, the answer would have the correct class applied to change colour. However, once the next question was presented the hover style was still applied to the last selected button. I moved the ans-btn:hover to a media query and this removed the highlighted question on mobile devices, but the answer text is changed to black. The issue is still present but not as noticable as it was previously.
### Validation

All files passed validation testing at 



- [HTML] - Issue with empty heading id=Progress-text due to it being filled by javascript during game to show progress.

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
