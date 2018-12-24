class Language(object):
    def __init__(self):
        self.langlist = ['Python']
        self.uselang = ''
        self.setUseLang('Python')
    def changeStringFormat(self,lang):
        return lang[0].upper() + lang[1:]
    def checkIsSupport(self, lang):
        lang = self.changeStringFormat(lang)
        if lang in self.langlist:
            return True
        return False
    def setUseLang(self, lang):
        lang = self.changeStringFormat(lang)
        if self.checkIsSupport(lang):
            self.uselang = lang
        else:
            self.uselang = lang +' Not Support'

class Keyword(object):
    datatype = ['int', 'str', 'None', 'list', 'dict', 'set', 'tuple', 'other']
    #operator = [ , ]
    set_value_operaotr = ['=', '+=', '-=', '*=', '/=']
    compute_operator = ['+', '-', '*',  '/' , '%','//', '**']
    compare_operaotor = ['==', '!=', '>', '>=', '<', '<=']
    logic_operator = ['and', 'or', 'not', 'is', 'is not','in']
    bitwise_operator = ['&', '|', '~', '^']

    structure = ['if', 'elif', 'else']
    function = ['def']
    class_ = ['class']
    design_pattern = []


# assertTrue(expr, msg=None)
# assertFalse(expr, msg=None)
# assertEqual(first, second, msg=None)
# assertNotEqual(first, second, msg=None}})