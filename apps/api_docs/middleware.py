class ContentTypeMiddleware(object):

    def process_request(self, request):
        content_type = getattr(request.META, "CONTENT_TYPE", "")
        if content_type == 'application/x-www-form-urlencoded; charset=UTF-8':
            request.META['CONTENT_TYPE'] = 'application/x-www-form-urlencoded'
        return None
