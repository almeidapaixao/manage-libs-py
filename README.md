# 📦 Python Dependency Manager

Este repositório contém um script chamado `manage_dependencies.py` que automatiza o gerenciamento de dependências de projetos Python usando:

- [`pip-tools`](https://github.com/jazzband/pip-tools) (`pip-compile`) para travar versões de forma confiável
- [`pip-audit`](https://github.com/trailofbits/pip-audit) para verificar vulnerabilidades conhecidas em bibliotecas instaladas

---

## ✅ O que o script faz

Este script automatiza uma **pipeline local de dependências**, realizando as seguintes etapas:

1. **Verifica se `pip-tools` e `pip-audit` estão instalados**
2. **Faz backup do `requirements.txt` atual** com timestamp
3. **Executa `pip-compile --upgrade`** com base no `requirements.in`
4. **Cria (ou atualiza) o ambiente virtual `.venv`**
5. **Instala todas as dependências do projeto**
6. **Executa uma análise de segurança com `pip-audit`**

---

## 🧑‍💻 Pré-requisitos

- Python 3.8+
- Ter um arquivo `requirements.in` no diretório raiz do projeto, com as **dependências diretas** listadas.

Exemplo:

```txt
# requirements.in
fastapi~=0.110
requests>=2.31,<3.0
