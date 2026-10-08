from models import Autor, Livro


def popular_banco(session):
    """Cadastre autores e livros iniciais para testar a aplicação."""

    novo_autor1 = Autor(nome="Romerito", pais="Brasil")
    novo_autor2 = Autor(nome="Lucas", pais="Estados Unidos")
    novo_autor3 = Autor(nome="Brenda", pais="Espanha")

    novo_livro1 = Livro(titulo="Matemática", ano=2026, autor_id=2, disponivel=True)
    novo_livro2 = Livro(titulo="Português", ano=2000, autor_id=3, disponivel=False)
    novo_livro3 = Livro(titulo="Flask", ano=1900, autor_id=1, disponivel=True)
    novo_livro4 = Livro(titulo="SQLAlchemy", ano=2076, autor_id=1, disponivel=True)
    novo_livro5 = Livro(titulo="Magia", ano=1800, autor_id=3, disponivel=False)
    novo_livro6 = Livro(titulo="Como tirar nota alta?", ano=2027, autor_id=2, disponivel=True)

    session.add_all([novo_autor1, novo_autor2, novo_autor3, novo_livro1, novo_livro2, novo_livro3, novo_livro4, novo_livro5, novo_livro6])

    session.commit()