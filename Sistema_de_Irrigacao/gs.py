#importando biblioteca para conseguir limpar o console
import os
#importando as nossa função
import framework
#importando uma biblioteca para nos informarmos qual o seu sistema operacional
import platform

#escolha é igual a 1 para poder entrar no laço
escolha = 1
#vetor dos resultados
lista_resultados = []

#enquanto o escolha for diferente de 0, vai ficar repetindo
while escolha != 0:
    print("SISTEMA DE IRRIGAÇÃO\n0- Sair\n1- Medição da Umidade Gravimétrica\n2- Consultar Resultados")#menu
    escolha = int(input("Escolha: "))#escolha do menu
    match escolha:
        case 1:
            #abaixo você informa os dados para que seja possível os nossos calculos
            print("Para calcular a Umidade Gravimétrica do seu solo, precisamos de algumas informações. Informe abaixo:")
            solo_umido = float(input("O seu SOLO ÚMIDO em gramas: "))#variável
            solo_seco = float(input("O seu SOLO SECO em gramas: "))#variável
            #chamando a função e mostrando o resultado
            resultado = framework.Umidade_Gravimetrica(solo_umido, solo_seco)
            #adicionando os resultados no vetor
            lista_resultados.append(resultado)
            #motrando o resultado da função
            print(f"Determinação da Umidade Gravimétrica do seu solo é: {resultado}%")
            if resultado <= 0.2:#se o resultado for abaixo de 20%
                #ativa a irrigação
                print("A irrigação está ATIVADA.")
            elif resultado > 0.2 or resultado <= 0.6:#senão se for maior que 20% ou menos que 60%
                #desativa a irrigação
                print("A irrigação está DESATIVADA.")
            else:#senão
                #ele informa que a umidade está acima do recomendado devido a condições ambientais
                print("O solo precisa de atenção, a umidade está acima do recomendado ⚠️.")
                # para retornar para o menu, você tem que apertar a tecla enter
            input("Aperte ENTER para retornar ao menu!")
            if platform.system() == "Windows":#se o seu sitema for windows, ele utiliza esse comando:
                #para que seja possível a limpeza do console, é utilizado o comando do cmd "cls" no windows.
                os.system("cls")
            else:#senão, ele utiliza esse comando:
                #para que seja possível a limpeza do console, é utilizado o comando do cmd "cls" no macOS
                os.system("clear")
        case 2:
            framework.Consultar(lista_resultados)
            print("Lista de Resultados:", framework.Consultar(lista_resultados))#mostra os resultados
            input("Aperte ENTER para retornar ao menu!")  # para retornar para o menu, você tem que apertar a tecla enter
        case 0:#se a escolha for igual a 0
            break#o programa para
        case _:
            print("Informe um caractere válido")#caso você digite um caractere incorreto
            input("Aperte ENTER para retornar ao menu!")#ele te da a opção de retornar para o menu