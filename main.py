import argparse
import requests
import threading
import concurrent.futures
from time import perf_counter

#Initilized an argument parser
parser = argparse.ArgumentParser(prog='fuzzer', description='A tool for finding hidden files and directories on a web server.')

#Created a seperate argument group
requiredNamed = parser.add_argument_group('required named arguments')

#Invoked required arguments
requiredNamed.add_argument('-url', dest='url', action='store', required=True, 
help="Used to parse a valid URL for fuzzing")
requiredNamed.add_argument('-wordlist', dest='wordlist', action='store', required=True,
help="Used to parse wordlist file for fuzzing")
requiredNamed.add_argument('-threads', dest='threads', type=int, action='store', required=True,
help="Used to request a specific number of threads to be used")

#Parsed arguments to the args variable
args = parser.parse_args(['-h'])

#Created a thread pool with the target of the Fuzzer function
def main(args):
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads,) as executor:
            executor.map(Fuzzer(args), range(args.threads))
    except:
        print("Error!")
        return 0

#Sends requests to a specified web server using paths from a file
def Fuzzer(args):
    startTime = perf_counter()
    with open(args.wordlist, 'r') as file:
        for line in file.read().split('\n'):
            r = requests.get(args.url+line)
            if(r.ok):
                print(r.url)
            else:
                continue
    endTime = perf_counter()
    executionTime = endTime - startTime
    print(f"Completed in %H:%M:%S", executionTime, " seconds!")

#Invoked the main function, along with the arguments
main(args)