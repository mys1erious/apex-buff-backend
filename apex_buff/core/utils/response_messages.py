class Context(dict):
    def __init__(self):
        attrs = {
            'message': '',
            'detail': '',
            'errors': [],
            'data': {}
        }
        for key, val in attrs.items():
            super().__setattr__(key, val)
        super().__init__()

        self._created = False

    def update(self, other=None, **kwargs):
        if other is not None:
            if isinstance(other, dict):
                for k, v in other.items():
                    self[k] = v
            else:
                for k, v in other:
                    self[k] = v
        else:
            for k, v in kwargs.items():
                self[k] = v

    def __setitem__(self, key, value):
        if key not in self.__dict__:
            raise KeyError(key)
        dict.__setitem__(self, key, value)


class Messages:
    ERROR = {}
    SUCCESS = {}


def success_requests_base_msg(obj, name, request_type):
    request_types_map = {
        'POST': 'created',
        'PUT': 'updated',
        'DELETE': 'deleted'
    }

    return f'{obj} `{name}` has been successfully {request_types_map[request_type]}.'


def success_post_msg(obj, name):
    return success_requests_base_msg(obj, name, 'POST')


def success_put_msg(obj, name):
    return success_requests_base_msg(obj, name, 'PUT')


def success_delete_msg(obj, name):
    return success_requests_base_msg(obj, name, 'DELETE')


def error_requests_base_msg(obj, name, request_type):
    request_types_map = {
        'POST': 'creation',
        'PUT': 'update',
        'DELETE': 'deletion'
    }

    return f'Error during {request_types_map[request_type]} of {obj} `{name}`.'


def error_post_msg(obj, name):
    return error_requests_base_msg(obj, name, 'POST')


def error_put_msg(obj, name):
    return error_requests_base_msg(obj, name, 'PUT')


def error_delete_msg(obj, name):
    return error_requests_base_msg(obj, name, 'DELETE')


Messages.ERROR = {
    'VALIDATION': 'Validation errors have occurred.',
    'POST': error_post_msg,
    'PUT': error_put_msg,
    'DELETE': error_delete_msg
}
Messages.SUCCESS = {
    'POST': success_post_msg,
    'PUT': success_put_msg,
    'DELETE': success_delete_msg
}
