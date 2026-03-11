import smtplib
import csv  
from config import EMAIL_REMETENTE, SENHA


# Função para montar e enviar email
def enviar_email(destinatario, nome, empresa):

    # Conexão com o servidor SMTP e envio
    servidor = smtplib.SMTP("smtp.gmail.com", 587)
    servidor.starttls()
    servidor.login(EMAIL_REMETENTE, SENHA)
    servidor.send_message(msg_email)
    servidor.quit()

# Ler planilha e enviar emails
with open("../data/leads.csv", newline='', encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        if linha["enviado"] == "nao":
            enviar_email(linha["email"], linha["nome"], linha["empresa"])
            print("Email enviado para", linha["nome"])