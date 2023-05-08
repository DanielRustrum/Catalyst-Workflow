def dictToYAML(dictionary, path):
    pass

def YAMLtoDict(path):
    pass

def storeFile(namespace, path):
    file = path.split("\\")[-1]
    print(f"C:/'Program Files/Catalyst/{namespace}/{file}'")

def fetchFile(namespace, file):
    return "C:/'Program Files'/Catalyst/{namespace}/{file}"
