import variable
import strcture

class Function_Paramter(variable.Base):
    def __init__(self):
        super(Base,self).__init__()
        self.content = 'pass'
        self.parameter = False
        self.paramterList = []
        self.variable = False
        self.variableList = []
        self._if = False
        self._elif = False
        self._elifList = []
        self._else = False
        self.callmethod = False
        self.callmethodList = []
        self.callmodule = False
        self.callmoduleList = []
        self._return = False
        self._print = False

        #variable
        #if elif else #condition
        #call method
        #call module
        #return
        #print


class IFunction(Function_Paramter):
    def generate(self):
        pass

class Function(IFunction):
    def __init__(self):
            super().__init__()
    def generate(self):
        function_str = 'def ' + self.name + '('+ \
        ', '.join(self.variable) +\
        '):\n' + self.space + \
        self.content
        return  function_str

F =Function()
F.name = 'abc'
F.variable = ['a','b','c']
print(F.generate())
