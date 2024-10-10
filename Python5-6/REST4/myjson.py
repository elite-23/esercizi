import json
from pathlib import Path

def JsonSerialize(data, sFile):
    with open(sFile, "w") as write_file:
        json.dump(data, write_file,indent=4)

def JsonDeserialize(sFile):
    with open(Path(__file__).with_name(sFile), "r") as read_file:
        return json.load(read_file)