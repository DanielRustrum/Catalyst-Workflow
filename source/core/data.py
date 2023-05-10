CATALYST_DIR = "C:\\Program Files\\Catalyst\\"

import os, configparser
class Literal:
    def __init__(self, string):
        self.string = string

class DictToYAML:
    def __init__(self, dictionary):
        self.lines = []
        self._traverseObj(dictionary, 0)
        self.result = "\n".join(self.lines)

    def _traverseObj(self, obj, depth):
        depth_tabs = "    "*depth
        for key, value in obj.items():
            if type(value) is dict:
                self.lines.append(f"{depth_tabs}{key}:")
                self._traverseObj(value, depth + 1)
                continue
            if type(value) is list:
                self.lines.append(f"{depth_tabs}{key}:")
                self._traverseArray(value, depth + 1)
                continue
            if isinstance(value, Literal):
                self.lines.append(f"{depth_tabs}{key}: {value.string}")
                continue
            self.lines.append(f"{depth_tabs}{key}: \"{value}\"")

    def _traverseArray(self, array, depth):
        depth_tabs = "    " * depth
        for value in array:
            if isinstance(value, Literal):
                self.lines.append(f"{depth_tabs}- {value.string}")
                continue
            self.lines.append(f"{depth_tabs}- \"{value}\"")

class Configs:
    config = None

    @staticmethod
    def fetch(path):
        raw_config = configparser.ConfigParser()
        raw_config.read(path)
        Configs.config = raw_config
        return Configs

class Files:
    @staticmethod
    def write(path, content):
        with open(path, "w+") as file:
            file.write(content)

    @staticmethod
    def create(path):
        if not os.path.isfile(path):
            with open(path, "w+"):
                pass

class Directory:
    @staticmethod
    def delete(path):
        for root, dirs, files in os.walk(path):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))

        os.rmdir(path)

    @staticmethod
    def create(path):
        if not os.path.isdir(path):
            os.mkdir(path)

import pickle, atexit
class Store:
    data = {}

    @staticmethod
    def set(dictionary):
        Store.data.update(dictionary)

    @staticmethod
    def get():
        return Store.data

DATA_FILE_LOC = f"{CATALYST_DIR}/data.bin"
Files.create(DATA_FILE_LOC)
if os.path.getsize(DATA_FILE_LOC) > 0:
    with open(DATA_FILE_LOC, "rb") as data_file:
        Store.data = pickle.load(data_file)

def onClose():
    with open(DATA_FILE_LOC, "wb+") as data_file:
        pickle.dump(Store.data, data_file)

atexit.register(onClose)
