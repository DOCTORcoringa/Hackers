# Doctor Coringa - Ferramentas de Hacking Ético para Termux

![Efeito de digitação](assets/img/typing.gif)

---

## Guia rápido de instalação e execução

#!/bin/bash
pkg update -y
pkg upgrade -y
pkg install python git clang libffi openssl rust make pkg-config libsodium -y
pip install --no-cache-dir --upgrade pip setuptools wheel
SODIUM_INSTALL=system pip install pynacl paramiko requests shodan
git clone https://github.com/DOCTORcoringa/Hackers.git
cd Hackers
python Ferramentas.py

---

## Observações importantes

- O pacote `rust` é necessário para compilar algumas dependências Python.
- Não atualize o `pip` manualmente no Termux, use sempre a atualização via `pkg upgrade`.
- Para executar novamente depois, entre na pasta e rode: 

---

## Sobre o projeto

Este repositório contém diversas ferramentas de hacking ético implementadas em Python, otimizadas para rodar no Termux do Android com efeito interativo.

---

## Contato

Siga o projeto e acompanhe novidades no GitHub!

---

**Este README está pronto para você colar como arquivo README.md no seu repositório e deixar o seu projeto mais profissional e atrativo!**

