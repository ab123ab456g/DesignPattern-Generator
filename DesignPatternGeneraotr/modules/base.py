class Base_Parameter(object):
    def __init__(self):
        self.name = ''

class IBase(Base_Parameter):
    def tab(self):
        pass

class Base(IBase):
    def __init__(self):
        super(IBase, self).__init__()

