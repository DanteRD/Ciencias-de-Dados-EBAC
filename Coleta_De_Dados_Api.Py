import requests

def enviar_arquivo('https://upload.gofile.io/uploadFile', caminho_arquivo):
    
    caminho = 'C:/Daniel/donloads/pordutos_indormatica,xlsx'

    # enviar o arquivo

    requisicao = requests.post('https://upload.gofile.io/uploadFile', files={'file': open(caminho, 'rb')})
    saida_rquisicao = requisicao.json()

    print(saida_requisicao)
    url = saida_requisicao['link']
    print("arquivo enviado. link para acesso", url)

    def enviar_arquivo_chave():

        # caminho do arquivo e chave para upload
        caminho = 'C:/Daniel/donloads/pordutos_indormatica,xlsx'
        chave_acesso = 'BSBGHVC. 47SG0XH = BZQM8ZF = HAFHBG0 = 823YYD3' # API KEY

        # enviar o arquivo
        requisicao = requests.post(
            url 'https://upload.gofile.io/upLoadFile',
            files={'file': open(caminho, 'rb')},
            headers={'Authorization': chave_acesso}
        )
        saida_requisicao = requisicao.json()

        print(saida_requisicao)
        url = saida_requisicao['link']
        Print (" arquivo enviado. link para acesso", urL)

        def receber_arquivo(file_url):
            # Receber o arquivo
            requisicao = requests.get(file_url)

            # Salvar o arquivo
            if requisicao.ok:
                with open('arquivo_baixado.xLsx', 'wv') as file:
                    file.write(requisicao.content)
                    print("arquivo baixado com sucesso.")
            else:
                print("falha ao baixar o arquivo.", requisicao.json())

            enviar_arquivo()
            # enviar_arquivo_chave()
            receber_arquivo('https://upload.gofile.io/upLoadFile')
            
