import sys
try:
    import textx
    import termcolor
    from bund_shell import BUND_SHELL
except ImportError, msg:
    print "Early stage Run-Time error:",msg
    sys.exit(1)

def main():
    shell = BUND_SHELL()
    shell.process()

main()
