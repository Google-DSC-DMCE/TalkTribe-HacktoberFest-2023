# About
> TalkTribe is a social networking website that enables users to connect with others who share similar interests. Users can create chat rooms, join existing ones, and participate in discussions with other users. The website offers a search functionality to find chat rooms based on keywords or topic categories. Users can also view each other's profile

# How to _Run_ this project-

## 1.Clone the Repository:

```git clone https://github.com/Google-DSC-DMCE/TalkTribe-HacktoberFest-2023.git```

## 2.Setting Up the Virtual Environment (If you want)
2.1.Move the the project directory
```cd project1```

2.2.Create a Virtual Environment:
In the project directory, create a new virtual environment. If you haven't done this previously, you can use Python's built-in venv module (on macOS and Linux, use python3):

```python -m venv venv```

2.3.Activate the Virtual Environment:
Activate the virtual environment based on your operating system:
On Windows:
```venv\Scripts\activate```
On macOS and Linux:
```source venv/bin/activate```

## 3.Installing Dependencies
Install Project Dependencies:
With the virtual environment active, install the project's dependencies from the requirements.txt file:

```pip install -r requirements.txt```
If Problems occur, manually install the required packages using pip.

## 4.Running the Server
4.1.Set Up the Database:

If you're using a database other than SQLite, configure the database settings in your project, create the database, and apply migrations.

For SQLite, start with an empty database. If you have an existing database or data to share, provide it separately.

4.2.Run the Django Development Server:

Start the Django development server using the following command:
```python manage.py runserver```
Open a web browser and navigate to http://localhost:8000/ to view the Django project. If you've created a superuser account, you can access the admin interface at http://localhost:8000/admin/.
