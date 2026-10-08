from sqlalchemy import select

from models import Autor, Livro


def listar_livros(session):
    """Liste todos os livros com o nome do autor e o status de disponibilidade."""
    livros = session.scalars(select(Livro)).all()
    for livro in livros:
        if livro.disponivel:
            status = "Disponível"
        else:
            status = "Indisponível"

        print (f"Livro: {livro.titulo}, Autor: {livro.autor.nome}, Status: {status}")


def listar_livros_disponiveis(session):
    """Liste apenas os livros disponíveis."""
    livros = session.scalars(select(Livro).where(Livro.disponivel==True)).all()

    for livro in livros:
        if livro.disponivel:
            status = "Disponível"
        else:
            status = "Indisponível"
        print(f"Livro: {livro.titulo}, Status: {status}")


def buscar_livros_por_titulo(session, trecho):
    """Busque livros por parte do título."""
    livros = session.scalars(select(Livro).where(Livro.titulo.like(f"%{trecho}%"))).all()

    for livro in livros:
        if livro.disponivel:
            status = "Disponível"
        else:
            status = "Indisponível"
        
        print(f"Livro: {livro.titulo}, Status: {status}")


def listar_livros_por_autor(session, nome_autor):
    """Liste os livros de um autor informado pelo nome."""
    autores = session.scalars(select(Autor).where(Autor.nome==nome_autor))
    for autor in autores:
        for livro in autor.livros:
            print(f"Livro: {livro.titulo}")
