import os
import zipfile

RAW_DATA_DIR = "../raw_data/"
UNZIPPED_DIR = "../unzipped/"

def unzip_all_files(raw_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for file_name in os.listdir(raw_dir):
        if file_name.endswith(".zip"):
            zip_path = os.path.join(raw_dir, file_name)
            target_folder = os.path.join(dest_dir, os.path.splitext(file_name)[0])

            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            print(f"🔓 Extraindo: {file_name} para {target_folder}")
            try:
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(target_folder)
                print(f"✅ Extração concluída: {file_name}")
            except zipfile.BadZipFile:
                print(f"❌ ERRO: Arquivo ZIP corrompido: {file_name}")

if __name__ == "__main__":
    unzip_all_files(RAW_DATA_DIR, UNZIPPED_DIR)
