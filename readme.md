# Painel Interativo – Projeto Kalulu

Este projeto visa construir um painel interativo para visualização e análise dos dados gerados pelo jogo educacional Kalulu, utilizado em intervenções pedagógicas para o desenvolvimento da leitura.

## ✅ Pré-requisitos

Antes de rodar o projeto, você precisará ter instalado:

- Python 3.11 ou superior
- PostgreSQL 12+
- Git
- Virtualenv (opcional, mas recomendado)

## 🚀 Como rodar o projeto localmente

### 1. Clone o repositório

```bash
git clone https://github.com/marjcarvalhodev/pydashboard.git
cd pydashboard
```

### 2. Crie e ative o ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados

Crie um banco PostgreSQL com os seguintes dados (ou ajuste conforme necessário):

- **Nome do banco:** `pydashboard`
- **Usuário:** `postgres`
- **Senha:** `postgres`
- **Host:** `localhost`
- **Porta:** `5432`

### 5. Configure as variáveis de ambiente

Crie um arquivo chamado `.env` na raiz do projeto com o seguinte conteúdo:

```env
DEBUG=True
SECRET_KEY=sua-chave-secreta-aqui
DATABASE_URL=postgres://postgres:postgres@localhost:5432/pydashboard
```

> Dica: copie de `.env.example` se houver.

### 6. Aplique as migrações

```bash
python manage.py migrate
```

### 7. Inicie o servidor local

```bash
python manage.py runserver
```

Acesse: [http://localhost:8000](http://localhost:8000)

---

## 🧪 Comandos úteis

Carregar os dados CSV:

```bash
python manage.py load_logs --source=csv
```

Resetar o banco de dados (apagar tudo e recriar):

```bash
bash scripts/reset_db.sh
```

---

## 📂 Estrutura esperada

- `dashboard/` – App principal com os modelos, views e templates
- `data/csv/` – Onde devem estar os arquivos `.csv` para ingestão
- `scripts/` – Scripts auxiliares para automação
- `.env` – Arquivo com as configurações locais

---

## 📝 Observações

Este projeto está em desenvolvimento e será futuramente implantado em ambiente de produção. Por enquanto, o foco é facilitar o uso em máquina local para testes e validação.