import sys


def main():
    if len(sys.argv) == 2:
        try:
            f = open(sys.argv[1], 'r')
            input_lines = f.readlines()
        except FileNotFoundError as e:
            print("Invalid file")
            exit()
        # Solve pt 1

        # Solve pt 2
    else:
        print(f"Usage: \n{sys.argv[0]} <filename>")
        exit()


if __name__=="__main__":
    main()