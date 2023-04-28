from . import core

def startContainer(args):
    out = core.runPSCommand(f"Write-Output \"{args}\"")[0]
    print(out)

def stopContainer(args):
    pass

def createContainer():
    pass
