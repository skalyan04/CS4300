Commands For Setting Up:
- cd movie_theater_booking <-- to navigate into the project directory
- source ../myenv/bin/activate <-- to activate the virtual environment
- pip install -r ../requirements.txt <-- install the dependencies
- python manage.py migrate <-- run database migrations
- python manage.py runserver <-- Start the development server

SuperUser Login Information for Creating Movies for the Bookings, etc:
Username: user
Email: user@email.com
Password: yellow

To Add Movies as Admin:
- python manage.py createsuperuser <-- to create a superuser account to log in with, already created one in this case
- python manage.py runserver <-- make sure the server is running, run it from within the first mvoie_theater_booking because that's where it is
- Go to: http://127.0.0.1:8000/admin/ and you can see everything, including the ability to add a movie with title, description and duration before hitting save as well.

After adding the movies, view them live at: http://127.0.0.1:8000/movies/

To use the actual application to book a seat in a movie:
Go to: http://127.0.0.1:8000/ <-- AFTER ACTIVATING the server

JSON Responses for the API Models Found at the Following Links:
http://127.0.0.1:8000/api/movies/
http://127.0.0.1:8000/api/seats/
http://127.0.0.1:8000/api/bookings/
