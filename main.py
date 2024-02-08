#!/bin/python3

import sys
import os

from modules import fileHandler




def printHelp():
    print("Finnish grammarchecker for tex files")
    print("-h,  --help      prints this help text")



def main():

    args= sys.argv[1:]      # skip first arg we dont need to know the filename
    argc= len(sys.argv)-1   # we are skipping first arg
    

    if(argc==0):
        printHelp()
        exit(0)
    

    # interpret cmd arguments to file to determine what we want to do
    #loop args to see what we are doing
    for arg in args:
        match arg:
            case "-h" | "--help":
                printHelp()

            case _:

                # this is probably filename check if exists
                # if so then start doing the reading
                # if filename not real then do error thing
                
                if(os.path.isfile(arg)):
                    fileHandler.handleFile(arg)
                    # start to do the things init the start voikko pipeline
                else:
                    print("unknown filename ",arg )
                    exit(1)

    
        








if __name__ == "__main__":
    main()
else:
    print("file is not supposed to be imported")
    exit(1)
