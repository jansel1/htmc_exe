import requests, os, random, time

from colorama import Fore, Style

os.system('color 8')
os.system('cls')

print(f"{Fore.GREEN} HTMC: The Tool To Clone The HTML From Websites!{Fore.RESET}")
print(f"{Fore.LIGHTRED_EX} Do not use for malicious purposes!\n{Fore.RESET}")

try:
    while True:
        url = input(" Website To Clone: ")

        POSSIBLE_REASONS = ("""
            1. No Internet access
            2. URL does not exist\n
        """)

        def Copy(url: str):
            if url in ["", None]:
                print(f"{Fore.RED} URL Cannot be empty!{Fore.RESET}\n")

                return 1
            
            CLEAN_URL = (str(url)
                    .replace('http://', '', 1)
                    .replace('https://', '', 1)
                    .replace('http', '', 1)
                    .replace('https', '', 1)
                    .replace('.com', '')
                    .replace('www', '', 1)
                    .replace('.', '', 0)
                    .replace('/', '-')
                )

            if not url.startswith("https://") and not url.startswith("http://"):
                url = f"https://{url}"

            try:
                response = requests.get(url=url).text
            except:
                print(f"{Fore.RED} Could not scrape the HTML from {Fore.RESET}{Fore.BLUE} {url} {Fore.RESET}{Fore.RED} Error may be due to the following reasons:{Fore.RESET}\n")
                print(POSSIBLE_REASONS)

                return 1
            

            with open(f"{CLEAN_URL} {random.randint(20, 500)}.htm", "x+") as file:
                try:
                    file.write(f"<!-- {CLEAN_URL} -->\n{response}")

                    print(f"{Fore.GREEN} Success on cloning!{Fore.RESET}")
                    print(f"{Fore.LIGHTGREEN_EX} File Adress: {os.path.abspath(file.name)}{Fore.RESET}\n")

                except:
                    pass

        Copy(url)
except KeyboardInterrupt:
    print(f"{Fore.RED}\n Exiting...{Fore.RESET}")
    time.sleep(0.5)

    print(f"{Fore.GREEN} Farewell, user!{Fore.RESET}")
    time.sleep(1)

    quit()
    

# Source code for HTMC.
# Made into an EXE with AutoPyToExe