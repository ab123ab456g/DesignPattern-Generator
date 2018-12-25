from . import variable
from . import generator_variable
import xml.etree.ElementTree as ET


class Base(object):
    pass

class VariableBuilder(Base):
    def __init__(self):
        self.facotry = variable.VariableFactory_equal()
        self.variable = None
        self.generator = generator_variable.GeneratorVariable()

    def changeFacotry(self,facotry):
        self.facotry = facotry

    def setVariable(self, obj):
        self.variable = obj

    def generate(self):
        print(self.generator.generate(self.variable))
        return self.generator.generate(self.variable)

    def Save(self):
        with open('test.py','w') as f :
            f.writelines(self.generate() + '\n' )

    def Load(self):
        tree = ET.parse('DesignPatternGenerator/test/variable.xml')
        root = tree.getroot()
        print(root.tag, root.attrib)
        element = root
        if element.tag == 'variable':
            self.setVariable(self.facotry.setInt())
            self.variable.name = element.attrib['name']
            self.variable.datatype = element.attrib['datatype']
            self.variable.operator = element.attrib['operation']
            self.variable.value = element.text

class CodeBuilder(Base):
    pass