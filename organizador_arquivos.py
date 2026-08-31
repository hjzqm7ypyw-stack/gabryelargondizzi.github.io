"""
Organizador de Arquivos
------------------------
Automação que varre uma pasta e move os arquivos para subpastas
de acordo com o tipo (Imagens, Documentos, Planilhas, Compactados,
Áudio, Vídeo, Outros).

Uso:
    python organizador_arquivos.py "C:/Users/voce/Downloads"

Se nenhuma pasta for informada, usa a pasta atual.
"""

import os
import shutil
import sys

CATEGORIAS = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Documentos": [".pdf", ".doc", ".docx", ".txt", ".odt"],
    "Planilhas": [".xls", ".xlsx", ".csv"],
    "Compactados": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Audio": [".mp3", ".wav", ".flac", ".ogg"],
    "Video": [".mp4", ".mkv", ".avi", ".mov"],
}


def categoria_do_arquivo(extensao):
    for categoria, extensoes in CATEGORIAS.items():
        if extensao.lower() in extensoes:
            return categoria
    return "Outros"


def organizar(pasta, simular=False):
    if not os.path.isdir(pasta):
        print(f"Pasta não encontrada: {pasta}")
        return

    arquivos = [
        f for f in os.listdir(pasta)
        if os.path.isfile(os.path.join(pasta, f))
    ]

    if not arquivos:
        print("Nenhum arquivo solto para organizar.")
        return

    movidos = 0
    for nome_arquivo in arquivos:
        caminho_origem = os.path.join(pasta, nome_arquivo)
        _, extensao = os.path.splitext(nome_arquivo)
        categoria = categoria_do_arquivo(extensao)

        pasta_destino = os.path.join(pasta, categoria)
        caminho_destino = os.path.join(pasta_destino, nome_arquivo)

        if simular:
            print(f"[SIMULAÇÃO] {nome_arquivo} -> {categoria}/")
            continue

        os.makedirs(pasta_destino, exist_ok=True)
        shutil.move(caminho_origem, caminho_destino)
        print(f"{nome_arquivo} -> {categoria}/")
        movidos += 1

    if not simular:
        print(f"\n{movidos} arquivo(s) organizado(s) em '{pasta}'.")


if __name__ == "__main__":
    pasta_alvo = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()

    print(f"Pasta selecionada: {pasta_alvo}")
    confirmacao = input("Simular antes de mover de verdade? (s/n): ").strip().lower()

    if confirmacao == "s":
        organizar(pasta_alvo, simular=True)
        seguir = input("\nExecutar de verdade agora? (s/n): ").strip().lower()
        if seguir == "s":
            organizar(pasta_alvo, simular=False)
    else:
        organizar(pasta_alvo, simular=False)
