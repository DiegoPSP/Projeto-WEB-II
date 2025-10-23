# 🚀 Sistema de Gestão de Tarefas (Projeto Acadêmico)

Este é um projeto acadêmico completo desenvolvido para a disciplina de Projeto Web II. Trata-se de um sistema web para gerenciamento de tarefas (task manager) construído com o framework Django.

O sistema permite que usuários **Administradores** (`is_staff`) criem projetos, categorias e tarefas, associando imagens a elas. Usuários comuns (**Colaboradores**) podem se registrar, visualizar as tarefas abertas, se inscrever nelas e, por fim, marcá-las como "Concluídas".

O projeto utiliza um tema escuro e é totalmente responsivo, graças ao **Bootstrap 5**, e implementa interatividade assíncrona com **HTMX** para inscrições.

## ✨ Funcionalidades Principais

Este projeto cumpre todos os requisitos obrigatórios da disciplina:

* **Modelo Relacional (5 Classes):** O sistema é construído sobre 5 modelos Django que se relacionam: `Projeto`, `Categoria`, `Tarefa`, `Inscricao` e `Comentario`.
* **CRUD Completo (Admin):** Administradores (`is_staff`) podem Criar, Ler, Atualizar e Excluir todas as Tarefas, Projetos e Categorias através do painel de admin ou do `/admin/` do Django.
* **Sistema de Autenticação:** Sistema completo de Login, Registro e Logout de usuários, com separação de permissões entre usuários comuns (colaboradores) e administradores (`is_staff`).
* **Paginação:** A lista principal de tarefas é paginada.
* **Estilização com Bootstrap:** A interface é totalmente responsiva e utiliza componentes do Bootstrap 5 (Navbar, Cards, Forms, Badges) com um tema escuro.
* **Inscrição em Tarefas:** Usuários podem se inscrever em tarefas que estão com o status "Aberta".
* **Conclusão de Tarefas:** Usuários que estão inscritos em uma tarefa podem marcá-la como "Concluída".

## 🚀 Desafios Extras Implementados

O projeto também implementa com sucesso os desafios opcionais:

* **Upload de Imagens:** Administradores podem associar uma imagem de capa a cada tarefa no momento da criação ou edição.
* **Atualizações Assíncronas (HTMX):** O botão "Inscrever-se" utiliza HTMX para registrar a inscrição e atualizar a interface do usuário (mostrando "Inscrito com sucesso!") sem a necessidade de recarregar a página.
* **Projeto no GitHub:** O projeto está documentado e disponível neste repositório.

## 🛠️ Tecnologias Utilizadas

* **Backend:** Python 3, Django 5.x
* **Frontend:** HTML5, Bootstrap 5.3
* **Interatividade:** HTMX
* **Banco de Dados:** SQLite 3 (padrão de desenvolvimento)
* **Imagens:** Pillow (para `ImageField`)

## 🗂️ Modelo Relacional (Estrutura do Banco)

O diagrama abaixo (renderizado pelo GitHub) representa as 5 classes customizadas (+ a classe `User` do Django) e suas inter-relações:

```mermaid
erDiagram
    User ||--o{ Projeto : "cria (criador)"
    User ||--o{ Tarefa : "cria (criador)"
    User ||--o{ Comentario : "escreve (autor)"
    User ||--o{ Inscricao : "realiza (colaborador)"

    Projeto }o--|| Tarefa : "contém (1-N)"
    Categoria }o--|| Tarefa : "classifica (1-N)"

    Tarefa ||--o{ Inscricao : "possui (1-N)"
    Tarefa ||--o{ Comentario : "recebe (1-N)"