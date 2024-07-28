## ProjetoDjango

# Para criar um ambiente virtual python no terminal digite:
:computer: Linux: python3 -m venv venv
:computer: Windows: python -m venv venv

# Após a criação do venv vamos ativa-lo, no terminal digite:
:computer: Linux: source venv/bin/activate
:computer: Windows: venv\Scripts\Activate
# Caso algum comando retorne um erro de permissão execute o código e tente novamente:
:computer: Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

# Instalando o servidor Django
:computer: pip install django

# Criando um projeto Django
:computer: django-admin startproject meusite .
