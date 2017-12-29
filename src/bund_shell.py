from bund_version import BUND_VERSION
from bund_terminal import BUND_TERMINAL
from bund_cmd import BUND_GEN, BUND_HELP
from bund_env import BUND_ENV

class BUND_SHELL(BUND_TERMINAL, BUND_GEN, BUND_HELP, BUND_ENV):
    def __init__(self):
        BUND_HELP.__init__(self)
        BUND_ENV.__init__(self)
        BUND_GEN.__init__(self,  "(bund) ver %s" % BUND_VERSION, "bund - BUND Shell")
        BUND_TERMINAL.__init__(self)
