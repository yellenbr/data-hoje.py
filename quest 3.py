import os

def listar_arquivos(caminho):
    arquivos = os.listdir(caminho)
    return arquivos
caminho_digitado = input("Digite o caminho de um diretório: ")

arquivos = listar_arquivos(caminho_digitado)

print("todos os rquivos e diretórios em {}: {}".format(caminho_digitado, arquivos))
