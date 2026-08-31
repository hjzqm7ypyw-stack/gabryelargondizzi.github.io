"""
Sistema de Cadastro de Contatos
--------------------------------
CRUD simples (Criar, Ler, Atualizar, Deletar) que guarda os
contatos em um arquivo JSON local, sem precisar de banco de dados.
"""

import json
import os

ARQUIVO = "contatos.json"


def carregar_contatos():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_contatos(contatos):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(contatos, f, ensure_ascii=False, indent=2)


def proximo_id(contatos):
    if not contatos:
        return 1
    return max(c["id"] for c in contatos) + 1


def cadastrar(contatos):
    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()
    email = input("E-mail: ").strip()

    contato = {
        "id": proximo_id(contatos),
        "nome": nome,
        "telefone": telefone,
        "email": email,
    }
    contatos.append(contato)
    salvar_contatos(contatos)
    print(f"\nContato '{nome}' cadastrado com sucesso (id {contato['id']}).\n")


def listar(contatos):
    if not contatos:
        print("\nNenhum contato cadastrado.\n")
        return
    print("\nID  | Nome                 | Telefone       | E-mail")
    print("-" * 60)
    for c in contatos:
        print(f"{c['id']:<4}| {c['nome']:<21}| {c['telefone']:<15}| {c['email']}")
    print()


def buscar(contatos):
    termo = input("Buscar por nome: ").strip().lower()
    encontrados = [c for c in contatos if termo in c["nome"].lower()]
    if not encontrados:
        print("\nNenhum contato encontrado.\n")
        return
    for c in encontrados:
        print(f"\nID: {c['id']}\nNome: {c['nome']}\nTelefone: {c['telefone']}\nE-mail: {c['email']}\n")


def editar(contatos):
    try:
        id_busca = int(input("ID do contato a editar: "))
    except ValueError:
        print("\nID inválido.\n")
        return

    for c in contatos:
        if c["id"] == id_busca:
            print("Deixe em branco para manter o valor atual.")
            nome = input(f"Nome [{c['nome']}]: ").strip()
            telefone = input(f"Telefone [{c['telefone']}]: ").strip()
            email = input(f"E-mail [{c['email']}]: ").strip()

            if nome:
                c["nome"] = nome
            if telefone:
                c["telefone"] = telefone
            if email:
                c["email"] = email

            salvar_contatos(contatos)
            print("\nContato atualizado.\n")
            return

    print("\nContato não encontrado.\n")


def remover(contatos):
    try:
        id_busca = int(input("ID do contato a remover: "))
    except ValueError:
        print("\nID inválido.\n")
        return

    for c in contatos:
        if c["id"] == id_busca:
            confirmacao = input(f"Remover '{c['nome']}'? (s/n): ").strip().lower()
            if confirmacao == "s":
                contatos.remove(c)
                salvar_contatos(contatos)
                print("\nContato removido.\n")
            return

    print("\nContato não encontrado.\n")


def menu():
    contatos = carregar_contatos()

    opcoes = {
        "1": ("Cadastrar contato", cadastrar),
        "2": ("Listar contatos", listar),
        "3": ("Buscar contato", buscar),
        "4": ("Editar contato", editar),
        "5": ("Remover contato", remover),
    }

    while True:
        print("=== Sistema de Cadastro de Contatos ===")
        for chave, (texto, _) in opcoes.items():
            print(f"{chave}. {texto}")
        print("0. Sair")

        escolha = input("\nEscolha uma opção: ").strip()

        if escolha == "0":
            print("Até mais!")
            break
        elif escolha in opcoes:
            _, funcao = opcoes[escolha]
            funcao(contatos)
        else:
            print("\nOpção inválida.\n")


if __name__ == "__main__":
    menu()
