from config import EMAIL_REMETENTE
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# montar email
def montar_email(destinatario, empresa):
    assunto = "Convite para beta fechado — Criação de posts com IA focados em conversão"
    
    corpo = f"""
    Olá, Tudo bem?

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
    msg_email = MIMEMultipart()
    msg_email["From"] = EMAIL_REMETENTE
    msg_email["To"] = destinatario
    msg_email["Subject"] = assunto

    msg_email.attach(MIMEText(corpo, "plain"))

    return msg_email