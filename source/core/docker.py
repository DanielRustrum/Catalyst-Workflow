from . import core, file

command = {
    "start": start,
    "create": create,
    "delete": delete,
    "update": update,
    "push": push,
    "file": file
}

def start(args):
    errored, req_arg = core.requireArgs(args, flags=["name"])

    if errored:
        return

def create(args):
    errored, req_args = core.requireArgs(args, flags=["name"])
    opt_args = core.optionalArgs(args, flags=["buildFile"])

    if errored:
        return

def delete(args):
    errored, req_arg = core.requireArgs(args, flags=["name"])

    if errored:
        return

def update(args):
    errored, req_args = core.requireArgs(args, flags=["name"])
    opt_args = core.optionalArgs(args, flags=["buildFile"])


def file(args):
    errored, req_args = core.requiredArgs(args, listed_length=3, flags=["name"])

    if errored:
        return


#* Utility

def moveFileToContainer(container, src, dest):
    core.runCommand(f"docker cp {src} {container}:{dest}")

def moveFileToHost(container, src, dest):
    core.runCommand(f"docker cp {container}:{src} {dest}")



