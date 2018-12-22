import variable

class Generator_Parameter(object):
    def __init__(self):
        self.space = '    '
        self.generatorList = []
        self.filename = 'demo.py'

class  IGenerator(Generator_Parameter):
    """docstring for  IGenerator"""
    def generator(self):
        pass
    def add(self, obj):
        pass

class Generator(IGenerator):
    def __init__(self):
        super(IGenerator,self).__init__()
    def generator(self, tab=False):
        with open(self.filename, 'w') as F:
            for g in self.generatorList:
                if tab:
                    F.writelines(self.space + g.generate() + '\n')
                else:
                    F.writelines(g.generate() + '\n')
    def add(self, *obj):
        for o in obj:
            self.generatorList.append(o)
    def addList(self, variableList):
        for name,value in variableList:
            A = variable.G_Int()
            A.name = name
            A.value = value
            self.add(A)
    def print(self, tab=False):
        for g in self.generatorList:
            if tab:
                print(self.space + g.generate())
            else:
                print(g.generate())

class VariablesGenerator(Generator):
    def __init__(self):
        super(Generator,self).__init__()
        self.variable = False


#print('test Generator')
# variableList = [('a',1),('b',2),('c',3),('d',4)]
# A = variable.G_Int()

# g = Generator()
# g.filename = 'demo.py'
# g.addList(variableList)
# g.print()
# g.generator()

#print('test VariablesGenerator')
# variableList = [('a',1),('b',2),('c',3),('d',4)]
# A = variable.G_Int()

# g = VariablesGenerator()
# g.filename = 'demo.py'
# g.addList(variableList)
# g.print()
# g.generator()