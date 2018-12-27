class Base(object):
    def __init__(self):
        self.name = ''
    def isSetValue(self, obj):
        if obj.name != '':
            return True
        else:
            return False
    def isSameType(self, obj):
        if issubclass(type(obj), Base):
            return True
        else:
            return False

class Variable(Base):
    def __init__(self):
        super().__init__()
        self.datatype = ''
        self.value = ''
        self.operator = ''
    def isSetValue(self, obj):
        if obj.name != '' and obj.value != '' and obj.operator != '':
            return True
        else:
            return False
    def isSameType(self, obj):
        if issubclass(type(obj), Variable):
            return True
        else:
            return False

class Structure(Base):
    def __init__(self):
        super().__init__()
        self.content = Content()
    def isSameType(self, obj):
        if issubclass(type(obj), Structure):
            return True
        else:
            return False
    def addContent(self, datatype, obj):
            c = Content()
            return c.addContent(datatype, obj)

class Operator(Base):
    def __init__(self):
        super().__init__()
        del self.name
        self.str1 = ''
        self.operator = ''
        self.str2 = ''
    def isSetValue(self, obj):
        if obj.str1 != '' and obj.str2 != '' and obj.operator != '':
            return True
        else:
            return False
    def isSameType(self, obj):
        if issubclass(type(obj), Operator):
            return True
        else:
            return False

class Content(Base):
    def __init__(self):
        super().__init__()
        self.AllowedDatatype = {
            Variable:Variable,
            Structure:Structure,
            Loop:Loop,
            Function:Function,
            Class:Class,
            Call:Call
        }
        del self.name
        self.contentlist = []
    def isSetValue(self, obj):
        if len(obj.contentlist )> 0:
            return True
        else:
            return False
    def isSameType(self, obj):
        if issubclass(type(obj), Content):
            return True
        else:
            return False
    def addContent(self, datatype, obj):
        if self.checkAddAllowedConententType(datatype, obj):
                if datatype().isSetValue(obj) and datatype().isSameType(obj):
                    self.contentlist.append((datatype,obj))
                    return True
        return False
    def checkAddAllowedConententType(self, datatype, obj):
        if datatype in self.AllowedDatatype:
            if issubclass(type(obj), self.AllowedDatatype[datatype]):
                return True
        return False

class Call(Base):
    def __init__(self):
        super().__init__()
        self.parameterlist = []
    def isSameType(self, obj):
        if issubclass(type(obj), Call):
            return True
        else:
            return False
    def addParameter(self, parameter):
        self.parameterlist.append(parameter)

class Loop(Base):
    def __init__(self):
        super().__init__()
        self.condition = ''
        self.contentlist = []
    def isSetValue(self, obj):
        if obj.condition != '':
            return True
        else:
            return False
    def isSameType(self, obj):
        if issubclass(type(obj), Loop):
            return True
        else:
            return False
    def addContent(self, datatype, obj):
            c = Content()
            return c.addContent(datatype, obj)

class Function(Base):
    def __init__(self):
        super().__init__()
        self.parameterlist = []
        self.content = Content()
    def isSetValue(self, obj):
        if obj.name != '':
            return True
        else:
            return False
    def isSameType(self, obj):
        if issubclass(type(obj), Function):
            return True
        else:
            return False
    def addParameter(self, parameter):
        self.parameterlist.append(parameter)

class Class(Base):
    def __init__(self):
        super().__init__()
        self.variablelist = []
        self.methodlist = []
        self.content = Content()
        self.inherit_class = ''
    def isSameType(self, obj):
        if issubclass(type(obj), Class):
            return True
        else:
            return False
    def isInherit(self, obj):
        if obj.inherit_class != '':
            return True
        else:
            return False
    def addVariable(self, variable):
        if Variable().isSameType(variable):
            if Variable().isSetValue(variable):
                self.variablelist.append(variable)
                return True
        return False
    def addMethod(self, method):
        if Function().isSameType(method):
            if Function().isSetValue(method):
                self.methodlist.append(method)
                return True
        return False

class DesignPattern(Base):
    def __init__(self):
        super().__init__()
        self.type = ''
        self.classlist = []
    def isSetValue(self, obj):
        if obj.name != '' and obj.type != '' and len(obj.classlist) != 0:
            return True
        else:
            return False
    def isSameType(self, obj):
        if issubclass(type(obj), DesignPattern):
            return True
        else:
            return False
    def addClass(self, class_):
        if Class().isSameType(class_):
            self.classlist.append(class_)
            return True
        return False

