import csv
import os
from pathlib import Path
import database_manager as db
from file_manager  import FileManager 
opcao = 0

base_dir = Path(__file__).parent
backups_dir = base_dir / 'backups'
exports_dir = base_dir / 'exports'

for directory in [backups_dir, exports_dir]:
    os.makedirs(directory, exist_ok=True)

fm = FileManager(base_dir)

while opcao != 9:
    print('='*30)
    print('1. Adicionar novo livro')
    print('2. Exibir todos os livros')
    print('3. Atualizar preço de um livro')
    print('4. Remover um livro')
    print('5. Buscar livros por autor')
    print('6. Exportar dados para CSV')
    print('7. Importar dados de CSV')
    print('8. Fazer backup do banco de dados')
    print('9. Sair')
    opcao = int(input('Escolha:'))
    if(opcao > 9 or opcao < 0):
        print('Opção inválida')
    else:
        if opcao == 1:
            print('='*30)
            titulo = input('Informe o Titulo: ')
            autor = input('informe o Autor: ')
            ano = int(input('Informe o Ano de publicação'))
            preco = float(input('Informe o preço: '))
            db.add_book(titulo,autor,ano,preco)
            fm.backup()
        elif opcao == 2:
            print('='*30)
            print('Livros:\n')
            livros = db.show_all_books()
            for livro in livros:
                print(livro)
            print('\n')
            input('Pressione enter para continuar')
            print('\n'*10)
        elif opcao == 3:
            print('='*30)
            id_livro = int(input('Informe o ID do livro: '))
            novo_preco = float(input('Informe um novo preço: '))
            db.update_price(id_livro, novo_preco)
            print('Preço atualizado com sucesso!')
            fm.backup()
        elif opcao == 4:
            id = int(input('Informe o id do livro: '))
            db.remove_book(id)
            fm.backup()
        elif opcao == 5:
            autor = input('Informe o nome do autor: ')
            db.search_book_by_author(autor)
        elif opcao == 6:
            books = db.show_all_books()
            fm.exportar_csv(books)
            
        elif opcao == 7:
            csv_file = input('Informe o nome do arquivo a ser importado: ')
            fm.import_from_csv(csv_file, db)
            fm.backup()
            print('Arquivo importado com sucesso')
        elif opcao == 8:
            print('='*30)
            fm.backup()
        elif opcao == 9:
            print('Saindo...')
        
