import os
from time import sleep

def mostrar_menu():
    os.system("cls")
    print("=====================================================")
    print("||      Bem vindo à Locadora 'Feliciano's Car'     ||")
    print("=====================================================")
    print("||      Escolha uma opção para prosseguir          ||")
    print("=====================================================")
    print("||     1 - Mostrar Portifólio                      ||")
    print("||     2 - Alugar um Veículo                       ||")
    print("||     3 - Devolver um Veículo                     ||")
    print("||     4 - Sair                                    ||")
    print("=====================================================")
    print("")
    opcao = input("Informe uma opção: ")
    return opcao

def acessar_base_de_dados():
    os.system("cls")
    print("=====================================================")
    print("||     Acessando Base de Dados...                  ||")
    print("=====================================================")
    sleep(3)

def mostrar_portifolio(portifolio, carros_alugados):
    os.system("cls")
    print("=====================================================")
    print("||                Portifólio                       ||")
    print("=====================================================")
    for marca, dados in portifolio.items():
        sleep(1.5)
        print("")
        print("Marca: {}".format(marca))
        modelos = dados["Modelo"]
        valores = dados["Valor"]
        for i in range(len(modelos)):
            modelo = modelos[i]
            if modelo not in carros_alugados:
                print("{} - Modelo: {} | Valor: R${}".format(i+1, modelo, valores[i]))

def alugar_veiculo(portifolio, carros_alugados):
    os.system("cls")
    print("=====================================================")
    print("||             Alugar um Veículo                   ||")
    print("=====================================================")
    print("")
    print("Marcas disponíveis:")
    
    marcas = list(portifolio.keys())
    for i, marca in enumerate(marcas, 1):
        print("{} - {}".format(i, marca))
    
    print("=====================================================")
    opcao_marca = int(input("Escolha uma marca pelo número: "))
    if opcao_marca < 1 or opcao_marca > len(marcas):
        print("Opção inválida! Retornando ao menu principal.")
        sleep(2)
        return
    
    marca_escolhida = marcas[opcao_marca - 1]
    modelos_disponiveis = portifolio[marca_escolhida]["Modelo"]
    valores_disponiveis = portifolio[marca_escolhida]["Valor"]
    
    print("")
    print("Modelos disponíveis para {}:".format(marca_escolhida))
    for i, modelo in enumerate(modelos_disponiveis, 1):
        print("{} - Modelo: {} | Valor: R${}".format(i, modelo, valores_disponiveis[i-1]))
    
    print("=====================================================")
    opcao_modelo = int(input("Escolha um modelo pelo número: "))
    if opcao_modelo < 1 or opcao_modelo > len(modelos_disponiveis):
        print("Opção inválida! Retornando ao menu principal.")
        sleep(2)
        return
    
    modelo_escolhido = modelos_disponiveis[opcao_modelo - 1]
    valor_escolhido = valores_disponiveis[opcao_modelo - 1]
    
    carros_alugados.append({"Marca": marca_escolhida, "Modelo": modelo_escolhido, "Valor": valor_escolhido})
    del portifolio[marca_escolhida]["Modelo"][opcao_modelo - 1]
    del portifolio[marca_escolhida]["Valor"][opcao_modelo - 1]
    
    print("=====================================================")
    print("Por quantos dias deseja alugar?")
    dias = int(input())
    print("=====================================================")
    print("Parabéns, Você alugou o modelo: {} da marca {} por {} dias, o valor total do seu aluguel é de R$ {}.".format(modelo_escolhido, marca_escolhida, dias, (dias * valor_escolhido)))
    print("")
    input("Pressione Enter para voltar ao menu...")

def devolver_veiculo(portifolio, carros_alugados):
    os.system("cls")
    if not carros_alugados:
        print("Não há carros alugados para devolver.")
        input("Pressione Enter para voltar ao menu...")
        return
    
    print("=====================================================")
    print("||            Devolver um Veículo                  ||")
    print("=====================================================")
    print("")
    print("Carros alugados:")
    for i, carro in enumerate(carros_alugados, 1):
        print("{} - {} {} | Valor: R${}".format(i, carro["Marca"], carro["Modelo"], carro["Valor"]))
    
    print("=====================================================")
    opcao_carro = int(input("Escolha um carro para devolver pelo número: "))
    if opcao_carro < 1 or opcao_carro > len(carros_alugados):
        print("Opção inválida! Retornando ao menu principal.")
        sleep(2)
        return
    
    carro_devolvido = carros_alugados[opcao_carro - 1]
    marca_devolvida = carro_devolvido["Marca"]
    modelo_devolvido = carro_devolvido["Modelo"]
    valor_devolvido = carro_devolvido["Valor"]
    
    portifolio[marca_devolvida]["Modelo"].append(modelo_devolvido)
    portifolio[marca_devolvida]["Valor"].append(valor_devolvido)
    
    del carros_alugados[opcao_carro - 1]
    
    print("=====================================================")
    print("Você acaba de devolver o {} {}.".format(marca_devolvida, modelo_devolvido))
    print("")
    input("Pressione Enter para voltar ao menu...")

portifolio = {
    "Honda": {
        "Modelo": ['Civic', 'City', 'Fit', 'CRV', 'HRV'],
        "Valor": [200, 250, 200, 350, 400]
    },
    "Hyundai": {
        "Modelo": ['HB20', 'Creta', 'IX35', 'Tucson', 'Azera'],
        "Valor": [200, 300, 350, 300, 250]
    },
    "Chevrolet": {
        "Modelo": ['Spin', 'Onix', 'Cruze', 'S10', 'Camaro'],
        "Valor": [180, 200, 350, 400, 600]
    }
}

carros_alugados = []

while True:
    opcao = mostrar_menu()
    
    if opcao == "1":
        acessar_base_de_dados()
        mostrar_portifolio(portifolio, carros_alugados)
        print("")
        input("Pressione Enter para voltar ao menu...")
    elif opcao == "2":
        acessar_base_de_dados()
        alugar_veiculo(portifolio, carros_alugados)
    elif opcao == "3":
        acessar_base_de_dados()
        devolver_veiculo(portifolio, carros_alugados)
    elif opcao == "4":
        print("")
        print("Obrigado pela visita!")
        print("")
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção entre 1 e 4.")
        sleep(2)
