from chalice import Response


class UnprocessableResponse(Response):
    def __init__(self, errors):
        body = {"title": "invlaid parameters", "errors": errors}
        status_code = 422
        headers = {'Content-Type': 'application/problem+json'}
        return super().__init__(
            body=body, status_code=status_code, headers=headers)


class SuccessResponse(Response):
    def __init__(self, body):
        body = {"title": "ok", "response": body}
        status_code = 200
        headers = {'Content-Type': 'application/json'}
        return super().__init__(
            body=body, status_code=status_code, headers=headers)
