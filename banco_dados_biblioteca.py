"""
Banco de Dados - Biblioteca
-----------------------------
Modelagem, consultas e gerenciamento de informações usando SQLite
(banco de dados embutido, não precisa instalar servidor nenhum).

Tabela: livros (id, titulo, autor, ano, lido)
"""

import sqlite3

BANCO = "biblioteca.db"


def conectar():
    return sqlite3.connect(BANCO)


def criar_tabela():
    with conectar() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS livros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                ano INTEGER,
                lido INTEGER DEFAULT 0
            )
        """)


def adicionar_livro(titulo, autor, ano, lido=False):
    with conectar() as conn:
        conn.execute(
            "INSERT INTO livros (titulo, autor, ano, lido) VALUES (?, ?, ?, ?)",
            (titulo, autor, ano, int(lido)),
        )


def listar_livros():
    with conectar() as conn:
        cursor = conn.execute("SELECT id, titulo, autor, ano, lido FROM livros")
        return cursor.fetchall()


def buscar_por_autor(autor):
    with conectar() as conn:
        cursor = conn.execute(
            "SELECT id, titulo, autor, ano, lido FROM livros WHERE autor LIKE ?",
            (f"%{autor}%",),
        )
        return cursor.fetchall()


def marcar_como_lido(id_livro):
    with conectar() as conn:
        conn.execute("UPDATE livros SET lido = 1 WHERE id = ?", (id_livro,))


def remover_livro(id_livro):
    with conectar() as conn:
        conn.execute("DELETE FROM livros WHERE id = ?", (id_livro,))


def imprimir_livros(livros):
    if not livros:
        print("Nenhum livro encontrado.\n")
        return
    print(f"\n{'ID':<4}{'Título':<25}{'Autor':<20}{'Ano':<6}{'Lido'}")
    print("-" * 60)
    for id_, titulo, autor, ano, lido in livros:
        status = "Sim" if lido else "Não"
        print(f"{id_:<4}{titulo:<25}{autor:<20}{ano or '-':<6}{status}")
    print()


def menu():
    criar_tabela()

    while True:
        print("=== Banco de Dados - Biblioteca ===")
        print("1. Adicionar livro")
        print("2. Listar todos os livros")
        print("3. Buscar por autor")
        print("4. Marcar livro como lido")
        print("5. Remover livro")
        print("0. Sair")

        escolha = input("\nEscolha uma opção: ").strip()

        if escolha == "1":
            titulo = input("Título: ").strip()
            autor = input("Autor: ").strip()
            ano = input("Ano (opcional): ").strip()
            adicionar_livro(titulo, autor, int(ano) if ano.isdigit() else None)
            print("\nLivro adicionado.\n")

        elif escolha == "2":
            imprimir_livros(listar_livros())

        elif escolha == "3":
            autor = input("Nome do autor: ").strip()
            imprimir_livros(buscar_por_autor(autor))

        elif escolha == "4":
            id_livro = input("ID do livro: ").strip()
            if id_livro.isdigit():
                marcar_como_lido(int(id_livro))
                print("\nLivro marcado como lido.\n")

        elif escolha == "5":
            id_livro = input("ID do livro: ").strip()
            if id_livro.isdigit():
                remover_livro(int(id_livro))
                print("\nLivro removido.\n")

        elif escolha == "0":
            print("Até mais!")
            break

        else:
            print("\nOpção inválida.\n")


if __name__ == "__main__":
    menu()
