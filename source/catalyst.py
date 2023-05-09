import sys, types
from core import docker, args


def main():
    command, cargs, _ = args.getCommand()
    command(cargs)

if __name__ == '__main__':
    main()
