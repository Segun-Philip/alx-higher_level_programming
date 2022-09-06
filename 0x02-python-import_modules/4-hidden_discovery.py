#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    """Print all names defined by the compiled module"""
    hidden = dir(hidden_4)

    for i in hidden:
        if i[:2] != "__":
            print(i)
