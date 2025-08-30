# Doctor Coringa - Ferramentas de Hacking Ético para Termux

![Efeito de digitação](assets/img/typing.gif)

---

## Guia rápido de instalação e execução

Faça os passos abaixo no seu Termux para instalar todas as dependências do sistema e do Python, clonar este repositório e rodar o script.

Atualiza a lista de pacotes do Termux
pkg update -y && \

Atualiza os pacotes instalados para versões mais recentes
pkg upgrade -y && \

Instala Python, Git, compilador Clang e bibliotecas essenciais para executar pacotes Python complexos
pkg install python git clang libffi openssl rust -y && \

Instala as bibliotecas Python essenciais para o script
pip install paramiko requests shodan && \

Clona o repositório com os scripts Python
git clone https://github.com/DOCTORcoringa/Hackers.git && \

Entra no diretório do projeto clonado
cd Hackers && \

Executa o script Python principal
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

