<h1 align="center">Moview - Movie Review Site</h1>

[View the live project here.](https://moview-site.herokuapp.com/)

## User Experience (UX)

-   ### User stories

    -   #### First Time Visitor Goals

        1. As a First Time Visitor, I want to understand the purpose of the site and what I can do.
        2. As a First Time Visitor, I want to be able to easily navigate throughout the site to find movies and reviews.
        3. As a First Time Visitor, I want to be able to sign up for an account for the site to access more capabilities.

    -   #### Returning Visitor Goals

        1. As a Returning Visitor, I want to add a new movie entry of one of my favourite films.
        2. As a Returning Visitor, I want to leave a review on a movie I have seen before that has an entry.
        3. As a Returning Visitor, I want to see my profile and the reviews I have left before, and edit those reviews.

    -   #### Frequent User Goals
        1. As a Frequent User, I want to check to see if there are any newly added movies.
        2. As a Frequent User, I want to check to see if there are any reviews other than my own on movies.
        3. As a Frequent User, I want to check and see if there are any movies worth watching based on others' reviews.

-   ### Design
    -   #### Colour Scheme
        -   The two main colours used are pink and blue.
    -   #### Typography
        -   The Nunito font is the large headers font used in the site and the subtext is Raleway.
    -   #### Imagery
        -   The main background image I encorporated was from [Wallpaper Better](https://www.wallpaperbetter.com).
        -   The other images used in the site are user specific and uploaded by them through URLs.

*   ### Wireframes

    -   Wireframe - [View]( https://wireframepro.mockflow.com/view/ )

## Features

-   Responsive on all device sizes

-   CRUD Functionality on movies and reviews

## Technologies Used

-   [Flask](https://flask.palletsprojects.com/en/2.0.x/) 
-   [PyMongo](https://pypi.org/project/pymongo/)

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://www.javascript.com/)
-   [Python](https://www.python.org/)

### Frameworks, Libraries & Programs Used

1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Titillium Web' font into the style.css file which is used on all pages throughout the project.
2. [jQuery:](https://jquery.com/)
    - jQuery came with Materialize to make the components functional but also was used to add event listeners and assist with creating cleaner JS.
3. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
4. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
5. [Photoshop:](https://www.adobe.com/ie/products/photoshop.html)
    - Photoshop was used to create the logo, resizing images and editing photos for the website.
6. [MockFlow:](https://mockflow.com/)
    - Balsamiq was used to create the [wireframes](https://github.com/) during the design process.

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C Markup Validator](https://validator.w3.org/) - [Results](./docs/css-validate.png)
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://github.com/)

### Testing User Stories from User Experience (UX) Section

-   #### First Time Visitor Goals

     1. As a First Time Visitor, I want to understand the purpose of the site and what I can do.

        1. Upon entering the site, users are automatically greeted with a clean and easily readable navigation bar to go to the page of their choice. Underneath there page title and description about the site and it's capabilites.
        2. The main points are made immediately with the description
        3. The user has two options, click the movie posters or links or scroll down, both of which will lead to the same place, to view more movies.

    2. As a First Time Visitor, I want to be able to easily navigate throughout the site to find movies and reviews.

        1. The site has been designed to be fluid and never to entrap the user. At the top of each page there is a clean navigation bar, each link describes what the page they will end up at clearly.
        2. The contents table on the side of the page clearly lists all movies with a click on the link sending the user to that part of the page.
        3. In each movie entry is a scrollable section displaying the reviews and it's subsequent reviewer.

    3. As a First Time Visitor, I want to be able to sign up for an account for the site to access more capabilities.
        1. When the new visitor loads the page, they are displayed a modal notifying them of their limited capabilities, presenting them with 
        two buttons to login or register.
        2. The user can also click on one of the naviagation links to login or register.

-   #### Returning Visitor Goals

    1. As a Returning Visitor, I want to add a new movie entry of one of my favourite films.

        1. These are clearly shown in the Add Movie Entry panel.
        2. They can also click the link in the navbar to add a movie.

    2. As a Returning Visitor, I want to leave a review on a movie I have seen before that has an entry.

        1. The movies are displayed fluidly on one page with either poster click, side content click, or scroll navigation available to access them.
        2. In each entry is a review section with a large add button, allowing the user to submit a new review.
        3. Upon clicking the button a modal appears with a textarea for the review itself.
        4. When a user submits that review, a notification is displayed confirming the success or failure of said request.
        5. If successful, the user can see their new review instantly in the movie entry.

    3. As a Returning Visitor, I want to see my profile and the reviews I have left before, and edit those reviews.
        1. When looking at the movie entries reviews, the reviewers username is displayed. If the username is of the user, an edit and delete button clearly appear for that user.
        2. If the user clicks the edit button a modal will pop up with the current review in the textarea, and if they click delete a confirm modal will popup, ensuring the user is sure they want to complete the irreversible action.

-   #### Frequent User Goals

    1. As a Frequent User, I want to check to see if there are any newly added movies.

        1. The user would already be comfortable with the website layout and can easily check the contents list, poster collection, or scroll down to view all the entries.

    2. As a Frequent User, I want to check to see if there are any reviews other than my own on movies.

        1. The user would already be comfortable with the website layout and can easily view the reviews on the movies they submitted.

    3. As a Frequent User, I want to edit one of my movie entries.
        1. For every movie a user entered, an edit and delete button will clearly be displayed indicating their authority to do so.
        2. On clicking the edit link, the user is redirected to the edit page, with a form displaying all the current data to be edited.
        3. There is a confirm modal if a user wishes to delete an entry after pressing the delete button. They are warned of the irreversability of their actions and made confirm their choice.

### Further Testing

-   The Website was tested on Google Chrome, Firefox and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, RealMe7, and Google Pixel.
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Known Bugs

-   On some mobile devices the there is side scroll due to minimal overflow.
    -   A slight side movement is visible when swiping left or right
-   When certain movie fields are left empty, the border doesn't span the height of the cell on the movies page.
-   The starring chips can prevent the placeholder being displayed on the edit movie page, even though the starring was left empty.

## Deployment

### Heroky

The project was deployed to GitHub Pages using the following steps...

1. Log in to Heroku and add a new app.
2. Click link with GitHub and enter the repository name under the account you have linked with Heroku.
3. Add all necessary environment varaibles, to the config vars section under settings.
4. Add a requirements.txt and Procfile into your repo to ensure that the correct modules are installed and the python proccess is run.
5. Click the "Open App" button at the top of the page, after a successful build.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/gamefootage/mongo-movie-review)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/gamefootage/mongo-movie-review)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/gamefootage/mongo-movie-review
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/gamefootage/mongo-movie-review
> Cloning into `mongo-movie-review`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

### Content

-   All content was written by the developer or taken from [Wikipedia](https://en.wikipedia.org/wiki/Wiki).

### Media

-   Images were taken off Google Images and from [PNG Tree](https://pngtree.com/), [Wallpaper Better](https://www.wallpaperbetter.com/), and [IMDB](https://www.imdb.com/).

### Acknowledgements

- Myself for pulling this off in time after a week in the hospital.

- The doctors for allowing my laptop in the hospital and helping me get better in time to complete this project.