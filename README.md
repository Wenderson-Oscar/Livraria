
# Livraria Web

## Descrição do Projeto

<p align="center"> Projeto de uma livraria web, onde o usuário pode visualizar os livros e suas informações, além de poder fazer uma leitura e baixar o livro em PDF. Poder interagir com outros usuários, comentando e avaliando os livros, e Marcar em sua lista de favoritos.
Também tem grupo de usuário responsavel por adicionar, editar e remover livros.</p>
Você também pode pedi para ser parte desse grupo, basta entrar em contato com o administrador do grupo e pedir para ser adicionado.


## Funcionalidades

Aqui está uma matriz que descreve as permissões para diferentes tipos de usuários:

| Funcionalidade                         | Visitante       | Usuário | Administrador | Usuário de Grupo | Adm. de Grupo |
| -------------------------------------  | ----------------- | ------- | ------------- | ----------------- | ------------- |
| Visualizar livros                      | ✔️               | ✔️     | ✔️           | ✔️               | ✔️           |
| Visualizar informações do livro        | ✔️               | ✔️     | ✔️           | ✔️               | ✔️           |
| Visualizar comentários                 | ✔️               | ✔️     | ✔️           | ✔️               | ✔️           |
| Ler livro                              | ✔️               | ✔️     | ✔️           | ✔️               | ✔️           |
| Buscar livros pelo nome                | ✔️               | ✔️     | ✔️           | ✔️               | ✔️           |
| Criar conta                            | ✔️               |✔️      |✔️            |✔️                |✔️            |
| Login                                  | ❌              |✔️      |✔️            |✔️                |✔️            |
| Avaliar livro                          | ❌              |✔️      |✔️            |✔️                |✔️            |
| Comentar livro                         | ❌              |✔️      |✔️            |✔️                |✔️            |
| Adicionar livro a lista de favoritos   | ❌              |✔️      |✔️            |✔️                |✔️            |
| Remover livro da lista de favoritos    | ❌              |✔️      |✔️            |✔️                |✔️            |
| Editar perfil                          | ❌              |✔️      |✔️            |✔️                |✔️            |
| Refinir senha                          | ❌              |✔️      |✔️            |✔️                |✔️            |
| Excluir conta                          | ❌              |✔️      |✔️            |✔️                |✔️            |
| Editar comentário                      | ❌              |✔️      |✔️            |✔️                |✔️            |
| Excluir comentário                     | ❌              |✔️      |✔️            |✔️                |✔️            |
| Recuperar senha                        | ❌              |✔️      |✔️            |✔️                |✔️            |
| Adicionar livro                        | ❌              |❌     |✔️            |✔️                |✔️            |
| Remover livro                          | ❌              |❌     |✔️            |✔️                |✔️            |
| Editar livro                           | ❌              |❌     |✔️            |✔️                |✔️            |
| Adicionar Usuário ao Grupo             | ❌              |❌     |✔️            |❌               |✔️            |
| Remover Usuário do Grupo               | ❌              |❌     |✔️            |❌               |✔️            |
| Remover Administrador do Grupo         | ❌              |❌     |✔️            |❌               |✔️            |
| Adicionar Administrador de um Grupo    | ❌              |❌     |✔️            |❌               |❌           |
| Remover Permissão de um Grupo          | ❌              |❌     |✔️            |❌               |❌           |
| Adicionar Permissão a um Grupo         | ❌              |❌     |✔️            |❌               |❌           |
| Criar Grupos                           | ❌              |❌     |✔️            |❌               |❌           |
| Remover Grupo                          | ❌              |❌     |✔️            |❌               |❌           |
| Editar Grupo                           | ❌              |❌     |✔️            |❌               |❌           |





## 🛠 Habilidades

<img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white">
<img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white">
<img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white">




## Rodando localmente

Clone o projeto

```bash
  git clone https://github.com/Wenderson-Oscar/Livraria.git
```

Entre no diretório do projeto

```bash
  cd Livraria
```

Crie um ambiente virtual

```bash
  python -m venv venv
```

Ative o ambiente virtual

Windows
```bash
  venv\Scripts\activate
```

Linux
```bash
  . venv/bin/activate
```

Instale as dependências

```bash
  pip install -r requirements.txt
```

### Configure o arquivo .env

Crie o arquivo `.env` na raiz do projeto

```bash
touch .env
```

Adicione as seguintes variáveis de ambiente ao arquivo `.env`

gerador de chave secreta `SECRET_KEY`: [Djecrety](https://djecrety.ir/).

```bash
SECRET_KEY="sua_chave_secreta"
DEBUG=False
EMAIL_HOST_USER = 'seu_email'
EMAIL_HOST_PASSWORD = 'sua_chave_de_email'
```

Crie o banco de dados

```bash
  python manage.py migrate
```

Inicie o servidor

```bash
  python manage.py runserver
```


## Licença

[MIT](https://choosealicense.com/licenses/mit/)

