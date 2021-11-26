from pytube import YouTube
from pytube.cli import on_progress
import PySimpleGUI as sg
import time

lt=[
    [sg.Text('Informe o link do vídeo', size=(10, 0)),
    sg.InputText(size=(70, 0), key='link'), sg.Stretch()],
    [sg.Text('Local do arquivo:'), sg.InputText(key='caminho'),
    sg.FolderBrowse('Caminho...', size=(20, 1)), sg.Stretch()],
    [sg.Button('Informações', size=(21, 2), key='info', disabled=False),
    sg.Button('Baixar', size=(21, 2), key='baixar', disabled=False),
    sg.Button('Sair', size=(21, 2), key='sair'), sg.Stretch()],
    [sg.Text('Título do video', key='txtNome')],
    [sg.Multiline('', key='saidaTitulo', size=(80, 1))],
    [sg.Text('Data do video', key='txtData'),sg.Text('', key='saidaData', size=(80, 1))],
    [sg.Text('Tamanho do video', key='txtTamanho'),sg.Text('', key='saidaTamanho', size=(80, 1))],
    [sg.Text('Imagem', key='txtImagem'),sg.Text('', key='saidaImagem', size=(80, 1))],
    [sg.Text('', key='final', size=(80, 1))],
    [sg.Output(size=(30,20)), sg.Stretch()]
]
janela = sg.Window('Downloader do Youtube',size=(600, 500), resizable=True).layout(lt)

def baixarVideo(link):
    try:
        # lk = YouTube(link, on_progress_callback=on_progress)
        lk = YouTube(link, on_progress_callback=on_progress)
        # lk.register_on_progress_callback(show_progress_bar)
        baixar = lk.streams.get_highest_resolution()
        caminho = valor['caminho']
        baixar.download(caminho)
        return 'Concluido'
    except:
        janela['final'].update("Ocorreu um problema. Por favor verifique o link")

def dadosVideo(link):
    try:
        lk = YouTube(link, on_progress_callback=on_progress)
        titulo = lk.title
        imagem = lk.thumbnail_url
        tamanho = lk.length
        data = lk.publish_date
        janela['saidaTitulo'].update(titulo)
        janela['saidaData'].update(data)
        janela['saidaTamanho'].update(tamanho)
        janela['saidaImagem'].update(imagem)
    except:
        janela['final'].update("Existe um problema, favor tentar novamente")

while True:
    evento, valor = janela.Read()
    if (evento == 'sair' or evento == sg.WINDOW_CLOSED):
        break
    else:
        try:
            link = valor['link']
            if(evento == "info"):
                dadosVideo(link)
            if(evento == "baixar"):
                baixarVideo(link)
                janela['final'].update(baixarVideo(link))
        except:
            janela['final'].update("Existe um problema, favor tentar novamente")