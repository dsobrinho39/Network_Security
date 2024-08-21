# Collecting Information from Network Devices (Cisco Routers or Cisco Switches)

Este script coleta informações de dispositivos de rede (roteadores ou switches Cisco) de forma automatizada utilizando a biblioteca **Netmiko**. Ele se conecta a cada dispositivo listado, executa uma série de comandos e salva o resultado em arquivos de texto organizados por IP.

## Funcionalidades

- Conexão automatizada com dispositivos Cisco.
- Execução de comandos comuns de diagnóstico e configuração, como:
  - `show version`
  - `show ip route`
  - `show cdp neighbors`
  - `show ip int brief`
  - `show ip eigrp neighbors`
  - `show tech-support`
- Salvamento dos logs de cada dispositivo em arquivos `.txt` organizados por diretórios.

## Requisitos

- Python 3.6 ou superior
- Biblioteca [Netmiko](https://github.com/ktbyers/netmiko)
- Arquivo JSON contendo credenciais (`credentials.json`)
- Arquivo de texto contendo a lista de IPs (`Lista_de_IPs.txt`)

## Estrutura dos Arquivos

- `credentials.json`: Arquivo JSON com as credenciais de login.

  ```json
  {
      "username": "seu_usuario",
      "password": "sua_senha"
  }
  ```

- Lista_de_IPs.txt: Arquivo de texto contendo os IPs dos dispositivos, um por linha.
```
192.168.1.1
192.168.1.2
192.168.1.3
```

## Como Usar
- Clone o repositório:
- git clone https://github.com/dsobrinho39/Network_Security.git
- Adicione as credenciais no arquivo `credentials.json´.
- Insira os IPs dos dispositivos no arquivo `Lista_de_IPs.txt´.

## Execute o script:

- Windows:

- `py Collect_info_R&S.py´

- Linux:

- `python3 Collect_info_R&S.py´

- Os logs coletados serão salvos em pastas nomeadas com o IP de cada dispositivo, com arquivos .txt contendo os resultadosdos comandos.
- Exemplo de Saída:

```
192.168.1.1/
└── 192.168.1.1.txt
```

#### Instalando as Dependências

Antes de executar o script, instale as dependências necessárias:

```bash
pip install netmiko
```

## Autor
Desenvolvido por Daniel Sobrinho.


