import os


def excluir_subpastas_vazias(pasta):
    """Exclui todas as subpastas vazias de uma pasta."""

    # Percorre todas as subpastas
    for subpasta in os.listdir(pasta):
        # Obtém o caminho completo da subpasta
        subpasta_caminho = os.path.join(pasta, subpasta)

        # Verifica se a subpasta é um diretório
        if os.path.isdir(subpasta_caminho):
            # Verifica se a subpasta está vazia
            if len(os.listdir(subpasta_caminho)) == 0:
                # Exclui a subpasta
                os.rmdir(subpasta_caminho)
                print(subpasta_caminho)
            elif os.path.isdir(subpasta_caminho):
                excluir_subpastas_vazias(subpasta_caminho)  # Chama a função recursivamente para subpastas


if __name__ == "__main__":
    # Define a pasta
    pasta = os.path.join(os.path.expanduser("~"), "OneDrive\\google_backup_cloud")

    # Exclui as subpastas vazias
    excluir_subpastas_vazias(pasta)
