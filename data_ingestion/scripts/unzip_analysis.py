import os
import re
from datetime import datetime

LOG_FILE = "../unzipped/unzip_log.txt"

def parse_log_file(log_path):
    if not os.path.exists(log_path):
        print(f"❌ Arquivo de log não encontrado: {log_path}")
        return

    extracted_count = 0
    corrupted_count = 0
    io_error_count = 0
    unexpected_error_count = 0
    start_time = None
    end_time = None

    with open(log_path, "r", encoding="utf-8") as f:
        for line in f:
            # Verifica o início do processo
            if "Iniciando processo de extração" in line:
                timestamp_str = line.split(']')[0].strip('[')
                start_time = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")

            # Verifica o fim do processo
            elif "Processo de extração finalizado" in line:
                timestamp_str = line.split(']')[0].strip('[')
                end_time = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")

            # Conta arquivos extraídos com sucesso
            elif "✅ Extração concluída" in line:
                extracted_count += 1

            # Conta arquivos corrompidos
            elif "❌ ERRO: Arquivo ZIP corrompido" in line:
                corrupted_count += 1

            # Conta erros de I/O
            elif "❌ ERRO: Falha de I/O" in line:
                io_error_count += 1

            # Conta erros inesperados
            elif "❌ ERRO inesperado" in line:
                unexpected_error_count += 1

    print("\n📊 Análise do Log de Extração:")
    print(f"Total de arquivos extraídos com sucesso: {extracted_count}")
    print(f"Total de arquivos ZIP corrompidos: {corrupted_count}")
    print(f"Total de erros de I/O (ex: falta de espaço em disco): {io_error_count}")
    print(f"Total de erros inesperados: {unexpected_error_count}")

    if start_time and end_time:
        duration = end_time - start_time
        print(f"Tempo total de execução: {duration}")
    else:
        print("⚠️ Não foi possível calcular o tempo total (início ou fim não encontrado no log).")

if __name__ == "__main__":
    parse_log_file(LOG_FILE)
