from pytube import YouTube
import os
import shutil
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
ntitle = yt.streams[0].title
title = ntitle + ".mp4"
print()

def progress_bar(done):
    print("\033[1;97m\rBaixando ➤ [{0:50s}] {1:.1f}%".format('#' * int(done * 50), done * 100), end='')


def test():
    for n in range(101):
        progress_bar(n / 100)
        time.sleep(0.01)


def move():
    shutil.move("C:/Users/Adailton/PycharmProjects/PyDyout/download_video/{}".format(title), "c:/Users/Adailton/Downloads/{}".format(title))
    print()
    print('Alocando na Pasta Download, Por favor aguarde um pouco. ')


def low_quality():
    print('Não foi possível fazer download em FullHD, gostaria fazer download em uma resolução inferior? ')
    qd = int(input('Pressione "1" para baixar ou "2" para cancelar: '))
    print()
    if qd == 1:
        yt.streams.filter(res="360p").first().download('download_video')
        test()
        time.sleep(5)
        move()
        print("\n\n\033[0;32mBaixado com Sucesso [ ✔️ ]")
    else:
        print('Download Cancelado! Encerrando o programa')


try:
    yt.streams.filter(res="720p").first().download('download_video')
    test()
    print("\n\n\033[0;32mBaixado com Sucesso [ ✔️ ]")
    time.sleep(5)
    move()

##  Parei aqui-----------------------------
except:
    low_quality()
finally:
    print('encerrendo o sistema')
# print("ERRO AO BAIXAR")
# print()
