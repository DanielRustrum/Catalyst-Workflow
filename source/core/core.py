import subprocess

def runCommand(cmd, command_type="powershell", detached=False):
    if(command_type == "powershell"):
        command_process = subprocess.Popen([
            "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
            "-Command",
            cmd
        ])
        
        Fif not detached:
            std_out, std_err = command_process.communicate()

        has_err = command_process.returncode != 0
        error_info = None
        if has_err:
            error_info = command_process.stderr

        out = command_process.stdout.decode('utf-8')

        return {
            out: out,
            error: {
                errored: has_err,
                code: command_process.returncode,
                info: error_info
            },
            process: command_process
        }

def requireArgs(
        args, 
        flags=[], 
        listed_length=0, 
        flag_error=lambda x:f"{x} is Required", 
        arg_error=""):
    errored = False
    formatted_args = {}

    for flag in flags:
        try:
            formatted_args[flag] = args[1][flag]
        except KeyError:
            print(f"Key Error: {flag_error(flag)}")
            errored = True

    if len(args[0]) < listed_length:
        print(f"Argument Error: {arg_error}")
        errored = True
    formatted_args["_"] = args[0]

    return (errored, formatted_args)

def optionalArgs(
        args, 
        flags=[], 
        listed_length=0, 
        flag_default={},
        listed_default=[]):

    formatted_args = {}
    for flag in flags: 
        try:
            formatted_args[flag] = args[1][flag]
        except KeyError:
            try: 
                formatted_args[flag] = flag_default[flag]
            except KeyError: 
                formatted_args[flag] = None

    if len(args[0]) < listed_length:
        formatted_args["_"] = listed_default
    else:
        formatted_args["_"] = args[0]
    
    return (errored, formatted_args)


