[View the site live here!](https://musicians-blog-a58fa5a0530b.herokuapp.com/)

# Musician's blog

Musician's blog is a social blog aimed for users that are interested in anything and everything related about music.

Users will attempt to beat the computer by eliminating its 5 ships before it finds and sinks the user's own 5 ships.
Each ship occupies one cell on the grid.

Here, users can read blog posts about instruments, songs, or other fascinating topics of the musically inclined.
They can comment on posts, create their own profiles with bios and also follow other users' profiles to become more engaged with the blog's community.

The blog is based of Code Institute's CodeStar Blog, which is a full stack project built using the Django Framework.
The follow and profile functionalities are heavily inspired from the Youtube channel 'Codemy.com' and their series called 'Django Wednesdays Twitter'
The follow and profile functionality follows from 'Django Wednesdays Twitter #1' to 'Django Wednesdays Twitter #6'

![Responsive Mockup](documentation/media-size.jpg)

## Features

### Existing Features

- **Navigation Bar**
  
  - Featured on all pages. Includes links to logo, Home, About, (Register, Login) or Logout, Profiles, My Profile and is the same on each page for easy navigation.
  -  Users are displayed as logged in at the top right corner. (Otherwise it will display: "You are not logged in, click 'here' to log in.", in which 'here' links to the login page)

- **Footer**
  
  - Featured on all pages. Includes social links. (None of the links are real, they just lead to each website's homepage)

- **Homepage**

  - The homepage is the first page the user will encounter. It displays a list of blog posts with their titles, publication dates, and author details. Each post is represented as a card containing brief information and a link to read more.
  - The navigation bar provides links to essential sections like Home, About, Register and Login.
  - To access more functionalities like commenting on posts or clicking on authors'/users' links to view their profiles, the user has to register and be logged in.
  - If the user is logged in, the navigation bar provides links to essential sections like Home, About, Logout, Profiles and My Profile.
    - Logged in users can comment on posts, and they can also click on authors' or commenters' names, in which it will lead to that user's profile page.
  - The blog posts' titles serve as clickable links that direct users to detailed view of the blog post.
  - Pagination allows users to navigate through multiple pages of blog posts.

- **About**

  - The About page showcases a combination of text (right side) and an accompanying image (left side) and is used to convey the essence of the blog, its objectives, and its focus on various aspects of music.
  - The About page shows when it was last updated.
  - **Collaboration Form:** Users are encouraged to collaborate or reach out through a form present on the page.

- **Register, Login and Logout**

  - Allows the user to register and make an account. The authentication functionalities are powered using Django's allauth package.
    - **Register:** Users can create an account by registering through the provided registration form.
    - **Login:** Registered users can log in using their credentials via the login form.
    - **Logout:** Allows logged-in users to sign out securely from their accounts.

- **Profiles**

  - It is a profile list. It Displays the total count of profiles excluding the current logged in user's profile.
  - Each profile entry consists of:
    - **Username:** Displayed as the card title.
    - **Profile Creation Date:** Shows when the profile was created.
    - **View Profile Button:** Redirects to the individual user's profile page.

- **Profile**

  - The profile of another user.
  - Here the user can read a bio about the user.
  - They can choose to follow or unfollow the specific user by a button.
  - See how many and who they follow.
  - See how many and who they are followed by.

- **My Profile**

  - This is the current logged in user's own profile.
  - Here they can read the bio about themself.
  - See how many and who they follow.
  - See how many and who they are followed by.

### Features Left to Implement

- 1
  - **Reasons**: 1

- 2
  - **Reasons**: 2

- 3
  - **Reasons**: 3

## User Experience - UX

The design and functionalities of the website is based around user stories and agile methodology.

### User Stories

The user stories are accessible in the Musician's Blog User Stories project
https://github.com/Masorr/musicians_blog/projects?query=is%3Aopen

- Epic: Posts
  - #1 As a site user I can view a paginated list of posts so that I can select which post I want to read
  - #2 As a site user I can click on a post so that I can read the post's content
  - #3 As a site admin I can create, read, update and delete posts so that I can manage my blog content
  - #8 As a site admin I can create draft posts so that I can finish writing the content later

- Epic: About Page
  - #11 As a site admin I can create and update the About information so that I can make it available to users
  - #12 As a site user I can click on the About link so that read more about the site

- Epic: Collaboration Requests
  - #13 As a potential collaborator I can fill in a contact form so that I can submit a request for collaboration
  - #14 As a site owner I can store collaboration requests in the database so that I can review them
  - #15 As a site owner I can mark collaboration requests as 'read' so that I can see how many I still need to process

- Epic: Comments
  - #5 As a site user I can leave comments on a post so that I can be involved in the conversation
  - #6 As a site user / admin I can view the comments on an individual post so that I can read the conversation
  - #7 As a site user I can modify or delete my comments on a post so that I can be involved in the conversation
  - #9 As a site admin I can approve or disapprove comments so that I can filter out objectionable comments

- Epic: User Accounts and Profiles
  - #4 As a site user I can create/register an account so that I can comment on a post
  - #10 As a site user I can choose to follow another user so that I can become more involved with the community
  - #16 As a site user I can visit other users' profiles so that I can become more engaged with the community

## Design

- Since the blog is based off Code Institute's CodeStar blog project. The design retains this style.

- **Wireframes**

  - The initial game page flowchart.
    ![Flowchart game](flowcharts/flowchart.png)

- **Wireframes / End Design Likeness**

  - 

- **ERD (Entity Relationship Diagrams)**

- **Colours**

  - There are mainly 4 prevalent colour types.
  - Light grey (most common). Mostly used as background.
  - Dark grey (common). For footer, post texts and also to make some contrasting styles.
  - Greenish (uncommon). Used mostly for buttons or actions the user can perform.
  - Orange (rare). Used on some buttons.

## Testing

### Manual Testing

![Testing-1](documentation/tests-1.png)
![Testing-2](documentation/tests-2.png)

### Validator Testing

- Python
  - No errors or warnings were found when passing through the PEP8 python validator: <https://pep8ci.herokuapp.com/>

- PEP8 validator result for run.py

  ![PEP8 validation](documentation/validate-python.jpg)

### Media

- Tested on Microsoft Edge, Mozilla Firefox and Chrome.
- Screen media mockup tested on <https://ui.dev/amiresponsive?url=https://musicians-blog-a58fa5a0530b.herokuapp.com/>
- Tested on desktop, laptop and mobile.

### Fixed Bugs

- When attempting to make a follow model. A few models were made, migrated and then scrapped. The coder then wanted to update model in profile without doing python3 manage.py blog zero. This was in order to keep the blogs and comments as the coder did not want to loose data.
- <https://www.postgresql.org/docs/current/sql-droptable.html> by following these steps. The coder went into the database server (elephantSQL) and took took DROP TABLE blog_profile_follows and blog_profile.
- When attempting to make new migrations and migrate, no changes were made.
- Coder then attempted to run python3 manage.py migrate blog 0006 to revert to previous migration, error came up
	django.db.utils.ProgrammingError: table "blog_profile_follows" does not exist. This was because in order to revert back to a previous migration, the tables in elephantsql were needed to be able to revert back, even python3 manage.py blog zero didn't work.
  - Bug was fixed when coder ran python3 manage.py sqlmigrate blog 0007 to see the SQL code tables generating for elephantSQL. (These include the tables that were wrongly removed from the database). They were then re-added according to <https://www.postgresql.org/docs/current/sql-createtable.html>
  - The tables were remade for elephantSQL by running
    - CREATE TABLE "blog_profile" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "bio" text NOT NULL, "created_on" timestamp with time zone NOT NULL, "user_id" integer NOT NULL UNIQUE);
    - CREATE TABLE "blog_profile_follows" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "from_profile_id" bigint NOT NULL, "to_profile_id" bigint NOT NULL);
    - When these were readded to the database, the coder could run python3 manage.py migrate blog 0006 to modify the models without having to reset all migrations and preventing unnecessary loss of data.

### Unfixed Bugs

- There are no known unfixed bugs.

## Deployment

- The site was deployed to Heroku:
  - Create a new Heroku app.
  - Add config var for Cloudinary: 'CLOUDINARY_URL' and value: 'your cloudinary api key'.
  - Add config var for database: 'DATABASE_URL' and value: 'your postgres database url'.
  - Add config var for secret key: 'SECRET_KEY' and value: 'your secret key'.
  - Go to deploy, select deployment method (GitHub).
  - Search for 'musicians_blog' in app to connect to GitHub and connect the repository to Heroku.
  - Hit 'deploy branch' at bottom of page.
  - Select 'Open app' at the top of the page.

Link to live site - <https://musicians-blog-a58fa5a0530b.herokuapp.com/>

- Cloning the Repository:
  - On the repository page, click the 'Code' box.
  - Pick local then HTTPS and copy the link that is shown, which is: <https://github.com/Masorr/musicians_blog.git>
  - Open the terminal in your code editor and specify the directory you want to have your clone.
  - Type 'git clone' into your terminal and paste the link <https://github.com/Masorr/musicians_blog.git> and hit enter.

## Credits

### Content

- The base of the blog comes from Code Institute's CodeStar blog walkthrough project. This most of the functionality of the website. Including home page, pagination of posts, commenting and its CRUD functionality. Login functionality and registering of users and the about page.
- The profiles, my profile and following of users are credited and heavily inspired to Codemy.com and their Youtube channel <https://www.youtube.com/@Codemycom>. Especially their videos, from 'Django Wednesdays Twitter'. Going from 'Django Wednesdays Twitter #1' to 'Django Wednesdays Twitter #6'.

## Thanks

- I want to thank Code Institute and their tutors for their program and lessons, and giving me the opportunity to learn by myself by coding this full stack blog website using the django framework.
- I want to thank Codemy.com and their excellent youtube tutorials.
- I want to thank the Slack community and my mentor Dick Vlaanderen for feedback and inputs.
