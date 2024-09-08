#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 1
    print("{} arguments :".format(len(sys.argv)))
    for arg in sys.argv:
        print("{}: {}".format(i, arg))
        i += 1
