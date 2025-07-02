import os
import requests

# Caminhos dos diretórios e log
RAW_DATA_DIR = "../raw_data/"
UNZIP_LOG_FILE = "../unzipped/unzip_log.txt"
BASE_URL = "https://arquivos.receitafederal.gov.br/dados/cnpj/dados_abertos_cnpj/"

def get_failed_files():
    failed_files = []
    with open(UNZIP_LOG_FILE, "r", encoding="utf-8") as log_file:
        for line in log_file:
            # Ajuste aqui o critério de erro, pode ser só 'ERRO' ou algo mais específico
            if "❌ ERRO" in line or "BadZipFile" in line:
                # Exemplo de linha de log: "[data] ❌ ERRO: Arquivo ZIP corrompido: 2023-08/Empresas.zip"
                parts = line.strip().split(":")
                if len(parts) >= 2:
                    zip_file_name = parts[-1].strip()
                    failed_files.append(zip_file_name)
    return failed_files

def re_download_files(failed_files):
    for relative_zip_path in failed_files:
        # Exemplo: relative_zip_path = "2023-08/Empresas.zip"
        folder, zip_file = os.path.split(relative_zip_path)
        file_url = BASE_URL + folder + "/" + zip_file
        local_folder = os.path.join(RAW_DATA_DIR, folder)

        print(f"🔁 Re-baixando: {file_url}")

        try:
            response = requests.get(file_url)
            if response.status_code == 200:
                # Criar pasta se não existir
                if not os.path.exists(local_folder):
                    os.makedirs(local_folder)

                file_path = os.path.join(local_folder, zip_file)
                with open(file_path, "wb") as f:
                    f.write(response.content)
                print(f"✅ Download refeito: {file_path}")
            else:
                print(f"❌ Erro ao rebaixar {file_url} (status {response.status_code})")
        except Exception as e:
            print(f"❌ Falha ao tentar rebaixar {file_url} - Erro: {e}")

if __name__ == "__main__":
    failed_files = get_failed_files()
    if failed_files:
        print(f"\n🚨 Arquivos com erro encontrados no log: {failed_files}\n")
        re_download_files(failed_files)
    else:
        print("✅ Nenhum arquivo com erro encontrado no log.")
