import sys


def do_copy(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        contents = f.read()
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(contents)


def do_reverse(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        contents = f.read()
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(contents[::-1])


def do_duplicate_contents(input_path, n):
    with open(input_path, "r", encoding="utf-8") as f:
        contents = f.read()
    with open(input_path, "w", encoding="utf-8") as f:
        f.write(contents * n)


def do_replace_string(input_path, needle, new_string):
    with open(input_path, "r", encoding="utf-8") as f:
        contents = f.read()

    new_contents = contents.replace(needle, new_string)

    with open(input_path, "w", encoding="utf-8") as f:
        f.write(new_contents)


command = sys.argv[1]


if command == "reverse":
    print("reverse が呼ばれました")
    do_reverse(sys.argv[2], sys.argv[3])


elif command == "copy":
    print("copy が呼ばれました")
    do_copy(sys.argv[2], sys.argv[3])


elif command == "duplicate-contents":
    print("duplicate-contents が呼ばれました")
    do_duplicate_contents(sys.argv[2], int(sys.argv[3]))


elif command == "replace-string":
    print("replace-string が呼ばれました")
    do_replace_string(sys.argv[2], sys.argv[3], sys.argv[4])


else:
    print("知らないサブコマンドです")
