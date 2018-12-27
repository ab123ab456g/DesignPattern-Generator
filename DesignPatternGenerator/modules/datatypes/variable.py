from . import basic
from .base import Variable 

class G_Int(Variable):
    def __init__(self, operator='='):
        super().__init__()
        self.datatype = basic.Keyword.datatype[0]
        self.operator = operator

class G_Str(Variable):
    def __init__(self, operator='='):
        super().__init__()
        self.datatype = basic.Keyword.datatype[1]
        self.operator = operator

class G_List(Variable):
    def __init__(self, operator='='):
        super().__init__()
        self.datatype = basic.Keyword.datatype[3]
        self.operator = operator

class G_Dict(Variable):
    def __init__(self, operator='='):
        super().__init__()
        self.datatype = basic.Keyword.datatype[4]
        self.operator = operator

class G_Set(Variable):
    def __init__(self, operator='='):
        super().__init__()
        self.datatype = basic.Keyword.datatype[5]
        self.operator = operator

class G_Tuple(Variable):
    def __init__(self, operator='='):
        super().__init__()
        self.datatype = basic.Keyword.datatype[6]



class G_Other(Variable):
    ''''doc object string'''
    def __init__(self, Obj, operator='='):
        super().__init__()
        self.datatype = basic.Keyword.datatype[7]
        self.operator = operator
        self.value = Obj

class abstrctVariableFactory(object):
    def __init__(self):
        self.operator


class VariableFactory_equal(abstrctVariableFactory):
    def __init__(self):
        self.operator = basic.Keyword.set_value_operaotr[0]
    def setInt(self):
        return G_Int(self.operator)
    def setStr(self):
        return G_Str(self.operator)
    def setList(self):
        return G_List(self.operator)
    def setDict(self):
        return G_Dict(self.operator)
    def setSet(self):
        return G_Set(self.operator)
    def setTuple(self):
        return G_Tuple(self.operator)
    def setOther(self, otherObj):
        return G_Other(otherObj, self.operator)

class VariableFactory_add_equal(abstrctVariableFactory):
    def __init__(self):
        self.operator = basic.Keyword.set_value_operaotr[1]
    def setInt(self):
        return G_Int(self.operator)
    def setStr(self):
        return G_Str(self.operator)
    def setList(self):
        return G_List(self.operator)
    def setDict(self):
        return G_Dict(self.operator)
    def setSet(self):
        return G_Set(self.operator)
    def setTuple(self):
        return G_Tuple(self.operator)
    def setOther(self, otherObj):
        return G_Other(otherObj, self.operator)

class VariableFactory_sub_equal(abstrctVariableFactory):
    def __init__(self):
        self.operator = basic.Keyword.set_value_operaotr[2]
    def setInt(self):
        return G_Int(self.operator)
    def setStr(self):
        return G_Str(self.operator)
    def setList(self):
        return G_List(self.operator)
    def setDict(self):
        return G_Dict(self.operator)
    def setSet(self):
        return G_Set(self.operator)
    def setTuple(self):
        return G_Tuple(self.operator)
    def setOther(self, otherObj):
        return G_Other(otherObj, self.operator)


class VariableFactory_multi_equal(abstrctVariableFactory):
    def __init__(self):
        self.operator = basic.Keyword.set_value_operaotr[3]
    def setInt(self):
        return G_Int(self.operator)
    def setStr(self):
        return G_Str(self.operator)
    def setList(self):
        return G_List(self.operator)
    def setDict(self):
        return G_Dict(self.operator)
    def setSet(self):
        return G_Set(self.operator)
    def setTuple(self):
        return G_Tuple(self.operator)
    def setOther(self, otherObj):
        return G_Other(otherObj, self.operator)

class VariableFactory_divi_equal(abstrctVariableFactory):
    def __init__(self):
        self.operator = basic.Keyword.set_value_operaotr[4]
    def setInt(self):
        return G_Int(self.operator)
    def setStr(self):
        return G_Str(self.operator)
    def setList(self):
        return G_List(self.operator)
    def setDict(self):
        return G_Dict(self.operator)
    def setSet(self):
        return G_Set(self.operator)
    def setTuple(self):
        return G_Tuple(self.operator)
    def setOther(self, otherObj):
        return G_Other(otherObj, self.operator)


