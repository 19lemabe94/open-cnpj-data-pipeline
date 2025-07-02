import os
from datetime import datetime

LOG_FILE = "../unzipped/unzip_log.txt"

def parse_log_file(log_file):
    extracted = 0
    errors = 0
    start_time = None
    end_time = None

    with open(log_file, "r", encoding="utf-8") as f:
        for line in f:
            # Captura o timestamp
            timestamp_str = line.split(']')[0].strip('[')
            try:
                timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
                if not start_time:
                    start_time = timestamp
                end_time = timestamp
            except ValueError:
                continue  # Se alguma linha estiver fora do formato, ignora.

            # Contagem de sucesso
            if "✅ Extração concluída:" in line:
                extracted += 1

            # Contagem de erro
            if "❌ ERRO: Arquivo ZIP corrompido:" in line:
                errors += 1

    return extracted, errors, start_time, end_time

def analyze_unzip_log():
    if not os.path.exists(LOG_FILE):
        print("❌ Log de extração não encontrado!")
        return

    extracted, errors, start_time, end_time = parse_log_file(LOG_FILE)

    print("\n📊 Análise do Log de Extração 📊")
    print(f"✅ Arquivos extraídos com sucesso: {extracted}")
    print(f"❌ Arquivos com erro (corrompidos): {errors}")

    if start_time and end_time:
        total_time = end_time - start_time
        print(f"⏱️ Tempo total de execução: {total_time}")
    else:
        print("⚠️ Não foi possível calcular o tempo total (timestamps ausentes ou mal formatados).")

if __name__ == "__main__":
    analyze_unzip_log()
