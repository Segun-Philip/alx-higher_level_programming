#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total_count = 0
    arg_count = len(sys.argv) - 1
    
    for i in range(arg_count):
        total_count += int(sys.argv[i + 1])
    print("{}".format(total_count))
