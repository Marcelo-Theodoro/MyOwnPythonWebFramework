

def index(request):
    try:
        message = 'Hello {}'.format(request.vars['name'])
    except KeyError:
        message = 'What is your name?'

    context = {
        'message': message,
    }
    return context
