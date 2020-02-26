#Define imports 
#argparse is used to parse arguments and get the filename that will be used
import argparse
#Sys is used to check the version of python being used
import sys
#os is used to check if the file exists
import os
#use ipaddress module to sort
try:
    import ipaddress
except:
    pass


parser = argparse.ArgumentParser()                                             
parser.add_argument("--file", "-f", type=str, required=True)
parser.add_argument("--deduplicate", "-d", default=False, action="store_true")
args = parser.parse_args()

if sys.version_info.major <= 2:
    print("This application requires python 3 to work properly and you used " + str(sys.version_info.major))
    #send exit status of 1
    sys.exit(1)
# Checks to see if the file exists
if os.path.isfile(args.file):
    with open(args.file) as filehandle:
        #will help strip out whitespace lines
        lines = (line.rstrip() for line in filehandle)
        #sorts the ip addresses and sends to standard out if the line is not blank
        ips = sorted(ipaddress.ip_address(line.strip()) for line in lines if line)
        #checks for the deduplication flag and will remove duplicates if enabled. 
        if args.deduplicate:
            deduplicated_ips = sorted(list(set(ips)))
            print('\n'.join(map(str,deduplicated_ips)))
        else:
            print('\n'.join(map(str, ips)))
