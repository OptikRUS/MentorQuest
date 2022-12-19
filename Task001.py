class Request:
    _url: str
    _method: str
    _params = {}

    def __init__(self, url: str, method: str, **kwargs):
        self._url = url
        if method == 'get':
            self._method = 'GET'
        elif method == 'post':
            self._method = 'POST'
        else:
            self._method = None
        if 1 < len(kwargs) < 6:
            for key, value in kwargs.items():
                self._params[key] = value
        else:
            print('Неверное количество параметров')

    @property
    def url(self):
        url = ''
        if self._method == 'GET':
            url = f'https://{self._url}?'
            for k, v in self._params.items():
                url += f'{k}={v}&'
            else:
                url = url[:-1]
                url += '/'
        elif self._method == 'POST':
            url = f'https://{self._url}/'
        return url

    @property
    def method(self):
        return self._method

    @property
    def params(self):
        par = ''
        for k, v in self._params.items():
            par += f'{k}={v}, '
        return par[:-2]

request = Request('www.www.com', 'get', k=1, b=2)

print(request.method)
print(request.url)
print(request.params)
