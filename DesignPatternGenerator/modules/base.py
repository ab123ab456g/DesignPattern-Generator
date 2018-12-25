class Base(object):
    def __init__(self):
        self.name = ''
    def isSetVaule(obj):
        pass
    def isSameType(obj):
        pass

class Variable(Base):
    def __init__(self):
        super().__init__()
        self.datatype = ''
        self.value = ''
        self.operator = ''
    def isSetValue(obj):
        return IsSetValueFacotry.Variable(obj)
    def isSameType(variable):
        if issubclass(type(variable), Variable):
            return True
        else:
            return False

class Structure(Base):
    def __init__(self):
        super().__init__()
        self.contentlist = []
    def addContent(self, content):
        self.contentlist.append(content)
    def isSetValue(obj):
        return IsSetValueFacotry.Structure(obj)
    def isSameType(structure):
        if issubclass(type(structure), Structure):
            return True
        else:
            return False

class Operator(Base):
    def __init__(self):
        super().__init__()
        self.str1 = ''
        self.operator = ''
        self.str2 = ''
    def isSetValue(obj):
        return IsSetValueFacotry.Operator(obj)
    def isSameType(variable):
        if issubclass(type(variable), Operator):
            return True
        else:
            return False

class Loop(Base):
    def __init__(self):
        super().__init__()
        self.condition = ''
        self.contentlist = []
    def isSetValue(obj):
        return IsSetValueFacotry.Loop(obj)
    def isSameType(variable):
        if issubclass(type(variable), Loop):
            return True
        else:
            return False

class Function(Base):
    def __init__(self):
        super().__init__()
        self.parameterlist = []
        self.contentlist = []
    def isSetValue(obj):
        return IsSetValueFacotry.Function(obj)
    def isSameType(variable):
        if issubclass(type(variable), Function):
            return True
        else:
            return False

class Class(Base):
    def __init__(self):
        super().__init__()
        self.parameterlist = []
        self.methodList = []
        self.inherit_class = ''
    def isSetValue(class_):
        if class_.name != '':
            return True
        else:
            return False
    def isSameType(variable):
        if issubclass(type(variable), Class):
            return True
        else:
            return False
    def isInherit(class_):
        if class_.inherit_class != '':
            return True
        else:
            return False

class DesignPattern(Base):
    def __init__(self):
        super().__init__()
        self.type = ''
        self.classlist = []
    def addClassList(self, class_):
        self.classlist.append(class_)

class BaseMethod(object):
    def isSetVaule(obj):
        pass
    def isSameType(obj):
        pass

class VariableIsSetValue(BaseMethod):
    def isSetValue(obj):
        if obj.name != '' and obj.value != '' and obj.operator != '':
            return True
        else:
            return False

class StructureIsSetValue(BaseMethod):
    def isSetValue(obj):
        if obj.name != '' and obj.condition != '' :
            return True
        else:
            return False

class OperatorIsSetValue(BaseMethod):
    def isSetValue(obj):
        if obj.str1 != '' and obj.str2 != '' and obj.operator != '':
            return True
        else:
            return False

class LoopIsSetValue(BaseMethod):
    def isSetValue(obj):
        if obj.name != '':
            return True
        else:
            return False

class FunctionIsSetValue(BaseMethod):
    def isSetValue(obj):
        if obj.name != '':
            return True
        else:
            return False

class ClassIsSetValue(BaseMethod):
    def isSetValue(obj):
        if obj.name != '':
            return True
        else:
            return False

class DesignPatternIsSetValue(BaseMethod):
    def isSetValue(obj):
        if obj.name != '' and obj.type != '' and len(obj.classlist) != 0:
            return True
        else:
            return False

class IsSetValueFacotry(BaseMethod):
    def Variable(obj):
        return VariableIsSetValue.isSetValue(obj)
    def Structure(obj):
        return StructureIsSetValue.isSetValue(obj)
    def Operator(obj):
        return OperatorIsSetValue.isSetValue(obj)
    def Loop(obj):
        return LoopIsSetValue.isSetValue(obj)
    def Function(obj):
        return FunctionIsSetValue.isSetValue(obj)
    def Class(obj):
        return ClassIsSetValue.isSetValue(obj)
    def DesignPattern(obj):
        return DesignPatternIsSetValue.isSetVaule(obj)
