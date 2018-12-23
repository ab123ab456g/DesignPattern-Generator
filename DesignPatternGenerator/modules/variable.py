from . import base
from . import basic

class Variable(base.Base):
    def __init__(self):
        super(base.Base, self).__init__()
        self.datatype = ''
        self.value = ''

class G_Int(Variable):
    def __init__(self):
        super(Variable,self).__init__()
        self.datatype = 'int'

class G_Str(Variable):
    def __init__(self):
        super(Variable,self).__init__()
        self.datatype = 'str'

class G_List(Variable):
    def __init__(self):
        super(Variable,self).__init__()
        self.datatype = 'list'

class G_Dict(Variable):
    def __init__(self):
        super(Variable,self).__init__()
        self.datatype = 'dict'

class G_Set(Variable):
    def __init__(self):
        super(Variable,self).__init__()
        self.datatype = 'set'

class G_Tuple(Variable):
    def __init__(self):
        super(Variable,self).__init__()
        self.datatype = 'tuple'



class G_Other(Variable):
    ''''doc object string'''
    def __init__(self, Obj):
        super(Variable,self).__init__()
        self.datatype = 'other'
        self.value = Obj

class VariableFactory(object):
    def setVariable(self):
        return Variable()
    def setInt(self):
        return G_Int()
    def setStr(self):
        return G_Str()
    def setList(self):
        return G_List()
    def setDict(self):
        return G_Dict()
    def setSet(self):
        return G_Set()
    def setTuple(self):
        return G_Tuple()
    def setOther(self, otherObj):
        return G_Other(otherObj)
