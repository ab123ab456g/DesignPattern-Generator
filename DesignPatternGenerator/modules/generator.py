from . import base
from . import variable 
from . import Operator
from . import structure
from . import function
from . import class_


class G_Base(object):
    def generate(self, object):
        pass

class G_Variable(G_Base):
    def __init__(self):
        super().__init__()
    def generate(self, object):
        if base.Variable.isSetValue(object) and base.Variable.isSameType(object):
            if object.datatype == 'str' or object.datatype == '' or object.datatype == None:
                return object.name + ' = ' + '\'' + str(object.value) + '\''
            elif object.datatype == 'set':
                if type(object.value)  == str:
                    return object.name + ' = '  + str(set(object.value))
                else:
                    return object.name + ' = '  + str(set(object.value)) 
            else:
                return object.name + ' = '  + str(object.value)

class G_Operator(G_Base):
    def __init__(self):
        super().__init__()
    def generate(self, object):
        if base.Operator.isSetValue(object) and base.Operator.isSameType(object):
            return object.str1 + ' ' + object.operator + ' ' + object.str2

class G_Structure(G_Base):
    def __init__(self):
        super().__init__()
        self.G_Operator = G_Operator()
        self.G_Content = G_Content()
    def generate(self, object):
        if base.Structure.isSetValue(object) and base.Structure.isSameType(object):
            condition = self.G_Operator.generate(object.condition)
            content = 'pass'
            return 'if ' + condition + ' :\n' + content

class G_Function(G_Base):
    def __init__(self):
        super().__init__()
        self.G_Content = G_Content()
    def generate(self, object):
        if base.Function.isSetValue(object) and base.Function.isSameType(object):
            content = 'pass'
            return 'def ' + object.name + '():\n' + content

class G_Class(G_Base):
    def __init__(self):
        super().__init__()
        self.G_Content = G_Content()
    def generate(self, object):
        content = 'pass'
        if base.Class.isSetValue(object) and base.Class.isSameType(object):
            if base.Class.isInherit(object):
                return 'class ' + object.name + '(' + object.inherit_class + '):\n' + content
            else:
                return 'class ' + object.name + ':\n' + content

class G_Content(G_Base):
    def __init__(self):
        super().__init__()
    def generate(self, object):
        if base.Structure.isSetValue(object) and base.Structure.isSameType(object):
            condition = self.g_operator.generate(object.condition)
            content = 'pass'
            return 'if ' + condition + ':\n' + content



