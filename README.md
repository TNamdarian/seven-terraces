# Seven Terraces! – Third milestone project
Seven Terraces is an app that allows its users to save their properties online and edit them anytime they need to. This app also allows the users to share their properties with other users, save the properties that they like and contact the admin if they have enquiries. 

The app also gives the users the option to search for properties based on names and descriptions. 

![Seven Terraces](/documentation/mockups/am_i_responsive.png)

[View live version of website via Heroku](https://seven-terraces.herokuapp.com/)
___
<br>

<a></a>
## Table of Contents 
* [UX](#ux)
    * [User Goals](#user-goals) 
    * [Site Owners Goals](#site-owners-goals) 
    * [User Requirements and Expectations](#user-requirements-and-expectations)
        * [Requirements](#requirements)
        * [Expectations](#expectations)
    * [User Stories](#user-stories)
        * [Guest Users](#guest-users)
        * [Registered Users](#registered-users)
        * [Admin Users](#admin-users)
* [UI Design](#ui-design) 
    * [Font](#font)
    * [Colour Scheme](#colour-scheme)
    * [Icons](#icons)
    * [Structure](#structure)
* [Wireframes](#wireframes)
* [Data Structure](#data-structure)
* [Existing Features](#existing-features)
* [Future Features](#future-features)
* [Technologies used](#technologies-used)
    * [Languages](#languages)
    * [Libraries & Frameworks](#libraries-&-frameworkes)
    * [Tools](#tools)
    * [Design](#design)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)
___
<br>

<a name="ux"></a>
## **UX**
### **User Persona**
This website project will target users who are interested in viewing and sharing information about property deals. The main focus is on providing an easy to navigate and responsive website that allows users to be a part of a community with a portfolio of properties. Most pages except "View property", "Add property" and "Edit proeprty" use parallax feature to make the site more visually appealing. As these three pages are content heavy, parallax feature has been excluded for them. 

<a></a>
### **User Goals**
- View **featured properties** posts per month created by the admin;
- View **property posts** created by the Seven Terraces community;
- View, edit, search, delete **property posts** created by them;
- The website has to work well on all kinds of devices like mobile phones, tablets and desktops.

<a></a>
### **Site Owners Goals**
- Be the “go-to” place for users to source property deals. 
- To create a community for users to source property deals for one another.

<a></a>
### **User Requirements and Expectations**
#### **Requirements**
- Easy to navigate by using the navigation menu.
- Relevant content for each strategy.
- Appealing visuals.
- Easy way to find properties relevant to the user.
#### **Expectations**
- When clicking social media links expect the page to open in a separate browser.
- Expect that the navigation links work properly to take the user where they intended to go.
- Expect to be able to read, add, edit or delete items created by the user.
- Feedback whether or not registered, logged in, logged out.

<a></a>
### **User Stories**
#### **Guest User**
1. As a Guest User, I want the main purpose of the site to be clear so that I immediately know what the site is intended for upon entering;
2. As a Guest User, I want to be met with a visually appealing and easy to read layout of created items;
3. As a Guest User, I want to view the **featured property** posts of the month to get a sense of the value if I sign up as a registered user and they don't have to search for it;
4. As a Guest User, I want to be able to sign-up to create and edit my own **property posts**;
5. As a Guest User, I want to be able to get in contact via social media if I like enquire about properties or have suggestions.
#### **Registered User**
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
13. As a Registered User, I want to be able to get in touch with the admin regarding the deals I’m interested in viewing. 
#### **Admin User**
The Admin user shares the same expectations as the Registered user with some additional ones as below:
1. As an Admin User, I would like the ability to **log in to an admin account** so that I can **create, edit and delete featured property posts** for each month;
2. As an Admin User, I want to be able to view all **property posts** added by other members of the community as well as the ability to **edit or delete any property posts** so that I can **maintain the site to stay updated**
___
<br>

<a></a>
## **UI Design**
### **Font**
- I used [Google Fonts](https://fonts.google.com/) to highlight the various texts.
- The project has the main font of [Roboto](https://fonts.google.com/specimen/Roboto) as it is easy to read and modern
- “Sans-Serif” is used as the default backup font in cases Roboto has difficulty loading.

<a></a>
### **Colour Scheme**
- The colour scheme is based on creating an environment with energy, excitement and warmth;
- The logo was created on [Wix logo maker](https://www.wix.com/logo/maker/esh/zoe-editor?industry=%7B%22industry%22%3A%22609d10f90c3f7f79f9eed882_bf61b613f48c3e7af17cfc6c_property%20landing%20page%22%2C%22isCustom%22%3Afalse%7D&tags=creative%2Cformal%2Ctimeless%2Cdynamic&selectedWebsiteId=0&logoId=f9be001c-54be-4ac7-81c2-eea8e24dd21e&referralAdditionalInfo=arenaSplitPage) 
- All colours were checked with WebAIM [https://webaim.org/properties/contrastchecker/](https://webaim.org/properties/contrastchecker/) to check the accessibility of the colours and present a pass.

![Results](/documentation/mockups/contrast_test.png)

<a></a>
#### **Colour Palette**
Below is the colour scheme used for the website. 
![Colour Palette](/documentation/mockups/colour_palette.png) 
![Colour Palette](/documentation/mockups/colour_palette2.png) 

using [https://coolors.co/](https://coolors.co/)
- #FFFFFF: This colour is used for the background.
- #FCA311: This colour is used as the main text colour and where the background of the CTA buttons.
- #14213D: This colour is used as the primary colour and sets the tone for the website. It’s the dominant colour in the footer, header and background images in the heading. It’s also the colour of some texts. 
- #000000: This colour is used as a secondary colour for fonts.
- #E5E5E5: This colour is used as a tertiary accent colour where something to highlight forms. 
- #8ECAE6: This colour is used as an accent colour and mainly used for hovering over some buttons. 
- #219EBC: This colour is also used as an accent colour and mainly used for hovering over some buttons. 
For the social media, the colours match the exact tones of these applications using [https://www.webnots.com/color-codes-for-social-networking-site-icons/](https://www.webnots.com/color-codes-for-social-networking-site-icons/). 

<a></a>
### **Icons**
- **[Materialized:](https://materializecss.com/)** Majority of icons from the Materialized Icons library was used unless there was not an appropriate icon available then the Font Awesome library is used. 
- **[FontAwesome:](https://fontawesome.com/)** In some cases if a FontAwesome icon was more appropriate I have also used FontAwesome.

<a></a>
### **Structure**
The overall structure that was used is the Materialize framework. Materialize provides various elements of CSS and Javascript which is very helpful to keep a good structure on applications. 

___
<br>

<a></a>
## **Wireframes**
I have used Balsamic to create low-fidelity wireframes. First I created a basic wireframe for desktops. The website will be easy to navigate by using the navigation bar or by scrolling down the page.

Below you can see the mock-ups that I drew using 
[Balsamiq](https://balsamiq.com/#) 

[WireFrames](https://balsamiq.cloud/s8m4gdi/pwvh8nd)

*Guest User*
- [Landing Page](/documentation/mockups/landing_page.png)
- [Log In Page](/documentation/mockups/log_in.png)
- [Registration Page](/documentation/mockups/sign_up.png)

*Registered User*
- [Landing Page](/documentation/mockups/landing_page.png)
- [Profile Page](/documentation/mockups/profile.png)
- [Properties Page](/documentation/mockups/properties.png)
- [Contact Page](/documentation/mockups/contact_us.png)
- [View_property](/documentation/mockups/view_property.png)
- [Add_property](/documentation/mockups/add_property.png)
- [Edit_property](/documentation/mockups/edit_property.png)

*Admin User*
- [Landing Page](/documentation/mockups/landing_page.png)
- [Manage Properties Admin Dashboard Page](/documentation/mockups/admin_dashboard.png)

The final website differs from the original wire-frames because, when working on the design, I sometimes I found more appropriate ways to display different sections.
___
<br>

<a></a>
## **Data Structure**
A database structure was designed to be specifically suited for Seven Terraces. It was important to make sure the nesting relationships between the collections and the keys worked logically. The database was created as a usable non-relational database where data is stored in a consistent and well-organised manner. To maintain a database configuration in a single location where it can be changed easily, ObjectId's are used in several collections to ensure key values are more accurate by using the ObjectId's rather than strings.

**[MongoDB](https://www.mongodb.com/)** is utilised to store data for Seven Terraces. It is a non-relational database-backed Flask web application that allows users to easily create, locate, display, edit and delete data records on Seven Terraces web app.

The data structure outline: ![Data Structure](/documentation/mockups/collections.png)

### **Collections**
- **Categories collection**
    - This collection holds the strategy_name key which is a string datatype. 
    - This field data is passed to other collections by utilising the ObjectID rather than the string above.

- **Properties collection**
    - This collection holds several keys for the properties page where the user can view all the properties in the database.
    - The data keys include the strategy name, property name, description, date added, features, link to the image, type, price, sourcing fee, property_details, property description and author.  
    - All the above keys are strings except for the property details, features, and amenities which are arrays. Featured is a Boolean. 

- **Amenities collection**
    - This collection holds several keys for the amenities where the user can view all the amenities in the database.
    - This field data is passed to other collections by utilising the ObjectID rather than the string above.

- **Type collection**
    - This collection holds the type key which is a string datatype. 
    - This field data is passed to other collections by utilising the ObjectID rather than the string above.

- **Users collection**
    - This collection holds several keys about the user which is provided by the user on the register page and used again on the log in page.
    - The data keys include the username, password and bookmarks. 
    - All the above keys are strings except for the bookmarks key as this is an array datatype. 
    - The bookmarks key is created if the user has bookmarked a property on the properties page. The property ObjectID is then used as the value for the item in the array.
<br>

<a></a>
## **Existing Features**
- There is a mobile-first focus and therefore I wanted to keep in mind first what will work on mobile.
### Elements on every page
#### Header
1. Logo
- Allows the user to easily recognise the brand of Seven Terraces”. If the user clicks on the logo, it will return the users to the “Home” section as they would expect.

2. Navbar
- Navigation Bar - Allows the user to easily navigate the website's sections and find what they are looking for with ease and speed.
- The navigation bar features the Seven Terraces logo in the top left corner.
- For visitors to the site who are not logged in (*Guest Users*), these menu links are available for them to use:
    - Home
    - Log in
    - Sign Up 
- For users who are logged in(*Registered Users*), the list items are as follows:
    - Home
    - Properties
    - Profile 
    - Contact
    - Log out
- Python determines if the user is logged in or not by checking if 'user' in session and passes this data to Jinja to display the correct navbar for the user.
- The navbar is collapsed into a burger icon on small screens.

#### Footer
- The footer features links to social media for Social Icons - Allows the user to access the social platforms. Since this is a fictional website, the links take the users to the home page of these sites. 

### Landing Page
- The landing page gives the user an immediate welcome and indication of what the site is about.
- Scrolling down, users can view the Featured Properties of the month (Featured Properties section) which was important that they go there if they want to quickly find the most recent Properties added by the administrator.

#### Featured Section
- On the landing page the featured Properties of the month is selected and added by the administrator.
- The purpose is to have one Property for each strategy each month to be showcased.
- Guest users are also able to view these Properties as well as Registered users. 

### Log in Page
- The login page features a simple **form** where the user can enter either their username and password.
- There is helper text under each input field to guide the user as to the parameters they can input.
- The user will receive validation or error feedback when they enter information in the input field which is also be accompanied by colours to show validation (green for correct and red for incorrect).
- If the user lands on the log in page but realises they don't have an account yet and would like to register, there is a link on the page that will take them to the registration page or they can click on the navbar menu Sign up button.

### Profile Page 
- Then if the user logs in or register successfully they are taken to their Profile Page.
- This page will feature their username at the top to personalise the user experience.
- There are links to take the user to the Properties Page or the Featured section on the landing page.
- The user can see all their bookmarked Properties on their profile if they have any.
- The user can change their password if they click on the Change Password button. A modal will pop up and ask for the new password. If they confirm to change their password, their password will be updated in the database under the Users collection.
- The user can delete their profile if they click on the Delete Profile link. This will open a modal to confirm if they want to continue to delete their profile. If they confirm, their username, email and password will be detailed from the Users collection. They will then be logged out and returned to the landing page as Guest users.

### Properties Page
- Only a Registered user can view the Properties Page where the registered user can then view, search, add, edit or delete properties. The edit and delete functions will only be available if the user created the property.
- The user can search by property description and reset the search box. If there are no results, there will be a message to the user to say there are no results.
- If the user clicks on the "Add Properties" button it will take them to the Add Property Page.
- If the user created the property, they will see the edit button for the property. If the user clicks on the "Edit" button it will take them to the Edit Property Page.
- If the user created the property, they will see the delete button for the property. If the user clicks on the "Delete" button, the property will be deleted.
- The user can bookmark a property. If they click on the bookmark icon, this will confirm to them it has been added as a bookmark and appears on their profile.
- Each time a property is viewed the number of views will increase which will indicate the popularity of the property. 

### View Property Page
- If the user clicked on the view property button on a property card then they will be taken to this page.
- The view property page features all the details of the property including name, image, type, strategy, amenities, features, price and sourcing fees as well as propery descriptions and details. 
- If the user is the creator of that property, they should be able to have access to the delete and edit buttons on the same page. 

### Registration & Sign Up Page
- The sign-up page features a simple form, where the user can input a username and password. The form was kept deliberately simple so that signup has minimum barriers.
- If the user lands on the registration page but realises they already have an account and would like to log in, there is a link on the page that will take them to the login page or they can click on the navbar menu Log in Page link. 
- There is a message to the user about not sharing their information to put the user's mind at ease.

### Add Property Page
- If the user clicked on the Add Property button on the Properties page then they will be taken to this page.
- The add Properties page features a simple form, where the user can input the basic required information.
- The user will be able to select from the current categories as well as additional information to all the required fields for the Property.
- There is helper text under each input field to guide the user as to the parameters they can input.
- The user will receive validation or error feedback when they enter information in the input field which is also be accompanied by colours to show validation (green for correct and red for incorrect).
- If the user clicks add property button, it will add the new property to the database.
- If the user clicks on the cancel button it will take them back to the Properties Page.

### Edit Property Page
- The edit properties page features a simple form, where the user can edit only a property added by them. 
- If the user clicked on the Edit Property button on the Properties Page then they will be taken to this page. They will only be able to edit the property if they created the property.
- The current property information will be shown and the user can change the information and save it. This will update the database with the new information.
- The user will be able to select from the current categories and types, amenities as well as additional information to all the required fields for the property.
- There is helper text under each input field to guide the user as to the parameters they can input.
- The user will receive validation or error feedback when they enter information in the input field which is also be accompanied by colours to show validation (green for correct and red for incorrect).
- If the user clicks on the cancel button it will take them back to the Properties Page.

### Admin Dashboard Page
- This page can only be viewed by the admin user.
- From here the user can manage the featured Properties, and categories. 
- The admin user can add a new featured Property or edit current featured Properties. If the admin user clicks on the Add new Featured Properties button, then they will be taken to the Property page. If the admin usercan toggle on the switch button on the property card, it will take them to the landing page so that they can view featured Property form directly from the featured section.
- The admin user can add a new strategy if they click on the Add strategy button. This will take them to the Add New strategy page.
- The admin user can edit current Categories. If the user clicks on the edit button for that strategy, they will be taken to that edit strategy page. 

#### Add New Strategy page
- This page can only be viewed by the admin user.
- If the admin user clicked on Add new strategy button on the Dashboard, then this page will display.
- The Add New strategy page features a simple form, where the admin user can input the basic required information. 
- There is helper text under each input field to guide the admin user as to the parameters they can input.
- The admin user will receive validation or error feedback when they enter information in the input field which is also be accompanied by colours to show validation (green for correct and red for incorrect).
- If the admin user clicks Add strategy button, it will add the new strategy to the database in the Categories collection.
- If the user clicks on the cancel button it will take them back to the Manage Properties admin dashboard page.

#### Edit Strategy page
- This page can only be viewed by the admin user.
- If the admin user clicked on the Edit strategy button on the Dashboard, then this page will display.
- The current strategy information will be shown and the admin user can change the information and save it. This will update the database with the new information.
- There is helper text under the input field to guide the user as to the parameters they can input.
- The user will receive validation or error feedback when they enter information in the input field which is also be accompanied by colours to show validation (green for correct and red for incorrect).
- If the admin user clicks the Update strategy button, it will update the strategy in the database for the Categories collection.
- If the user clicks on the cancel button it will take them back to the Manage Properties admin dashboard page.

### Log Out 
- If a registered or admin user clicks on the log out button, they will be logged out of their current session and will no longer be able to see the pages they would if they were logged in.
- A registered user will have to log in again if they want to see their Profile or the Properties Page.
- A Admin user will have to log in again if they want to see their Profile, Properties Page or the Manage Property Dashboard Page.
___
<br>

<a></a>
## **Future Features**
These are possible future features to be added to the project which was suggested by users during the usability tests. As these features were not part of a minimum viable products launch phase, they will be implemented in future releases.
- Have a 'forgot password' functionality on the log in page.
- Have a more extensive user profile with, profile image, preferences and email to which you can send updates, newsletters etc. Have a profile feature to view the Properties the user added there.
- Events in the form of a calendar to visually represent events and not have it be part of the general properties.
- User can search by any word related to the property also, have the searched word stay in the search box
- Adding filters to only display properties according to amenities, price, types and dates. I thought of this feature once the website was finished and I couldn't spend more time working on the project as I needed to get going with the rest of the course.
- Currently, the feedback for bookmarking appears on the profile page. In future, the plan is to have feedback to the user about bookmarking a Property on the Properties page.
- If a user adds a property, it will be added to the top. Therefore, a user will always see the most recent properties added to the site. 
- I'd like to add some feature to the site, so the users can view their properties added in one section. 
- I would like the users to be able to filter properties from the most expensive to the cheapest in the future. 
- I'd like the rewrite the code for the bookmark funtionality using ajax, POST or PUT methods.
___
<br>

<a></a>
## **Technologies Used**

### **Languages**
- This project uses HTML, CSS, JavaScript and Python programming languages.

### **Libraries & Frameworks**
- [Materialize](https://materializecss.com/)
    - The project uses **Materialize** to simplify the structure of the website and help make the website responsive easy to do. The majority of the icons used in this project are from the Materlize library.
- [Font Awesome](https://fontawesome.com/)
    - Where the Materialize icon library did not have a usable icon, the fallback icon library used was the Fontawesome for the icons.
- [Google Fonts](https://fonts.google.com/)
    - The project uses **Google fonts** to style the website fonts.
- [Hover.css](https://cdnjs.com/libraries/hover.css/2.1.0)
    - The project uses **Hover.css** to apply hover effects to the projects navbar.
- [Pymongo](https://pypi.org/project/pymongo/) and [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/) 
    - To connect Python and Flask to the MongoDB database
- [Flask](https://flask.palletsprojects.com/en/2.0.x/) 
    - To construct and render pages.
- [MongoDB Atlas](https://www.mongodb.com/)
    - Non-relational database hosting service used.
- [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/ )
    - A WSGI web application library used for passwords for Python.
- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)
    - Templating language for Python, to simplify displaying data from the backend of this project smoothly and effectively in HTML.
- [jQuery](https://jquery.com/)
    - JavaScript library
- [MongoDB](https://www.mongodb.com/) 
    - to store user data. 

### **Tools**
- [Gitpod](https://www.gitpod.io/)
    - IDE used to build the website
- [Github](https://github.com/)
    - Used to host the repository of all previous versions of the build and linked to Heroku to push the latest changes to the deployed build version held there.
- [Heroku](https://www.heroku.com/)
    - A cloud platform as a service enabling deployment of the site.
- [Am I Responsive](http://ami.responsivedesign.is/#)
    - The project used **Am I Responsive** to view images of the website on different devices if the site was responsive to various devices.
- [W3C Markup Validator](https://validator.w3.org/)
    - For testing HTML code
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
    - For testing CSS code
- [JSHint Validator](https://jshint.com/)
    - For detecting errors and potential problems in your JavaScript code
- [Python Tester](https://extendsclass.com/python-tester.html) 
    - Python code syntax checker
- [PEP8 online checker](pep8online.compep8online.com)
    - to ckeck Pyton code is PEP complient. 
- [Google Mobile-Friendly Test Mobile](https://search.google.com/test/mobile-friendly)
    - To check if site is mobiole friendly
- [Tiny-PNG](https://tinypng.com/)
    - I used tinypng for big images up to 5M needed to be compressed to improve the website's loading time.
- [CompressJPEG](https://compressjpeg.com/) 
    - The big images bigger than 5M needed to be compressed to improve the website's loading time.
- Chrome DevTools
    - For this project, the web developer tools built directly into the Google Chrome browser was used to help edit pages and diagnose problems quickly.

### **Design**
- [Balsamiq](https://balsamiq.com/)
    - To design low fidelity mockups
___
<br>

<a></a>
## **Testing**
Testing information can be found in the separate [TESTING.md file](documentation/TESTING.md)
___
<br>

<a></a>
## **Deployment**
This project uses GitHub for version control, GitPod as the cloud-based IDE and Heroku to deploy the site into production. The below steps are specific to Gitpod therefore depending on your IDE, you might need to adjust the below steps.

### To clone the project:
From the application's repository, click the "code" button and download the zip of the repository. Alternatively, you can clone the repository using the following line in your terminal: 
```
git clone https://github.com/TNamdarian/seven-terraces
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

___
<br>

<a></a>
## **Credits**

### **Content**
- The contents for this website was written by Teema Namdarian. 
- The information about each property was copied from [onthemarket](https://www.onthemarket.com/). 

### **Media**
- The images used are from [Pixabay](https://pixabay.com/) and [onthemarket](https://www.onthemarket.com/).

### **Code**
- CSS for color roots adapted from [CSS Tricks](https://css-tricks.com/the-shapes-of-css/)
- HTML for the navbar and form adapted from [Materialize](https://materializecss.com/)
- HTML for modals adapted from [Materialize](https://materializecss.com/)
- JQuery for validation from Task Manager walkhtrough project by Code Institute
- JQuery for navbar menu active item adapted from [InfoWorld](https://www.infoworld.com/article/3304440/setting-an-active-menu-item-based-on-the-current-url-with-jquery.html)
- JQuery for bookmark from adpated from https://stackoverflow.com/questions/5828965/bookmark-on-click-using-jquery

### **Acknowledgements**
For the design of the site, I was sinpired by the following sites in terms of UX and UI designs: 
- [the-growth-club](https://github.com/Franciskadtt/the-growth-club). 
- [CookBook](https://github.com/elenasacristan/CookBook)

As always the **slack** community has been very helpful when I had any question.

I'm also really thankful to the **tutors** who help me understand how to set up environmental variables in vscode.

And HUGE thanks to my **mentor** Guido Cecilio Garcia for helping me with this project.

##### back to [top](#table-of-contents)