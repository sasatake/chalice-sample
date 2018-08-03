from ..util.logger import getLogger
from ..validators.product import VALIDATOR
from .responses import UnprocessableResponse, SuccessResponse


def _get_parameters_decorator(func):
    def marge_parameters(*args, **kwargs):
        query = args[0].get('query_params').copy() if args[0].get(
            'query_params') else {}
        uri = args[0].get('uri_params').copy() if args[0].get(
            'uri_params') else {}
        query.update(uri)
        result = func(*args, params=query)
        return result

    return marge_parameters


@_get_parameters_decorator
def get_product(request={}, params={}):
    logger = getLogger('getProduct')
    validation = VALIDATOR.validate('getProduct', params)

    if not validation['result']:
        logger.error({'params': request, 'errors': validation['errors']})
        return UnprocessableResponse(errors=validation['errors'])

    return SuccessResponse(body=request)
