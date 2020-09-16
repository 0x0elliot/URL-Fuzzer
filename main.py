import requests
def main():
    while True:
        try:
            print("Welcome to my URL Fuzzer")
            url = input("What is your URL?")
            wordlist = input("What is the file for your wordlist?")
            threadCount = input("How many threads (1-500)?")
            r = requests.get(url+wordlist, stream=True)
            if(r.ok):
                print(r.url)
                print(r.status_code)
                print("Success!")
            else:
                print(r.status_code)
                print("Failure!")
                return 0
        except:
            print("Error! Please try again.")
            main()

        
main()

