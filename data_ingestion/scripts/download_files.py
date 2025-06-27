import os
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://arquivos.receitafederal.gov.br/dados/cnpj/dados_abertos_cnpj/"
RAW_DATA_DIR = "../raw_data/"
LOG_FILE = "../raw_data/downloaded_files.log"

def read_downloaded_log():
    if not os.path.exists(LOG_FILE):
        return set()
    with open(LOG_FILE, "r") as f:
        return set(line.strip() for line in f.readlines())

def write_downloaded_log(file_path):
    with open(LOG_FILE, "a") as f:
        f.write(file_path + "\n")

def download_files():
    downloaded_files = read_downloaded_log()

    folders = [
        "2023-05", "2023-06", "2023-07", "2023-08", "2023-09", "2023-10", "2023-11", "2023-12",
        "2024-01", "2024-02", "2024-03", "2024-04", "2024-05", "2024-06", "2024-07", "2024-08",
        "2024-09", "2024-10", "2024-11", "2024-12", "2025-01", "2025-02", "2025-03", "2025-04",
        "2025-05", "2025-06"
    ]

    for folder in folders:
        print(f"\n📂 Acessando pasta: {folder}/")
        url = BASE_URL + folder + "/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        for link in soup.find_all("a"):
            href = link.get("href")
            if href and href.endswith(".zip"):
                # Construir o caminho relativo com a subpasta para log
                file_relative_path = os.path.join(folder, href)

                if file_relative_path in downloaded_files:
                    print(f"✅ Já baixado: {file_relative_path} — pulando...")
                    continue

                file_url = url + href
                print(f"Baixando: {file_url}")

                r = requests.get(file_url)
                if r.status_code == 200:
                    # Criar pasta do mês se não existir
                    folder_path = os.path.join(RAW_DATA_DIR, folder)
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)

                    file_path = os.path.join(folder_path, href)
                    with open(file_path, "wb") as f:
                        f.write(r.content)

                    print(f"Download concluído: {file_path}")
                    write_downloaded_log(file_relative_path)
                else:
                    print(f"❌ Erro ao baixar {file_url} (status {r.status_code})")

if __name__ == "__main__":
    download_files()
