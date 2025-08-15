nome = input('Digite seu nome: ')
idade =int(input('Digite sua idade: '))
if idade >= 12:
    print("Entrada autorizada para seguintes filmes: ")
while True :
  print('1- Sala 1')
  print('2- Sala 2')
  print('3- Sala 3')
  print('4 Sala 4')
  print('5- Sala 5')
  print('6- Sair')
  def verificar_idade(idade):
      if  idade >= 10:
        print("Entrada autorizada!")
      else :
        print("Entrada proibida. Você precisa ter pelo menos 18 anos.")
  pass

  opcao = input('Digite sua opção: ')

  if opcao == '1' :
    while True:
     if opcao== '1':
        print('1-Como treinar seu dragão(+ 10 anos)')
        print('2-Guardiões da Galaxia(+ 10 anos)')
        print('3- bela e a fera (+ 10 anos)')
        opcao_filme = input('Escolha um filme: ')
        if opcao =='1':
            print('1-Como treinar seu dragão(+ 10 anos)')
        elif opcao =='2':
            print('2-Guardiões da Galaxia(+ 10 anos)')
        elif opcao =='1':
            print('3- bela e a fera (+ 10 anos)')
        else:
            print('Imprimindo seu ingresso')
        break


  elif opcao == '2':
    print('Vingadores')
    print('Sherek 5')
    print('Gente grande')
  elif opcao == '3':
    print('Velozes Furiosos 1')
    print('Velozes Furiosos 2')
    print('Velozes Furiosos 3')
  elif opcao == '4':
    print('Sexta feira 13')
    print('Freddy Grugger')
    print('Chuccky')
  elif opcao == '5':
    print('Capitão América')
    print('Guerra Civil')
    print('Matrix')
  elif opcao == '6':
    print('Sistema fechando.')
    break
  else:
    print('Saindo')
