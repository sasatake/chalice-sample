from .validator import VALIDATOR
from ..util.responses import UnprocessableResponse
from functools import wraps


def handle_validation_error(schema_name):
    def wrapper(func):
        @wraps(func)
        def validation(*args, **kwargs):
            query = args[0].get('query_params').copy() if args[0].get(
                'query_params') else {}
            uri = args[0].get('uri_params').copy() if args[0].get(
                'uri_params') else {}
            query.update(uri)
            result = VALIDATOR.validate(schema_name, query)

            if not result['result']:
                return UnprocessableResponse(errors=result['errors'])

            return func(*args, **kwargs)

        return validation

    return wrapper
