# not support strange variable

datatype = ['int', 'str', 'None', 'list', 'dict', 'set', 'tuple', 'other']

class Base_Parameter(object):
    def __init__(self):
        self.name = ''
        self.space = '    '

class IBase(Base_Parameter):
    def tab(self):
        pass

class Base(IBase):
    def __init__(self):
        super(IBase, self).__init__()

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

class G_other(Variable):
    def __init__(self):
        super(Variable,self).__init__()
        self.datatype = 'other'



#test int
# v =Variable()
# v.name = 'abc'
# v.datatype = 'int'
# v.value = '53'
# print(v.generate())

#test string
# v =Variable()
# v.name = 'abc'
# v.datatype = 'str'
# v.value = '53'
# print(v.generate())

#test None
# v =Variable()
# v.name = 'abc'
# v.datatype = 'str'
# v.value = None
# print(v.generate())

#test list
# v =Variable()
# v.name = 'abc'
# v.datatype = 'list'
# v.value = []
# print(v.generate())

# #test dict
# v =Variable()
# v.name = 'abc'
# v.datatype = 'dict'
# v.value = {}
# print(v.generate())

# #test set
# v =Variable()
# v.name = 'abc'
# v.datatype = 'set'
# v.value = set({1:1,2:2})
# print(v.generate())

# #test tuple
# v =Variable()
# v.name = 'abc'
# v.datatype = 'dict'
# v.value = (1,2)
# print(v.generate())

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
