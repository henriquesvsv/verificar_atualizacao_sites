# open-webpage.py
import urllib.request, urllib.error, urllib.parse
import filecmp
import modules.servidor_email as servidor_email, modules.comparacao as comparacao, modules.gerar_novo_arquivo as gerar_novo_arquivo, modules.linhas_alteradas as linhas_alteradas
import os 
from os import path
from pathlib import Path
import time

temp="temp"
fixo="fixo"
##oii
def executar():
    while(True):
        List_sites = open('lista_de_sites.txt')
        sites=List_sites.readlines()


        for site in sites:
            site_sem_barra = site.replace("/", "_")
            siteexist = os.path.exists("./sitestocompare/"+"/"+site_sem_barra)
            if(siteexist):
                gerar_novo_arquivo.dowload_site(site,"temp")
                if(comparacao.comparar(site_sem_barra)==True):
                  
                    servidor_email.send_email(site)
                    with open("./sitestocompare/"+"/"+site_sem_barra+"/"+site_sem_barra+temp+".txt", 'r+') as arquivo_temporario:
                        arquivo1=arquivo_temporario.read()

                    with open("./sitestocompare/"+"/"+site_sem_barra+"/"+site_sem_barra+fixo+".txt", 'r+') as arquivo_fixo: 
                            arquivo_fixo.write(arquivo1)
                    os.remove("./sitestocompare/"+"/"+site_sem_barra+"/"+site_sem_barra+temp+".txt")
                else:
                      os.remove("./sitestocompare/"+"/"+site_sem_barra+"/"+site_sem_barra+temp+".txt")
            else:
                print(str(site_sem_barra))
                desktop = "./sitestocompare"
                path=os.path.join(desktop,str(site_sem_barra))
                os.mkdir(path)
                gerar_novo_arquivo.dowload_site(site,"fixo")
               
        time.sleep(1800)        

executar()  

