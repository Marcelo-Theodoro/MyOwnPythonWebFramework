
def router(url, default_app='myapp', default_index='index'):
    '''
    Do the url router thing.
    Not totally implemented yet.

    '''

    if len(url) == 0:
        return (default_app, default_index)
    elif len(url) == 1:
        return (url[0], default_index)
    return (url[0], url[1])
