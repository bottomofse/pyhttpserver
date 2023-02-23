class Request:
    def __init__(self, raw_request):
        row_header, *row_body = raw_request.split(b'\r\n\r\n')
        self.hear = RequestHeader(row_header)
        self.body = RequestBody(row_body[0]) if row_body else None

    def __str__(self):
        return str(vars(self))

class RequestHeader:
    def __init__(self, raw_header):
        self.raw_header = raw_header
        print(raw_header)

    def __str__(self):
        return str(vars(self))

class RequestBody:
    def __init__(self, raw_body):
        self.raw_body = raw_body
        print(raw_body)

    def __str__(self):
        return str(vars(self))