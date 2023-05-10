from . import data, core
import os

#* Interface
def start(args):
    arg_map, errored = args.required(flags=["name"]).result()

    if errored:
        return

    core.runCommand(
        f"docker compose -f C:/'Program Files'/Catalyst/envs/{arg_map['name']}/compose.yaml up --detach",
        detached=True,
        quiet=True
    )

def stop(args):
    arg_map, errored = args.required(flags=["name"]).result()

    if errored:
        return

    core.runCommand(
        f"docker compose -f C:/'Program Files'/Catalyst/envs/{arg_map['name']}/compose.yaml down",
        quiet=True
    )

def focus(args):
    arg_map, errored = args.required(flags=["name"]).result()

    if errored:
        return
    
    core.runCommand(f"docker exec -it {arg_map['name']} bash")

def create(args):
    arg_map, errored = args\
            .required(flags=["name"])\
            .optional(flags={
                "config": None
            })\
            .result()

    if errored:
        return

    data.Directory.create(f"C:/Program Files/Catalyst/envs/{arg_map['name']}")

    yaml = data.DictToYAML({
        "version": "3.9",
        "services": {
            "devenv": {
                "image": "ubuntu:latest",
                "container_name": arg_map["name"],
                "ports": [
                    "80:80",
                    "443: 443"
                ],
                "stdin_open": data.Literal("true"),
                "volumes": [
                    data.Literal(f"devenv:/root/{arg_map['name']}")
                ]
            }
        },
        "volumes": {
            "devenv": {}
        }
    })

    data.Files.write(f"C:/Program Files/Catalyst/envs/{arg_map['name']}/compose.yaml", yaml.result)
        
    

def delete(args):
    arg_map, errored = args.required(flags=["name"]).result()

    if errored:
        return

    data.Directory.delete(f"C:/Program Files/Catalyst/envs/{arg_map['name']}")

def file(args):
    arg_map, errored = args.required(flags=["name"], order=["direction", "src", "dest"]).result()

    if errored:
        return

    if arg_map['direction'] == "to":
        core.runCommand(f"docker cp {arg_map['src']} {arg_map['name']}:{arg_map['dest']}")
    if arg_map['direction'] == "from":
        core.runCommand(f"docker cp {arg_map['name']}:{arg_map['src']} {arg_map['dest']}")

def purge(args):
    arg_map, errored = args.result()
    print(data.Store.get(), type(data.Store.get()))
    data.Store.set({
        "test": "hello!"
    })

command = {
    "start": start,
    "stop": stop,
    "focus": focus,
    "create": create,
    "delete": delete,
    "file": file,
    "purge": purge
}
