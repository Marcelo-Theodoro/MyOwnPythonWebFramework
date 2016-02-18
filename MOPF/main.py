import os
import sys
from importlib import import_module
from request import Request
from router import router

MOPF_HOME = os.path.abspath(os.path.join(os.path.dirname( __file__  ), '..'))
MOPF_APPLICATIONS = os.path.join(MOPF_HOME, 'applications')

def app(env, start_response):
    # Create the request object
    request = Request(env)

    # Defines which app and controller is being requested
    # The url must be something like:
    #   http://127.0.0.1:8080/[app]/[controller]
    app_requested, controller_requested = router(request.url)

    try:
        # Try to import the controller requested.
        if MOPF_APPLICATIONS not in sys.path:
            sys.path.insert(0, MOPF_APPLICATIONS)
        # import the module and 'func' will get the attributes of the controller_requested
        func = getattr(import_module('{0}.controllers'.format(app_requested)),
                       controller_requested)
    except AttributeError:
        # The requested controller/app does not exists
        start_response('404 NOT FOUND', [('Content-Type', 'text/html; charset=utf-8')])
        return [b'NOT FOUND']

    # Execute the controller
    controller_response = func(request)

    # Start the response
    start_response('200 Ok', [('Content-Type', 'text/html; charset=utf-8')])
    response_body = str(controller_response)
    return [response_body.encode()]


