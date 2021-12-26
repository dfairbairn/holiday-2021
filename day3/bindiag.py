import sys

class BinDiagError(Exception):
    pass


class BinDiagStats:
    def __init__(self, n=0):
        self.arr = []
        self.N = n
        for i in range(n):
            self.arr.append({0: 0, 1: 0})

    def add_line(self, bin_str):
        char_counts = BinDiagStats.parse_line(bin_str, self.N)

        for i, c in enumerate(char_counts):
            # print(f"{self.arr}, i: '{i}', c: '{c}'")
            self.arr[i][c] += 1
        # print(self)

    def __repr__(self):
        return self.arr.__repr__()


    @staticmethod
    def parse_line(bin_str, N):
        # First N chars of the line should all be 0 or 1
        # print(f"bin_str: {bin_str}, len of bin: '{len(bin_str) - 1}', supplied arg N: '{N}'")
        l = [0 for i in range(N)]
        if bin_str.count('\n') > 1:
            raise BinDiagError("Multiple lines!")
        elif len(bin_str) < 5:
            raise BinDiagError("Incomplete line!")
        for i, c in enumerate(bin_str):
            if c not in "01":
                continue  # Includes the \n
                # raise BinDiagError("Bad binary character in line!")
            print(f"{i=},{c=},{l=}")
            l[i] += int(c)
        print(l)
        return l


def get_bindiag_len(line):
    return len(line) - 1


def parse_5bit_lines(lines):
    n = get_bindiag_len(lines[0])
    bds = BinDiagStats(n=n)
    for line in lines:
        bds.add_line(line)
    return bds


def get_rate(bds, rate="gamma"):
    ans = []
    d = {}
    for i, bindict in enumerate(bds.arr):
        if (bindict[0] > bindict[1] and rate == "gamma") or (bindict[0] < bindict[1] and rate == "epsilon"):
            ans.append("0")
            continue
        elif (bindict[1] > bindict[0] and rate =="gamma") or (bindict[1] < bindict[0] and rate == "epsilon"):
            ans.append("1")
            continue
        elif bindict[1] == bindict[0]:
            raise BinDiagError(f"Warning: Equal numbers of 0's and 1's in bit number '{i}'")
        else:
            raise BinDiagError(f"Error: Bad combo. Shouldn't happen?")
    import functools
    ans = functools.reduce(lambda x, y: x+y, ans)
    print(f"{ans}={int(ans,2)}")
    # Calculate gamma rate as decimal of the binary value
    return int(ans, 2)


def main():
    if len(sys.argv) == 2:
        try:
            f = open(sys.argv[1], 'r')
            input_lines = f.readlines()
        except FileNotFoundError as e:
            print("Invalid file")
            exit()
        # Solve pt 1
        bds = parse_5bit_lines(input_lines)
        print(bds)
        gamma = get_rate(bds, rate="gamma")
        epsilon = get_rate(bds, rate="epsilon")
        print(gamma * epsilon)

        # Solve pt 2
    else:
        print(f"Usage: \n{sys.argv[0]} <filename>")
        exit()


if __name__=="__main__":
    main()