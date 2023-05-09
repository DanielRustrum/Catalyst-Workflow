import subprocess

def _help(args):
    with open("./help.txt", 'r') as help_file:
        print(help_file.read())

def runCommand(cmd, command_type="powershell", detached=False, quiet=False):
    if(command_type == "powershell"):
        if quiet:
            command_process = subprocess.Popen([
                "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
                "-Command",
                cmd
            ], stdout=subprocess.DEVNULL)
        else:
            command_process = subprocess.Popen([
                "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
                "-Command",
                cmd
            ])
        
        if not detached:
            std_out, std_err = command_process.communicate()

        if quiet:
            return {}

        has_err = command_process.returncode != 0
        error_info = None
        if has_err:
            error_info = command_process.stderr
        
        out = command_process.stdout

        return {
            "out": out,
            "error": {
                "errored": has_err,
                "code": command_process.returncode,
                "info": error_info
            },
            "process": command_process
        }

