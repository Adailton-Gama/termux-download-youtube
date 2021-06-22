from pytube import YouTube
from tqdm import tqdm
from time import sleep
import os
import pytube
import sys
import time
import pyfiglet

os.system("clear")

ascii_banner = pyfiglet.figlet_format("DownTube")
print(ascii_banner)

carregar = "\033[1;31m================> By Vini <================\n\n"

for i in list(carregar):
    print(i, end='')
    sys.stdout.flush()
    time.sleep(0.08)

link = input("\033[1;34mCopie o link do Vídeo aqui: ")
yt = YouTube(link)

yt.streams.filter(res="720p").first().download('download_video')

def progress_bar(done):
    print("\033[1;97m\rBaixando ➤ [{0:50s}] {1:.1f}%".format('#' * int(done * 50), done * 100),end='')

def test():
    for n in range(101):
        progress_bar(n/100)
        time.sleep(0.01)
test()

os.system("mv download_video /home/storage/downloads")

print("\n\n\033[0;32mBaixado com Sucesso [ ✔️ ]")
