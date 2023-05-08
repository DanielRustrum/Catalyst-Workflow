from . import core, file
import os

#* Interface
def start(args):
    errored, req_args = core.requireArgs(args, flags=["name"])

    if errored:
        return

    core.runCommand(
        f"docker compose -f C:/'Program Files'/Catalyst/envs/{req_args['name']}/compose.yaml up --detach",
        detached=True,
        quiet=True
    )

def stop(args):
    errored, req_args = core.requireArgs(args, flags=["name"])

    if errored:
        return

    core.runCommand(
        f"docker compose -f C:/'Program Files'/Catalyst/envs/{req_args['name']}/compose.yaml down",
        quiet=True
    )

def focus(args):
    errored, req_args = core.requireArgs(args, flags=["name"])

    if errored:
        return
    
    core.runCommand(f"docker exec -it {req_args['name']} bash")

def create(args):
    errored, req_args = core.requireArgs(args, flags=["name"])
    opt_args = core.optionalArgs(args, flags=[
        "buildFile", 
        "composeFile", 
        "linkRepo",
        "isolated"
    ])

    if errored:
        return


    if not os.path.isdir(f"C:/Program Files/Catalyst/envs/{req_args['name']}"):
        os.mkdir(f"C:/Program Files/Catalyst/envs/{req_args['name']}")

    if errored:
        return

    with open(f"C:/Program Files/Catalyst/envs/{req_args['name']}/compose.yaml", "w+") as yaml_file:
        yaml_file.write(f"""version: "3.9"
services:
    devenv:
        image: "ubuntu:latest"
        container_name: "{req_args['name']}"
        ports:
            - "80:80"
            - "443:443"
        stdin_open: true
        tty: true
        volumes:
            - devenv:/root/{req_args['name']}
volumes:
    devenv:
""")
    

def delete(args):
    errored, req_args = core.requireArgs(args, flags=["name"])

    if errored:
        return

    for root, dirs, files in os.walk(f"C:/Program Files/Catalyst/envs/{req_args['name']}"):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

    os.rmdir(f"C:/Program Files/Catalyst/envs/{req_args['name']}")

def file(args):
    errored, req_args = core.requiredArgs(args, listed_length=3, flags=["name"])

    direction = req_args["_"][0]
    src_path = req_args["_"][1]
    dest_path = req_args["_"][2]

    if errored:
        return

    if direction == "to":
        core.runCommand(f"docker cp {src} {req_args['name']}:{dest}")
    if direction == "from":
        core.runCommand(f"docker cp {req_args['name']}:{src} {dest}")

command = {
    "start": start,
    "stop": stop,
    "focus": focus,
    "create": create,
    "delete": delete,
    "file": file
}
