

def index(request):
    '''
    If the query string "name" is supplied, we return
    Hello, {{name}}. If it's not, we ask about the user name.
    '''
    name = request.vars.get('name')
    context = {
        'message': 'Hello %s' % name if name else 'What\'s your name?',
        'method': request.request_method,
    }
    return context
