class ApiUtils:
    def __init__(self, api_request):
        self.api_request = api_request

    def post_method(self, url, **kwargs):
        return self.api_request.post(url=url, **kwargs)

    def put_method(self, url, **kwargs):
        return self.api_request.put(url=url, **kwargs)

    def get_method(self, url, **kwargs):
        return self.api_request.get(url=url, **kwargs)

    def delete_method(self, url, **kwargs):
        return self.api_request.delete(url=url, **kwargs)

    def patch_method(self, url, **kwargs):
        return self.api_request.patch(url=url, **kwargs)
