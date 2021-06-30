from pytube import YouTube
from tqdm import tqdm
from time import sleep
from sys import exit
import os
import pytube
import sys
import time
import pyfiglet

os.system('cls')

ascii_banner = pyfiglet.figlet_format("DownTube")
print(ascii_banner)

carregar = "\033[1;31m================> By Vini <================\n\n"

for i in list(carregar):
    print(i, end='')
    sys.stdout.flush()
    time.sleep(0.08)

link = input("\033[1;34mCopie o link do Vídeo aqui: ")
yt = YouTube(link)
try:
    yt.streams.filter(res="720p").first().download('download_video')
except:
    print('Não foi possível fazer download em FullHD, gostaria fazer download em uma resolução inferior? ')
    qd = input('Pressione "1" para baixar ou "2" para cancelar ')
    print()
    if qd == 1:
        yt.streams.filter(res="360p").first().download('download_video')
    elif qd==2:
        print('Download Cancelado! Encerrando o programa')
def progress_bar(done):

    print("\033[1;97m\rBaixando ➤ [{0:50s}] {1:.1f}%".format('#' * int(done * 50), done * 100),end='')

def test():
    for n in range(101):
        progress_bar(n/100)
        time.sleep(0.01)
test()

os.system("move download_video c:/Users/Adailton/Downloads")

print("\n\n\033[0;32mBaixado com Sucesso [ ✔️ ]")
