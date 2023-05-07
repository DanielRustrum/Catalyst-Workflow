import yaml

def convertToYAML(dictionary, path):
    with open(path, 'w+') as yaml_file:
        yaml.dump(dictionary, yaml_file, allow_unicode=True)

def fetchYAML(path):
    pass

def storeFile(namespace, path):
    file = path.split("\\")[-1]
    print(f"C:/'Program Files/Catalyst/{namespace}/{file}'")

def fetchFile(namespace, file):
    return "C:/'Program Files'/Catalyst/{namespace}/{file}"
