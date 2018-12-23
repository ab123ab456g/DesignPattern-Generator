from . import base
from . import basic

class Operator(base.Base):
    def __init__(self):
        super(base.Base, self).__init__()
        self.str1 = ''
        self.operator = ''
        self.str2 = ''
