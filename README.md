# Atividade Prática 02 - Biblioteca Persistente

Complete os arquivos da base usando SQLAlchemy ORM.

## Como executar

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

## Defesa escrita

Responda ao final:

1. Para que serve o campo `disponivel` em `Livro`?
O campo disponível serve para verificar se o livro está disponível, assim, verificando a disponibilidade para que o usuário possa emprestá-lo ou devolvê-lo.

2. Por que é necessário chamar `session.commit()` após emprestar ou devolver?
Porque é necessário que haja a modificação no banco de dados da coluna "disponivel", assim, modificando esse campo para True ou False de acordo com a ação.

3. Em qual consulta você usa o relacionamento entre `Livro` e `Autor`?
Na consulta "listar_livros_por_autor", onde os livros são acessado de acordo com a presença em autor.livros que é salvo por meio do relationship.
