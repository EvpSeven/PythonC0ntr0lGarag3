import re
import csv

class carro:
	def __init__(self, matricula, marca, nif):
		self.matricula = matricula
		self.marca = marca
		self.nif = nif

	def display(self):
		print("{} : ('{}', '{}')".format(self.nif, self.matricula, self.marca))


def main():
    # MENU OPÇÕES
    acess = {}
    while True:

        print("""Opcoes disponiveis:
    0 - Terminar
    1 - Ler ficheiro de clientes
    2 - Imprimir clientes ordenados
    3 - Mostrar matriculas por Cliente
    4 - Adicionar acesso ao parque
    5 - Gravar acessos ao parque
    6 - Gerar fatura para um cliente
    Opcao?
             """)

        num = input()

        if num == "1":
            print("\n Nome do Ficheiro?")
            try:
                nome_file=input()
                matricula, marca, NIF, x= read_carros(nome_file)
                print("Foram importados ", x, "registos.\n") #print nºregistos
            except FileNotFoundError as error: #Imprimir o erro
                print("Erro ao ler o ficheiro!", error)
                print("Opção 1 falhou!")
        elif num == "2":
            try:
                carros=print_carros(matricula,marca,NIF)
            except UnboundLocalError:
                print("Não existem clientes!")
        elif num == "3":
            try: #se clicar no 3 antes de abrir o file UnboundLocalError: local variable 'matricula' referenced before assignment
                nif_matriculas(matricula,NIF)
            except UnboundLocalError:
                print("Não existem clientes!")
        elif num == "4":
            print("Matricula?")
            mat=input()
            validar=valid_matricula(mat)
            while validar==False:
                print("Invalida!")
                print("Matricula?")
                mat=input()
                validar=valid_matricula(mat)
            print("Duração?")
            time=int(input())
            try:
                acess[mat] += time
            except KeyError:
                acess[mat] = time
        elif num == "5":
            #print(acess)
            escrever_acesso(acess)
            print("Ficheiro gravado com sucesso!")
        elif num == "6":
            print("NIF?")
            nif_carro=input()
            #print(acess)
            temp1=calculo_nif(acess, carros,nif_carro)
            print(temp1)
            print("Fatura NIF: ", nif_carro)
            print("{:10} {:<12} {:>10} {:>10}".format("Matricula", "Marca", "Duração", "Custo")) #FORMAT DO PRINT
            total=0
            for c in temp1:
                print("{:10} {:<12} {:>10} {:>10}".format(c[0], c[1], c[3], c[3]*0.01))
                total+=(c[3]) #aparamente existe um bug que nao dá para somar decimais menores que 1
            print("{:34} {:>10}".format("Total:",total*0.01))
        elif num == "0":
            print("Obrigado por usar software desenvolvido em CTE!")
            break

def read_carros(nome_file):
    NIF=[]
    marca=[]
    matricula=[]
    x=0
    with open(nome_file, 'r') as f: #
        f.readline()
        lines = f.readline().strip("\n") #ele esta a ler a linha e o .strip esta a remover o \n
        while lines:
            matri, marc, NI = lines.split(';') #Okay, now we want to split each line into the data we need.
            matricula.append(matri)
            marca.append(marc)
            NIF.append(NI)
            x+=1
            lines = f.readline().strip("\n")

    return matricula,marca,NIF,x

def print_carros(matricula,marca,NIF):
    carros = []
    for i in range (len(NIF)) :
        carros.append(carro(matricula[i], marca[i], NIF[i]))

    carros.sort(key=lambda x: (x.nif,x.matricula))  # sorts in place(nif e depois matricula)
    for c in carros:
        c.display()

    return carros

def nif_matriculas(matricula,NIF):
    puf={} #dicionario
    for i in range (len(NIF)): #rodar os NIFs
        try: #para cada NIF repetido vai adicionar ao que ja estava anteriormente
            temp=puf[NIF[i]]
            temp.append(matricula[i])
            puf[NIF[i]]=temp
        except KeyError: #da erro quando temp=puf[NIF[i]] quando é a primeira vez do NIF
            puf[NIF[i]]=[matricula[i]]
    for key in puf: #format dic
        print("{} : {}".format(key, puf[key]))
    return puf
def valid_matricula(matricula):
    return bool(re.match(r"[a-zA-Z][a-zA-Z][0-9][0-9][a-zA-Z][a-zA-Z]", matricula))

def escrever_acesso(acess):
    w= csv.writer(open("parque.csv", "w",newline=""),delimiter=";") #write in files
    for key,val in acess.items():
        w.writerow([key,val])

def calculo_nif(acess,carros,nif_carro):
    out=[] #list
    for c in carros:
        if c.nif==nif_carro:
            try:
                out.append((c.matricula,c.marca,c.nif,acess[c.matricula]))  #tuplo
            except KeyError:
                continue
    return out
main()