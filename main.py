import requests

print("Welcome to my URL Fuzzer")
url = input("What is your URL? ")
wl = input("What is the file for your wordlist? ")
threadCount = input("How many threads (1-500)? ")

def main(url,wl,threadCount):
    with open(wl, 'r') as file:
        for line in file.read().split('\n'):
            r = requests.get(url+line)
            if(r.ok):
                print("Success")
                print(r.url)
            else:
                print("Fail")
                print(r.url)

main(url,wl,threadCount)