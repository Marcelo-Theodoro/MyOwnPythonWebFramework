class Request(object):
    '''
    Class to parse the client request.
    Each method of the class should take care of
    one of the environ variables[1].

    [1] https://www.python.org/dev/peps/pep-3333/#id24
    '''

    def __init__(self, env):
        self.env = env
        # Parse the infos of the request.
        self.url = self.PathInfoParser(self.env['PATH_INFO'])
        self.vars = self.QueryStringParser(self.env['QUERY_STRING'])
        self.request_method = self.RequestMethodParser(self.env['REQUEST_METHOD'])

    def RequestMethodParser(self, request_method):
        '''
        There's not so much to be done here yet.
        '''
        return request_method

    def PathInfoParser(self, path_info):
        '''
        PATH_INFO is the remainder of the requested URL.
        This method turns it to a list, eg:
        '/user/mike' to ['client', 'mike']
        '''
        return [n for n in path_info.split('/') if n]

    def QueryStringParser(self, query_string):
        '''
        Receive query_string and return a dict with all the vars if any.
        Any invalid query strings like '&b=' or '&=f' are ignored.
        '''
        QR = {}
        for q in query_string.split('&'):
            if '=' in q:
                key, value = q.split('=', 1)
                if key and value:
                    QR[key] = value
        return QR
