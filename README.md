# Seven Terraces! – Third milestone project
Seven Terraces is an app that allows its users to save their properties online and edit them anytime they need to. This app also allows the users to share their properties with other users, save the properties that they like and contact the admin if they have enquiries. 

The app also gives the users the option to search for properties based on names and descriptions. 

![Seven Terraces](/documents/mockups/am_i_responsive.png)

[View live version of website via Heroku](https://seven-terraces.herokuapp.com/)

## **Wireframes**
I have used Balsamic to create low-fidelity wireframes. First I created a basic wireframe for desktops. The website will be easy to navigate by using the navigation bar or by scrolling down the page.

Below you can see the mock-ups that I drew using 
[Balsamiq](https://balsamiq.com/#) 

##### Log in page
![login](/documents/mockups/log_in.png)

##### Log out page
![logout](/documents/mockups/properties.png)

##### Logged in page
![login](/documents/mockups/logged_in.png)

##### Register page
![registration](/documents/mockups/sign_up.png)

##### Home page
![Home](/documents/mockups/landing_page.png)

##### View property page
![view_property](/documents/mockups/view_property.png)

##### Add property page
![add_property](/documents/mockups/add_property.png)

##### Edit property page
![edit_property](/documents/mockups/edit_property.png)

##### Admin Dashboard page
![admin_dashboard](/documents/mockups/admin_dashboard.png)

##### Profile page
![profile](/documents/mockups/profile.png)

##### Contact Us page
![contact](/documents/mockups/contact_us.png)

- The final website differs from the original wire-frames because, when working on the design, I sometimes I found more appropriate ways to display different sections.

## **UX**
### **User Persona**
This website project will target users who are interested in viewing and sharing information about property deals. The main focus is on providing an easy to navigate and responsive website that allows users to be a part of a community with a portfolio of properties. Most pages except "View property", "Add property" and "Edit proeprty" use parallax feature to make the site more visually appealing. As these three pages are content heavy, parallax feature has been excluded for them. 

### **User Goals**
- View **featured properties** posts per month created by the admin;
- View **property posts** created by the Seven Terraces community;
- View, edit, search, delete **property posts** created by them;
- The website has to work well on all kinds of devices like mobile phones, tablets and desktops.

### **Site Owners Goals**
- Be the “go-to” place for users to source property deals. 
- To create a community for users to source property deals for one another.

### **User Requirements and Expectations**
#### **Requirements**
- Easy to navigate by using the navigation menu.
- Relevant content for each category.
- Appealing visuals.
- Easy way to find properties relevant to the user.

#### **Expectations**
- When clicking social media links expect the page to open in a separate browser.
- Expect that the navigation links work properly to take the user where they intended to go.
- Expect to be able to read, add, edit or delete items created by the user.
- Feedback whether or not registered, logged in, logged out.

## **UI Design**
### **Font**
- I used [Google Fonts](https://fonts.google.com/) to highlight the various texts.
- The project has the main font of [Roboto](https://fonts.google.com/specimen/Roboto) as it is easy to read and modern
- “Sans-Serif” is used as the default backup font in cases Roboto has difficulty loading.

### **Colour Scheme**
- The colour scheme is based on creating an environment with energy, excitement and warmth;
- The logo was created on [Wix logo maker](https://www.wix.com/logo/maker/esh/zoe-editor?industry=%7B%22industry%22%3A%22609d10f90c3f7f79f9eed882_bf61b613f48c3e7af17cfc6c_property%20landing%20page%22%2C%22isCustom%22%3Afalse%7D&tags=creative%2Cformal%2Ctimeless%2Cdynamic&selectedWebsiteId=0&logoId=f9be001c-54be-4ac7-81c2-eea8e24dd21e&referralAdditionalInfo=arenaSplitPage) 
- All colours were checked with WebAIM [https://webaim.org/resources/contrastchecker/](https://webaim.org/resources/contrastchecker/) to check the accessibility of the colours and present a pass.

![Results](/documents/mockups/contrast_test.png)


#### **Colour Palette**
Below is the colour scheme used for the website. 
![Colour Palette](/documents/mockups/colour_palette.png) 
![Colour Palette](/documents/mockups/colour_palette2.png) 

using [https://coolors.co/](https://coolors.co/)
- #FFFFFF: This colour is used for the background.
- #FCA311: This colour is used as the main text colour and where the background of the CTA buttons.
- #14213D: This colour is used as the primary colour and sets the tone for the website. It’s the dominant colour in the footer, header and background images in the heading. It’s also the colour of some texts. 
- #000000: This colour is used as a secondary colour for fonts.
- #E5E5E5: This colour is used as a tertiary accent colour where something to highlight forms. 
- #8ECAE6: This colour is used as an accent colour and mainly used for hovering over some buttons. 
- #219EBC: This colour is also used as an accent colour and mainly used for hovering over some buttons. 
For the social media, the colurs match the exact tones of these applications using [https://www.webnots.com/color-codes-for-social-networking-site-icons/](https://www.webnots.com/color-codes-for-social-networking-site-icons/). 

### **Icons**
- **[Materialized:](https://materializecss.com/)** Majority of icons from the Materialized Icons library was used unless there was not an appropriate icon available then the Font Awesome library is used. 
- **[FontAwesome:](https://fontawesome.com/)** In some cases if a FontAwesome icon was more appropriate I have also used FontAwesome.

### **Structure**
The overall structure that was used is the Materialize framework. Materialize provides various elements of CSS and Javascript which is very helpful to keep a good structure on applications. 

### **User Stories**
*Guest User*
1. As a Guest User, I want the main purpose of the site to be clear so that I immediately know what the site is intended for upon entering;
2. As a Guest User, I want to be met with a visually appealing and easy to read layout of created items;
3. As a Guest User, I want to view the **featuredproperty** posts of the month to get a sense of the value if I sign up as a registered user and they don't have to search for it;
4. As a Guest User, I want to be able to sign-up to create and edit my own **property posts**;
5. As a Guest User, I want to be able to get in contact via social media if I like enquire about properties or have suggestions.

*Registered User*
1. As a Registered User, I want the main purpose of the site to be clear so that I immediately know what the site is intended for upon entering;
2. As a Registered User, I want to be met with a visually appealing and easy to read layout of created items;
3. As a Registered User, I want to view the featured items of the month so that I don't have to search for them;
4. As a Registered User, I want to be able to log back into the site with my credentials;
5. As a Registered User, I want to be able to view **property posts** added by other members of the community;
6. As a Registered User, I want to be able to create, edit and delete the **property posts** I have added;
7. As a Registered User, I would like to be able to search the site so that I can easily find properties that I am looking for;
8. As a Registered User, I want to be able to bookmark properties I find interesting and remove a bookmark.
9. As a Registered User, I want to be able to change my password on my profile;
10. As a Registered User, I want to be able to delete my account and profile;
11. As a Registered User, I want to be able to log out of my account;
12. As a Registered User, I want to be able to get in contact via social media if I like enquire about properties or have suggestions.
13. As a Registered User, I wan to be able to get in touch with the admin regarding the deals I’m interested in viewing. 

*Admin User*
The Admin user shares the same expectations as the Registered user with some additional ones as below:
1. As an Admin User, I would like the ability to **log in to an admin account** so that I can **create, edit and delete featured property posts** for each month;
2. As an Admin User, I want to be able to view all **property posts** added by other members of the community as well as the ability to **edit or delete any property posts** so that I can **maintain the site to stay updated**

## Features
### On all pages
- **Navigation Bar:** I have created the navigation bar using [Materialize](<[https://materializecss.com/](https://materializecss.com/)>) nav bar with **Icon Links** and I have also included the **Mobile Collapse Button**. Then I have customised it to be in line with the website design.

- **Mobile Collapse Button / Sidebar:** The **Mobile Collapse Button** will appear on smaller screens (tablets and mobiles) and by clicking on it, it will then show the navigation bar as a sidebar.

- **Logo:** The logo will appear in the navigation bar for every section of the website and when clicked it will redirect the user to the home page (get_properties.html). 

- **Social media links:** They appear on the page footer on every website page and by clicking on them the user will get re-directed to the media websites to follow Time2Eat. (since the website is fictitious they will be redirected to the login page for all the social media apps).

- **Footer:** I have used the footer from [Materialize](<[https://materializecss.com/](https://materializecss.com/)>) to include the social media links and the contact details.

- **Contact Us:** Provides the user with the website contact details in case he/she wants to get in touch.

### login.html
- The login page has an input form where the users will enter their username and password.

- **Flash message** If the username is not registered or if the password is incorrect an error message will appear.
- New users can click on the link "Register here" to get redirected to the register page.

### register.html
- New users will have to register using the input form in this page in order to start using the app.

- **Flash message** If the username entered in the form has already been used by another user then an error message indicating this issue will be displayed.
- In order to store the passwords securely in MongoDB, the passwords have been hashed using the bcrypt function.
- Users already registered can click on the link "Login here" to get redirected to the login page.

### Log Out 
- If a registered or admin user clicks on the log out button, they will be logged out of their current session and will no longer be able to see the pages they would if they were logged in.
- A registered user will have to log in again if they want to see their Profile or the Resources Page.
- A Admin user will have to log in again if they want to see their Profile, Resources Page or the Manage Resource Dashboard Page.

### get_properties.html
This is the home page where the cards with all the properties are displayed. In this page the user can search properties entering words in the search box. 

- **Search input box**: On the top of the page the users can enter text to search for a specific word in the name or description of the property in the properties database. As a result all the properties containing that word will be displayed. This can be very useful if users are looking for specific property.

- **Cards:** The first time the user lands on this page will be able to see all the properties available in the app by clicking on the caret on the right side of each card. The property in the cards will be revealed. 

- **Views and bookmarks:** The user can also see the number of views and also can bookmark/save the property which would be displayed on the profile page. 

- **View property button:** By clicking on "view property" button in the card reveal section, the user will be redirected to the "view property" page where they can see all the details available for the property.

- **Edit / Delete buttons:** The author of each property, then, can edit or delete the property from the properties page if they wish. 

- **Switch “Featured”:** : The Admin can activate this switch if they’d like to add that particular property on the home page. 

### View property page
This page will display the main attributes for the property. If the property belongs to the user they will have the option to remove or edit the property. Each time the property is viewed, the number of views will increase by 1. 

- **Delete button:** This button will only be visible if the property belongs to the user and will allow the user to remove the property. Before the property gets removed a confirmation message will appear so the user can confirm if they want to delete the property or not.

- **Edit button:** This button will only be visible if the property belongs to the user and will allow the user to edit the property by redirecting the user to the "edit property" page.

- **Modal:** When the user clicks on "delete button" the confirmation message will be displayed on a modal window and the property will only be removed if "YES" is selected. This modal has been taken from [Materialize](<[https://materializecss.com/](https://materializecss.com/)>).

### add_property.html & edit_property.html
These pages will be used by the user to enter a new property or to edit an existing one.

- **Form:** The whole page is a form with different input types. The form used and all the input fields inside the form have been taken from [Materialize](<[https://materializecss.com/](https://materializecss.com/)>).

- **Input (type text)** I have used input type text for name of the property and calories inputs. Name of properties is required. 

- **Modal:** When the user clicks on "Upload image" a modal window will appear containing the input (type file).

- **Input (type file):** Allows the user to upload an image for the property. This field is optional. If the user doesn't upload an image then the default image will be used for the property.

- **Input (price):** I have used input type number for the "price" field. This field will be compulsory and needs to be a number.

- **Select input:** I have used "single" select inputs for the fields "strategy", "Property Type". All of them are compulsory as they will also be used in the dashboard section and in order to show further details of the properties on the view_property page. 
 
I have also used "multiple" select input to select the “amenities” and “features” in the properties. 

- **Textarea:** I have used textareas for the fields "Property details", “Property description” and “Date added”. 
 These fields are compulsory because they are the most important information about any property.
 The user needs to enter every "Property details” on a different line to make sure it displays correctly in the view property page and also to be able to convert the input to array.

- **Button 'Add/Edit Property':** By clicking this button the form will be submitted and the property will be inserted into the database.
  After adding/editing the property the user gets redirected to the home page.

- **Button 'Save changes':** By clicking this button the form will be submitted and the property will be updated in the database. After editing a property the user gets redirected to the property that they have just edited.

### Manage categories
- **Input box** This input box also comes from [Materialize](<[https://materializecss.com/](https://materializecss.com/)>) and allows the user to enter a new type of strategy if the type of strategy that they need is not already on the list displayed.

- **container** I'm using a container from [Materialize](<[https://materializecss.com/](https://materializecss.com/)>) in order to display the list of categories on the admin dashboard page. 
In the first section the admin is able to add and edit featured properties by clicking on the relevant buttons. In the second part, the user can delete or edit strategies/categories. 

- **Modal:** When the user clicks on "delete strategy" the confirmation message will be displayed on a modal window and the type of strategy will only be removed if "delete" is selected. This modal has been taken from [Materialize](<[https://materializecss.com/](https://materializecss.com/)>).

## Features Left to Implement
- **Favourites:** Adding filters to only display properties according to amenities, price, types and dates. I thought of this feature once the website was finished and I couldn't spend more time working on the project as I needed to get going with the rest of the course.

## Technologies Used

#### Database:
- **[MongoDB](https://www.mongodb.com/)** to store user data. 

#### Mock-up tool:
- **[Balsamiq](https://balsamiq.com/#)** to create the mock-ups for the website.

#### Languages:
- **HTML5:** is the main language used to create the structure of the website.

- **CSS3:** is the language used to add styles to the HTML.

- **[JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)** This is the language used to add interactivity to the website. It has been used to create the initialise cards, navbar, date picker, modal, validate Materialize selects,  and the function to preview the image uploaded using input type file.

- **[Python](https://www.python.org/)** The main logic of the website has been created using Python.

- **[Flask](https://palletsprojects.com/p/flask/)** I have used the web Flask framework.

- **[PyMongo](https://pypi.org/project/pymongo/)** & **[Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/)** to connect Python and Flask to the MongoDB database

- **[Jinja](http://jinja.pocoo.org/)** I have used Jinja templating engine in order to use template inheritance, add **for loops** and **if statements** in the html files and in order to pass information between back and front ends.

- **[Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/)** a WSGI web application library used for passwords on Python.

- **[Tiny-PNG](https://tinypng.com/)** I used tinypng for big images up to 5M needed to be compressed to improve the website's loading time.

- **[CompressJPEG](https://compressjpeg.com/)** The big images bigger than 5M needed to be compressed to improve the website's loading time.

#### Dependencies:
In order to run the app, I had to install the following packages, these packages are listed in the requirements.txt file. Each of these packages had installed additional packages but the additional packages have been removed from the requirements.txt file because they will be automatically installed when installing the main packages on the list:

**flask:**  Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. 

` Flask==2.0.1 `

**dnspython:** dnspython is a DNS toolkit for Python. It supports almost all record types. It can be used for queries, zone transfers, and dynamic updates.

` dnspython==2.2.1`

**flask-pymongo:** MongoDB support for Flask applications.

` Flask-PyMongo==2.0.1`

**bcrypt:** In order to do the password hashing when user register.

`bcrypt==3.2.0  `

**mockupdb** Mock server for testing MongoDB clients and creating MongoDB Wire Protocol servers.

`mockupdb==1.7.0 `

#### Libraries:
- **[jQuery](https://jquery.com/)** Is needed for the **[Materialize](https://materializecss.com/)** JavaScript components to function.

- **[Material Icons:](https://material.io/tools/icons/?style=baseline)** to add extra features on several parts of the website.

- **[Google Fonts:](https://fonts.google.com/)** to style the fonts on the website.

#### Version control system:
- **[Gitpod](https://www.gitpod.io/)** to code the website.

- **[Github](https://github.com/)** to host the repository of all previous versions of the build and linked to Heroku to push the latest changes to the deployed build version held there.

#### Hosting service:
**[Heroku:](https://www.heroku.com/)** to deploy the website.

## Testing

### Validation

- **[HTML:](https://validator.w3.org/)** to validate the HTML code.

- **[CSS:](https://jigsaw.w3.org/css-validator/)** to validate the CSS code.

- **[JavaScript](https://jshint.com/)** to check the JavaScript code.

- **[Responsinator](http://www.responsinator.com/)**
    - The project used **Responsinator** to determine if the site was responsive to various devices.

- **[Am I Responsive](http://ami.responsivedesign.is/#)** to view images of the website on different devices if the site was responsive to various devices.

- Chrome DevTools
    - For this project, the web developer tools built directly into the Google Chrome browser was used to help edit pages and diagnose problems quickly.
    - Lighthouse in Google dev tool
    - For testing the performance of the website

- **[Link Checker](https://validator.w3.org/checklink)** to check all links on the website and see if all links work. 



- **[TestProject](https://testproject.io/)**
    - For automated testing of website

- **[Python Tester](https://extendsclass.com/python-tester.html)**
    - Python code syntax checker

- **[Closing Tag Checker for HTML5](https://www.aliciaramirez.com/closing-tags-checker/)**
    - Validates all tags are opening and closing correctly.

- **[Google Mobile-Friendly Test Mobile](https://search.google.com/test/mobile-friendly)**
    - To check if site is mobiole friendly

- **[AutoPrefixer](https://autoprefixer.github.io/)**
    - Autoprefixer to parse CSS and adds vendor prefixes

## **Deployment**
This project uses GitHub for version control, GitPod as the cloud-based IDE and Heroku to deploy the site into production. The below steps are specific to Gitpod therefore depending on your IDE, you might need to adjust the below steps.

### To clone the project:
From the application's repository, click the "code" button and download the zip of the repository. Alternatively, you can clone the repository using the following line in your terminal: 
```
git clone https://github.com/Franciskadtt/the-growth-club.git
```

The following must be installed on your IDE:
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Python 3](https://www.python.org/downloads/)

### Database Creation with MongoDB Atlas
You have to create an account with MongoDB. You can see [here](https://docs.atlas.mongodb.com/) how to set up your MongoDB Atlas account. Sign-in or sign-up to MongoDB and create a new cluster then follow the below steps:
1. Go to Collections
2. Go to "+Create Database"
3. Click on "Create Collection"
4. Then add all the collections (see data structure above)
5. Click on "Insert Document"
6. Add key and value - then click "Insert"

### Create the Flask Application
1. Install Flask - type in terminal: 
    ```
    pip3 install Flask
    ```
2. Now we need to create a few new files. First, our Python file that will be the foundation of our application. You can name it something else, in this case, I used app.py, so type in the terminal: 
    ```
    touch app.py
    ```
3. Next, we will be storing some sensitive data, and we need to hide them using environment variables. You can use the terminal or just create a new file. I used the terminal, so type in the terminal:
    ```
    touch env.py
    ```
4. That file should never be pushed to GitHub, so we need to be able to ignore it somehow, so type in the terminal:
    ```
   touch .gitignore
    ```
5. Double check in the gitignore file that you see "env.py" and "pycache/"
6. Go to the env.py file and add the following:
    ```
    import os
 
    os.environ["PORT"] = "5000"
    os.environ["SECRET_KEY"] = "YOUR_SECRET_KEY"
    os.environ["DEBUG"] = "True"
    os.environ["MONGO_URI"] = "YOUR_MONGODB_URI"
    os.environ["MONGO_DBNAME"]= "DATABASE_NAME"
    ```
7. Go to app.py file and import the following:
    ```
    import os
    from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
    from flask_pymongo import PyMongo
    from bson.objectid import ObjectId
    from werkzeug.security import generate_password_hash, check_password_hash
    if os.path.exists("env.py"):
        import env
    ```
8. Create an instance of Flask
    ```
    app = Flask(__name__)
    ```
9. To test your application, tell your app how and where to run your application. Set your IP and PORT environment variables in the hidden env.py file. Make sure to update this to debug=False before the actual deployment of your project.
    ```
    if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)
    ```
10. You can now run your application, type in the terminal:
    ```
    python3 app.py
    ```

### Deploying to Heroku
1. In the workspace terminal, run pip3 freeze --local > requirements.txt to collect any dependencies.
2. Run python app.py > Procfile to create a Procfile required for Heroku deployment.
3. Go to the [Heroku](https://www.heroku.com/) website. Register for an account and click on "Create a new app".
4. Setup a Heroku app within the Heroku dashboard - Type in the app name and select region the click on create app.
5. In Heroku, in your app, click on "GitHub" to connect to your repository. Type in the repository name as on GitHub. Click on "Connect".
6. Search for your repo (or sign in and connect GitHub account) and select this.
7. In the 'settings tab, click 'Reveal Config Vars' and input your environment variable from your local build in the key/value inputs.
8. Then click "Hide Config Vars" in Heroku.
9. In Heroku, select 'Automatic Deploys' to automatically rebuild the app when a new Git commit is pushed.
10. Once the initial build is complete, click 'Open App' in the top right of the screen to view the application.

## **Credits**

### **Content**
- The copy and text for this website was created by Teema Namdarian 

### **Media**
- All Images used are from [Pixabay](https://pixabay.com/)

### **Code**
- CSS for color roots adapted from [CSS Tricks](https://css-tricks.com/the-shapes-of-css/)
- HTML for the navbar and form adapted from [Materialize](https://materializecss.com/)
- HTML for modals adapted from [Materialize](https://materializecss.com/)
- JQuery for validation from Task Manager walkhtrough project by Code Institute
- JQuery for navbar menu active item adapted from [InfoWorld](https://www.infoworld.com/article/3304440/setting-an-active-menu-item-based-on-the-current-url-with-jquery.html)
- JQuery for bookmark from adpated from https://stackoverflow.com/questions/5828965/bookmark-on-click-using-jquery

### **Acknowledgements**
As always the **slack** community has been very helpful when I had any question.

I'm also really thankful to the **tutors** who help me understand how to set up environmental variables in vscode.

And thanks to my **mentor** Guido Cecilio Garcia for helping me with this project.
