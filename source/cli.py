
# =======================================
#           Command Formater
# =======================================
command = {
    'action': "",
    'args': {
        'flags': {},
        'unnamed': {}
    },
    'logging': None,
    'has-logging': False,
    'is-noisy': False,
    'noise-level': 1
}


def formatCommand():
    '''Formats the Command into a Consumable Singleton Format'''
    from sys import argv as args
    args_len = len(args)
    
    if args_len <= 1:
        command['action'] = "help"
        return

    command['action'] = args[1]

    if args_len <= 2:
        return

    def getArgKeyValue(arg):
        arg.replace("%20", " ")

        if arg.startswith("--"):
            result = arg[2:].split("=", 1)
        elif arg.startswith("-"):
            result = arg[1:].split("=", 1)
        else: 
            result = arg.split("=", 1)

        if len(result) == 1:
            return [result[0], None]
        return result

    unnamed_index = 0

    for arg in args[2:]:
        arg_key, arg_value = getArgKeyValue(arg)
        
        if not (arg.startswith("--") or arg.startswith("-")):
            unnamed_index += 1
            command["args"]['unnamed'][unnamed_index] = arg_key
            continue

        
        if arg.startswith("--log"):
            if arg_value is None:
                command["logging"] = "catalyst.log"
            else:
                command["logging"] = arg_value
            command["has-logging"] = True
            continue

        if arg.startswith("--noisy"):
            command["is-noisy"] = True
            continue

        if arg.startswith("--noise-level"):
            if arg_value is None:
                command["noise-level"] = 1
            else:
                command["noise-level"] = int(arg_value)
            command["has-logging"] = True
            continue
        
        command['args']['flags'][arg_key] = arg_value
        



# =======================================
#       Logging
# =======================================

def setupLogging():
    '''provides a logging object to use'''
    import logging, sys
    handlers = []
    if command['has-logging']:
        handlers.append(logging.FileHandler(filename=command['logging']))
    
    if command['is-noisy']:
        handlers.append(logging.StreamHandler(stream=sys.stdout))


    logging.basicConfig(
        level=logging.DEBUG,
        format=f'[%(asctime)s] ({command["action"]}) %(levelname)s - %(message)s',
        handlers=handlers
    )

def actionLogger(level = "Debug", message = ""):
    '''Log a Message to the Console with a criticality level of 1-5'''
    import logging
    
    Levels = {
        "debug": [logging.DEBUG, 1],
        "info": [logging.INFO, 2],
        "warning": [logging.WARNING, 3],
        "error": [logging.ERROR, 4],
        "critical": [logging.CRITICAL, 5]
    }

    if level.lower() not in Levels:
        raise Exception(f"Level {level} is not a valid logging level.")

    level_status, level_amount = Levels[level.lower()]

    if level_amount < command['noise-level']:
        return

    Logger = logging.getLogger(command['action'])
    
    if command['has-logging'] or command['is-noisy']:            
        Logger.log(level_status, message)



# =======================================
#           STD-IN Stream Reader
# =======================================
def readFromSTDIN():
    pass



# =======================================
#           Actions
# =======================================
actions: dict = {}

def executeAction():
    '''Executes a given Action'''
    if command["action"] not in actions:
        print("Error: Subcommand not available.")
        actions['help']['callback'](actionLogger, command["args"])
        return
    
    import inspect
    callback_args = inspect.getfullargspec(
        actions[command['action']]["callback"]
    )[0]
    arg_length = len(callback_args)

    if arg_length == 0:
        actions[command["action"]]["callback"]()
        return

    if arg_length == 1:
        actions[command["action"]]["callback"](actionLogger)
        return

    actions[command["action"]]["callback"](actionLogger, command["args"])

def action(action_name: str, expected_args=[], expected_flags={}):
    '''Declarator for declaring that the function is a CLI Action'''
    def decorator(func):
        actions[action_name] = {}
        actions[action_name]["expected"] = {}
        actions[action_name]["expected"]["args"] = expected_args
        actions[action_name]["expected"]["flags"] = expected_flags
        actions[action_name]["callback"] = func
    return decorator



# =======================================
#           Help Command
# =======================================
description = """A Config Manager that allows you to change config on the fly
while still allowing you to Personalize."""

@action("help", ["Provides Specific Information about a Specified Sub Command"])
def help(log, args):
    '''Provides a list of subcommands along side what they do and how to use them.'''
    print("\n====== Catalyst Help ======")
    if len(args["unnamed"]) > 0:
        action_name = args["unnamed"][1]
        
        if action_name not in actions:
            print("Subcommand not Available.")
            return

        action = actions[action_name]

        desc =  action["callback"].__doc__ \
            if action["callback"].__doc__ is not None\
            else "Undocumented Subcommand."

        print(f'\n{action_name}:\n    {desc}')
        
        if len(action["expected"]["args"]) != 0:
            print("\n    Arguments:")
            for arg_position, arg_desc in enumerate(action["expected"]["args"]):
                print(f"      - {arg_position + 1}: {arg_desc}")


        if len(action["expected"]["flags"]) != 0:
            print("\n    Flags:")
            for flag_name, flag_desc in action["expected"]["flags"].items():
                print(f"      - {flag_name}: {flag_desc}")
    else:
        print(description, "\n")
        for action_name, action in actions.items():
            desc =  action["callback"].__doc__ \
                if action["callback"].__doc__ is not None\
                else "Undocumented Subcommand."\

            print(f'{action_name}: {desc}')

    print("\n")
