import smtplib
import csv  
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Carregar variáveis de ambiente
load_dotenv()
EMAIL_REMETENTE = os.getenv("EMAIL_REMETENTE")
SENHA = os.getenv("SENHA_EMAIL")

# Função para montar e enviar email
def enviar_email(destinatario, nome, empresa):
    assunto = "Convite para beta fechado — Criação de posts com IA focados em conversão"
    
    corpo = f"""
Oi {nome}, Tudo bem?

Vi que a {empresa} trabalha bastante com conteúdo, então resolvi entrar em contato.

Nós da Wevo, estamos desenvolvendo uma plataforma que ajuda empresas a criarem posts e carrosséis de forma muito mais rápida, usando IA — sem perder a identidade da marca.
A ideia é simples: você escreve em poucas palavras o que quer comunicar, e a ferramenta transforma isso em um conteúdo pronto para postar, com estrutura, visual consistente e pensado para conversão.  
Hoje, criar conteúdo dá trabalho, toma tempo e muitas vezes vira um gargalo. A plataforma nasceu justamente pra resolver isso.

Estamos abrindo um beta fechado, totalmente gratuito  para o Creative Flow, e estamos chamando algumas empresas pra testar a ferramenta e nos dar um feedback sincero antes do lançamento oficial.

Achei que a {empresa} poderia se interessar.
Se fizer sentido, o cadastro é rápido (e no final da página) por aqui:
https://creative-flow-nine.vercel.app/

Para qualquer dúvida, estou à disposição.

Abraços,
Gustavo
"""

    # Montar email
    msg = MIMEMultipart()
    msg["From"] = EMAIL_REMETENTE
    msg["To"] = destinatario
    msg["Subject"] = assunto

    msg.attach(MIMEText(corpo, "plain"))

    # Conexão com o servidor SMTP e envio
    servidor = smtplib.SMTP("smtp.gmail.com", 587)
    servidor.starttls()
    servidor.login(EMAIL_REMETENTE, SENHA)
    servidor.send_message(msg)
    servidor.quit()

# Ler planilha e enviar emails
with open("../data/leads.csv", newline='', encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        if linha["enviado"] == "nao":
            enviar_email(linha["email"], linha["nome"], linha["empresa"])
            print("Email enviado para", linha["nome"])
            linha["enviado"] = "sim"