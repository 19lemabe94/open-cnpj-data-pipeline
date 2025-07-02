import os
import zipfile
from datetime import datetime

# Diretórios de origem (onde estão os ZIPs) e destino (onde ficará o conteúdo extraído)
RAW_DATA_DIR = "../raw_data/"
UNZIPPED_DIR = "../unzipped/"
LOG_FILE = os.path.join(UNZIPPED_DIR, "unzip_log.txt")  # Caminho do arquivo de log

# Função para registrar mensagens no log e também imprimir no console
def log(message):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    full_message = f"{timestamp} {message}"
    print(full_message)

    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(full_message + "\n")

# Função principal para extrair todos os ZIPs
def unzip_all_files(raw_dir, dest_dir):
    # Criar diretório de destino se não existir
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    log("🚀 Iniciando processo de extração dos arquivos ZIP...")

    # Percorre todos os subdiretórios (mês a mês, igual o download)
    for root, dirs, files in os.walk(raw_dir):
        for file_name in files:
            if file_name.endswith(".zip"):
                zip_path = os.path.join(root, file_name)

                # Mantém a mesma estrutura de pastas do RAW_DATA_DIR dentro de UNZIPPED_DIR
                relative_folder = os.path.relpath(root, raw_dir)
                target_folder = os.path.join(dest_dir, relative_folder, os.path.splitext(file_name)[0])

                log(f"🔓 Extraindo: {file_name} para {target_folder}")

                try:
                    # Cria a pasta de destino se ainda não existir
                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)

                    # Faz a extração
                    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                        zip_ref.extractall(target_folder)

                    # Renomeia o CSV extraído
                    for extracted_file in os.listdir(target_folder):
                        if extracted_file.endswith(".csv"):
                            old_csv_path = os.path.join(target_folder, extracted_file)
                            new_csv_name = f"{os.path.splitext(file_name)[0]}.csv"
                            new_csv_path = os.path.join(target_folder, new_csv_name)
                            os.rename(old_csv_path, new_csv_path)
                            log(f"📄 CSV renomeado: {extracted_file} ➡️ {new_csv_name}")
                            break  # Só renomeia o primeiro CSV encontrado

                    log(f"✅ Extração concluída: {file_name}")

                    # Remove o ZIP original após a extração
                    os.remove(zip_path)
                    log(f"🗑️ ZIP deletado: {file_name}")

                except zipfile.BadZipFile:
                    log(f"❌ ERRO: Arquivo ZIP corrompido: {file_name}")

    log("🏁 Processo de extração finalizado.")

# Execução direta (quando rodar o script)
if __name__ == "__main__":
    unzip_all_files(RAW_DATA_DIR, UNZIPPED_DIR)
