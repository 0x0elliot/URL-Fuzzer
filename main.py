import argparse
import requests
import threading
import concurrent.futures
from time import perf_counter

parser = argparse.ArgumentParser(prog='fuzzer', description='A tool for finding hidden files and directories on a web server.')
parser.add_argument('--url', dest='url', action='store', 
help="Used to parse a valid URL for fuzzing")
parser.add_argument('--wordlist', dest='wordlist', action='store', 
help="Used to parse wordlist file for fuzzing")
parser.add_argument('--threads', dest='threads', type=int, action='store',
help="Used to request a specific number of threads to be used")
args = parser.parse_args()

def main(args):
    try:
        start = perf_counter()
        with open(args.wordlist, 'r') as file:
            for line in file.read().split('\n'):
                r = requests.get(args.url+line)
                if(r.ok):
                    print(r.url)
                else:
                    continue
    except:
        return 0

    end = perf_counter()
    execution_time = end - start
    print(f"Completed in {execution_time} seconds!")

with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads,) as executor:
    executor.map(main(args), range(args.threads))