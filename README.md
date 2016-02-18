# MyOwnPythonFramework


A MVC and WSGI compliant *web framework*.

I DO NOT recommend use in production. I'm writing this web framework for learning purpose only, at least until now.


# How to

Clone the repository. Execute the server.py file and access http://127.0.0.1:8080/ from the web browser.

You can write your on controllers in the controllers.py file.

Views and models are not implemented yet.


# Files

* server.py - Start the server using werkzeug module.

* request.py - Contains a class that parse de information from the request and return it when needed.

* main.py - That's the parte that talks to the webserver. It receives the information and returns it processed.

* router.py - The function that will handler url and tell to the application what controller is being requested.

* controller.py - Where you define the functions(pages) of the web application.


# TODOs

* Tests.

* Implement a template engine for the view.

* Implement a model file.

* Create a setup.py