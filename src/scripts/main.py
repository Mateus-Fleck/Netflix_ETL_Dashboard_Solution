# Importar bibliotecas necessárias para o projeto
# import libraries required for the project

import pandas as pd
import os
import glob

# Criar uma variável para armazenar o caminho da pasta data raw.
# Create a variable to store the path of the data raw folder.
folder_path = 'src/data/raw'

# Criar uma lista com todos os arquivos do diretorio.
# Create a list with all files from the directory.
excel_files = glob.glob(os.path.join(folder_path, '*.xlsx'))

if not excel_files:
    print("Nenhum arquivo compatível encontrado")  # Validação / Validation
else:

    # dataframe = tabela na memoria para guardar os conteúdos dos arquivos.
    # dataframe = table in memory to store the contents of the files.
    dfs = []
    
    # ler todos os arquivos do diretorio
    # read all files from the directory
    for excel_file in excel_files:
        try:
            # ler o arquivo excel
            # read the excel file
            df_temp = pd.read_excel(excel_file)

            # Pegar o nome do arquivo
            # Get the file name
            file_name = os.path.basename(excel_file)

            # Crie uma nova coluna chamada filename com o nome do arquivo
            # Create new column called filename with the file name
            df_temp['filename'] = file_name

            # Crie uma nova coluna chamada location com nome do país
            # Create a new column called location with the name of the country
            if 'brasil' in file_name.lower():
                df_temp['location'] = 'Brasil'
            elif 'france' in file_name.lower():
                df_temp['location'] = 'França '
            elif 'italian' in file_name.lower():
                df_temp['location'] = 'Itália'

            # Crie uma nova coluna chamada campanha com nome de cada campanha por lead.
            # Create a new column called campaign com nome de cada campanha por lead.
            df_temp['campaign'] = df_temp['utm_link'].str.extract(r'utm_campaign=(.*)')

            # Guarda dados tratados dentro de um dataframe comum.
            # Store treated data within a common dataframe.
            dfs.append(df_temp)

        except Exception as e:
            print(f"Erro ao ler o arquivo {excel_file}: {e}") # Validação / Validation

if dfs:
    # Concatenar todos os dataframes
    # Concatenate all dataframes
    result = pd.concat(dfs, ignore_index=True)

    # Salvar o dataframe em um arquivo csv
    # Save the dataframe to a csv file
    output_file = os.path.join('src', 'data', 'ready', 'clean.xlsx')
    
    # Config motor de escrita de excel
    # Configure excel writing engine
    writer = pd.ExcelWriter(output_file, engine='xlsxwriter')

    # Leva os dados do resultado a ser escrito no motor de excel configurado
    # Take the data from the result to be written to the configured excel engine
    result.to_excel(writer, index=False)

    # Salva o arquivo de Excel
    # Save the Excel file
    writer._save()
    print("Arquivo salvo com sucesso!") # Validação / Validation
    
else:
    print("Nenhum arquivo encontrado.") # Validação / Validation