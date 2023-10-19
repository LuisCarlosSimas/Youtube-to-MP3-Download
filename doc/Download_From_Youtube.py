print('Bem vindo. Aguarde a janela "Download Youtube"')

import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
from moviepy.editor import VideoFileClip
import os

def baixar():
    link=url.get()
    diretorio=os.getcwd()
    diretorio=diretorio.replace("\\","/")
    if link=="":
        print("Insira um endereço URL do Youtube!")
        return

    try:
        video = YouTube(link)
        print("Baixando vídeo...")
        clip = video.streams.get_highest_resolution()
        download_path = diretorio
        clip.download(output_path=download_path)
        print("Download concluido. Aguarde!")

    except Exception as e:
        messagebox.showerror("ERRO","Link de download incorreto, ou vídeo não disponivel para download!")
        print(f"ERRO! {str(e)}")
        return

    arquivos_do_diretorio=os.listdir(diretorio)
    arquivo_mais_recente=max(arquivos_do_diretorio, key=os.path.getctime)

    #converção mp3
    try:
        video_file = f'{diretorio}/{arquivo_mais_recente}'
        mp3_output_path = f'{diretorio}/{arquivo_mais_recente}.mp3'
        print("Convertendo vídeo para mp3...")
        video = VideoFileClip(video_file)
        audio = video.audio
        audio.write_audiofile(mp3_output_path)
        audio.close()
        video.close()

        os.remove(f'{diretorio}/{arquivo_mais_recente}')

        url.delete(0, "end")

        messagebox.showinfo("Sucesso","Novo mp3 baixado com sucesso!")
        print("Arquivo mp3 criado com sucesso!")

        print("Fim da execução!")

    except Exception as e:
        messagebox.showerror("ERRO","Erro ao converter o vídeo para mp3")
        print(f"ERRO! {str(e)}")
        return

janela=tk.Tk()
janela.title("Download Youtube")
janela.geometry("300x100")

tk.Label(janela,text="URL do vídeo",).pack(anchor="center")

url=tk.Entry(janela)
url.pack(anchor="center",ipadx=60,pady=5)
url.focus_set()

botaoBaixar=tk.Button(janela,text="Baixar mp3",command=baixar,default="active",cursor="hand2")
botaoBaixar.pack(anchor="center")

janela.bind('<Return>', lambda event=None: botaoBaixar.invoke())

janela.mainloop()