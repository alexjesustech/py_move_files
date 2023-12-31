import os


def excluir_arquivos(pasta: str, extensao: str):
    """Exclui todos os arquivos com uma determinada extensão na pasta especificada e suas subpastas.

    Args:
        pasta (str): caminho para a pasta onde os arquivos serão pesquisados
        extensao (str): extensão dos arquivos a serem excluídos

    Returns:
        None

    """
    for item in os.listdir(pasta):
        item_caminho = os.path.join(pasta, item)

        if os.path.isfile(item_caminho) and item_caminho.lower().endswith(extensao):
            os.remove(item_caminho)
            print(item_caminho)
        elif os.path.isdir(item_caminho):
            excluir_arquivos(item_caminho, extensao)  # Chama a função recursivamente para subpastas


if __name__ == "__main__":
    pasta_imagens = os.path.join(os.path.expanduser("~"), "OneDrive\\google_backup_cloud")
    # print(pasta_imagens)
    excluir_arquivos(pasta_imagens, ".FR12")
