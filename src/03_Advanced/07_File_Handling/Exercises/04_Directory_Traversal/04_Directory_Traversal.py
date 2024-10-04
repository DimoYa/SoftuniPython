import os

files_by_extension = {}
directory = "./Example"
for item in os.listdir(directory):

    item_path = os.path.join(directory, item)

    if os.path.isfile(item_path):
        _, extension = os.path.splitext(item)
        extension = extension.lstrip(".")
        if extension not in files_by_extension:
            files_by_extension[extension] = []
        files_by_extension[extension].append(item)

sorted_extensions = sorted(files_by_extension.keys())

report_path = os.path.join("./", "report.txt")
with open(report_path, "w") as report:
    for extension in sorted_extensions:
        report.write(f".{extension}\n")
        for file_name in sorted(files_by_extension[extension]):
            report.write(f"- - - {file_name}\n")

