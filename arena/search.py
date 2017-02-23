from arena.resource import Resource, paginated


class Search(Resource):
    base_endpoint = '/search'

    @paginated
    def all(self, query, **kwargs):
        kwargs['params'].update({'q': query})
        return self._get('', params=kwargs['params'])

    @paginated
    def channels(self, query, **kwargs):
        kwargs['params'].update({'q': query})
        return self._get('/channels', params=kwargs['params'])

    @paginated
    def blocks(self, query, **kwargs):
        kwargs['params'].update({'q': query})
        return self._get('/blocks', params=kwargs['params'])

    @paginated
    def users(self, query, **kwargs):
        kwargs['params'].update({'q': query})
        return self._get('/users', params=kwargs['params'])


search = Search()
