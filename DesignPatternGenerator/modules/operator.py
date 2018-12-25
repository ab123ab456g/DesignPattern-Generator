from . import base
from . import basic

class Operator(base.Base):
    def __init__(self):
        super(base.Base, self).__init__()
        self.str1 = ''
        self.operator = ''
        self.str2 = ''
    def isSetValue(Operator):
        if Operator.str1 != '' and Operator.str2 != '' and Operator.operator != '':
            return True
        else:
            return False
    def isSameType(variable):
        if issubclass(type(variable), Operator):
            return True
        else:
            return False

class Add(Operator):
    def __init__(self):
        super().__init__()
        self.operator = basic.Keyword.compute_operator[0]

class Sub(Operator):
    def __init__(self):
        super().__init__()
        self.operator = basic.Keyword.compute_operator[1]

class Multi(Operator):
    def __init__(self):
        super().__init__()
        self.operator = basic.Keyword.compute_operator[2]

class Divi(Operator):
    def __init__(self):
        super().__init__()
        self.operator = basic.Keyword.compute_operator[3]

class Remainder(Operator):
    def __init__(self):
        super().__init__()
        self.operator = basic.Keyword.compute_operator[4]

class DiviOnlyInteger(Operator):
    def __init__(self):
        super().__init__()
        self.operator = basic.Keyword.compute_operator[5]

class Power(Operator):
    def __init__(self):
        super().__init__()
        self.operator = basic.Keyword.compute_operator[6]

class And(Operator):
    def __init__(self):
        super().__init__()
        self.operator = basic.Keyword.logic_operator[0]

class Or(Operator):
    def __init__(self):
        super().__init__()
        self.operator = basic.Keyword.logic_operator[1]

class Not(Operator):
    def __init__(self):
        super().__init__()
        self.operator = basic.Keyword.logic_operator[2]

class Is(Operator):
    def __init__(self):
        super().__init__()
        self.operator = basic.Keyword.logic_operator[3]

class Is_Not(Operator):
    def __init__(self):
        super().__init__()
        self.operator = basic.Keyword.logic_operator[4]

class In(Operator):
    def __init__(self):
        super().__init__()
        self.operator = basic.Keyword.logic_operator[5]

class Eq(Operator):
    def __init__(self):
        super().__init__()
        self.operator = basic.Keyword.compare_operaotor[0]

class NEq(Operator):
    def __init__(self):
        super().__init__()
        self.operator = basic.Keyword.compare_operaotor[1]

class Bg(Operator):
    def __init__(self):
        super().__init__()
        self.operator = basic.Keyword.compare_operaotor[2]

class BEq(Operator):
    def __init__(self):
        super().__init__()
        self.operator = basic.Keyword.compare_operaotor[3]

class Lt(Operator):
    def __init__(self):
        super().__init__()
        self.operator = basic.Keyword.compare_operaotor[4]

class LEq(Operator):
    def __init__(self):
        super().__init__()
        self.operator = basic.Keyword.compare_operaotor[5]

class bit_And(Operator):
    def __init__(self):
        super().__init__()
        self.operator = basic.Keyword.bitwise_operator[0]

class bit_Or(Operator):
    def __init__(self):
        super().__init__()
        self.operator = basic.Keyword.bitwise_operator[1]

class bit_Not(Operator):
    def __init__(self):
        super().__init__()
        self.operator = basic.Keyword.bitwise_operator[2]

class bit_Xor(Operator):
    def __init__(self):
        super().__init__()
        self.operator = basic.Keyword.bitwise_operator[3]

class ComputeOperatorFacotry(object):
    def setAdd(self):
        return Add()
    def setSub(self):
        return Sub()
    def setMulti(self):
        return Multi()
    def setDivi(self):
        return Divi()
    def setRemainder(self):
        return Remainder()
    def setDiviOnlyInteger(self):
        return DiviOnlyInteger()
    def setPower(self):
        return Power()

class CompareOperatorFacotry(object):
    def setEq(self):
        return Eq()
    def setNEq(self):
        return NEq()
    def setBg(self):
        return Bg()
    def setBEq(self):
        return BEq()
    def setLt(self):
        return Lt()
    def setLEq(self):
        return LEq()

class BitwiseOperatorFacotry(object):
    def setAnd(self):
        return bit_And()
    def setOr(self):
        return bit_Or()
    def setNot(self):
        return bit_Not()
    def setXor(self):
        return bit_Xor()
