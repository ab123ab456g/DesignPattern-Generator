from . import base
from . import variable 
from . import Operator
from . import structure
from . import function


class G_Variable(base.Base_Generator):
    def __init__(self):
        super().__init__()
    def generate(self, object):
        if variable.Variable.isSetValue(object) and variable.Variable.isSameType(object):
            if object.datatype == 'str' or object.datatype == '' or object.datatype == None:
                return object.name + ' = ' + '\'' + str(object.value) + '\''
            elif object.datatype == 'set':
                if type(object.value)  == str:
                    return object.name + ' = '  + str(set(object.value))
                else:
                    return object.name + ' = '  + str(set(object.value)) 
            else:
                return object.name + ' = '  + str(object.value)

class G_Operator(base.Base_Generator):
    def __init__(self):
        super().__init__()
    def generate(self, object):
        if Operator.Operator.isSetValue(object) and Operator.Operator.isSameType(object):
            return object.str1 + ' ' + object.operator + ' ' + object.str2

class G_Structure(base.Base_Generator):
    def __init__(self):
        super().__init__()
        self.g_operator = G_Operator()
    def generate(self, object):
        if structure.Structure.isSetValue(object) and structure.Structure.isSameType(object):
            condition = self.g_operator.generate(object.condition)
            content = 'pass'
            return 'if ' + condition + ' :\n' + content

class G_Function(base.Base_Generator):
    def __init__(self):
        super().__init__()
    def generate(self, object):
        if function.Function.isSetValue(object) and function.Function.isSameType(object):
            content = 'pass'
            return 'def ' + object.name + '():\n' + content
