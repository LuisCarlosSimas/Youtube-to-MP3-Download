print('Bem vindo. Aguarde a janela "Download Youtube"')

import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
from moviepy.editor import VideoFileClip
import os

def baixar():
    #diretórios
    try:
        link=url.get()
        diretorio=os.getcwd()
        diretorio=diretorio.replace("\\","/")
        download_path = diretorio
        if link=="":
            print("Insira um endereço URL do Youtube!")
            return
        
    except Exception as e: 
        print(f"Erro de diretório. Consulte o desenvolvedor do programa! ERROR= {str(e)}")

    #download do vídeo
    try:
        video = YouTube(link)
        print("Baixando vídeo...")
        clip = video.streams.get_highest_resolution()
        clip.download(output_path=download_path)
        print("Download concluido. Aguarde!")

    except Exception as e:
        messagebox.showerror("ERRO","Link de download incorreto, ou vídeo não disponivel para download!")
        print(f"Erro ao baixar o vídeo! ERROR= {str(e)}")
        return

    #converção para mp3
    try:
        #diretório do vídeo
        try:
            arquivos_do_diretorio=os.listdir(diretorio)
            arquivo_mais_recente=max(arquivos_do_diretorio, key=os.path.getctime)
            video_file = f'{diretorio}/{arquivo_mais_recente}'
            arquivo_mais_recente=arquivo_mais_recente.replace(".mp4","")
            mp3_output_path = f'{diretorio}/{arquivo_mais_recente}.mp3'

        except Exception as e:
            print(f"Erro de diretório do vídeo. Consulte o desenvolvedor do programa! ERROR= {str(e)}")

        print("Convertendo vídeo para mp3...")

        video = VideoFileClip(video_file)
        audio = video.audio
        audio.write_audiofile(mp3_output_path)
        audio.close()
        video.close()

        #excluir o vídeo
        try:
            os.remove(video_file)
            url.delete(0, "end")

        except Exception as e:
            print(f"Erro ao excluir o vídeo. ERROR= {str(e)}")

        messagebox.showinfo("Sucesso","Novo mp3 criado com sucesso!")
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
