This readme is for the Django web framework application that will show the results
from our saved model from the Tf_serving document. This is basically  a simple application that takes the results from our client's output
and then uses Django to show the results on a web application.

The `tf_test_application` contains the web app project.
The `tf_model_test` contains the template and web urls. 

Steps: 
1) Start the server with `python manage.py runserver` to see if app works.

    Note: We can create a project using `django-admin startproject tf_test_application` and `python manage.py startapp tf_model_test` to start the application.

2) Include  `tf_model_tests.urls` in tf_test_application urls to point to application urls.

3) Create a folder called `templates` in `tf_model_test` and create a folder`tf_model_test` in that and include ur html files in that.

4) Add url endpoint in `tf_model_test` folders to `urls.py` file, the end point should seek same functions name as endpoint in `urls.py`.

5) Write the relative function in `views.py` file. 

6) Do `python manage.py runserver` to start app, this will open localhost application url. 

7) Go to localhost link and go to /test url to see results from saved model. 

Notes: At the end of this what we need to understand is we are enabling application to work from a saved model. So we have 2 servers running at this point. One `application server started with Django` and the other is the `TF Serving Server Model` the client application is able to talk to this. 