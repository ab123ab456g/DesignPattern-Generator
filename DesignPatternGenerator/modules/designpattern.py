from . import base
from . import basic

class DesignPattern(base.Base):
    def __init__(self):
        super(base.Base, self).__init__()
        self.type = ''
        self.classlist = []
    def addClassList(self, class_):
        self.classlist.append(class_)