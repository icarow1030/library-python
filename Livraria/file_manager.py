import csv
import os
import shutil
import database_manager as db
from datetime import datetime
from pathlib import Path

class FileManager:
        
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)
        self.exports_dir = self.base_dir / 'exports'

    def backup(self):
        backup_dir = Path('backups')

        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)

        backup_filename = f"backup{datetime.now().strftime('%Y%m%d_%H%M%S')}.db" # nome do arquivo com a data
        backup_filepath = os.path.join(backup_dir, backup_filename)

        shutil.copy(db.data_path, backup_filepath) # shutil copia arquivos

        backups = sorted(os.listdir(backup_dir)) # listdir lista todos os arquivos no diretório - colocar sorted pra garantir q estejam
        # na ordem certa

        if len(backups) > 5: # verifica se tem mais de 5 backups
            for old_backup in backups[:-5]: # recorta a partir do último da lista (mais recente) até o 6º
                os.remove(os.path.join(backup_dir, old_backup)) # remove os arquivos antigos
        print('Backup realizado com sucesso!')

    def exportar_csv(self, books):
        csv_file = self.exports_dir / 'livros_exportados.csv'
        with csv_file.open('w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Título', 'Autor', 'Ano de Publicação', 'Preço'])
            writer.writerows(books)
        print(f"Dados exportados para {csv_file}")

    def import_from_csv(self, csv_file, db):
        csv_path = self.exports_dir / csv_file
        if not csv_path.exists():
            print(f"Arquivo {csv_file} não encontrado.")
            return

        with csv_path.open('r') as file:
            reader = csv.reader(file)
            next(reader)  # Pular o cabeçalho deu erro no BACKUP
            for row in reader:
                _, titulo, autor, ano_publicacao, preco = row
                db.add_book(titulo, autor, int(ano_publicacao), float(preco))
        print(f"Dados importados de {csv_file}")