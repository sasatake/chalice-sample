from chalice import Response
from ..util.responses import SuccessResponse
from ..validators.handler import handle_validation_error


@handle_validation_error('get_product')
def get_product(request={}) -> Response:
    return SuccessResponse(body=request)
