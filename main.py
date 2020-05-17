import re
import os

def find_files(root_path):
    file_blob = os.popen("find " + root_path + " -type f -not -path '*.git*'").read()
    return file_blob.split("\n")[:-1]

def search_file(file_name, patterns):
    found_secrets = []
    file_contents = open(file_name, 'r').read()
    for pattern in patterns:
        matches = re.findall(pattern, file_contents)
        if matches:
            print("found ", len(matches), "counts of secrets in file: ", file_name, "consisting of:", matches)
            found_secrets += [file_name,matches]
    return found_secrets

output = []
patterns = ["script"]
root_path = "/"

file_list = find_files(root_path)
for file_name in file_list:
    output += search_file(file_name, patterns)


print(output)
