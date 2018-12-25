from . import base
from . import basic

class Function(base.Base):
    def __init__(self):
        super(base.Base, self).__init__()
        self.parameterlist = []
        self.contentlist = []
    def isSetValue(function):
        if function.name != '':
            return True
        else:
            return False
    def isSameType(variable):
        if issubclass(type(variable), Function):
            return True
        else:
            return False