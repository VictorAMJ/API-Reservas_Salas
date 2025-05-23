# 🖥️ API Reservas de Salas 🗃️

Esta é uma API RESTful desenvolvida em Flask para gerenciar reservas de salas. A API depende da **API de Gestão Escolar**, da qual consome dados de usuários, turmas e outras entidades relacionadas à organização acadêmica.

## 🔗 Dependência Externa

Esta API depende da API Gestão Escolar para validar dados como:

- Identificação do solicitante (professor/aluno)
- Existência de turmas ou atividades relacionadas à reserva

## ⚙️ Tecnologias Utilizadas

- Python 3
- Flask
- SQLite
- Docker

## 📁 Estrutura do Projeto

```bash
API-Reservas_Salas/
├── app.py                # Inicialização do app Flask
├── config.py             # Configurações da aplicação
├── ModelReservas.py      # Modelo SQLAlchemy da tabela de reservas
├── RoutesReservas.py     # Rotas para criar, listar e cancelar reservas
├── requirements.txt      # Dependências do projeto
└── README.md             # Documentação do projeto
```

---

## ▶️ Como Executar a API

### 1. Clone o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd API-Reservas_Salas
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a API

```bash
python app.py
```

A aplicação estará disponível em:
📍 `http://localhost:8082`

---

## 📌 Endpoints Principais:
- `POST /reserva` – Cria uma nova reserva
- `GET /reserva` – Lista todas as reservas

## 🧑‍💻 Autores

- Gabriela Araujo Rodrigues
- Victor Alexandre Martuzzo de Jesus
- Yara Castro Lima
