# The Seven Terraces Website - Testing details

[Main README.md file](/README.md)

[View live version of website via Heroku](https://seven-terraces.herokuapp.com/)
<br>

<a></a>
## Table of Contents 
* [Test User Stories](#test-user-stories)
* [Testing and Validation](#testing-and-validation) 
* [Manual testing](#manual-testing)
* [Bugs and Fixes](#bugs-and-fixes)
* [Further testing](#further-testing)
___
<br>

## **Test User Stories**
Testing user stories from the UX section
### *Guest User*
1. As a Guest User, I want the main purpose of the site to be clear so that I immediately know what the site is intended for upon entering;
- On the Home page landing section, it is clear what the site is about. 
   - [Landing section on Home page](/documentation/images/test_screenshots/landing_section_landing_page.png)
2. As a Guest User, I want to be met with a visually appealing and easy to read layout of created items;
- From the landing page and throughout the rest of the web app, the background is light and the text is darker for a modern and visually appealing site. The font is also large to ensure that the site is easy to read.
   - [Landing section on Home page](/documentation/images/test_screenshots/landing_section_landing_page.png)
3. As a Guest User, I want to view the featured **properties posts** of the month to get a sense of the value if I sign up as a registered user and they don't have to search for it;
- On the Home page a Guest user can see the featured items added by the administrator
   - [Featured section on Home page](/documentation/images/test_screenshots/featured_section_landing_page.png)
4. As a Guest User, I want to be able to sign-up to create and edit my own **property posts**;
- The user can click on the signup button in the navbar which is indicated in orange. They will then be redirected to the Register page to sign up to view, add, search, edit, bookmark and delete properties. There is also a button on the bottom of the page that will take the user to the login page where they can log in or click on the registration link to be taken to the registration page. If the user successfully registers, they will see a confirmation message and be taken to their Profile page.
   - [Register Page](/documentation/images/test_screenshots/register_page.png)
   - [New Registered User Confirmation](/documentation/images/test_screenshots/new_registered_user_confirmation.png)
5. As a Guest User, I want to be able to get in contact via social media if I like the site or have suggestions.
- The user can get in contact or follow the created or the site on social media as their social links are in the footer on every page of the website.
   - [Footer](documentation/images/test_screenshots/footer.png)

### *Registered User*
1. As a Registered User, I want the main purpose of the site to be clear so that I immediately know what the site is intended for upon entering;
- On the Home page landing section, it is clear what the site is about.
   - [Landing section on Home page](/documentation/images/test_screenshots/landing_section_landing_page.png)
2. As a Registered User, I want to be met with a visually appealing and easy to read layout of created items;
- From the landing page and throughout the rest of the web app, the background is light and the text is darker for a modern and visually appealing site. The font is also large to ensure that the site is easy to read.
   - [Landing section on Home page](/documentation/images/test_screenshots/landing_section_landing_page.png)
3. As a Registered User, I want to view the featured items of the month so that I don't have to search for them;
 - On the Home page a Registered user can see the featured items added by the administrator.
   - [Featured section on Home page](/documentation/images/test_screenshots/featured_section_landing_page.png)
4. As a Registered User, I want to be able to log back into site with my initial latest credentials;
- The user can click on the login menu link in the navbar to be taken to the login page where they can use their credentials to log in to view the properties. The user will receive a login confirmation once they have logged in.
   - [Log In Page](/documentation/images/test_screenshots/log_in_page.png)
   - [Log In Confirmation](/documentation/images/test_screenshots/log_in_welcome_profile_page.png)
5. As a Registered User, I want to be able to view **property posts** added by other members of the community;
- The user can go to the properties page, either by clicking the button on the profile page or in the navbar. On the properties page, the user can view all the current properties.
   - [Properties Page](/documentation/images/test_screenshots/properties_page.png)
6. As a Registered User, I want to be able to create, edit and delete the **property posts** I have added;
- On the Properties Page the user can click on the "Add property" button and will be taken to the Add properties Page where they can fill in the form and add a property. The form will have helper text to guide the user as well as validation.
   - [Properties Page](/documentation/images/test_screenshots/properties_page.png)
   - [Add Property Page](/documentation/images/test_screenshots/add_property_page.png)
   - [Property Added Confirmation](/documentation/images/test_screenshots/property_added_confirmation.png)
- On the properties Page the user can see an edit or delete button if they created the property, otherwise, they will not be able to edit or delete a property. If the property is edited, the user will receive confirmation that the property is edited & updated.
   - [Viewing Edit & Delete Buttons](/documentation/images/test_screenshots/delete_edit_buttons.png)
   - [Edit Property Page](/documentation/images/test_screenshots/edit_property_page.png)
   - [Edit Property Confirmation](/documentation/images/test_screenshots/edit_property_confirmation.png)
- If the user clicks on the delete button, they are asked for confirmation before they delete it. If the property is deleted, the user will receive confirmation that the property is deleted
   - [Delete Modal](/documentation/images/test_screenshots/delete_modal.png)
   - [Delete Property Confirmation](/documentation/images/test_screenshots/delete_property_confirmation.png)
7. As a Registered User, I would like to be able to search the site so that I can easily find properties that I am looking for;
- On the properties The user will be able to type text in the search input field and find properties that have keywords in their description. If no properties are found, then the user will see "No results found" and they can reset the search.
   - [Search Field](/documentation/images/test_screenshots/properties_search.png)
   - [No search results](/documentation/images/test_screenshots/no_results_search.png)
8. As a Registered User, I want to be able to bookmark properties I find interesting and remove a bookmark.
- On the properties page, the user can bookmark a property by clicking on the bookmark icon which will turn orange to show it was bookmarked. 
   - [Property Page: Bookmarked Properties](/documentation/images/test_screenshots/bookmarked_property_page.png)
- If the user has bookmarked properties, it will appear on their profile under the Bookmarks section.
   - [Profile page: Bookmarked Properties](/documentation/images/test_screenshots/bookmarked_profile.png)
- If the user wants to remove the bookmark they can click on the "x" button and the property will be removed, they will receive a confirmation message.
   - [Profile Page: Removed Bookmark Confirmation](/documentation/images/test_screenshots/bookmark_remove_confirmation.png)
9. As a Registered User, I want to be able to change my password on my profile;
- The user can change their password if they click on the "Change Password" button on the Profile page. If the user clicked on the Change password button, a modal will open and ask them to type in their new password. If they confirm to change their password, they will receive a confirmation message.
   - [Change Password Button](/documentation/images/test_screenshots/change_password_delete_profile_buttons.png)
   - [Change Password Modal](/documentation/images/test_screenshots/change_password_modal.png)
   - [Change Password Confirmation](/documentation/images/test_screenshots/password_confirmation.png)
10. As a Registered User, I want to be able to delete my account and profile;
- The user can delete their profile from their profile page. If they click on the "Delete Profile" link a modal will appear where it asks for confirmation. The user needs to enter their password and click on the confirmation button which will delete their profile. If their account was successfully deleted, then they will receive a confirmation message and returned it to the Home Page.
   - [Delete Profile Button](/documentation/images/test_screenshots/change_password_delete_profile_buttons.png)
   - [Delete Profile Modal](/documentation/images/test_screenshots/delete_profile_modal.png)
   - [Deleted Profile Confirmation](/documentation/images/test_screenshots/delete_profile_confirmation.png)
11. As a Registered User, I want to be able to log out of my account;
 - The user can click on the log out button in the Navbar to log out of their account. They will receive a confirmation message if they are logged out of their account successfully and be taken to the Home Page.
   - [Log Out Link](/documentation/images/test_screenshots/log_out_link.png)
   - [Log Out Confirmation](/documentation/images/test_screenshots/log_out_confirmation.png)
12. As a Registered User, I want to be able to get in contact via social media if I like the site or have suggestions.
 - The user can get in contact or follow the created or the site on social media as their social links are in the footer on every page of the website.
   - [Footer](/documentation/images/test_screenshots/footer.png)

### *Admin User*
The Admin user the same user stories as the Registered user above with the additional extras below:
1. As an Admin User, I would like the ability to **log in to an admin account** so that I can **create, edit and delete featured properties posts** for each month;
- The login features are similar to the above, but if the admin user is logged in, they can see the Manage properties Admin Dashboard. From here they can add & edit feature properties.
   - [Admin Dashboard Page](/documentation/images/test_screenshots/admin_dashboard.png)
- The admin user can add a featured property by clicking on the "Add featured property" button which will take them to the Add Featured property page where they can fill in the form and add a property. The form will have helper text to guide the user as well as validation. The user will receive confirmation if the featured property is added to the Home page Featured Section.
   - [Add Featured Properties](/documentation/images/test_screenshots/properties_page.png)
   - [Add Featured Properties Confirmation](/documentation/images/test_screenshots/add_featured_property_confirmation.png)
- The admin user can click on the "Edit or Delete Featured property" button on the Admin Dashboard and will be taken to the Featured property section on the Home page where they will be able to view Edit & Delete buttons. 
2. As an Admin User, I want to be able to view all **property posts** added by other members of the community as well as the ability to **edit or delete any property posts** so that I can **maintain the site to stay updated**
- The admin user can view all properties and also the edit & delete buttons. They can edit or delete any property regardless of who added the property.
    - [Admin User View of Property Page](/documentation/images/test_screenshots/property_page_view_admin.png)
___
<br>

##  **Testing and Validation**
### [Am I Responsive](http://ami.responsivedesign.is/)
- To view images of the website on different devices.
- Final version: [Am I Responsive ](/documentation/images/validator_screenshots/am_i_responsive.png)

### JavaScript
- [JSHint](https://jshint.com/)
   - [Test JavaScript Validation](/documentation/images/validator_screenshots/jshint_test.png)
   - [Final JavaScript Validation](/documentation/images/validator_screenshots/jshint_final.png)
   - Final version - addressing errors and warnings: 
      - Warning for ''let' is available in ES6 (use 'esversion: 6'). Can be safely ignored. If add /*jshint esversion: 6 */ at top of code so that JSHint does not raise unnecessary warnings for ECMAScript 6 features.
      - JSHint flags Jquery $ symbol as an undefined variable - safely ignored. 
- [JSEsprima](https://esprima.org/)
   - [Final JavaScript Validated](/documentation/images/validator_screenshots/js_esprima_final.png)

### [CSS: W3C CSS validation](https://jigsaw.w3.org/css-validator/)
- [Final CSS Validation](/documentation/images/validator_screenshots/css-validation.png)

### [HTML: W3C Markup Validation](https://validator.w3.org/)
- To validate the HTML code of the project by pasting code in by direct input method. Note the W3C Validator for HTML does not understand the Jinja templating syntax therefore if there are warnings related to this, this can be safely ignored.
- Final version: no errors or warnings
- Testing and Final results per page:
   - Error Pages - No Errors in testing and finally
      - [Error Pages Final](/documentation/images/validator_screenshots/html_validator_404_page_test.png)
   - Add Category Page - No Errors in testing and final
      - [Add Category Page - Final](/documentation/images/validator_screenshots/html_validator_add_category_page_final.png)
   - Edit Category Page - No Errors in testing and final
      - [Edit Category Page - Final](/documentation/images/validator_screenshots/html_validator_edit_category_page_final.png)
   - Add properties Page - No Errors in testing and final
      - [Add property Page - Final](/documentation/images/validator_screenshots/html_validator_add_property_page_final.png)
   - View properties Page - No Errors in testing and final
      - [View property Page - Final](/documentation/images/validator_screenshots/html_validator_view_property_page_final.png)
   - Add Admin Dashboard Page - Some errors in testing and no errors finally
      - [Add Admin Dashboard Page - Test](/documentation/images/validator_screenshots/html_validator_admin_dashboard_page_test.png)
      - [Add Admin Dashboard Page - Final](/documentation/images/validator_screenshots/html_validator_admin_dashboard_page_final.png)
   - Edit Category Page - No Errors in testing and final
      - [Edit Category Page  - Final](/documentation/images/validator_screenshots/html_validator_edit_category_page_final.png)
   - Edit property Page - No Errors in testing and final
      - [Edit property Page - Final](/documentation/images/validator_screenshots/html_validator_edit_property_page_final.png)
   - Home Page - Some errors in testing and no errors final
      - [Home Page - Test](/documentation/images/validator_screenshots/html_validator_home_page_test.png)
      - [Home Page - Final](/documentation/images/validator_screenshots/html_validator_home_page_final.png)
   - Log In Page - Some errors in testing and no errors final
      - [Log In Page - Test](/documentation/images/validator_screenshots/html_validator_login_page_test.png)
      - [Log In Page - Final](/documentation/images/validator_screenshots/html_validator_login_page_final.png)
   - Profile Page - Some errors in testing and no errors final
      - [Profile Page - Test](/documentation/images/validator_screenshots/html_validator_profile_page_test.png)
      - [Profile Page - Final](/documentation/images/validator_screenshots/html_validator_profile_page_final.png)
   - Register Page - No Errors in testing and final
      - [Register Page - Test](/documentation/images/validator_screenshots/html_validator_register_page_test.png)
      - [Register Page - Final](/documentation/images/validator_screenshots/html_validator_register_page_final.png)
   - Property Page - Some errors in testing and no errors final
      - [Properties Page - Test](/documentation/images/validator_screenshots/html_validator_property_page_test.png)
      - [Properties Page - Final](/documentation/images/validator_screenshots/html_validator_property_page_final.png)
   - Contact Page - Some errors in testing and no errors final
      - [Contact Page - Test](/documentation/images/validator_screenshots/html_validator_contact_page_test.png)
      - [Contact Page - Final](/documentation/images/validator_screenshots/html_validator_contact_page_final.png)

### Python
- [Extendsclass](https://extendsclass.com/python-tester.html) - No syntax errors
   - [Final Python Validated](/documentation/images/validator_screenshots/python_extendsclass_final.png)
- [PEP8 Online](/documentation/images/validator_screenshots/pep8-validation-results.png) 
   - [Final PEP Validation]() - Pythoon file is PEP8 compliant
___
<br>

## **Manual testing**
Manual testing of all elements and functionality on every page
1. Logo - click on the logo, returns to the “Home” section on all pages.
2. Navbar 
   - if *any user* click on the Home link - go to the Home page on all pages
   - if *Guest user* click on Login link - got to Login page
   - if *Guest user* click on Sign Up link - go to Register page 
   - if *Registered user* click on property link - go to the properties page
   - if *Registered user* click on Profile link - go to the Profile page
   - if *Registered user* click on the Log Out link - log the user out and go to the Home page
   - if *Admin user* click on Admin Dashboard link - go to Admin Dashboard page
3. Footer 
   - if *any user* click on the Instagram link - go to Instagram page
   - if *any user* click on the LinkedIn link - go to LinkedIn page
   - if *any user* click on the Twitter link - go to Twitter page
   - if *any user* click on the GitHub link - go to YouTube page. 
4. Landing Page
   - if *any user* click on the "View Featured properties of Month" Button - go to the Featured section at the bottom of the Home page
   - if *any user* click on each Featured property card "Visit property" button - go to the correct property external page
   - if *Guest user* click on "Log In to View More properties" button - got to Login page
   - if *Registered user* click on the "View More properties" button - go to the properties page
6. Registration & Sign Up Pages
   - if *Guest user* type in "Username", "Email" and "Password" fields - validation is given if correct and feedback is given if incorrect.
      - if click on the "Sign Up" button" user is added to the database, go to the profile page and feedback is given to the user that they are registered
   - if *any user* click on the "Login Here" link - go to the Login page
7. Log in Page
   - if *Registered users* type in their user details in the "Username" and "Password" fields validation is given if correct and feedback is given if incorrect.
      - if click on the "Login" button" the user is logged in, go to the profile page and feedback is given to the user that they are now logged in.
   - if *any user* click on the "Create an account here!" link - go to the Registration page
8. Profile Page 
   - if *Registered user* clicks on the "View Properties" button - go to properties Page
   - if *Registered user* clicks on the "View Featured properties" button - go to Home Page
   - if *Registered user* clicks on the "Change Password" button - open modal to change the password
      - if type in a new password and click the "Change password" button - the password is changed in the database and a success message is given to the user
      - if click on "Cancel" go back to a Profile page
   - if *Registered user* clicks on the "Click here to delete your profile" link - open modal to delete the account
      - if type in the password and click the "Delete my account forever" button - the account is deleted in the database and a success message is given to the user.
      - if click on "Cancel" go back to a Profile page
9. Properties Page
   - if *Registered user* type text in the search field and click on the "Search" button", the relevant matching property is shown. If there are no matching properties, the user is notified to try again. 
   - if click on the "Reset" button, the search field is reset.
   - if *Registered user* clicks on "Add property" - go to the Add property page 
   - if *Registered user* clicks on each property card "Visit property" button - go to the correct property external page
   - if *Registered user* created the property view Edit & Delete buttons
      - if the user clicks on each property card "Delete" Button - open modal to confirm delete property. If the user clicks on the "Delete" button, the property is deleted, removed from the database and the user gets a confirmation. If the user clicks on the "Cancel" button the modal is closed.
      - if the user clicks on each property card "Edit" Button - go to the Edit property page
   - if *Registered user* clicks on the bookmark button, the property is added to their profile, the button changes to orange and a feedback message is given
10. Add Property Page
   - if *Registered user* types in text in fields, validation is given if correct and feedback is given if incorrect.
   - if *Registered user* wants to select a date, a date picker opens with the current date and a date can be selected.
   - if *Registered user* click on the "Add property" button, a new property is added to the database and a success message is given to the user.
   - if *Registered user* click on cancel - go to properties Page
11. Edit Property Page
   - view current details of property
   - if type in text in fields, validation is given if correct and feedback is given if incorrect.
   - if want to select a date, a date picker opens with the current date and a date can be selected.
   - if click on the "Update property" button, the property is updated in the database and a success message is given to the user.
   - if click on cancel - go to the properties Page
12. Manage property Admin Dashboard Page
   - if *Admin user* click the "Add new Featured property" button, go to Add Featured property page. 
   - if *Admin user* click the "Delete or Edit Featured property" button, go to the Home page.
   - if *Admin user* click the info button, open info modal about Featured properties
   - if *Admin user* click the "Add Category" button, go to Add Category page. 
   - if *Admin user* click the "Edit" button in the Category section, go Edit Category page.
   - if *Admin user* click the "Delete" button in the Category section, the delete modal opens.
   - if click on cancel - close modal
   - if click on the "Delete" button, the category is deleted and a success message appears.
   - if *Admin user* click the info button, open info modal about Categories.
   - if click on cancel - close modal
13. Add New Category page
   - if *Admin user* types in text in fields, validation is given if correct and feedback is given if incorrect.
   - if *Admin user* click on the "Add Category" button, a new category is added to the database and a success message is given to the user.
   - if *Admin user* click on cancel - go to Admin Dashboard Page
15. Edit Category page
   - view current details of category
   - if *Admin user* types in text in fields, validation is given if correct and feedback is given if incorrect. 
   - if *Admin user* click on the "Update Category" button, the category is updated in the database and a success message is given to the user.
   - if *Admin user* click on cancel - go to Admin Dashboard Page

## **Bugs and Fixes**
### Bugs
- There were a few bugs during the development and deployment. A sheet was created to keep track of the bugs, the expected results and the solutions/fixes.
   - [Bugs, Expected Results & Fixes during Development Phase](/documentation/images/general_doc_images/bugs_and_fixes_development.png)
   - [Bugs, Expected Results & Fixes during Deployement Phase](/documentation/images/general_doc_images/bugs_and_fixes_deployment.png)

### Known Bugs
- Firefox Browser: For all forms, if a cateogry is selected, border-bottom does not change to green but red.

## **Further testing** 
- Usability tests were done with two users to analyse the User Experience. The feedback from the users were very helpful to determine what works, what can be improved and determine future features.  
- Asked fellow students, friends and family to look at the site on their devices and report any issues they find.
- Review all functionality and responsiveness on different desktop browsers and the website displayed correctly in all browsers including Safari, Chrome, Edge, Firefox and Opera browsers. (see Browser Compatibility section for detail)
### Deployment
- Ensured deployed page on Heroku loads up correctly.
- Ensured Debug variable in app.py file is set to False.
- Confirmed that there is no difference between the deployed version and the development version.

##### back to [top](#table-of-contents)