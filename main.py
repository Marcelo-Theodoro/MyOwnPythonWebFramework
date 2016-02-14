from request import Request
from router import router


def app(env, start_response):
    # Create the request object
    request = Request(env)

    # Defines which controller is being requested
    controller_requested = router(request.url)

    try:
        # Try to import the controller requested.
        func = getattr(__import__('controllers'), controller_requested)
    except AttributeError:
        # The requested controller does not exists
        start_response('404 NOT FOUND', [('Content-Type', 'text/html; charset=utf-8')])
        return [b'NOT FOUND']

    # Execute the controller
    controller_response = func(request)

    # Start the response
    start_response('200 Ok', [('Content-Type', 'text/html; charset=utf-8')])
    response_body = str(controller_response)
    return [response_body.encode()]

