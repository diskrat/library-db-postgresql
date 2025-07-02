-- init.sql

CREATE TABLE aluno (
    matricula INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    curso TEXT NOT NULL
);

CREATE TABLE livro (
    codigo INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    editora TEXT NOT NULL,
    ano INTEGER NOT NULL
);

CREATE TABLE exemplar (
    tombo INTEGER PRIMARY KEY,
    codigo_livro INTEGER NOT NULL REFERENCES livro(codigo)
);

CREATE TABLE emprestimo (
    codigo INTEGER PRIMARY KEY,
    data_emprestimo DATE NOT NULL,
    data_prev_dev DATE NOT NULL,
    matricula_aluno INTEGER NOT NULL REFERENCES aluno(matricula)
);

CREATE TABLE empr_exemplar (
    codigo_emprestimo INTEGER NOT NULL REFERENCES emprestimo(codigo),
    tombo_exemplar INTEGER NOT NULL REFERENCES exemplar(tombo),
    data_devolucao DATE,
    dias_atraso INTEGER
);
