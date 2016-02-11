# MyOwnPythonFramework


A WSGI compliant ?micro-framework?.

I DO NOT recommend use in production. I'm writing this framework for learning purpose only, at least until now.


# How to

Clone the repository. Execute the server.py file, access http://127.0.0.1:8080/ from the web browser.


# Files:

* server.py - Start the server using werkzeug module.

* request.py - Contains a class that parse de information from the request and return it when needed.

* main.py - That's the parte that talks to the webserver. It receives the information and returns it processed.

* controller.py - Where you define the functions(pages) of the web application.