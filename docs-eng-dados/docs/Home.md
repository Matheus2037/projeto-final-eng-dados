# Como rodar o projeto


### 1. Clonar o repositório

```bash
git clone https://github.com/Matheus2037/projeto-final-eng-dados.git
cd projeto-final-eng-dados
```


### 2. Instalar dependências & pre-commit

```bash
# instalar dependências do arquivo pyproject.toml
poetry install
```

```bash
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
