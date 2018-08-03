from cerberus import schema_registry, Validator


class ProductValidator:
    def __init__(self):
        print('validator init')
        schema_registry.add(
            'getProduct',
            {'id': {
                'type': 'integer',
                'min': 10,
                'max': 100,
                'coerce': int
            }})
        self.registry = schema_registry

    def validate(self, name, params):
        result = {}
        v = Validator(self.registry.get(name), allow_unknown=True)
        result['result'] = v.validate(params if params else {})
        result['errors'] = v.errors
        return result


VALIDATOR = ProductValidator()
