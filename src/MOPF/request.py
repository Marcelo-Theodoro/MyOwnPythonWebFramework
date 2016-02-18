class Request(object):
    '''
    Class to parse and return information about the client request.
    '''

    def __init__(self, env):
        self.env = env
        # Parse the infos of the request.
        self.url = self.PathInfoParser(self.env['PATH_INFO'])
        self.vars = self.QueryStringParser(self.env['QUERY_STRING'])

    def PathInfoParser(self, path_info):
        '''
        Receives path_info and returns a list within all the
        requested path.
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
