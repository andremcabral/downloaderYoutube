from pytube import YouTube, Playlist
from pytube.cli import on_progress
import PySimpleGUI as sg
import time

lt=[
    [sg.Text('Informe o link do vídeo', size=(10, 0)),
    sg.InputText(size=(70, 0), key='link'), sg.Stretch()],
    [sg.Text('Local do arquivo:'), sg.InputText('c:/',key='caminho'),
    sg.FolderBrowse('Caminho...', size=(20, 1)), sg.Stretch()],
    [sg.Radio('Apenas Áudio', group_id='res',key='audio'),
     sg.Radio('Menor Resolução', group_id='res',key='menor', default=True),
     sg.Radio('Maior Resolução', group_id='res',key='maior'),
     sg.Checkbox('Lista',key='lista')],
    [sg.Button('Informações', size=(21, 2), key='info', disabled=False),
    sg.Button('Baixar', size=(21, 2), key='baixar', disabled=False),
    sg.Button('Sair', size=(21, 2), key='sair'), sg.Stretch()],
    [sg.Text('', key='final', size=(80, 1))],
    [sg.Output(size=(80,20), key='out'), sg.Stretch()]
]
janela = sg.Window('Downloader do Youtube',size=(600, 500), resizable=True).layout(lt)

def baixarVideo(link):
    try:
        lk = YouTube(link, on_progress_callback=on_progress)
        lk = YouTube(link)
        print(f'Título: {lk.title}\nBaixando...')
        caminho = valor['caminho']
        if valor['audio'] == True:
            try:
                baixar = lk.streams.get_audio_only()
                baixar.download(filename=f'{lk.title}.mp3', output_path=caminho)
            except:
                print(f'FALHA NO DOWNLOAD DE: {lk.title}')
        elif valor['maior'] == True:
            try:
                baixar = lk.streams.get_highest_resolution()
                baixar.download(output_path=caminho)
            except:
                print(f'FALHA NO DOWNLOAD DE: {lk.title}')
        else:
            try:
                baixar = lk.streams.get_lowest_resolution()
                baixar.download(output_path=caminho)
            except:
                print(f'FALHA NO DOWNLOAD DE: {lk.title}')
    except:
        janela['final'].update("Ocorreu um problema. Por favor verifique o link")

def baixarLista(link):
    lista = Playlist(link)
    for link in lista:
        baixarVideo(link)
    return 'Concluido'

def dadosLista(link):
    lista = Playlist(link)
    titulo=[]
    imagem=[]
    data=[]
    tamanho=[]
    for link in lista:
        try:
            lk = YouTube(link, on_progress_callback=on_progress)
            titulo.append(lk.title)
            imagem.append(lk.thumbnail_url)
            tamanho.append(lk.length)
            data.append(format(lk.publish_date,'%d/%m/%Y'))
            print(f'Título: {titulo[-1]}\n         Tempo em segundos: {tamanho[-1]} - Data de publicação: {data[-1]}')
        except:
            janela['final'].update("Existe um problema, favor tentar novamente")
    print(f'\nQuantidade de vídeos: {len(titulo)}')

def dadosVideo(link):
    try:
        lk = YouTube(link, on_progress_callback=on_progress)
        titulo=lk.title
        imagem=lk.thumbnail_url
        tamanho=lk.length
        data=format(lk.publish_date,'%d/%m/%Y')
        print(f'Título: {titulo[-1]}\n         Tempo em segundos: {tamanho[-1]} - Data de publicação: {data[-1]}')
    except:
        janela['final'].update("Existe um problema, favor tentar novamente")

while True:
    evento, valor = janela.Read()
    if (evento == 'sair' or evento == sg.WINDOW_CLOSED):
        break
        quit()
    else:
        link = valor['link']
        if(evento == "info"):
            janela['final'].update('')
            janela['out'].update('')
            if(valor['lista'] == True):
                dadosLista(link)
            else:
                dadosVideo(link)
        if(evento == "baixar"):
            janela['final'].update('')
            janela['out'].update('')
            if(valor['lista'] == True):
                janela['final'].update(baixarLista(link))
            else:
                janela['final'].update(baixarVideo(link))
    janela['final'].update('Concluído')
