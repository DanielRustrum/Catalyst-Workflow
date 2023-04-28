import sys, types
from core import docker


#* // Command Functions //

def _help(args):
    with open("./help.txt", 'r') as help_file:
        print(help_file.read())

#* // Core Functions //
def formatArgs(arg_list):
    args = []
    flags = {}

    for arg in arg_list:
        if arg.startswith("--"):
            split_flag = "".join(arg[2:]).split("=")

            if len(split_flag) > 1:
                if "," in split_flag[1]:
                    flags[split_flag[0]] = split_flag[1].split(",")
                else:
                    flags[split_flag[0]] = split_flag[1]
            else:
                flags[split_flag[0]] = None
            
            continue

        args.append(arg)

    
    return (args, flags)

def getCommand():
    error = False
    command_arg = sys.argv[1]

    command_action = {
            "help": _help, 
        "container": {
            "start": docker.startContainer
        } 
    }

    try:
        if isinstance(command_action[command_arg], types.FunctionType):
            return (command_action[command_arg], formatArgs(sys.argv[2:]), error)
        else:
            subcommand_arg = sys.argv[2]
            return (command_action[command_arg][subcommand_arg], formatArgs(sys.argv[3:]), error)
    except Exception as e:
        print("Error: Command Doesn't Exist")
        error = True

    return (lambda x: None, ([], {}), error)

def main():
    command, args, _ = getCommand()
    command(args)

if __name__ == '__main__':
    main()
