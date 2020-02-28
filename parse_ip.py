#Define imports 
#argparse is used to parse arguments and get the filename that will be used
import argparse
#Sys is used to check the version of python being used
import sys
#os is used to check if the file exists
import os
#use socket to attempt to resolve hostnames
import socket
#use ipaddress module to sort
try:
    import ipaddress
except:
    pass

if sys.version_info.major <= 2:
    print("This application requires python 3 to work properly and you used " + str(sys.version_info.major))
    #send exit status of 1
    sys.exit(1)

parser = argparse.ArgumentParser()                                             
parser.add_argument("--file", "-f", type=str, required=True, help="The file to be sorted using new line delimiters.")
parser.add_argument("--deduplicate", "-d", default=False, action="store_true", help="Use this to remove duplicate entries.")
parser.add_argument("--lookup-hostname", "-l", dest="hostnames", default=False, action="store_true", help="Use this to resolve hostnames where possible this list will be deduplicated")
args = parser.parse_args()


# Checks to see if the file exists
if os.path.isfile(args.file):
    print('[*] File was found on disk grabbing a list of ip addresses from ' + str(args.file))
    with open(args.file) as filehandle:
        #will help strip out whitespace lines
        lines = (line.rstrip() for line in filehandle)
        #sorts the ip addresses and sends to standard out if the line is not blank
        ips = sorted(ipaddress.ip_address(line.strip()) for line in lines if line)
        #checks for the deduplication flag and will remove duplicates if enabled. 
        if args.deduplicate:
            print('[*] Deduplication was selected removing duplicates now')
            deduplicated_ips = sorted(list(set(ips)))
            for ip in deduplicated_ips:
                print('\n[+] ' + str(ip))
        #deduplicates to resolve names
        if args.hostnames:
            deduplicated_ips = sorted(list(set(ips)))
            print("[*] Attempting to resolve hostnames using reverse records for ips in the list")
            for ip in deduplicated_ips:
                try:
                    print('\n[+] ' + str(ip) + ' resolves to ' + socket.gethostbyaddr(str(ip))[0])
                except:
                    print('\n[-] No name for ' + str(ip))
                    pass

        if not args.deduplicate and not args.hostnames:
            for ip in ips:
                print('\n[+] ' + str(ip))
