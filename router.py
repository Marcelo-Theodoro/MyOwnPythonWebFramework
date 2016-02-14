
def router(url, index='index'):
    '''
    Do the url router thing.
    Not totally implemented yet.
    '''
    if not url:
        return index
    return url[0]
