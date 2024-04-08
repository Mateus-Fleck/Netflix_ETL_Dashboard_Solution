import pandas as pd
import os
import glob

# criar uma variavel para armazenar o caminho da pasta data raw
folder_path = 'src\\data\\raw'

# criar uma lista com todos os arquivos do diretorio
excel_files = glob.glob(os.path.join(folder_path , '*.xlsx'))