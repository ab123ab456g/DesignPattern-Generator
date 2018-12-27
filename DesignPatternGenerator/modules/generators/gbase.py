from ..datatypes import base
from ..datatypes import variable 
from ..datatypes import Operator
from ..datatypes import structure

class G_Base(object):
    def generate(self, object):
        pass

class G_Variable(G_Base):
    def __init__(self):
        super().__init__()
    def generate(self, object):
        if base.Variable().isSameType(object):
            if base.Variable().isSetValue(object):
                if object.datatype == 'str' or object.datatype == '' or object.datatype == None:
                    return object.name + ' = ' + '\'' + str(object.value) + '\''
                elif object.datatype == 'set':
                    if type(object.value)  == str:
                        return object.name + ' = '  + str(set(object.value))
                    else:
                        return object.name + ' = '  + str(set(object.value)) 
                else:
                    return object.name + ' = '  + str(object.value)

class G_Structure(G_Base):
    def __init__(self):
        super().__init__()
    def generate(self, object):
        if base.Structure().isSameType(object):
            if base.Structure().isSetValue(object):
                condition = G_Operator().generate(object.condition)
                string = G_Content().generate(object.content)
                return 'if ' + condition + ':\n' + string
            # else:
            #     condition = G_Operator().generate(object.condition)
            #     return 'if ' + condition + ':\n' + self.space + 'pass\n'

class G_Operator(G_Base):
    def __init__(self):
        super().__init__()
    def generate(self, object):
        if base.Operator().isSameType(object):
            if base.Operator().isSetValue(object):
                return object.str1 + ' ' + object.operator + ' ' + object.str2

class G_Content(G_Base):
    def __init__(self):
        super().__init__()
        self.space = '    '
        self.AllowedDatatypeGenerators = {
            base.Variable:G_Variable,
            base.Structure:G_Structure,
            # base.Loop:G_Loop,
            base.Function:G_Function,
            base.Class:G_Class,
            base.Call:G_Call
        }
    def generate(self, object):
        if base.Content().isSameType(object):
            if base.Content().isSetValue(object):
                return self.creaetContent(object)
        return self.space + 'pass' + '\n'

    def creaetContent(self, object):
        stringlist = []
        string = ''
        for datatype,obj in object.contentlist:
            G = G_Content().AllowedDatatypeGenerators[datatype]()
            result = G.generate(obj)
            if self.checkNeedToSplitNewline(datatype, result):
                split_result = self.split_newline(result)
                for i in split_result: 
                    stringlist.append(self.space + i)
            else:
                stringlist.append(self.space + result)

        string = self.listToString(stringlist)
        return string

    def checkNeedToSplitNewline(self, datatype ,result):
        if datatype == base.Structure or datatype == base.Function or datatype == base.Class:
            return True
        else:
            return False

    def split_newline(self, result):
        split_result = result.split('\n')
        split_result = split_result[:-1]
        return split_result
    def listToString(self,stringlist):
        string = ''
        for i in stringlist:
            string += i + '\n'
        return string

class G_Call(G_Base):
    def __init__(self):
        super().__init__()
    def generate(self, object):
        string = ''
        stringlist = []
        if base.Call().isSameType(object):
            for parameter in object.parameterlist:
                string += parameter + ', '
            string = object.name + '(' + string[:-2] + ')'
            return string

class G_Loop(G_Base):
    pass

class G_Function(G_Base):
    def __init__(self):
        super().__init__()
    def generate(self, object):
        if base.Function().isSameType(object):
            if base.Function().isSetValue(object):
                string = ''
                for parameter in object.parameterlist:
                    string += parameter + ', '
                content = G_Content().generate(object.content)
                string =  'def ' + object.name + '(' + string[:-2] + '):\n' + content
                return string

class G_Class(G_Base):
    def __init__(self):
        super().__init__()
    def generate(self, object):
        content = 'pass'
        if base.Class().isSameType(object):
            if base.Class().isSetValue(object):
                if len(object.variablelist) > 0:
                    F = self.createVarabile(object.variablelist)
                    object.content.addContent(base.Function, F)
                if len(object.methodlist) > 0:
                    for F in object.methodlist:
                        object.content.addContent(base.Function, F)
                string = G_Content().generate(object.content)
                if base.Class().isInherit(object):
                    return 'class ' + object.name + '(' + object.inherit_class + '):\n' + string
                else:
                    return 'class ' + object.name + ':\n' + string
    def createVarabile(self, variablelist):
        F = base.Function()
        F.addParameter('self')
        F.name = '__init__'
        for variable in variablelist:
            variable.name = 'self.' + variable.name
            F.content.addContent(base.Variable ,variable)
        return F


