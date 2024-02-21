import urllib.request, urllib.error, urllib.parse
from pathlib import Path

def dowload_site(site, name):
    site_sem_barra = site.replace("/", "_")
    response = urllib.request.urlopen(site)
    webContent = response.read().decode('utf-8')
    arquivo_site = open("./sitestocompare/"+"/"+site_sem_barra+"/"+site_sem_barra+name+".txt", "w")
    arquivo_site.write(webContent)

