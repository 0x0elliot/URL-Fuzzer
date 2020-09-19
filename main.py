import argparse, requests

parser = argparse.ArgumentParser(prog='fuzzer', description='A tool for finding hidden files and directories on a web server.')
parser.add_argument('--url', dest='url', action='store', 
help="Used to parse a valid URL for fuzzing")
parser.add_argument('--wordlist', dest='wordlist', action='store', 
help="Used to parse wordlist file for fuzzing")
parser.add_argument('--threads', dest='threads', action='store',
help="Used to request a specific number of threads to be used")
args = parser.parse_args()

def main(args):
    try:
        with open(args.wordlist, 'r') as file:
            for line in file.read().split('\n'):
                r = requests.get(args.url+line)
                if(r.ok):
                    print(r.url)
                else:
                    continue
    except requests.exceptions.HTTPError as e:
        print(e)

main(args)