from . import core, docker
import sys, types

INDEX_START = 2
COMMAND_TREE = {
    "help": core._help, 
    "devenv": docker.command 
}


def getArgs(index_offset = 0):
    flagged = {}
    listed = []
    exec_flag = []

    pwd = sys.argv[-1]
    interaction_start = INDEX_START + index_offset

    for arg in sys.argv[interaction_start:-1]:
        if arg.startswith("--"):
            split_flag = "".join(arg[2:]).split("=")

            if len(split_flag) > 1:
                if  (
                    "," in split_flag[1] and 
                    split_flag[1].startswith("(") and
                    split_flag[2].endswith(")")
                ):
                    flagged[split_flag[0]] = "".join(split_flagged[1][1:-1]).split(",")
                else:
                    flagged[split_flag[0]] = split_flag[1]
            else:
                flagged[split_flag[0]] = None

            continue

        if arg.startswith("-"):
            split_flag = "".join(arg[1:]).split("")
            exec_flag = exec_flag + split_flag
            
            continue

        listed.append(arg)

    class ArgManager:
        def __init__(self):
            self._ordered_args_length = 0
            self._arg_map = {
                "cwd": pwd
            }
            self._errored = False
            self._optional_declared = False

        def required(self, flags=[], order=[]):
            if self._optional_declared:
                raise Error("Optional Args Declared Before Required Args")

            for flag in flags:
                try:
                    self._arg_map[flag] = flagged[flag]
                except KeyError:
                    print(f"key error: {flag} is required")
                    self._errored = True
                    return self

            if len(listed) < len(order):
                print(f"argument error: not enough listed arguments found")
                self._errored = true
                return self

            for index, arg in enumerate(order):
                self._arg_map[arg] = listed[index]

            self._ordered_args_length = len(order)
            return self


        def optional(self, flags={}, short=[], order=[]):
            _optional_declared = True

            for flag in flags.keys():
                try:
                    self._arg_map[flag] = flagged[flag]
                except KeyError:
                    self._arg_map[flag] = flags[flag]

            for short_flag in short:
                if short_flag in exec_flag:
                    self._arg_map[short_flag] = True
                else:
                    self_arg_map[short_flag] = False

            for index, arg in enumerate(order):
                self._arg_map[arg] = listed[index + self._ordered_args_length]

            return self
        
        def result(self):
            return self._arg_map, self._errored

    return ArgManager()

def getCommand():
    try:
        error = False
        command_arg = sys.argv[1]

        try:
            if isinstance(COMMAND_TREE[command_arg], types.FunctionType):
                return (COMMAND_TREE[command_arg], getArgs(), error)
            else:
                subcommand_arg = sys.argv[2]
                return (COMMAND_TREE[command_arg][subcommand_arg], getArgs(1), error)
        except Exception as e:
            print(e)
            print("Error: Command Doesn't Exist")
            error = True

        return (lambda x: None, getArgs(), error)

    except TabError:
        _help(())
        return (lambda x: None, getArgs(), error)
