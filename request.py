class Request(object):
    '''
    Class to parse and return information about the client request.
    '''
    def __init__(self, args, vars, index='index'):
        self.index = index
        # Parse controller, args and vars
        self.controller, self.args = self.PathInfoParser(args)
        self.vars = self.QueryStringParser(vars)

    def __repr__(self):
        return 'controller: {0}, args: {1}, vars: {2}'.format(self.controller,
                                                              self.args, self.vars)

    def PathInfoParser(self, path_info):
        '''
        Receive path_info and parse the controller(first argument in the url),
        and args(the rest of the arguments if any).
        Return a tuple with (controller, args)
        '''
        if not path_info or path_info == '/':
            path_info = (self.index, [])
        else:
            path_info = [n for n in path_info.split('/') if n]
            path_info = (path_info[0], path_info[1:])
        return path_info

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