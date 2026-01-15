import sys
import math
import pdb

def create_pos(x, y, z):
    """
        add coordinates and catch valueerror
        if the input is invalid
    """
    coord = ()
    try:
        x = int(x)
        y = int(y)
        z = int(z)
        coord = (x, y, z)
        return coord
    except ValueError as e:
        print(f"Parsing invalid coordinates: {x},{y},{z}")
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}\n")
        return None


def parse_coordinates(argv):
    """
        parse either a string or many args
    """
    if len(argv) == 2:
        try:
            for i in argv:
                if i == ',':
                    return argv[1].split(",")
                else:
                    return argv[1].split(" ")
        except ValueError:
            return None

    elif len(argv) == 4:
        return argv[1], argv[2], argv[3]

    else:
        return None


if __name__ == "__main__":

    print("=== Game Coordinate System ===\n")
    coord = create_pos(10, 20, 5)
    x2 = coord[0]
    y2 = coord[1]
    z2 = coord[2]

    x1 = 0
    y1 = 0
    z1 = 0

    print(f"Position created: {coord}")
    res = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    print(f"Distance between (0, 0, 0) and ({coord}): {res}\n")
    res = float(res)

    if len(sys.argv) < 2:
        print("Insert some arguments")
    else:
        #pdb.set_trace()
        x2, y2, z2 = parse_coordinates(sys.argv)
        new_coord = create_pos(x2, y2, z2)
        if new_coord == None:
            pass
        else:
            res = math.sqrt((int(x2) - x1)**2 +
                        (int(y2) - y1)**2 + (int(z2) - z1)**2)
            res = float(res)

            print(f"Parsing coordinates: {sys.argv[1]}")
            print(f"Parsed position: ({x2}, {y2}, {z2})")
            print(f"Distance between (0, 0, 0) and ({x2}, {y2}, {z2}): {res}\n")

            last_coord = create_pos("abc", "def", "ghi")

            print("Unpacking demonstration:")
            print(f"Player at x={x2}, y={y2}, z={z2}")
            print(f"Coordinates: X={x2}, Y={y2}, Z={z2}")

