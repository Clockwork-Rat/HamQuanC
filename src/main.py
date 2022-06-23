from operator import le
import sys
from unitary import unitary, m_unitary
from decomp import decomp


def main(args):
    if len(args) == 0 or args[0] == "-h" or args[0] == "--help":
        print("Help options")
    elif args[0].endswith(".csv") or args[0].endswith(".tsv"):
        if len(args) == 1:
            u = unitary(args[0])
            print(u)
            decomp(u)
        else:
            u = m_unitary(args[0], int(args[1]))
            print("\nUnitary Matrices:\n")
            for i in range(len(u)):
                print(u[i])
    else:
        print ("Invalid input, please reference '-h|--help for"
        +" more information")

if __name__ == "__main__":
    if sys.argv[0].endswith(".py"):
        main(sys.argv[1:])
    else:
        main(sys.argv)