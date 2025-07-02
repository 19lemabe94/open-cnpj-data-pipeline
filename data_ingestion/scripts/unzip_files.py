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

    for file_name in os.listdir(raw_dir):
        if file_name.endswith(".zip"):
            zip_path = os.path.join(raw_dir, file_name)
            target_folder = os.path.join(dest_dir, os.path.splitext(file_name)[0])

            log(f"🔓 Extraindo: {file_name} para {target_folder}")

            try:
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)

                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(target_folder)

                log(f"✅ Extração concluída: {file_name}")

                # Opcional: excluir o zip após extração bem-sucedida
                # os.remove(zip_path)

            except zipfile.BadZipFile:
                log(f"❌ ERRO: Arquivo ZIP corrompido: {file_name}")

            except OSError as e:
                log(f"❌ ERRO: Falha de I/O ao extrair {file_name}: {str(e)}")

            except Exception as e:
                log(f"❌ ERRO inesperado ao extrair {file_name}: {str(e)}")

    log("🏁 Processo de extração finalizado.")

if __name__ == "__main__":
    unzip_all_files(RAW_DATA_DIR, UNZIPPED_DIR)
