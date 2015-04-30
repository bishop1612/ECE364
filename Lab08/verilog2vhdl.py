import sys
import vtools

if __name__ == "__main__":
    if(len(sys.argv) > 3 or len(sys.argv) < 2):
        print("Usage: verilog2vhd1.py [infile] [outfile]")
        sys.exit(1)

    if(len(sys.argv) == 2):
        infile = sys.argv[1]
        try:
            fp = open(sys.argv[1],"r")
        except :
            raise IOError(2)
            sys.exit(2)
    if(len(sys.argv) == 3):
        infile = sys.argv[1]
        try:
            fp = open(sys.argv[1],"r")
        except :
            raise IOError(2)
            sys.exit(2)
        outfile = sys.argv[2]
        try:
            fp = open(sys.argv[2],"w")
        except :
            raise IOError(3)
            sys.exit(3)

    if(len(sys.argv) == 2):
        lines = fp.readlines()
        #print(lines)
        for line in lines:
            print(line)
            comp,instance,cmp = vtools.parse_net(str(line))