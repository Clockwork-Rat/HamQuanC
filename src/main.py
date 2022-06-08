import sys


def main(args):
    if len(args) == 0 or args[0] == "-h" or args[0] == "--help":
        print("Help options")
    elif args[0].endswith(".csv") or args[0].endswith(".tsv"):
        raise Exception("Not Yet Implemented")
    else:
        print ("Invalid input, please reference '-h|--help for"
        +" more information")

if __name__ == "__main__":
    if sys.argv[0].endswith(".py"):
        main(sys.argv[1:])
    else:
        main(sys.argv)