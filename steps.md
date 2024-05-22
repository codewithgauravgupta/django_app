* Start Front end developement

* mkdir frontend -> yarn create react-app frontend-social-media-app

* cd frontend-social-media-app/ && yarn start

* Adding the React Router: yarn add react-router-dom@6

* edit the index.js for browserRouter

* Adding React Bootstrap: yarn add react-bootstrap bootstrap

*  import the bootstrap CSS file into the index.js file

* Creating the Home page by following steps:
    Creating the component and the page.
        Create a directory in src called pages.
            Inside the pages directory, create a new file called Home.jsx. This file will contain the UI for the Profile page:
                Register this page in the App.js file
    Registering the page in BrowserRouter with a URL.

* yarn add axios axios-auth-refresh and create a directory called `helpers` in the src folder of the React project and we’ll add a file called `axios.js`:

* protected routes: Create a new directory in the src directory called `routes` and create a file called `ProtectedRoute.jsx`.

* Adding a registration page

* Create login page, Inside the src/components/authentication directory, add a new file called LoginForm.jsx.

* Register login page, Inside the src/pages directory, create a file called Login.jsx

* Create custom hook, Inside the src directory, create a new directory called hooks. This directory will contain all the Hooks.

* Inside the newly created directory, add a file called user.actions.js.

* We are done with ui for auth, next we will do it for posts. We’ll implement listing, creating, updating, and deleting post features.

* Adding the NavBar component, Inside the src/components/ directory, add a new file called Navbar.jsx. 

* yarn add timeago.js, swr, @ant-design/icons@4.0.0

* Next updating a post

* Deleting a comment

* Next updating a comment

* Liking a comment

* User Profiles: Listing profiles on home page. In the src/components file, create a new directory called profile and inside it ProfileCard.jsx 

* import in home.jsx.

* Displaying user information on profile page.

* Configure django to upload files for avatar, Inside the settings.py file of the project:
    # Media files
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'uploads'

* Modify avatar field of user model.

* python manage.py makemigrations
python manage.py migrate

* Configure default avatar, In the settings.py file of the Django project:
    DEFAULT_AVATAR_URL = "https://api.dicebear.com/8.x/personas/svg"

* To create the ProfileDetails component, we have to create the file that will contain the code for this component, add the logic for the navigation, write the UI (JSX), and import the component on the “Profile” page

* Edit profile info

* The React application is nearly done. We have CRUD operations for authentication, posts, comments, and new users. Now, it’s time to focus on the quality and maintainability of our components.

* Testing frontend: 
* yarn add @faker-js/faker 
* yarn add uuid --dev
* yarn add jest-localstorage-mock --dev

* snapshot testing
* yarn add react-test-renderer

* Create a docker image:
    docker build -t django-project .

* Run docker image as container:
    docker run --name django-app -d -p 8000:8000 django-project

* Check running container:
    docker container ps -a

* Check logs of running container:
    docker logs --details django-app

* We must keep Dockerfile and Dockercompose in same directory, the above image we have create and the dcker file for our app will be added as a service in compose, along with other containers.

* pip install gunicorn
* pip install python-dotenv

* Configure env variables

* Config nginx.conf

* docker compose up -d --build

* Execute tests in container: remove all blank tests.py file before: 
    docker compose exec -T api pytest

