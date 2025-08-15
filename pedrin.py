nome = input('Digite seu nome: ')
idade =int(input('Digite sua idade: '))
if idade <= 18:
    print("Entrada autorizada para seguintes filmes: ")
    while True :
        print('1- Sala 1')
        print('2- Sala 2')
        print('3- Sala 3')
        print('6- Sair')
        opcao = input('Escolha uma opção: ')
        if opcao == '1' :
            while True:
                if opcao == '1':
                    print('1-Como treinar seu dragão(+ 10 anos)')
                    print('2-Guardiões da Galaxia(+ 10 anos)')
                    print('3- bela e a fera (+ 10 anos)')
                    break
            opcao_filme = input('Escolha um filme: ')
            if opcao_filme == '1':
                print('1-Como treinar seu dragão(+ 10 anos)')
                print('Imprimindo ingresso!')
            elif opcao_filme == '2':
                print('2-Guardiões da Galaxia(+ 10 anos)')
                print('Imprimindo ingresso!')
            elif opcao_filme =='3':
                print('3- bela e a fera (+ 10 anos)')
                print('Imprimindo ingresso!')
        elif opcao == '2' :
            while True:
                if opcao== '2':
                    print('1-Vingadores(+ 10 anos)')
                    print('2-Sherek 5(+ 10 anos)')
                    print('3-Gente grande(+ 10 anos)')
                    break
            opcao_filme = input('Escolha um filme: ')
            if opcao_filme =='1':
                print('1-Vingadores(+ 10 anos)')
                print('Imprimindo ingresso!')
            elif opcao_filme =='2':
                print('2-Sherek 5(+ 10 anos)')
                print('Imprimindo ingresso!')
            elif opcao_filme =='1':
                print('3-Gente grande(+ 10 anos)')
                print('Imprimindo ingresso!')
        elif opcao == '3': 
            while True:
                if opcao=='3':
                    print('1-Velozes Furiosos 1')
                    print('2-Velozes Furiosos 2')
                    print('3-Velozes Furiosos 3')
                    break
            opcao_filme = input('Escolha um fime: ')
            if opcao_filme == '1':
                print('Velozes Furiosos 1')
                print('Imprimindo ingresso!')
            elif opcao_filme == '2':
                print('Velozes Furiosos 2')
                print('Imprimindo ingresso!')
            elif opcao_filme == '3':
                print('Velozes Furiosos 3')
                print('Imprimindo ingresso!')
                break


else: 
    print('Entrada autorizada para seguintes salas: ')
    while True :
        print('4- Sala 4')
        print('5- Sala 5')
        print('6- Sair')
        opcao = input('Escolha uma opção: ')
        if opcao == '4':
            while True:
                if opcao == '4':
                    print('1-Sexta feira 13')
                    print('2-Freddy Grugger')
                    print('3-Chuccky')
                    break
            opcao_filme = input('Escolha um filme: ')
            if opcao_filme == '1':
                print('Sexta feira 13')
                print('Imprimindo ingresso!')
            elif opcao_filme == '2':
                print('Freddy Grugger')
                print('Imprimindo ingresso!')
            elif opcao_filme == '3':
                print('Chuccky')
                print('Imprimindo ingresso!')
        elif opcao == '5':
            while True:
                if opcao == '5':
                      print('1-Invocação do Mal')
                      print('2-American pie')
                      print('3-Super Bad')
                      break
            opcao_filme = input('Escolha um filme: ')
            if opcao_filme == '1':
                print('Invocação do Mal')
                print('Imprimindo ingresso!')
            elif opcao_filme == '2':
                print('American pie')
                print('Imprimindo ingresso!')
            elif opcao_filme == '3':
                print('Super Bad')
                print('Imprimindo ingresso!')
        elif opcao == '6':
            print('Saindo do sistema!')
            break
        else:
            print('Opção inválida')