import os
import pandas as pd

TABELAS = {
    'ABRIGADOS_EM_CANOAS_01.xlsx':'https://docs.google.com/spreadsheets/d/1-1q4c8Ns6M9noCEhQqBE6gy3FWUv-VQgeUO9c7szGIM/edit#gid=577467634',
    'NOMES_ABRIGOS_55.xlsx':'https://docs.google.com/spreadsheets/d/1eomOM6mQvYxLHbl9mYfaKjbUiz2Eqoe2QUl43wawTRE/edit#gid=1385089223',
    'RESGATADOS_ELDORADO_DO_SUL_05_DE_MAIO.xlsx':'https://docs.google.com/spreadsheets/d/1L04A8F3K9BZynRU_recfc9TO63YcVsor6HX9W1y4v24/edit#gid=0'
}
DIRETORIO = "listas"

def procurar_string_em_arquivos(string_especifica: str) -> list:
    global TABELAS
    info_strings_encontradas = []
    # Percorre todos os arquivos no diretório
    for arquivo in os.listdir(DIRETORIO):
        if arquivo.endswith(".xlsx"):
            caminho_arquivo = os.path.join(DIRETORIO, arquivo)
            # Abre o arquivo XLSX
            try:
                xls = pd.ExcelFile(caminho_arquivo)
                # Percorre todas as abas do arquivo XLSX
                for aba in xls.sheet_names:
                    df = pd.read_excel(xls, aba)
                    # Verifica se a string específica está presente em alguma célula do DataFrame
                    for index, row in df.iterrows():
                        if string_especifica.upper() in str(row).upper():
                            row['arquivo'] = arquivo
                            row['aba'] = aba
                            row['link'] = TABELAS[arquivo]
                            info_strings_encontradas.append(row.to_list())#.to_json()) # Index+2 para começar da linha 2 (considerando cabeçalho)
            except Exception as e:
                print(f"Erro ao ler o arquivo {arquivo}: {e}")

    return info_strings_encontradas