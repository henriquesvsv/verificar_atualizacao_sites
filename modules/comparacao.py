import filecmp

def comparar(site_sem_barra):
    fixo="fixo"
    temp="temp"
    file1=("./sitestocompare/"+"/"+site_sem_barra+"/"+site_sem_barra+fixo+".txt")
    file2=("./sitestocompare/"+"/"+site_sem_barra+"/"+site_sem_barra+temp+".txt")

    print(filecmp.cmp(file1, file2, shallow=False) )
    return filecmp.cmp(file1, file2, shallow=False) 

