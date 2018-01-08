from bund_version import BUND_VERSION
from bund_terminal import BUND_TERMINAL
from bund_cmd import BUND_GEN, BUND_HELP
from bund_env import BUND_ENV
from bund_args import BUND_ARGS

class BUND_SHELL(BUND_TERMINAL, BUND_GEN, BUND_HELP, BUND_ENV, BUND_ARGS):
    def __init__(self):
        self.doc = []
        BUND_HELP.__init__(self)
        BUND_ENV.__init__(self)
        BUND_GEN.__init__(self,  "(bund) ver %s" % BUND_VERSION, "bund - BUND Shell")
        BUND_ARGS.__init__(self)
        BUND_TERMINAL.__init__(self)
    def main_preflight(self):
        self._main_preflight()
