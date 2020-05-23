# PythonC0ntr0lGarag3
Python_Project_CTE

Universidade de Aveiro
Departamento de Eletrónica, Telecomunicações e Informática
Avaliação Prática de CTE – Módulo python
abril de 2020


Desenvolva um programa que simule o acesso de carros a um estacionamento pago. Deve implementar e testar individualmente cada uma das seguintes alíneas com funções, necessárias a uma correta resolução do problema. Tenha em consideração a validação de todas as situações de erro que podem ocorrer durante a execução do problema (ausência de dados, acesso a ficheiros, conversão de objetos, entre outras).

1.Escreva uma função para ler o conteúdo de um ficheiro com o nome ep1.csv, que se encontra no seu ambiente de trabalho. Este contém informação sobre os veículos registados no estacionamento. Cada linha contém informação sobre um veículo (matrícula, marca e NIF) e os vários campos estão separados por um ‘;’ como pode ver no ficheiro veiculos.csv. Exemplo de uma linha do ficheiro: AA00AA;Seat;801401501. Não existem matrículas repetidas, mas é possível várias matrículas estarem associadas a um mesmo NIF. Comece por decidir qual estrutura de dados que vai usar para representar esta informação (lista, dicionário, etc.). A função deverá depois devolver uma variável deste tipo. 
2.Escreva uma função que imprima no terminal todos os veículos registados no parque. O argumento da função deverá ser uma variável com os veículos registados que resultou da alínea a). A impressão deverá ser ordenada por ordem crescente de NIF e, para NIFs iguais, deverá ser ordenada por ordem crescente da matrícula (ex: AA00AA deverá aparecer antes de ZZ99ZZ). Tenha em consideração o formato de impressão de acordo com o exemplo de interação apresentado no final deste enunciado.
3.Escreva uma função que imprima no terminal a informação referente a todas as matrículas associadas a cada NIF. O argumento da função deverá ser uma variável com os veículos registados que resultou da alínea a). Tenha em consideração o formato de impressão de acordo com o exemplo de interação apresentado no final deste enunciado.
4.Escreva uma função que valide se uma string, passada como argumento, representa uma matrícula válida em Portugal. Considere apenas matrículas posteriores a 2020 compostas por dois dígitos no meio como no seguinte exemplo: AA00AA. A função deverá devolver um valor lógico Verdadeiro se a matrícula for válida e Falso, caso contrário.
5.Escreva uma função que peça ao utilizador a informação referente à utilização de um parque. Deverá ser introduzida a matrícula e a duração do estacionamento em minutos. Deverá garantir a validação da informação introduzida, isto é, utilizando a função anterior deverá garantir a introdução de uma matrícula válida e o tempo decorrido deverá ser um valor inteiro positivo. Se o utilizador introduzir valores inválidos, deve apresentar uma mensagem de erro e voltar a pedir o valor, como pode ver no exemplo de interação apresentado no final deste enunciado. No final, a função deve devolver a informação introduzida através de uma estrutura de dados à sua escolha (ex. tuplo, lista, etc.). 
6.Escreva uma função que permita escrever num ficheiro, com o nome “parque.csv”, todos os acessos ao parque, ordenados por ordem inversa da duração do estacionamento. Deverá escrever um acesso por linha, sendo os campos separados por um ‘;’. A função deverá receber como argumento uma variável contendo a informação sobre todos os acessos introduzidos.
7.Escreva uma função que permita criar uma fatura para um certo NIF, pedido ao utilizador. A fatura deverá conter todos os acessos dos veículos registados para o NIF em questão, bem como o cálculo do total faturado. Considere que o preço por minuto é 1 cêntimo. A função deverá receber como argumento a informação relativa a todos os veículos registados e a todas as utilizações do parque. Tenha em consideração o formato de impressão de acordo com o exemplo de interação apresentado no final deste enunciado.
8.Implemente agora um programa que permita gerir o parque baseado numa interação com um menu. Escreva uma função que apresenta ao utilizador um menu (texto com as opções disponíveis) e pede ao utilizador um valor inteiro correspondente à opção desejada, devolvendo no final este valor. O texto a apresentar deve seguir o exemplo de interação apresentado no final deste enunciado. Deve utilizar todas as funções desenvolvidas anteriormente e respeitar o exemplo de interação apresentado de seguida. Para cada opção do menu corresponde, basicamente, a chamada a uma função desenvolvida. Tenha em atenção a salvaguarda dos valores devolvidos pelas várias funções e a passagem dos argumentos certos. 


Opcoes disponiveis:
0 - Terminar
1 - Ler ficheiro de clientes
2 - Imprimir clientes ordenados
3 - Mostrar matriculas por Cliente
4 - Adicionar acesso ao parque
5 - Gravar acessos ao parque
6 - Gerar fatura para um cliente
Opcao? 2
Não existem clientes!

Opcoes disponiveis:
[Impressao das varias opcoes]
Opcao? 3
Não existem clientes!

Opcoes disponiveis:
[Impressao das varias opcoes]
Opcao? 1
Nome do ficheiro? x.csv
Erro ao ler o ficheiro! [Errno 2] No such file or directory: 'x.csv'
Opcao 1 falhou!

Opcoes disponiveis:
[Impressao das varias opcoes]
Opcao? 1
Nome do ficheiro? veiculos.csv
Foram importados 10 registos.

Opcoes disponiveis:
[Impressao das varias opcoes]
Opcao? 2
100100100 : ('UA50UA', 'Honda')
100200300 : ('AB11AA', 'Ford')
100200300 : ('KK44AB', 'BMW')
100200300 : ('XY99YZ', 'Lancia')
500600400 : ('AB22CD', 'Audi')
500600400 : ('SS99AA', 'Porsche')
801401501 : ('AA00AA', 'Seat')
900800700 : ('KL55XX', 'Tesla')
901401101 : ('CD00UA', 'Nissan')
901401101 : ('ZZ00XB', 'Mercedes')

Opcoes disponiveis:
[Impressao das varias opcoes]
Opcao? 3
801401501 : ['AA00AA']
901401101 : ['ZZ00XB', 'CD00UA']
100200300 : ['AB11AA', 'XY99YZ', 'KK44AB']
100100100 : ['UA50UA']
900800700 : ['KL55XX']
500600400 : ['SS99AA', 'AB22CD']

Opcoes disponiveis:
[Impressao das varias opcoes]
Opcao? 4
Matricula? 000000
Invalida! Matricula? ZZ00XB
Duracao?30

Opcoes disponiveis:
[Impressao das varias opcoes]
Opcao? 4
Matricula? CD00UA
Duracao?15

Opcoes disponiveis:
[Impressao das varias opcoes]
Opcao? 4
Matricula? AB22CD
Duracao?45

Opcoes disponiveis:
[Impressao das varias opcoes]
Opcao? 5
Ficheiro gravado com sucesso!

Opcoes disponiveis:
[Impressao das varias opcoes]
Opcao? 901401101

Opcoes disponiveis:
[Impressao das varias opcoes]
Opcao? 6
NIF? 901401101
[('ZZ00XB', 'Mercedes', '901401101', 30), ('CD00UA', 'Nissan', '901401101', 15)]
Fatura NIF: 901401101
Matricula  Marca             Duracao    Custo
ZZ00XB     Mercedes               30    0.30
CD00UA     Nissan                 15    0.15
Total:                                  0.45

Opcoes disponiveis:
[Impressao das varias opcoes]
Opcao? 0
Obrigado por usar software desenvolvido em CTE!
