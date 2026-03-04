# Automação de Prospecção por Email

Este projeto automatiza o envio de emails personalizados para leads utilizando Python.

O sistema:
- Lê uma planilha CSV com leads
- Envia emails personalizados
- Marca automaticamente como "enviado"
- Utiliza variáveis de ambiente para proteger credenciais

## Tecnologias

- Python 3
- SMTP (Gmail)
- CSV

## Estrutura

automacao_prospeccao/
│
├── main.py
├── data
├    └ leads.csv
└── .env

## Configuração

1. Clone o repositório
2. Instale as dependências:

pip install python-dotenv

3. Crie um arquivo .env com:

EMAIL_REMETENTE=seuemail@gmail.com
SENHA_EMAIL=sua_senha_de_app -> (pode ser sua senha mas é recomendado, por segurança, criar uma senha de app na sua conta gmail)

4. Renomeie o arquivo "exemplo_leads.csv" para "leads.csv" e siga a estrutura:

nome,email,empresa,enviado

## Executar o projeto

python main.py

## Melhorias futuras

- Delay entre emails
- Integração com banco de dados
- Interface gráfica
- Dashboard de métricas