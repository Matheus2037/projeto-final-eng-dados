# Projeto Final de Engenharia de Dados

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen.svg)](https://github.com/Matheus2037/projeto-final-eng-dados)
[![Docs](https://img.shields.io/badge/docs-mkdocs-blue)](https://github.com/Matheus2037/projeto-final-eng-dados)

Repositório para desenvolvimento do projeto final da disciplina de Engenharia de Dados do curso de Engenharia de Software da UNISATC.

## Desenho de Arquitetura

![image](https://github.com/jlsilva01/projeto-ed-satc/assets/484662/541de6ab-03fa-49b3-a29f-dec8857360c1)

## Pré-requisitos e ferramentas utilizadas

- **Linguagem:** Python 3.11+
- **Framework web:** FastAPI
- **Servidor ASGI:** Uvicorn
- **Qualidade de código:** pre-commit (ruff, black, isort, flake8, mypy)
- **Container:** Docker
- **Orquestração local:** Docker Compose
- **Documentação:** MkDocs + mkdocstrings + mkdocs-material

## Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/Matheus2037/projeto-final-eng-dados.git
cd projeto-final-eng-dados
```

### 2. Instalar dependências & pre-commit

```bash
# instalar dependências do arquivo pyproject.toml
poetry install

# instalar hooks do pre-commit
poetry run pre-commit install
```

### 3. Executar localmente

```bash
poetry run uvicorn app.main:app --reload
```

Acesse a API em `http://localhost:8000` e a documentação automática em:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc:       `http://localhost:8000/redoc`

## Documentação (MkDocs)

Toda a documentação está em `docs/`:

```bash
poetry run mkdocs build
poetry run mkdocs serve
```

Acesse o site em `http://127.0.0.1:8000`.

Para publicar o site estático:

```bash
poetry run mkdocs gh-deploy
```

## Colaboração

1. Abra uma **issue** para discutir sua feature ou bug.  
2. Crie um **branch**:  

   ```bash
   git checkout -b feature/nome-da-sua-feature
   ```
3. Faça suas alterações e **commit** seguindo o [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).  
4. Envie um **pull request** para `main`.  
5. Aguarde revisão e merge.

## Versão

Fale sobre a versão e o controle de versões para o projeto.

## Autores

* **Jean Guichard** - [(https://github.com/Guichardx2)](https://github.com/Guichardx2)
* **João Carlos** - [https://github.com/Churima](https://github.com/Churima)
* **Lucas Silva** - [https://github.com/Lorrust](https://github.com/Lorrust)
* **Matheus Daminelli** - [https://github.com/daminellis](https://github.com/daminellis)
* **Matheus Gastaldi** - [https://github.com/Matheus2037](https://github.com/Matheus2037)

## Licença

Este projeto está sob a Licença MIT - veja o arquivo [LICENSE](https://github.com/Matheus2037/projeto-final-eng-dados/blob/main/LICENSE) para detalhes.   

## Referências

Cite aqui todas as referências utilizadas neste projeto, pode ser outros repositórios, livros, artigos de internet etc.
