import os


def print_directory_contents(path, indent_level=0, output_file=None):
    for child in os.listdir(path):
        child_path = os.path.join(path, child)
        if os.path.isdir(child_path):
            print(f"{'  ' * indent_level}{child}/", file=output_file)
            print_directory_contents(child_path, indent_level + 1, output_file)
        else:
            print(f"{'  ' * indent_level}{child}", file=output_file)


# Provide the directory path here
directory_path = os.getcwd()

# Provide the output file path here
output_file_path = "output.txt"

with open(output_file_path, "w") as output_file:
    print_directory_contents(directory_path, output_file=output_file)

print(f"Output saved to {output_file_path}")