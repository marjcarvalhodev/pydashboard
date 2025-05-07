# 🧠 Painel Interativo – Projeto Kalulu

Este projeto visa construir um painel interativo para visualização e análise dos dados gerados pelo jogo educacional **Kalulu**, utilizado em intervenções pedagógicas para o desenvolvimento da leitura.

O sistema foi pensado para **professores e pesquisadores** acompanharem a evolução de alunos através dos registros de jogo.

---

## ✅ Pré-requisitos

Antes de rodar o projeto, você precisará ter instalado:

- Python 3.11 ou superior
- PostgreSQL 12+
- Git
- Virtualenv (opcional, mas recomendado)
- Gettext (para suporte a traduções):  
  ```bash
  sudo apt install gettext
  ```

---

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

### 5. Configure o banco de dados

Crie um banco PostgreSQL com os seguintes dados (ou ajuste conforme necessário):

- **Nome do banco:** `pydashboard`
- **Usuário:** `postgres`
- **Senha:** `postgres`
- **Host:** `localhost`
- **Porta:** `5432`

As configurações estão em `pydashboard/settings.py` e podem ser ajustadas diretamente.

### 6. Aplique as migrações

```bash
python manage.py migrate
```

### 7. Carregue os dados dos jogos (via CSV)

Coloque os arquivos `.csv` dentro da pasta `data/csv/` e então execute:

```bash
python manage.py load_logs --source=csv
```

### 8. Gere os usuários com base nos logs

```bash
python manage.py populate_users_from_logs
```

> Isso criará automaticamente usuários do tipo "student" com base nos dados dos jogos.

### 9. Crie um usuário pesquisador para acessar o sistema

```bash
python manage.py create_staff_user --username=professor1 --password=abc123
```

---

### 10. Inicie o servidor local

```bash
python manage.py runserver
```

Acesse: [http://localhost:8000](http://localhost:8000)


---

## 📊 Acessos disponíveis

- **Página inicial pública:** `/`
- **Login:** `/login/`
- **Dashboard (pesquisador):** `/dashboard/`
- **Visualização de aluno:** `/dashboard/user/<user_id>/`

---

## 🌍 Internacionalização (i18n)

Este projeto suporta múltiplos idiomas. Atualmente disponíveis:
- 🇺🇸 Inglês (`en`)
- 🇧🇷 Português - Brasil (`pt-br`)

### Como traduzir:

1. Marque strings com `{% trans "texto" %}` ou `{% blocktrans %}`.
2. Gere os arquivos `.po`:

```bash
django-admin makemessages -l pt_BR --ignore=venv/*
```

3. Edite `locale/pt_BR/LC_MESSAGES/django.po`
4. Compile:

```bash
django-admin compilemessages
```

---

## 📂 Estrutura esperada

- `dashboard/` – App principal com modelos, views, templates e comandos
- `data/csv/` – Local dos arquivos `.csv` de entrada
- `locale/` – Traduções
- `scripts/` – Scripts auxiliares (ex: reset do banco)
- `.env` – Variáveis de configuração local

---

## 📝 Observações finais

- Por enquanto, **o uso via Docker não está configurado**, apesar de mencionado no relatório.  
- O projeto está funcional via ambiente virtual Python e banco local.
- Testado com dados reais da intervenção Kalulu.
