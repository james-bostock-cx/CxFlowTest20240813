import os
import sys

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        os.remove(arg)
