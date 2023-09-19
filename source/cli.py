
import sys

commands = {}
current_command_data = {
    "in-file": None,
    "out-file": None,
    "logging": False,
    "command-name": None
}

def addCommand(
    reference,
    callback = lambda args, io: None,
    flags = {},
):
    '''Adds possible command to map'''
    commands[reference] = (
        callback,
        flags,
    )


class IOWrapper:
    class IOAction:
        def __init__(self, file = None, action_type="in"):
            self.file = file

        def __iter__(self):
            return self

        def next(self):
            if self.file is None:
                raise StopIteration
            
            line = self.file.readline()
            
            if line in ["Exit", "", None]:
                raise StopIteration
            else:
                return line

        def line(self, *data):
            match action_type:
                case "in":
                    if self.file is None:
                        return ""
                    return self.file.readline()
                case "out":
                    message = data[0:1]
                    if self.file is None:
                        return
                    self.file.write(f"{message}\n")
                case "log":
                    log_level, message = data[0:1]
                    self.file.write(f"{log_level}: {message}\n")
                case _:
                    pass

    def __init__(self, use="in"):
        self.use = use

    def __enter__(self):
        return IOWrapper.IOAction(
            action_type=self.use
        )

    def __exit__(self):
        pass

def executeCommand():
    ''' Reads in STDIN or File and writes out to a file or STDOUT.
    If there is an error, write out to STDERR.
    If a log file is specified then it logs to the specified file.
    '''
    #TODO: Find Command
    command = "help"

    #TODO: Get Command Data
    callback, expected_flags = commands[command]
    
    try:
        callback(args, IOWrapper)
    except error:
        sys.stderr.write(f"An Unexpected Error Has Occured while running {command}.\n\n{error}\n")
