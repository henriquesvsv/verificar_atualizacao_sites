import smtplib


def send_email(site):
    servidor_email = smtplib.SMTP('smtp.gmail.com', 587)
    servidor_email.starttls()
    servidor_email.login('henriqueflorip@gmail.com', 'jbil yuoh rxwb btgd')
    remetente = 'henriqueflorip@gmail.com'
    destinatarios = 'henriqueflorip@gmail.com'
    site_limpo = site.replace("https://", "www.")
    oba="oba "
    acaboudeatualizar= "\nacabou de atualizar!"
    conteudo = oba+site_limpo+acaboudeatualizar
    print(conteudo)
    servidor_email.sendmail(remetente, destinatarios, conteudo)
    servidor_email.quit()

 