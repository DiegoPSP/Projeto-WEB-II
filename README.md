# 🚀 Sistema de Gestão de Tarefas (Projeto Acadêmico)

Este é um projeto acadêmico completo desenvolvido para a disciplina de Projeto Web II. Trata-se de um sistema web para gerenciamento de tarefas (task manager) construído com o framework Django.

O sistema permite que usuários **Administradores** (`is_staff`) criem projetos, categorias e tarefas, associando imagens a elas. Usuários comuns (**Colaboradores**) podem se registrar, visualizar as tarefas abertas, se inscrever nelas e, por fim, marcá-las como "Concluídas".

O projeto utiliza um tema escuro e é totalmente responsivo, graças ao **Bootstrap 5**, e implementa interatividade assíncrona com **HTMX** para inscrições.

## 📸 Screenshots

| Página Principal (Listagem) | Detalhes da Tarefa (com Imagem) |
| :---: | :---: |
| ![Placeholder da Página Principal](https://placehold.co/600x400/212529/dee2e6?text=Página+Principal) | ![Placeholder dos Detalhes da Tarefa](https://placehold.co/600x400/212529/dee2e6?text=Detalhes+da+Tarefa) |
| **Painel Administrativo** | **Formulário de Edição** |
| ![Placeholder do Painel Admin](https://placehold.co/600x400/212529/dee2e6?text=Painel+Admin) | ![Placeholder do Formulário de Edição](https://placehold.co/600x400/212529/dee2e6?text=Formulário+Editar) |

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

## 🗂️ Estrutura do Banco de Dados (Modelos)

1.  **`Projeto`**: Agrupador principal de tarefas (Ex: "Website", "App Mobile").
2.  **`Categoria`**: Tipo de tarefa (Ex: "Bug", "Design", "Documentação").
3.  **`Tarefa`**: A tarefa em si. Relaciona-se com `Projeto`, `Categoria` e `User` (criador).
4.  **`Inscricao`**: Tabela-pivô que liga um `User` (colaborador) a uma `Tarefa`.
5.  **`Comentario`**: Permite que um `User` (autor) comente em uma `Tarefa`.

## 🏁 Como Rodar o Projeto Localmente

**Pré-requisitos:** Python 3.10+ e Git instalados.

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
    cd SEU_REPOSITORIO
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # (Para Mac/Linux)
    python3 -m venv venv
    source venv/bin/activate
    
    # (Para Windows)
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    (Este projeto requer Django e Pillow para o upload de imagens)
    ```bash
    pip install django pillow
    ```

4.  **Crie as migrações do banco de dados:**
    ```bash
    python manage.py makemigrations projeto_webII_app
    python manage.py migrate
    ```

5.  **Crie um superusuário (Admin):**
    ```bash
    python manage.py createsuperuser
    ```
    (Siga as instruções para criar seu usuário `admin`)

6.  **Rode o servidor:**
    ```bash
    python manage.py runserver
    ```

7.  **Acesse o site:**
    Abra seu navegador e acesse `http://127.0.0.1:8000/`

8.  **(IMPORTANTE) Crie os dados iniciais:**
    * Acesse o painel de admin: `http://127.0.0.1:8000/admin/`
    * Crie algumas **Categorias** (ex: "Bug", "Design") e **Projetos** (ex: "Site Principal").
    * Agora, saia do admin e, logado como admin no site, vá em "Painel Admin" -> "Adicionar Nova" para criar sua primeira tarefa.