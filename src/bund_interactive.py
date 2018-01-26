import readline
import atexit
import textx
from textx.exceptions import *
from bund_machine import BUND_MACHINE

class BUND_INTERACTIVE:
    def __init__(self):
        self.machine = BUND_MACHINE()
    def preflight(self):
        pass
    def SHELL(self):
        history_file="%s/.bund_history"%self.cfg['BUND_HOME']
        readline.parse_and_bind("tab: complete")
        readline.parse_and_bind("set editing-mode emacs")
        try:
            readline.read_history_file(history_file)
            readline.set_history_length(4096)
        except:
            pass
        atexit.register(readline.write_history_file, history_file)
        while True:
            try:
                line = raw_input("let Main -> ")
            except EOFError:
                break
            _src = "let Main -> %s ;;"%line
            self.ok(_src)
            try:
                _model = self.machine(_src)
            except textx.exceptions.TextXSyntaxError, msg:
                self.error("line: %d col: %d : %s"%(msg.line, msg.col, msg.message))
                continue
            self.machine.resolve(self, _model)
