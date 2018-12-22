import Gclass

class Function_Paramter(object):
    def __init__(self):
        self.name = ''
        self.Variable = []
        self.content = 'pass'
        self.Variable = False
        self.Variable_num = 0
        self.function = False
        self._if = False
        self._elif = False
        self._else = False
        self.callmethod = False
        self.callmodule = False
        self._return = False
        self._print = False
        self.space = '    '
        #Gclass
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
        ', '.join(self.Gclass) +\
        '):\n' + self.space + \
        self.content
        return  function_str

F =Function()
F.name = 'abc'
F.Gclass = ['a','b','c']
print(F.generate())
