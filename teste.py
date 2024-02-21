
with open("emailepassword.txt", 'r+') as arquivo:
    arquivo1=arquivo.readline().split("=")[1]
    arquivo2=arquivo.readline().split("=")[1]

    print(arquivo2)