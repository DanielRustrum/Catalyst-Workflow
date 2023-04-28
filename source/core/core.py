import subprocess

def runPSCommand(cmd):
    command_process = subprocess.run(["powershell","-Command",cmd], capture_output=True)
    
    has_err = command_process.returncode != 0
    error_info = None
    if has_err:
        error_info = command_process.stderr

    out = command_process.stdout.decode('utf-8')

    return (out, has_err, error_info, command_process)


