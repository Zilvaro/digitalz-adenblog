![DigitalZ Aden Logo](/assets/readme_files/digitalz-aden-logo.jpg)


# Welcome!


This digitalz-aden application is a real-life prototype destined to replace the current adenwell.com website.
Aden Wellness is a brand of wellness products (supplements, essential oils,..) that is starting its activities with launching several products on Amazon USA. To promote their philosophy of business, present products, direct users to e-commerce or Amazon site they need an interactive website with an ability to offer users to comment and post their own ideas. 

Therefore, the app has 2 distinctive parts:
1.	Top part is the content selection of more permanent materials that are managed by the company (admin, UserAdmins)
2.	Then blog/ad area - where the announcements, promotions, thoughts (including third parties) are displayed. It includes more interactivity with likes & comments.  

The working version of the Digitals-AdenWell app can be found [here](https://digitalz-adenwell.herokuapp.com)


![website preview](/assets/readme_files/am-i-responsive-black.JPG)




## Table of Contents

- [Welcome!](#welcome)
  - [Table of Contents](#table-of-contents)
  - [User Experience (UX)](#user-experience-ux)
    - [Strategy](#strategy)
      - [Flexibility \& Impact](#flexibility--impact)
      - [Security](#security)
      - [User Stories - usage](#user-stories---usage)
      - [User Stories - creation](#user-stories---creation)
      - [Things, left "for next Iteration"](#things-left-for-next-iteration)
    - [Stages](#stages)
      - [Ideation, prioritization and planning](#ideation-prioritization-and-planning)
      - [User Stories](#user-stories)
    - [Structure](#structure)
      - [Database Model](#database-model)
    - [Skeleton](#skeleton)
      - [Wireframes](#wireframes)
    - [Surface](#surface)
      - [Color Scheme](#color-scheme)
      - [Typography](#typography)
  - [Features](#features)
    - [General](#general)
    - [Home Page](#home-page)
    - [About Page](#about-page)
    - [Search Results Page](#search-results-page)
    - [Question Detail Page](#question-detail-page)
    - [Ask Question Page](#ask-question-page)
    - [Leave Reply Page](#leave-reply-page)
    - [Edit Question Page](#edit-question-page)
    - [Delete Question Page](#delete-question-page)
    - [Edit Reply Page](#edit-reply-page)
    - [Delete Reply Page](#delete-reply-page)
    - [Authentication Pages](#authentication-pages)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Libraries and Frameworks](#libraries-and-frameworks)
    - [Packages / Dependecies Installed](#packages--dependecies-installed)
    - [Database Management](#database-management)
    - [Tools and Programs](#tools-and-programs)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [Deploying on Heroku](#deploying-on-heroku)
    - [Forking the Repository](#forking-the-repository)
    - [Creating a Clone](#creating-a-clone)
  - [Finished Product](#finished-product)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Code](#code)
  - [Known Bugs](#known-bugs)
  - [Acknowledgements](#acknowledgements)


***


## User Experience (UX)

### Strategy

In effect, Digitalz-Adenwell is a business presentation and customer engagement application with full content creation and management functionality from the front-end, strictly following the user admin rights (although everything can be altered and overwritten from the admin-backend too).

#### Flexibility & Impact

* All content except of navbars can be created/updated or deleted by user from the front-end or admin module

* Most of the fields support text & images.

* ALT text can be created directly in the content form for higher searchability of the content

* User can choose between layout options and how many items to put on one row on the screen

* User can set the specific place for a specific content by assigning the content-order number 

* User can set-up the height of the elements for larger screens.

* User can create draft content and access it later to publish/update or delete

* Structure is easy to understand and navigates effortlessly.


#### Security

* Site users are able to register an account in order to interact with the content.

* User can't select the author, he is author by default.

* Update/Delete content/post are not accessible via browser if you are not the author.

* Users can update/delete only the posts/content they have created.

* Users can't make a draft of the Post - to keep the system and database cleaner.


#### User Stories - usage

1.	As a **Site User** I can **register an account** so that **I can comment and like**
2.	As a **Site User** I can **view a list of posts** so that **I can select one to read**
3.	As a **Site User** I can **click on a post** so that **I can read the full text**
4.	As a **Site User** I can **leave comments on a post** so that **I can be involved in the conversation**
5.	As a **Site User** I can **like or unlike a post** so that **I can interact with the content**
6.	As a **Site User** I can **click on a content** so that **I can read more about the topic**
7.	As a **User / Admin** I can **view the number of likes on each post** so that **I can see which is the most popular or viral**
8.	As a **User / Admin** I can **view comments on an individual post** so that **I can read the conversation**


#### User Stories - creation

9.	As a **User-admin** I can **create, edit, and delete a) content & b) posts directly on app** so that **I can manage the content area without accessing admin module**
10.	As an **Admin** I can **create draft content** so that **I can publish/ update or delete later** 
11.	As an **Admin** I can **approve or disapprove comments** so that **I can filter out objectionable comments**
12.	As an **Admin** I can **set the content width** so that **I can place different number of items on one row**
13.	As a **Site Admin** I can **assign the post position number**, so **I can place posts according to importance** 
14.	As an **Admin** I can **select the card height** so that **I can create better looking design**
15.	As an **Admin** I can **select the card template** so that **I can create dynamic looking design**
16.	As a **User** I can **create a contact message** so that **I can express my opinion or ask to contact back**

  

#### Things, left "for next Iteration"

* As a **Site Admin** I can **set the publishing and validity date (&time) of the content** so that **I can manage content appearance**.

* As a **Site Admin** I can **set the end date for the post** after which it moves to 'draft' status so that **I can keep the site cleaner**.
  
* Social media sign-up


### Stages

The Planning & Execution of DigitalZ-Aden project was in 4 distinct phases: 

#### Ideation, prioritization and planning

The current webdesign of AdenWellness [here](https://adenwell.com/) was reviewed and discussed, what would be the 'wishes' for the new design:

* Responsive design

* Account registration

* Create, edit and delete content from fron-ent, not only from admin module

* Separate permanent content from the promotional materials and posts

* Ability to interact with users via comments and contact messages

* Ability to create interesting and varied content without other tools (editors, design tools)

* No link (at the moment) to external sorces : Amazon, e-commerce, etc.


As a outcome - simple sketch of structure was drawn. 

**Second Phase**

* Ability to add profile picture

* 

* Add tags to the questions


#### User Stories

GitHub projects was used as my project management tool to track user stories. Using a Kanban board helped to focus on specific tasks and track the project progress.

**Start**
![User Stories Progress - Start](assets/readme_files/user_stories_start.png)

**Week 1**
![User Stories Progress - Week 1](assets/readme_files/user_stories_week1.png)

**Week 2**
![User Stories Progress - Week 2](assets/readme_files/user_stories_week2.png)

**Week 3**
![User Stories Progress - Week 3](assets/readme_files/user_stories_week3.png)


### Structure

The website has been organized in a Hierarchical Tree Structure to ensure the site user navigates through the site effortlessly and intuitively. Here you can you can find the website map design.

![Digitalz Aden website map](assets/readme_files/sitemap.jpg)

* Header, footer and navigation bar are consistent through all pages.

* Links and forms provide clear feedback to the site user.

* The opportunity to add additional content to the website is provided for the site user once they register an account.

* A 404-error page is available.


#### Database Model

The database model has been designed using [drawsql](https://drawsql.app/). The type of database being used for the is relational database being managed using [PostgreSQL](https://www.postgresql.org/).

![Digitalz Aden website map](assets/readme_files/db_model.png)

**Question Model**

* Title: Unique question title provided by the author.

* Author: Store the author of the question as a User foreign key.

* Content: Question details provided by the author.

* Slug: Store a unique slug to identify the question by.

* Created On: Date and time set automatically at the question's creation.

* Last updated: Date and time set automatically every time the question is updated.

* Votes score: Calculated score of the question's votes.

**Reply Model**

* Question: A foreign key from the Question model, storing the question being replied.

* Author: Store the author of the reply as a User foreign key.

* Body: Reply body with details provided by the author.

* Created On: Date and time set automatically at the reply's creation.

* Last updated: Date and time set automatically every time the reply is updated.

* Votes score: Calculated score of the reply's votes.

**QuestionVote Model**

* Voter: Foreign key from the User model, storing the user voting the question.

* Score: Score provided by the voter. The options are upvote with a value of 1 or downvote with a value of -1.

* Question: A foreign key from the Question model, storing the question being voted.

**ReplyVote Model**

* Voter: Foreign key from the User model, storing the user voting the reply.

* Score: Score provided by the voter. The options are upvote with a value of 1 or downvote with a value of -1.

* Reply: A foreign key from the Reply model, storing the question being voted.


### Skeleton

#### Wireframes

[Balsamiq](https://balsamiq.com/) has been used to showcase the appearance of the site and display the placement of the different elements whitin the pages.

Page | Desktop Version | Mobile Version
--- | --- | ---
Index / User Logged Out | ![Desktop index / user logged out wireframe image](assets/wireframes/index_dektop_logged_out.png) | ![Mobile index / user logged out wireframe image](assets/wireframes/index_mobile_logged_out.png)
Sign Up | ![Desktop sign up wireframe image](assets/wireframes/signup_dektop.png) | ![Mobile sign up wireframe image](assets/wireframes/signup_mobile.png)
Log In | ![Desktop log in wireframe image](assets/wireframes/login_dektop.png) | ![Mobile log in wireframe image](assets/wireframes/login_mobile.png)
Index / User Logged In | ![Desktop index / user logged in wireframe image](assets/wireframes/index_dektop_logged_in.png) | ![Mobile index / user logged out wireframe image](assets/wireframes/index_mobile_logged_in.png)
Ask Question | ![Desktop ask question wireframe image](assets/wireframes/ask_question_desktop.png) | ![Mobile ask question wireframe image](assets/wireframes/ask_question_mobile.png)
Open Question | ![Desktop open question wireframe image](assets/wireframes/question_dektop.png) | ![Mobile open question wireframe image](assets/wireframes/question_mobile.png)
Leave Reply | ![Desktop leave reply wireframe image](assets/wireframes/leave_reply_desktop.png) | ![Mobile leave reply wireframe image](assets/wireframes/leave_reply_mobile.png)


### Surface

#### Color Scheme

![Color scheme image](assets/readme_files/color-pallet.jpg)

The colors used in the website respect the green-golden color-scheme of Aden Wellness, represented in the logo. 

Main colors in the application are achieved through images, so complementary slate-gray (#445261) and baby powder (#FFFFFD) were chosen just to create some contrast, improve readibility and maintain consistent look. 


#### Typography

The main font being used in the site is Segoe UI with occasional introduction of Roboto, with sans-serif as a fallback in case Segoe UI doesn't get imported correctly. 

Segoe UI was chosen after refresher-research on fonts that are better for reading, however Segoe UI has proven to be font-of-choice for a few years in app development.

[Back to top ⇧](#code-buddy)


## Features

### General

* The website has been designed from a mobile first perspective.

* Responsive design across all device sizes.

* Navigation Bar
![Digitalz Aden Navigation Bar image](assets/readme_files/nav-bar.JPG)

    *  Contains the main logo, links and Welcome! with user name.


* Footer
  ![Digitalz Aden Footer image](assets/readme_files/footer-bar.JPG)

    * The footer includes a logo and link to social media channels (hidden while waiting for Aden Wellness approval to use).


### Home Page

* Question list
![Digitalz Aden Question List image](assets/readme_files/code_buddy_question_list.png)

    * Display a paginated list of all the question and its relevant information for the user to identify.

    * Provide the Site User with a link to the detailed question.

    * Question score as well as voting possibilities for registered users is provided next to the question.

    * For registered users, a Ask Question button is provided to allow the user to access the Ask Question Page to create new questions.

    * Edit and Question buttons are provided for the questions the registered Site User has created.


### About Page

![Digitalz Aden About Page image](assets/readme_files/code_buddy_about.png)

* Provide relevant information about the website's objective.


### Search Results Page
![Digitalz Aden About Page image](assets/readme_files/code_buddy_search_results.png)

* Display information about the Search being handled

* Display a paginated list of the questions matching the search and its relevant information for the user to identify.


### Question Detail Page
![Digitalz Aden Question Detail Page image](assets/readme_files/code_buddy_question_detail.png)

* Display the full question a well as a list of its replies.

* Question and reply scores as well as voting possibilities for registered users is provided next to each item.

* For registered users, a Leave Reply button is provided to allow the user to access the Leave Reply page to create a new reply to the question.

 * Edit and Question buttons are provided for the questions and replies the registered Site User has created.


### Ask Question Page
![Digitalz Aden Ask Question Page](assets/readme_files/code_buddy_ask_question.png)

* Provide a form to allow registered Site Users to create a new question.

### Leave Reply Page
![Digitalz Aden Leave Reply Page](assets/readme_files/code_buddy_leave_reply.png)

* Provide a form to allow registered Site Users to create a new reply to the questions.


### Edit Question Page
![Digitalz Aden Edit Question Page](assets/readme_files/code_buddy_edit_question.png)

* Provide a prepopulated form to allow the Site User to edit a question they created.


### Delete Question Page
![Digitalz Aden Edit Question Page](assets/readme_files/code_buddy_delete_question.png)

* Provide a form to allow the Site User to delete a question they created.


### Edit Reply Page
![Digitalz Aden Edit Question Page](assets/readme_files/code_buddy_edit_reply.png)

* Provide a prepopulated form to allow the Site User to edit a reply they created.


### Delete Reply Page
![Digitalz Aden Edit Question Page](assets/readme_files/code_buddy_delete_reply.png)

* Provide a form to allow the Site User to delete a reply they created.


### Authentication Pages

Page | Purpose | Image |
--- | --- | --- |
Register | Allow the Site User to sign up an account for the website. | ![Digitalz Aden Sign Up Page](assets/readme_files/code_buddy_sing_up.png) |
Login | Allow the Site User to sign in with their account. | ![Digitalz Aden Sign In Page](assets/readme_files/code_buddy_sign_in.png) |
Logout | Allow the Site User to sign out from their account. | ![Digitalz Aden Sign Out Page](assets/readme_files/code_buddy_sign_out.png) |


[Back to top ⇧](#code-buddy)


## Technologies Used

### Languages Used

* [HTML5](https://en.wikipedia.org/wiki/HTML)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))


### Libraries and Frameworks

* [Django](https://www.djangoproject.com/)   
    * Django was used as web framework.

* [Django Template](https://jinja.palletsprojects.com)  
    * Django Template was used as a templating language for Django to display backend data to HTML.
   
* [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)  
    * Bootstrap 5 was used throughout the website to help with styling and responsiveness.

* [Google Fonts](https://fonts.google.com)  
    * Google fonts was used to import the fonts into the html file, and were used on all parts of the site.

* [Font Awesome](https://fontawesome.com)  
    * Font Awesome was used throughout the website to add icons for aesthetic and UX purposes. 

* [jQuery 3.6.0](https://jquery.com/)  
    * jQuery was used as a JavaScript library to help writing less JavaScript code.  


### Packages / Dependecies Installed

* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/)  
    * Django Allauth was used for user authentication, registration, and account management.

* [Django Crispy Form](https://django-crispy-forms.readthedocs.io/en/latest/)   
    * Django Crispy Form was used to control the rendering of the forms. 
 
* [Gunicorn](https://gunicorn.org/)  
    * Gunicorn was used as Python WSGI HTTP Server for UNIX to support the deployment of Django application.  

* [Summernote](https://summernote.org/) 
    * Summernote has been used as WYSIWYG editor.

* [Cloudinary](https://cloudinary.com/)
    * Cloudinary has been used as image management solution

### Database Management
* [Heroku Postgres](https://www.heroku.com/postgres)   
    * Heroku Postgres database was used in production, as a service based on PostgreSQL provided by Heroku.


### Tools and Programs

* [Git](https://git-scm.com)  
    * Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub. 

* [GitPod](https://gitpod.io/)
     * GitPod was used for writing code, committing, and then pushing to GitHub.

* [GitHub](https://github.com)  
   GitHub was used to store the projects code after being pushed from Git. 

* [Heroku](https://www.heroku.com)   
    * Heroku was used to deploy the website.

* [Am I Responsive](ami.responsivedesign.is)  
    * Am I Responsive was used to preview the website across a variety of popular devices.

* [Tiny PNG](https://tinypng.com)    
    * Tiny PNG was used to reduce the file size of the images.

* [Coolors](https://coolors.co)  
    * Coolors was used to create a color scheme for the website.

* [Balsamiq](https://balsamiq.com/)
     * Balsamiq was used to create the wireframes during the design phase of the project

* [Chrome DevTools](https://developer.chrome.com/docs/devtools/)
    * Chrome DevTools was used during development process for code review and to test responsiveness.

* [W3C Markup Validator](https://validator.w3.org/)
    * W3C Markup Validator was used to validate the HTML code.

* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
    * W3C CSS Validator was used to validate the CSS code.

* [JSHint](https://jshint.com/) 
    * The JSHints JavaScript Code Quality Tool was used to validate the site's JavaScript code.

* [Favicon.cc](https://www.favicon.cc/) 
    * Favicon.cc was used to create the site favicon.

[Back to top ⇧](#code-buddy)

## Testing

The testing documentation can be found [here](https://github.com/Zilvaro/digitalz-adenblog/blob/main/TESTING.md#digitalz-adenblog-testing).

[Back to top ⇧](#code-buddy)

## Deployment

This project was developed using a [GitPod](https://gitpod.io/) workspace. The code was commited to [Git](https://git-scm.com/) and pushed to [GitHub](https://github.com/") using the terminal.

### Deploying on Heroku
To deploy this page to Heroku from its GitHub repository, the following steps were taken:

1. Create the Heroku App:
    - Select "Create new app" in Heroku.
    - Choose a name for your app and select the location.

2. Attach the Postgres database:
    - In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.

3. Prepare the environment and settings.py file:
    * In the Settings tab, click on Reveal Config Vars and copy the url next to DATABASE_URL.
    * In your GitPod workspace, create an env.py file in the main directory. 
    * Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
    * Add the SECRET_KEY value to the Config Vars in Heroku.
    * Update the settings.py file to import the env file and add the SECRETKEY and DATABASE_URL file paths.
    * Update the Config Vars with the Cloudinary url, adding into the settings.py file also.
    * In settings.py add the following sections:
        * Cloudinary to the INSTALLED_APPS list
        * STATICFILE_STORAGE
        * STATICFILES_DIRS
        * STATIC_ROOT
        * MEDIA_URL
        * DEFAULT_FILE_STORAGE
        * TEMPLATES_DIR
        * Update DIRS in TEMPLATES with TEMPLATES_DIR
        * Update ALLOWED_HOSTS with ['app_name.heroku.com', 'localhost']

4. Store Static and Media files in Cloudinary and Deploy to Heroku:
    - Create three directories in the main directory; media, storage and templates.
    - Create a file named "Procfile" in the main directory and add the following:
        - web: gunicorn project-name.wsgi
    - Go to Deploy tab on Heroku and connect to the GitHub, then to the required recpository.
    Click on Delpoy Branch and wait for the build to load. When the build is complete, the app can be opened through Heroku.

### Forking the Repository
By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log into [GitHub](https://github.com/login) or [create an account](https://github.com/join).
2. Locate the [GitHub Repository](https://github.com/josswe26/code-buddy).
3. At the top of the repository, on the right side of the page, select "Fork"
4. You should now have a copy of the original repository in your GitHub account.

### Creating a Clone
How to run this project locally:
1. Install the [GitPod Browser](https://www.gitpod.io/docs/browser-extension/ "Link to Gitpod Browser extension download") Extension for Chrome.
2. After installation, restart the browser.
3. Log into [GitHub](https://github.com/login "Link to GitHub login page") or [create an account](https://github.com/join "Link to GitHub create account page").
2. Locate the [GitHub Repository](https://github.com/josswe26/code-buddy).
5. Click the green "GitPod" button in the top right corner of the repository.
This will trigger a new gitPod workspace to be created from the code in github where you can work locally.

How to run this project within a local IDE, such as VSCode:

1. Log into [GitHub](https://github.com/login) or [create an account](https://github.com/join).
2. Locate the [GitHub Repository](https://github.com/josswe26/code-buddy).
3. Under the repository name, click "Clone or download".
4. In the Clone with HTTPs section, copy the clone URL for the repository.
5. In your local IDE open the terminal.
6. Change the current working directory to the location where you want the cloned directory to be made.
7. Type 'git clone', and then paste the URL you copied in Step 3.
```
git clone https://github.com/josswe26/code-buddy
```
8. Press Enter. Your local clone will be created.

Further reading and troubleshooting on cloning a repository from GitHub [here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)



[Back to top ⇧](#code-buddy)

## Finished Product

Page | Desktop | Mobile |
--- | --- | --- |
| Home | ![Desktop Home Page image](assets/readme_files/home-desktop.jpg) | ![Mobile Home Page image ](assets/readme_files/home-mobile.jpg) |
| Content | ![Desktop Content Page image](assets/readme_files/content-desktop.JPG) | ![Mobile Content Page image](assets/readme_files/content-mobile.jpg) |
| Post | ![Desktop Post Page image](assets/readme_files/post-desktop.jpg) | ![Mobile Post Page image](assets/readme_files/post-mobile.jpg) |
| Contact |![Desktop Contact Page image](assets/readme_files/contact-desktop.JPG) | ![Mobile Contact Page image](assets/readme_files/contact-mobile.JPG) |
| Register |![Desktop Register Page image](assets/readme_files/register-desktop.JPG) | ![Mobile Register Page image](assets/readme_files/register-mobile.JPG) |
| Log-in |![Desktop Log-in Page image](assets/readme_files/login-desktop.JPG) | ![Mobile Log-in Page image](assets/readme_files/login-mobile.JPG) |
| Log-out | ![Desktop Log-out Page image](assets/readme_files/logout-mobile.JPG) | ![Mobile Log-out Page image](assets/readme_files/logout-mobile.JPG) |


[Back to top ⇧](#code-buddy)

## Credits

### Content

* Website content was written by the developer.
* Example images & some quotes were taken from [Aden Wellness](https://adenwell.com/)-

### Media

* [Pexels](https://www.pexels.com/)

    * About Page image: Taken by [Buro Millennial](https://www.pexels.com/@buro-millennial-636760/).

* [Unsplash](https://unsplash.com/)

    * 404 Error Page image: Taken by [Tai Bui](https://unsplash.com/@agforl24).

### Code

* [Stack Overflow](https://stackoverflow.com/) and [W3Schools](https://www.w3schools.com/) were consulted on a regular basis for inspiration and sometimes to be able to better understand the code being implement.

* Message implementation an dismissal code is taken from [Code Institute](https://codeinstitute.net/)'s django-blog project.

[Back to top ⇧](#code-buddy)

## Known Bugs

* Upvote/downvote button selection stay the same for all users. This do to an error in the logic. Even though the developer has an idea on how to solve the issue. The solution is yet to be implemented due lack of time.

* The same applies for pagination is Search Results page which is currently not working.

* A known issue with Summernote field validation is present in the project. An invalid form will be posted if the field is empty. A message will however be displayed, informing the user that there has been a problem with the submission.

[Back to top ⇧](#code-buddy)

## Acknowledgements

* My partner, for her unconditional love, help and continued support in all aspects of life, specially when I did not have time for anything else than to work with this project. You made it possible!

* My friend, Miguel, for being always there to help, no matter what time of the day.

* My tutor, Marcel, for his invaluable support, feedback and guidance through the whole process.

* Code Institute and its amazing Slack community for their support and providing me with the necessary knowledge to complete this project.

[Back to top ⇧](#code-buddy)