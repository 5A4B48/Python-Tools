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
args = parser.parse_args()

if sys.version_info.major <= 2:
    print("This application requires python 3 to work properly and you used " + str(sys.version_info.major))
    #send exit status of 1
    sys.exit(1)
# Checks to see if the file exists
if os.path.isfile(args.file):
    with open(args.file) as filehandle:
        #sorts the ip addresses and sends to standard out
        ips = sorted(ipaddress.ip_address(line.strip()) for line in filehandle)
        print('\n'.join(map(str, ips)))
