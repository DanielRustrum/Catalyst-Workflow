import cli

@cli.action("test", ["Test Arg 1 (Optional)"], {
    "Test": "Test Flag (Optional)"
})
def func1():
    '''A Test Function Don't Touch'''

cli.formatCommand()
cli.setupLogging()
cli.executeAction()
