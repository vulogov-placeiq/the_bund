from textx.metamodel import metamodel_from_str
from bund_grammar import BUND_GRAMMAR

class BUND_MACHINE(object):
    def __init__(self):
        self.mm = metamodel_from_str(BUND_GRAMMAR)
    def __call__(self, _src):
        return self.mm.model_from_str(_src)
    def run(self, _shell, name, _statement):
        res = []
        if type(_statement) == type([]):
            for s in _statement:
                res.append(self.run(_shell, name, s))
        else:
            print _statement.__class__.__name__
            print dir(_statement)
    def resolve(self, _shell, _model):
        res = []
        for f in _model.functors:
            res.append(self.run(_shell, f.name, f.statements))
