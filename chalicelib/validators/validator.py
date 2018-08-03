from cerberus import schema_registry, Validator as validator


class Validator:
    def __init__(self):
        schema_registry.add(
            'get_product',
            {'id': {
                'type': 'integer',
                'min': 10,
                'max': 100,
                'coerce': int
            }})
        self.registry = schema_registry

    def validate(self, name, params):
        result = {}
        v = validator(self.registry.get(name), allow_unknown=True)
        result['result'] = v.validate(params if params else {})
        result['errors'] = v.errors
        return result


VALIDATOR = Validator()
