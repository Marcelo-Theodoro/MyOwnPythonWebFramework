from request import Request

def app(env, start_response):
    # Request infos
    r_path_info = env['PATH_INFO']
    r_vars = env['QUERY_STRING']
    # Creating the object 'request' and it will parse the informations
    request = Request(r_path_info, r_vars)

    # Import the controller requested. If not found throw a 404 error.
    try:
        func = getattr(__import__('controllers'), request.controller)
    except AttributeError:
        start_response('404 NOT FOUND', [('Content-Type', 'text/html; charset=utf-8')])
        return [b'NOT FOUND']

    # Execute the controller
    controller_response = func(request)

    # Start the response
    start_response('200 Ok', [('Content-Type', 'text/html; charset=utf-8')])
    response_body = str(controller_response)
    return [response_body.encode()]

