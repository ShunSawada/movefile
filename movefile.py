import shutil
import os
import json

with open('labels.json') as f:
    labels = json.load(f)

for filename in labels:
    dirname = labels[filename]
    os.makedirs(dirname, exist_ok=True)
    new_path = shutil.move(filename, dirname)
