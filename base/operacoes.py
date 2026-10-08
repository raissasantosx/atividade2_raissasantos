from sqlalchemy import select

from models import Livro


def emprestar_livro(session, titulo):
    """Marque um livro como indisponível."""
    # TODO: busque o livro pelo título.
    # TODO: se o livro não existir, exiba uma mensagem.
    # TODO: se já estiver indisponível, exiba uma mensagem.
    # TODO: se estiver disponível, altere disponivel para False e faça commit.

    livro = session.scalars(select(Livro).where(Livro.titulo==titulo)).first()

    if livro:
        if livro.disponivel:
            livro.disponivel = False
            session.commit()

            print("Livro emprestado com sucesso!")

        else:
            print("Livro indisponível!")

    else:
        print("Esse livro não existe!")


def devolver_livro(session, titulo):
    """Marque um livro como disponível."""
    # TODO: busque o livro pelo título.
    # TODO: se o livro não existir, exiba uma mensagem.
    # TODO: se já estiver disponível, exiba uma mensagem.
    # TODO: se estiver indisponível, altere disponivel para True e faça commit.

    livro = session.scalars(select(Livro).where(Livro.titulo==titulo)).first()
    
    if livro:
        if not livro.disponivel:
            livro.disponivel = True
            session.commit()

            print("Livro devolvido com sucesso!")

        else:
            print("Livro disponível!")

    else:
        print("Esse livro não existe!")