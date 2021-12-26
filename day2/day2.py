import sys
from dataclasses import dataclass


@dataclass
class BathState:
    x: int = 0
    y: int = 0
    depth: int = 0

    def _add(self, s):
        self.x += s.x
        self.y += s.y
        self.depth += s.depth

    def move(self, movement):
        """
        Takes a bathymetric state and a movement operation string, returns new bathymetric state
        """
        move_state = BathState.parse_movement(movement)
        self._add(move_state)

    @staticmethod
    def parse_movement(movement_str: str):
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


def main():
    if len(sys.argv) == 2:
        try:
            f = open(sys.argv[1],'r')
        except FileNotFoundError as e:
            print("Invalid file")
            exit()
        # Parse movements
        movements = f.readlines()
        s = BathState(0, 0, 0)
        for move in movements:
            # print(move)
            s.move(move)
        # print(s)
        print(s.x*s.depth)
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