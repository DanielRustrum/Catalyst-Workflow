from . import cli

def help(args, io):
    with io("out") as out:
        out.line("Hello!")

cli.addCommand("help", callback=help)
cli.executeCommand()
