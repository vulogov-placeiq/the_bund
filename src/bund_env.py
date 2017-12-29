import UserDict
from Queue import LifoQueue
from bund_env_modcache import MODCACHE
from bund_lib import *

class CFG(UserDict.UserDict):
    def __init__(self, d={}, **kw):
        UserDict.UserDict.__init__(self)
        if len(d.keys()) > 0:
            _d = d
        else:
            _d = kw
        for k in _d.keys():
            self[k.upper()] = get_from_env(k.upper(), kw=_d)
    def add_missing(self, name, params, default):
        self[name.upper()] = get_from_env(name.upper(), kw=params, default=default)




class BUND_ENV(UserDict.UserDict, MODCACHE):
    def __init__(self, _shell=None, **kw):
        UserDict.UserDict.__init__(self)
        MODCACHE.__init__(self)
        self.ready = False
        self.shell = _shell
        self.params = kw
        self.Globals = {}
        self.Queries = {}
        self.RefBase = "+."
        self.envs = None
        self.srv = {}
        self.ready = self.reload()
    def registerGlobals(self, name, _ref):
        self.Globals[name] = _ref
    def reload(self):
        self.cfg = CFG(self.params)
        self.set_defaults()
        return True
    def set_defaults(self):
        self.cfg["BUND_HOME"] = "/tmp"
        self.cfg["BUND_REF_BASE"] = self.RefBase
        self.cfg["BUND_ENV_NAME"] = "default"
        self.cfg["BUND_MAX_PIPELINE"] = 100
        self.cfg["BUND_MAX_ENV_STACK"] = 100
        self.cfg["BUND_VERBOSE"] = 0
        self.cfg["BUND_UNSAFE_GLOBALS"] = False
        self.envs = LifoQueue(self.cfg["BUND_MAX_ENV_STACK"])


class ENV_CTL(UserDict.UserDict):
    def __init__(self):
        UserDict.UserDict.__init__(self)
        self.current = None
    def set_current(self, name):
        if name in self.keys():
            self.current = name
        return self[name]
    def __setitem__(self, key, val):
        self.current = key
        return UserDict.UserDict.__setitem__(self, key, val)
    def __delitem__(self, key):
        UserDict.UserDict.__delitem__(self, key)
        if self.current == key:
            self.current = None

ENV = ENV_CTL()

def ENVIRONMENT(name, _env=None):
    global ENV
    if ENV.has_key(name):
        return ENV[name]
    elif ENV.has_key("default"):
        ENV["default"] = _env
    elif _env != None:
        ENV[name] = _env
    else:
        ENV[name] = ZQ_ENV()
    return ENV[name]
