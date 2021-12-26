import sys
from dataclasses import dataclass


@dataclass
class BathState:
    """ Bathymetric state for part 1 based on x/y/-z directions and commands in the X (forward) and Z (up/down) """
    x: int = 0
    y: int = 0
    depth: int = 0

    def _add(self, s):
        """ Sum two bathstate vectors """
        self.x += s.x
        self.y += s.y
        self.depth += s.depth

    def move(self, movement):
        """ Takes a bathymetric state and a movement operation string, returns new bathymetric state """
        move_state = BathState.parse_movement(movement)
        self._add(move_state)

    @staticmethod
    def parse_movement(movement_str: str):
        """ Extract word and number from movement string, interpret as movement operation for a bathymetric state """
        try:
            dir, dist = movement_str.split(' ')
            dist = int(dist)
        except Exception as e:
            print(f"Error: bad movement str")
            return BathState(0,0,0)
        if dir == 'forward':
            return BathState(dist, 0, 0)
        elif dir == 'up':
            return BathState(0, 0, -dist)
        elif dir == 'down':
            return BathState(0, 0, dist)
        print("Warning: Unrecognized direction")
        return BathState(0, 0, 0)

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.depth})"


@dataclass
class BathStatePart2:
    x: int = 0
    aim: int = 0
    depth: int = 0

    def move(self, movement_str):
        """
        Takes a bathymetric state and a movement operation string, returns new bathymetric state
        """
        try:
            dim, magnitude = movement_str.split(' ')
            magnitude = int(magnitude)
        except Exception as e:
            print(f"Error: bad movement str")
            raise Exception(e)
        if dim == 'forward':
            self.x += magnitude
            self.depth += self.aim * magnitude
        elif dim == 'up':
            self.aim -= magnitude
        elif dim == 'down':
            self.aim += magnitude

    def __repr__(self):
        return f"({self.x}, {self.aim}, {self.depth})"


def solve(movements, part="part2"):
    if part == "part1":
        s = BathState(0, 0, 0)
    elif part == "part2":
        s = BathStatePart2(0, 0, 0)
    else:
        print(f"Error: no part {part}")
    for move in movements:
        s.move(move)
    return s.x * s.depth


def main():
    if len(sys.argv) == 2:
        try:
            f = open(sys.argv[1],'r')
        except FileNotFoundError as e:
            print("Invalid file")
            exit()
        # Parse movements
        movements = f.readlines()
        # If we're solving Part 1:
        # solve(movements, part="part1")
        # Otherwise, if solving Part 2:
        sol = solve(movements, part="part2")
        print(sol)
    else:
        print(f"Usage: \n{sys.argv[0]} <filename>")
        exit()



def test_moves():
    # Test movement parsing
    BathState.parse_movement('forward 5 ')

    s = BathState(0, 0, 0)
    s.move('forward 2 ')
    s.move('forward 7 ')
    s.move('up 3 ')
    print(s)


if __name__=="__main__":
    main()