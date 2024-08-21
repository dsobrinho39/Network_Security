# Collecting information from Network Devices (Cisco Routers or Cisco Switches)
# By Daniel Sobrinho
#
import os
import json
from netmiko import ConnectHandler

def load_credentials():
    # Carrega as credenciais do arquivo JSON
    with open("credentials.json", "r") as file:
        credentials = json.load(file)
    return credentials["username"], credentials["password"]

def connect_and_execute(device, commands):
    try:
        # Criação da conexão usando ConnectHandler
        device_object = ConnectHandler(**device)
        print(f"Conectado ao dispositivo {device['host']}")

        # Verificação se a conexão está ativa
        if device_object.is_alive():
            print(f"Conexão com {device['host']} está ativa.\n")

            # Coleta o output dos comandos
            output = ""
            for command in commands:
                print(f"Executando '{command}' em {device['host']}")
                output += f"\n{'='*20} Executando: {command} {'='*20}\n"
                output += device_object.send_command(command) + "\n"
                print(output)

            # Retorno do resultado para possível uso futuro
            return output

        else:
            print(f"Falha ao conectar-se ao dispositivo {device['host']}")

    except Exception as e:
        print(f"Erro ao conectar ao dispositivo {device['host']}: {str(e)}")

    finally:
        # Garantindo que a conexão seja fechada corretamente
        device_object.disconnect()
        print(f"Conexão encerrada com {device['host']}.\n")

def main():
    # Nome do arquivo contendo a lista de IPs
    ip_file = "Lista_de_IPs.txt"

    # Carrega o login e senha do arquivo JSON
    USER, PASS = load_credentials()
    DEVICE_TYPE = "cisco_xe"  # Tipo de dispositivo para roteadores Cisco

    # Comandos que serão enviados para cada equipamento
    commands = [
        "show version",
        "show ip route",
        "show cdp neighbors",
        "show ip int brief",
        "show ip eigrp neighbors",
        "show tech-support"
    ]

    # Verifica se o arquivo com a lista de IPs existe
    if not os.path.isfile(ip_file):
        print(f"Arquivo {ip_file} não encontrado.")
        return

    # Lê a lista de IPs do arquivo
    with open(ip_file, "r") as file:
        ip_list = [line.strip() for line in file.readlines()]

    # Loop para acessar cada IP da lista
    for ip in ip_list:
        # Configuração de conexão para o equipamento
        device = {
            "device_type": DEVICE_TYPE,
            "host": ip,
            "username": USER,
            "password": PASS,
        }

        # Coleta o output dos comandos
        output = connect_and_execute(device, commands)

        if output:
            # Cria uma pasta com o nome do IP se ela não existir
            if not os.path.exists(ip):
                os.makedirs(ip)

            # Salva o output em um arquivo .txt dentro da pasta do IP
            log_file = os.path.join(ip, f"{ip}.txt")
            with open(log_file, "w") as file:
                file.write(output)

            print(f"Log salvo em {log_file}")

    print("Script finalizado.")

if __name__ == "__main__":
    main()
