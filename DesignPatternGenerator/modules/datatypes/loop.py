from . import base
from . import basic

class Loop(base.Base):
    def __init__(self):
        super(base.Base, self).__init__()
        self.condition = ''
        self.contentlist = []