# Sistema de Dados — API Flask + Frontend

API REST desenvolvida em Flask com autenticação JWT, arquitetura em camadas e frontend HTML integrado.

## Tecnologias

- **Python 3** + **Flask 3**
- **Flask-SQLAlchemy** — ORM / banco de dados (SQLite)
- **Flask-JWT-Extended** — autenticação via token JWT
- **Flask-Bcrypt** — hash seguro de senhas
- **Flask-Migrate** — migrações de banco de dados
- **Flask-CORS** — suporte a requisições cross-origin
- **Marshmallow** — validação e serialização de dados
- **Frontend** — HTML + Tailwind CSS (CDN) + JavaScript puro

## Arquitetura

```
rasp/
├── app/
│   ├── models/          # Camada de modelo (ORM)
│   │   ├── user.py
│   │   └── data.py
│   ├── repositories/    # Camada de acesso ao banco de dados
│   │   ├── user_repository.py
│   │   └── data_repository.py
│   ├── services/        # Camada de regra de negócio
│   │   ├── auth_service.py
│   │   └── data_service.py
│   ├── schemas/         # Validação de entrada (Marshmallow)
│   │   ├── user_schema.py
│   │   └── data_schema.py
│   ├── routes/          # Camada de apresentação (controllers)
│   │   ├── auth_routes.py
│   │   └── data_routes.py
│   ├── static/
│   │   └── index.html   # Frontend
│   └── __init__.py      # Factory da aplicação
├── run.py
├── requirements.txt
└── .env
```

## Configuração e execução

```bash
# 1. Clone o repositório
git clone <url-do-repositorio>
cd rasp

# 2. Crie e ative o ambiente virtual
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure as variáveis de ambiente
# Crie um arquivo .env com:
SECRET_KEY=sua-chave-secreta
JWT_SECRET_KEY=sua-chave-jwt
DATABASE_URL=sqlite:///data.db

# 5. Execute a aplicação
python run.py
```

Acesse o frontend em: **http://localhost:5000**

## Endpoints da API

### Autenticação

| Método | Rota             | Descrição                        | Auth |
|--------|------------------|----------------------------------|------|
| POST   | `/auth/register` | Cadastra novo usuário            | Não  |
| POST   | `/auth/login`    | Autentica e retorna token JWT    | Não  |
| GET    | `/auth/me`       | Retorna dados do usuário logado  | Sim  |

### Dados

| Método | Rota            | Descrição                  | Auth |
|--------|-----------------|----------------------------|------|
| GET    | `/data/`        | Lista todos os registros   | Sim  |
| POST   | `/data/`        | Cria novo registro         | Sim  |
| DELETE | `/data/<id>`    | Remove um registro         | Sim  |

**Header de autenticação:** `Authorization: Bearer <token>`

## Autores

- Nome 1
- Nome 2
- Nome 3
