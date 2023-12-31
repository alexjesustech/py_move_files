import os
import shutil


def mover_imagens(pasta_origem: str, pasta_destino: str) -> None:
    """
    Move todos os arquivos de imagem de uma pasta para outra, incluindo um pós-fixo e a contagem.

    Args:
        pasta_origem (str): Caminho da pasta de origem.
        pasta_destino (str): Caminho da pasta de destino.

    Returns:
        None: Nenhum retorno.

    """
    # Obtém todos os arquivos na pasta origem
    arquivos = os.listdir(pasta_origem)
    print(arquivos)

    # Percorre todos os arquivos
    for arquivo in arquivos:
        # Obtém o caminho completo do arquivo
        caminho_arquivo = os.path.join(pasta_origem, arquivo)
        print(caminho_arquivo)

        # Verifica se o arquivo é uma imagem
        if os.path.isfile(caminho_arquivo) and caminho_arquivo.lower().endswith(
                (".jpg", ".jpeg", ".png", ".gif", ".bmp")):
            print(caminho_arquivo)
            # Cria o nome do arquivo de destino
            nome_destino = arquivo
            contagem = 1
            while os.path.exists(os.path.join(pasta_destino, nome_destino)):
                nome_destino = f"({contagem})_{arquivo}"
                contagem += 1

            # Move o arquivo para a pasta destino
            print(f"Movendo {caminho_arquivo} para {os.path.join(pasta_destino, nome_destino)}")
            shutil.move(caminho_arquivo, os.path.join(pasta_destino, nome_destino))
        elif os.path.isdir(caminho_arquivo):
            mover_imagens(caminho_arquivo, pasta_destino)  # Chama a função recursivamente para subpastas


if __name__ == "__main__":
    print("Começou...")
    # Define a pasta origem
    pasta_origem = os.path.join(os.path.expanduser("~"), "OneDrive\\google_backup_cloud")
    print(pasta_origem)

    # Define a pasta destino
    pasta_destino = os.path.join(os.path.expanduser("~"), "OneDrive\\Imagens\\GoogleFotos")
    print(pasta_destino)

    # Move as imagens
    mover_imagens(pasta_origem, pasta_destino)
