# iitdh-merch-backend

This website is to check the orders placed by the customers and mark the orders as delivered by the agent.

This repo is a backend repo for the website.

We have used django framework for the backend.

---

### Setup

1. Download the Repository to your local machine <br>
2. Create a Virtual Environment in the [backend](./) folder with this command below <br>
   `python -m venv venv`
3. Activate the environment with this command <br>
   `.\venv\Scripts\activate`
4. Install the dependencies <br>
   `pip install -r requirements.txt `
5. Ensure that you have the PostgreSQL installed on your machine and is running on PORT **5432**

### Running the Application

1. Activate the environment with this command. <br>
   `.\venv\Scripts\activate`
2. Start the application by running this command (_Run the command where [manage.py](./manage.py) is
   located_) <br>
   ` python manage.py runserver`

### Accessing the Admin Panel

1. You can access the admin panel by running the server and opening <http://localhost:8000/admin>
2. Run `python manage.py createsuperuser` to create a user to access the admin panel.
3. Set up the Username and Password
4. You can log in and change the database values anytime.

### Loading Data

Run `python manage.py process_tasks` to load the data from the csv files.

### Deploying

1. Add the hosted domain name in `ALLOWED_HOSTS` in [settings.py](./backend/settings.py)
2. Update the `CORS_ORIGIN_WHITELIST` list and `CORS_ORIGIN_ALLOW_ALL` variable
3. Update the `DATABASES` in [settings.py](./backend/settings.py)
4. Set the Environment variables in [dev.env](./dev.env)

