# Assignment 4 - Creating Tweeter (A Twitter Clone)

## Author



## Description

You will be creating a social website called Tweeter that will allow users to
be able to make posts called Twits that other users can view.
Users of the site will be able to make Twits that contain both text and
pictures via a URL to a picture, and like Twits that other users make.

Ensure that you have a `requirements.txt` file with your required packages. I will not grade the assignment if I can't restore the packages easily!

The program should allow the following functionality:

1. A Custom User model that adds a date of birth.
2. Full user authentication so that only authenticated users can use the site.
3. Sign up and authentication forms / views so that users can authenticate with the system.
4. Ability for users to be able to change and reset their password. (Just use the same fake SMTP as the in-class.)
5. A profile page where a user can update details about themselves. (username, fname, lname, email, date of birth)
6. A Dashboard for each user that will show all the Twits in the system listed with the most recent ones first.
7. Pages / forms to be able to CUD a Twit. Update and Delete should be limited to the person that made the twit.
8. New Twits should allow both text and URL for a picture. Image URL can then be used with a img tag to render the image.
9. A Public Profile page for each user that shows all the Twits for that user. Similar to dashboard feed, but only contains all Twits for that specific user. Also most recent first.
10. Ability for users to like or unlike a particular Twit that someone has made using AJAX.
11. Ability for users to add a comment on Twits. This will only be create functionality. No need for update / delete.
12. Sufficient automated tests to verify all functionality.
13. Ensure `requirements.txt` is included in your project.


Documentation should include the following for this, and all future assignments:
* Comments at the top of each source code file that you add or edit with:
  * Your Name
  * Class
  * Date
* A comment after the definition of each method describing what it does. I would highly suggest you use the ''' (triple quote) method for the comment.
* Comments in the rest of the code where it isn't obvious what is going on. (I prefer above the line comments vs at the end of the line because who likes to horizontally scroll, but either will work)

### Database Requirements
Here are the requirements for the database in an ERD. There are other authentication related tables that I did not include but are provided via Django's auth system. The Users table is the only one that really needed to be shown since there are so many relations between Users and our other tables. There are no relations between the other authentication tables and our tables, which is why I omitted them.

NOTE: For the URL field on the Twit model, you are not using an ImageField. Those are extremely hard to properly set up. Perhaps if the semester was twice as long we could consider. Instead, you are simply loading images via a URLField. Meaning that the user will provide a URL to image that already exists on the internet. This will be WAY easier for you to implement. If you have questions about it, ask.

![Database Entity Relationship Diagram](https://barnesbrothers.net/cis218/assignment_images/assignment_4/cis218_assignment_4_erd.png "Database Entity Relationship Diagram")

### Screenshots

Here are some images of the non-admin pages that I made for my key. This is more or less to give you an idea as to what the general concept is in case the written description is not clear. I realize that your assignment may not end up as elaborate in style as mine, so don't feel as though it needs to visually match mine exactly. I am looking for the general concept though. I will also mention that I used Bootstrap to do my styling.

#### Sign Up
![Sign Up](https://barnesbrothers.net/cis218/assignment_images/assignment_4/cis218_assignment_4_screenshot_sign_up.png "Sign Up")

#### Login
![Login](https://barnesbrothers.net/cis218/assignment_images/assignment_4/cis218_assignment_4_screenshot_login.png "Login")

#### Forgot Password
![Forgot Password](https://barnesbrothers.net/cis218/assignment_images/assignment_4/cis218_assignment_4_screenshot_forgot_password.png "Forgot Password")

#### Dashboard
![Dashboard](https://barnesbrothers.net/cis218/assignment_images/assignment_4/cis218_assignment_4_screenshot_feed.png "Dashboard")

#### Private Profile
![Profile](https://barnesbrothers.net/cis218/assignment_images/assignment_4/cis218_assignment_4_screenshot_personal_profile.png "Profile")

#### Public Profile
![Public Profile](https://barnesbrothers.net/cis218/assignment_images/assignment_4/cis218_assignment_4_screenshot_public_profile.png "Public Profile")

#### Twit Create
![Twit Creation](https://barnesbrothers.net/cis218/assignment_images/assignment_4/cis218_assignment_4_screenshot_twit_add.png "Twit Creation")

#### Twit Edit
![Twit Edit](https://barnesbrothers.net/cis218/assignment_images/assignment_4/cis218_assignment_4_screenshot_twit_edit.png "Twit Update")

#### Twit Delete
![Twit Delete](https://barnesbrothers.net/cis218/assignment_images/assignment_4/cis218_assignment_4_screenshot_twit_delete.png "Twit Delete")

#### Comment Add
![Comment Creation](https://barnesbrothers.net/cis218/assignment_images/assignment_4/cis218_assignment_4_screenshot_twit_comment_add.png "Comment Creation")


### Notes
Once you have added any additional packages that you need to your project. Be sure to run pip freeze to dump the package information to requirements.txt

  pip freeze > requirements.txt

Remember that you can see all available Bootstrap examples here:

https://getbootstrap.com/docs/4.0/examples/

In addition, you can find the documentation for Bootstrap here:

https://getbootstrap.com/docs/4.0/getting-started/introduction/

## Grading
| Feature                                     | Points |
|---------------------------------------------|--------|
| Custom User Model                           | 5      |
| Full User Sign Up / Authentication          | 5      |
| Password change / reset functionality       | 5      |
| Personal Profile page                       | 5      |
| Public Profile page. Twits from one user.   | 10     |
| Dashboard feed of Twits from all users      | 10     |
| CUD Twit                                    | 10     |
| Allowing Text and Picture URL in Twit       | 5      |
| Liking / Unliking a Twit                    | 10     |
| New Comment Form                            | 10     |
| Styling                                     | 5      |
| Automated Tests                             | 10     |
| Documentation                               | 5      |
| Readme                                      | 5      |
| **Total**                                   | **100**|

## Outside Resources Used



## Known Problems, Issues, And/Or Errors in the Program

