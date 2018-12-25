from . import base
from . import variable 

class GeneratorVariable(base.Base_Generator):
    def __init__(self):
        super().__init__()
    def generate(self, object):
        if variable.Variable.isSetValue(object):
            if object.datatype == 'str' or object.datatype == '' or object.datatype == None:
                return object.name + ' = ' + '\'' + str(object.value) + '\''
            elif object.datatype == 'set':
                if type(object.value)  == str:
                    return object.name + ' = '  + str(set(object.value))
                else:
                    return object.name + ' = '  + str(set(object.value)) 
            else:
                return object.name + ' = '  + str(object.value)