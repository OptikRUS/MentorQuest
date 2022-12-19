class Request:
    url: str
    method: str
    params = {}

    def __init__(self, url: str, method: str, **kwargs):
        self.url = url
        if method == 'get':
            self.method = 'GET'
        elif method == 'post':
            self.method = 'POST'
        else:
            self.method = None
        if 1 < len(kwargs) < 6:
            for key, value in kwargs.items():
                self.params[key] = value
        else:
            print('Неверное количество параметров')


request = Request('www.www.com', 'get', k=1, b=2)

print(request.method)
print(request.url)
print(request.params)
