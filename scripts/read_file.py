def read_file(file):
    with open(file) as file:
        contents = file.read()

        print(contents)

if __name__ == "__main__":
    read_file("./get_logs.py")
