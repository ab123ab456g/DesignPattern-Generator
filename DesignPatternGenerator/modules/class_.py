from . import base
from . import basic

class Class(base.Base):
    def __init__(self):
        super(base.Base, self).__init__()
        self.parameterlist = []
        self.methodList = []