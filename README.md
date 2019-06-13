This is a vuejs + Django app in which the user can upload, delete and view the list of all the videos uploaded.

#Setting up the project

install python
install pip
install virtualenv
After that create virtual enviroment using the following command virtualenv venv <enviorment_name>

Activate the enciroment : source <enviorment_name>/bin/activat6

now goto testapp folder and run the following commands:

python manage.py makemigraions
python manage.py migrate
python manage.py runserver
now go out of the folder and cd to frontend in fontend folder run

npm install
npm run dev
Now browse to localhosst:8080 to view the app.
