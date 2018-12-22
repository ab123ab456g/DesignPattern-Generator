from .base import Base
# not support strange variable
class Datatype:
    datatype = ['int', 'str', 'None', 'list', 'dict', 'set', 'tuple', 'other']


class Variable_Parameter(Base):
    def __init__(self):
        super(Base, self).__init__()
        self.datatype = ''
        self.value = ''
class IVariable(Variable_Parameter):
    def generate(self):
        pass

class Variable(IVariable):
    def __init__(self):
        super(IVariable, self).__init__()
    def generate(self):
        if self.datatype == 'str':
            return self.name + '='  + '\'' + str(self.value) + '\''
        elif self.datatype == 'set':
            return self.name + '='  + str(set(self.value))
        else:
            return self.name + '='  + str(self.value)

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
    def __init__(self):
        super(Variable,self).__init__()
        self.datatype = 'other'

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
    def setOther(self):
        return G_Other()

# from datetime import datetime
# # #test datetime
# v =Variable()
# v.name = 'abc'
# v.datatype = 'datetime'
# v.value = datetime.now()
# print(v.generate())

# #test variable in function
# v =Variable()
# v.name = 'name'
# v.datatype = 'int'
# v.value = 1
# print(v.generate())

# #test variable in module
# v =Variable()
# v.name = 'self.name'
# v.datatype = 'int'
# v.value = 1
# print(v.generate())
