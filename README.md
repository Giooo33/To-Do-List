# To-Do List (Django + React + Vite)

Este projeto é uma aplicação de lista de tarefas (To-Do List) com backend em Django REST Framework e frontend em React (Vite + Tailwind CSS).

## Pré-requisitos

- Python 3.10 ou superior
- Node.js 18+ e npm
- Git (opcional, mas recomendado)

---

## Instalação do Backend (Django)

1. **Clone o repositório:**
   ```bash
   git clone <url-do-repositorio>
   cd App/backend
   ```

2. **Crie e ative um ambiente virtual:**
   - **Windows:**
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - **Linux/Mac:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instale as dependências do Python:**
   ```bash
   pip install -r requirements.txt
   ```
   > Se não existir o arquivo `requirements.txt`, crie-o com o seguinte conteúdo:
   ```
   asgiref==3.9.1
   Django==5.2.6
   django-cors-headers==4.8.0
   djangorestframework==3.16.1
   djangorestframework_simplejwt==5.5.1
   PyJWT==2.10.1
   sqlparse==0.5.3
   tzdata==2025.2
   ```

4. **Aplique as migrações do banco de dados:**
   ```bash
   python manage.py migrate
   ```

5. **Inicie o servidor Django:**
   ```bash
   python manage.py runserver
   ```
   O backend estará disponível em `http://localhost:8000/`.

---

## Instalação do Frontend (React + Vite)

1. **Acesse a pasta do frontend:**
   ```bash
   cd ../../frontend/To-do-List
   ```

2. **Instale as dependências do Node.js:**
   ```bash
   npm install
   ```

3. **Inicie o servidor de desenvolvimento:**
   ```bash
   npm run dev
   ```
   O frontend estará disponível em `http://localhost:5173/`.

---

## Observações
- Certifique-se de que o backend (Django) esteja rodando antes de acessar o frontend.
- O frontend faz requisições para o backend em `http://localhost:8000/` por padrão.
- Para produção, configure variáveis de ambiente e CORS adequadamente.

---

## Contato
Dúvidas ou sugestões? Abra uma issue ou entre em contato com o mantenedor do projeto.
