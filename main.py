import requests, os, logging, threading
from colorama import Fore

os.system("title 𝐆𝐢𝐭𝐡𝐮𝐛 𝐯𝐢𝐞𝐰𝐛𝐨𝐭𝐭𝐞𝐫 𝐛𝐲 𝐬𝐞𝐥𝐭𝐨𝐱")
requests = requests.Session()
logging.basicConfig(level=logging.INFO, format="\033[38;5;12m[\033[0m%(asctime)s.%(msecs)03d\033[38;5;12m] \033[0m-> %(message)s", datefmt="%H:%M:%S")

url = input (f'raw link:{Fore.LIGHTGREEN_EX} ')

class Viewbot(object):
    def __init__(self):
        self._link = (url)

    def SendViews(self):
        while True:
            r = requests.get(self._link)
            if r.status_code == 403:
                logging.info("invalid link")
                input()
                os._exit(0)
            else:
                logging.info("sent view | status code: {}".format(r.status_code))

if __name__ == "__main__":
    for i in range(700):
        t = threading.Thread(target=Viewbot().SendViews)
        t.start()