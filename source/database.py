import pickle, atexit

ROOT_DIR = "./buckets"

buckets = {}

def save():
    for (key, value) in buckets.items():
        with(`{ROOT_DIR}/{key}.bucket`) as bucket_file:
            pickle.dump(value, bucket_file)

def set(id, value):
    if id in buckets:
        buckets[id].update(value)
    else:
        buckets[id] = value

def get(id):
    if id not in buckets:
        with open(`{ROOT_DIR}/{id}.bucket`, "r") as bucket_file:
            buckets[id] = pickle.load(bucket_file)

    return buckets[id]

atexit.register(save)
