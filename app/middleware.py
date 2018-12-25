from django.utils.deprecation import MiddlewareMixin


class GlobalRequestMiddleware(MiddlewareMixin):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def process_request(self, request):
        GlobalRequestMiddleware.__instance = request

    @classmethod
    def getRequest(cls):
        return cls.__instance
