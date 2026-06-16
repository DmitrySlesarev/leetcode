def read_file_inefficient(filename):
    with open(filename, 'r') as f:
        return f.readlines()  # Loads EVERYTHING into memory


def read_file_efficient(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line  # One line at a time

if __name__ == "__main__":
    print(read_file_inefficient("textfile.txt"))  # type: ignore[call-arg]

    for line in read_file_efficient("textfile.txt"):
        print(line)