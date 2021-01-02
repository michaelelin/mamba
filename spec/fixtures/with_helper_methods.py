from mamba import description, it
from expects import expect, equal

def wrap_func(f):
    def wrapper():
        return f()
    return wrapper

with description('Fixture#with_helper_methods'):
    def helper_method(self):
        pass

    @property
    def helper_property(self):
        pass

    @wrap_func
    def wrapped_helper_method(self):
        pass
