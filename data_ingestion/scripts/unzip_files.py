import os
import zipfile
from datetime import datetime

RAW_DATA_DIR = "../raw_data/"
UNZIPPED_DIR = "../unzipped/"
LOG_FILE = os.path.join(UNZIPPED_DIR, "unzip_log.txt")

def log(message):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    full_message = f"{timestamp} {message}"
    print(full_message)
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(full_message + "\n")

def unzip_all_files(raw_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    log("🚀 Iniciando processo de extração dos arquivos ZIP...")

    # Percorre todas as subpastas e arquivos
    for root, _, files in os.walk(raw_dir):
        for file_name in files:
            if file_name.endswith(".zip"):
                zip_path = os.path.join(root, file_name)

                # Gera o caminho relativo da pasta onde está o ZIP dentro de raw_data
                relative_path = os.path.relpath(root, raw_dir)

                # Cria a mesma estrutura dentro de dest_dir
                target_folder = os.path.join(dest_dir, relative_path, os.path.splitext(file_name)[0])

                log(f"🔓 Extraindo: {zip_path} para {target_folder}")

                try:
                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)

                    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                        zip_ref.extractall(target_folder)

                    # Renomeia o CSV
                    for extracted_file in os.listdir(target_folder):
                        if extracted_file.endswith(".csv"):
                            old_path = os.path.join(target_folder, extracted_file)
                            new_name = os.path.splitext(file_name)[0] + ".csv"
                            new_path = os.path.join(target_folder, new_name)

                            if old_path != new_path:
                                os.rename(old_path, new_path)
                                log(f"🔄 Renomeado: {extracted_file} → {new_name}")

                    log(f"✅ Extração concluída: {file_name}")

                except zipfile.BadZipFile:
                    log(f"❌ ERRO: Arquivo ZIP corrompido: {file_name}")

    log("🏁 Processo de extração finalizado.")

if __name__ == "__main__":
    unzip_all_files(RAW_DATA_DIR, UNZIPPED_DIR)
