

def index(request):
    message = 'Welcome to the Other App. lol'

    context = {
        'message': message,
    }
    return context
