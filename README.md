
# Digital Nomads
- Digital Nomads is a website that allows developers to share their experiences outside the office.
- No desks, no cubicles, no offices.
- It is a platform for nomads in the digital world to share their personal adventures, tips and recommendations when working and exploring the world.

# Live Project
- The live website can be found [here](https://digital-nomad.herokuapp.com/).

# Purpose of the website.
- To provide a platform where users can share their stories as Digital nomads.
- To promote the idea that Developers can be flexible on the job, while working and traveling.
- To create a community and connect users in a "guild" of like minded people.
- To allow users to share their ideas and help each other both in front and behind the screen.

# Design:
The website was designed with the intent to allow Users to browse Posts easily and perform all CRUD functionalities.
It relied on colours that should be appealing to the User, especially for those who might use the Website on a daily basis.

For such, it makes use of a colour palette of a mere greenish, brownish and yellowish blend (COLOR # HERE) for the Navigation bar.
This gives a rustic feeling and is often associated with the nomadic camper life at the beach, desert and mountain.

The background is best defined by a grayish white (COLOR # HERE) and body of the Post with a lighter gray (COLOR # HERE), bordered by dashed lines.
The buttons in the Post borrow the same patterns and render a shadow beneath them to contrast the body.
This gives the illusion the User is writting a post on a piece of paper/document.

[IMG COLOR PALLETE]

For a website where its functionality consists on writing and reading articles, the Fonts used for this Website were both "Audiowide" and "Staatliches".
A choice that should appeal to a Users readability and block them from distractions of a complex design.
The Fonts and Logo on the Navigation bar are dyed in white, while the Body presents itself with a dark grayish tone that doesn't stand to much from the article.
Links in the Navigation bar are highlighted by white tone when hovered, and bold when active.
Links change color uppon hover, particularly the Title of the Post, the Username in a Post/Comment, the Social Media Links and links that redirect to other pages.
Icons were also integrated to the website, to give a much more asthetic touch and association of functionality of the Website.
The Navigation bar, Footer and pages in the Body makes use of Icons.
The Logo states "Digital Nomads" and is animated by an icon, to give the idea that devs are on the move. Red was the chosen color, to highlight it from the rest of the name.
Both the Header & Footer have an image attached to it, of a somebody Networking, to give the impression that they are typing and readig Posts. Hence the screen at the top and the hand at the bottom.

The structure of the website is cohrent and the base.html is present in all page. The skeleton of the body is consistant for pages.


# Features and Functionality for non-reg./reg Users & Superusers

## Non-Registered Users (Visitors)
- Visitors can read all posts from /home/.
- Visitors can read all users posts from /username/
- Visitors can create a User account through /register/
- Visitors can navigate to the Home/About/Login/Register pages
- Visitors can navigate through the pagination of /home/ and /username/
- Visitors can access external links on users posts/comments and footer.

## Registered Users (CRUD) can do the above as a Visitor, moreover:
- Users can Log In/Out through the "Log In/Out" functionality".
- Users can create posts through the "Post" functionality.
- Users can update their posts through the "Update" functionality.
- Users can delete their posts through the "Delete" functionality.
- Users can like/dislike all posts through the "Like/Dislike" functionality.
- Users can navigate to the Profile tab and update their "Bio".
- Users can navigate to the Profile tab and upload a Profile pipcture.

- Comments cannot be deleted by anyone, except Superusers.

## Superusers can manipulate information through the /admin/ panel.
- CRUD posts
- Change Password passwords
- Create/Update/Delete users
- Delete Comments
- Promote Users to Superuser

(ELABORTATE...)

# Design
## Navbar, Header & Favicon
- The Navbar features from left to right the [Logo], [Home], [About], [Login], [Register] and the [Search] fields. Furthermore for Users who are logged in, the [Post], [Profie] and [Logout] links. The links guide Users to the respective pages and remain "active" when and if on that page, with the exception of [Post].
- The Header features an image that splits in half, sharing the rest with the Footer. The screen of a Laptop can be seen together with the Logo of the website.
- On the browsers tab, the Favicon and Logo of the website can be found. A red gear.

<img src="media/readme_img/headernavpanel.png" alt="Navigation & Header">

## Footer
- The Footer is best defined by Bootstraps template. It features a Slogan on the left side and on the right the Social Media links. At the very bottom, a copyright notice.
- Above the Footer is the rest of the image shared with the Header. The keyboard of a laptop.
- Users can open the Social Media links in new tabs.

<img src="media/readme_img/footerpanel.png" alt="Footer">

## Home: Posts & Pagination
- The Homepage renders all of the Posts that Users create.
- If Users are logged in, then they are greeted with a message followed by their Usernmes.
- If no Posts are present in the board of Home, then the Homepage displays a message encouraging Users to create a Post.

<img src="media/readme_img/nopostspanel.png" alt="No Posts">

- If the Forum has been populated with Posts, then the Posts are displayed and organized in a vertical fashion, with the newst at the top and the oldest at the bottom.
- Per Post the Username, Picture, Date, Title, and Body truncated by 50 words are displayed.
- For every 6 posts, a new page for Pagination is created and Users can easily navigate from page to page.

<img src="media/readme_img/pagination.png" alt="Pagination">

## About
- The About page renders a small section of advertisement and information about the website. It also encourages users to either Log in or Register an account.

<img src="media/readme_img/aboutpanel.png" alt="About">

## Posts & Comments
- When Opening a Post, the details of that particlar Post is expanded, allowing Users to read the whole article.
- Users can read and engage with the Post, by leaving Comments and Likes.

<img src="media/readme_img/openpostandcommentpanels.png" alt="Open Posts and Comments">

## Search Field
- Users can use the Search functionality.
- Upon making a valid search, the page should retrieve a list of Threads, by a word populated either in the Title, Body or Username of a Post.

<img src="media/readme_img/charactersearch.png" alt="Search Field">

- If no Post exhibit such word, than a template prompts users to give in a valid word.

<img src="media/readme_img/wrongcharactersearch.png" alt="Search Field">

- Otherwise, if not character was introduced in the search field, Users are requested to input a valid character.

<img src="media/readme_img/nocharactersearch.png" alt="Search Field">

## User Profile
- The User profile can be best defined as a "Settings panel", where users can update their personal info.
- The fields that can be updated include Username, Profile picture, E-mail and Bio.

<img src="media/readme_img/profile.png" alt="Profile">
s
- Upon updating the Bio the User should have an Overview field.

<img src="media/readme_img/overviewpanel.png" alt="Overview">

- If a User created an account, but did not make any Posts, even though made Comments. The User profile remains inactive.

<img src="media/readme_img/usernopostspanel.png" alt="User no Profile">

## Registration & Deletion
- The Registration page requests that Users input a Username, E-mail and Password.

<img src="media/readme_img/registerationpanel.png" alt="Error 404">

## Log in/out
- The Log in page demands Users to input valid credentials, as per registered.

<img src="media/readme_img/loginpanel.png" alt="Log in">

- By Logging out, Users are fired with a Goodbye message.

<img src="media/readme_img/logoutpanel.png" alt="Log out">

## Deletion

<img src="media/readme_img/deletionpanel.png" alt="Deletion">

<img src="media/readme_img/deletionconfirmedpanel.png" alt="Deleted">

## Error 404
- If a User goes to a non-defined URL, then a 404 Error template is rendered, requesting users to leave that page.

<img src="media/readme_img/404.png" alt="Error 404">

## Planning & Agile:
This project was planed using Agile methodology and MoSCoW prioritization..
For such, the Project was best illustrated by 1 Milestone entitled "Submit the project to CI before Deadline" giving the Developer freedom to achieve all issues/tasks flexibly by the deadline.
Through out development new issues were added/removed that started from "Todo" moved into "In Progress" and finlized in "Done".
Issues were assigned to the sole Developer [TiagoMA90](https://github.com/TiagoMA90) and have been labelled as "could-have", "should-have" and "must-have".
Once completed, Issues were marked as "done", and once all were done, the Milestone was closed.

[Screenshots]
(Elaborate)

Navbar items Home, About, Regions, Logo, Search, Bucket List, Write Post, Logout and Profile are available for registered users.
The Navbar is fixed to the top of the screen even when the user is scrolling down the page to allow easier navigation.
The logo is linked to the Homepage and each menu item is linked to each page respectively to allow easier navigation.
The search bar allows users to easily search for a keyword they are looking for.
The navigation menu collapses on small/medium devices to optimise the menu for smaller screen sizes, as per Bootstrap.

## Development Process
The project started out as a forum for Ads of Events, where users could post Events taking place at a certain time in a certain location.
Users would therefore open up a thread give a brief description of the Event, target the location with Google Maps API and set the Date. After an event took place, it ought to be automatically deleted.

In the end, this project was simplified due to dateline limitations and time conciliations. It makes good use of familiar concepts such as Create Read Update Delete.
Upon re-creating this project, the developer resorted the idea of a "forum" or "discussion board", similar to [reddit](https://www.reddit.com/) but more focused on the nomadic lifestyle.

## Manual Testing and Website Functionality:

Manual testing has been performed for its overall purpose.
The website has proven to exhibit a dynamic functionality and responsive interactivity, both in the Front & Back-End.
After consecutive reherasls and manual testing, the website employd the desired role and met the final goal set by the Developer.

Based on the solid foundations of CRUD. Testing was perfromed:
- By navigating and accessing links in the Website.
- By Creating, Reading, Updating and Deleting an account for a Registered User.
- By Creating, Reading, Updating and Deleting Posts as/of a Registered User.
- By Creating and Reading Comments on a Post, as a Registered User.
- By Liking and Disliking a Post, as a Registered User.
- By Populating the Homepage with Posts in order to activate Pagination.
- By inputing and retrieving results from the Search box.
- By Reseting the Password of an account, via Email.
- By manipulating Posts, Users, Comments, Likes as a Superuser in the Admin panel.

By Clicking the links in the navigation panel, Users are redirected to the assigned pages.
- By clicking on "Home", Users are sent to the Homepage, where the board of Posts can be found. From here Users can browse Posts and select one to Read.
- By clicking on "About", Users are sent to the About page. Within that page, Users can read the introduction the mission Goal of the Website. User may navigate to the Registeration and Login pages.
- By clicking on "Post", Users are redirected to the Post Form, of which they must input a Title and Body to create a Thread. Posts are submitted by clicking the Submit Button. (Users mut be logged in in order to Post, otherwise they are prompt to the Login page.)
- Once a Post has been succesfully created, It can be accessed for reading by the whole community.
- Authors of that particular Thread can Edit, Delete, Like/Dislike and Comment that Post. Respectively that functionslity is achieved by clicking the following icons at the end of the Thread. The "Pencil", "Bin", "Heart" and the "Add Comment" links.
- Other Users can Like/Dislike and/or Comment that Post, by clicking the same icons, as stated above.
- Comments cannot be updated or deleted by anyone once submited, except by Administrators. To submited a comment once in the Commnt page, Users must click the button "Submit Comment".
- By clicking on "Profile", Users are sent to the Profile Panel, where they can update their Username, E-Mail, Bio and Profile Image. To Update such fields, Users should click the "Update" button.
- By clicking on "Register", Users are sent to the Register page, where Users are requested to input a Username, input an E-mail and Password. Users are not requested to confirm their newly accounts via inbox. Usres may created multiple accounts using the same e-mail.
- By clicking on "Login", Users are sent to the Log in page. From there Users are requested to input their log in credentials, Username and Password. If by any chance the User does not remember the Password, they can still reset the password by clickig in "Reset password?".
- By clickign in "Reset password", Users are requiered to input their e-mail. From there, an e-mail is dispacthed to the given e-mail with further details on how to reset the Password. (An hyperlink is generated and sent to User. The User must click that link in order to procceed)
- By Reseting the Password, Users are required to input a new Password.
- By clicking a "Username" within the Posts, Users are sent to that particular User page. This page render all of the posts created by that particular User. The Bio is included.
- If the User did not create any Posts, the profile can still be accessible, but render a page informing visitors that particular User has not many any Posts.
- By clicking on "Logout", Users are logged out and sent a farewell message page. From there they can go back to the Log in page.
- By clicking on "Delete Profile" Usuers are warned if they wish to proceed to execute such action. If "Delete" is clicked, Users are automatically logged out and the account is eliminated. (Profile, Posts & Comments associated with that User account are deleted). If "Cancel" is clicked, the User is sent back to the Profile.
- By clicking in any of Social Media links, located in the "Footer", Users are redirected to external pages opened in a new tabs. This ensures the Website is not overidden by exteranal pages.

Bugs and Excluded :
- The ckeditor failed to render properly in the body of the Post. Eventually ckeditor was removed from the project altogether, give Users the possibility to write a basic TextField.

[Screenshots]
(Elaborate)

- This website was developed on Gitpod hosted by GitHub, making use of both Front-end and Back-end.

Errors and Removed functionalities:
- ckeditor - (traces of the code are still visible in the code) - Had trouble with assets such as "brown-paper" & others.
- Imported and uploaded manually, but the interface was unrecognizable. Eventually moved back to models.TextField()

Languages
- HTML (markup language)
- CSS (style sheet language)
- Python (programming language)

Frameworks
- Bootsrap (css framework)
- Django (web framework)

and  and deployed on Heroku.
