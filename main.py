from datetime import date
from sqlalchemy.exc import OperationalError
from sqlalchemy import text
from db import SessionLocal
from services import aluno_service, livro_service, exemplar_service, emprestimo_service, emprestimo_exemplar_service

def main():
    db = SessionLocal()
    try:
        # Test the connection by executing a simple query
        db.execute(text("SELECT 1"))
        print("Conexão com o banco de dados bem-sucedida!")
    except OperationalError as e:
        print(f"Falha ao conectar com o banco de dados: {e}")
        return  # Exit if connection fails

    # Testando Aluno
    print("--- Testando Aluno ---")
    aluno_data = {"matricula": 2024001, "nome": "João da Silva", "email": "joao.silva@example.com", "curso": "Ciência da Computação"}
    novo_aluno = aluno_service.create_aluno(db, aluno_data)
    print(f"Aluno criado: {novo_aluno.nome}")

    # Testando Livro
    print("\n--- Testando Livro ---")
    livro_data = {"codigo": 1, "titulo": "Uma Breve História do Tempo", "autor": "Stephen Hawking", "editora": "Intrínseca", "ano": 2015}
    novo_livro = livro_service.create_livro(db, livro_data)
    print(f"Livro criado: {novo_livro.titulo}")

    # Testando Exemplar
    print("\n--- Testando Exemplar ---")
    exemplar_data = {"tombo": 1001, "codigo_livro": novo_livro.codigo}
    novo_exemplar = exemplar_service.create_exemplar(db, exemplar_data)
    print(f"Exemplar criado: Tombo {novo_exemplar.tombo} para o livro '{novo_livro.titulo}'")

    # Testando Emprestimo
    print("\n--- Testando Empréstimo ---")
    emprestimo_data = {
        "codigo": 5001,
        "data_emprestimo": date.today(),
        "data_prev_dev": date(2025, 7, 16),
        "matricula_aluno": novo_aluno.matricula
    }
    novo_emprestimo = emprestimo_service.create_emprestimo(db, emprestimo_data)
    print(f"Empréstimo criado: Código {novo_emprestimo.codigo} para o aluno '{novo_aluno.nome}'")

    # Testando EmprestimoExemplar
    print("\n--- Testando Empréstimo-Exemplar ---")
    emprestimo_exemplar_data = {
        "codigo_emprestimo": novo_emprestimo.codigo,
        "tombo_exemplar": novo_exemplar.tombo
    }
    novo_ee = emprestimo_exemplar_service.create_emprestimo_exemplar(db, emprestimo_exemplar_data)
    print(f"Relação Empréstimo-Exemplar criada.")

    # Deletando os dados
    print("\n--- Deletando dados ---")
    emprestimo_exemplar_service.delete_emprestimo_exemplar(db, novo_ee.codigo_emprestimo, novo_ee.tombo_exemplar)
    emprestimo_service.delete_emprestimo(db, novo_emprestimo.codigo)
    exemplar_service.delete_exemplar(db, novo_exemplar.tombo)
    livro_service.delete_livro(db, novo_livro.codigo)
    aluno_service.delete_aluno(db, novo_aluno.matricula)
    print("Dados de teste deletados.")

    db.close()

if __name__ == "__main__":
    main()
