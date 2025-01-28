AGENDA = {}

AGENDA['Anderson'] = {
  'telefone': '1234-5678', 
  'email': 'acgoulartmail@gmail.com'
  }

AGENDA['João'] = {
  'telefone': '1234-5678', 
  'email': 'joao@joao.com'
  }

def mostrar_contatos():
  if AGENDA:
    for contato in AGENDA:
      buscar_contato(contato)
  else:
    print('Agenda vazia')
  print()

def buscar_contato(contato):
  try:
    print('Nome:', contato)
    print('Telefone:', AGENDA[contato]['telefone'])
    print('Email:', AGENDA[contato]['email'])
    print('------------------------------------------------------')
  except KeyError:
    print('Contato inexistente')

def incluir_editar_contato(contato, telefone, email):
  AGENDA[contato] = {
    'telefone': telefone,
    'email': email
  }
  print()
  print('Contato {} adicionado com sucesso'.format(contato))  
  print()

def excluir_contato(contato):
  try:
    AGENDA.pop(contato)
    print()
    print('Contato {} excluído com sucesso'.format(contato))  
    print()
  except KeyError:
    print('Contato inexistente')

def exportar_contatos(nome_arquivo):
  try:
    #fazer com que o arquivo gerado tenha o nome + .CSV no final do nome difgitado pelo usuário
    nome_arquivo = nome_arquivo + '.csv'

    with open(nome_arquivo, 'w') as arquivo:
      for contato in AGENDA:
        telefone = AGENDA[contato]['telefone']
        email = AGENDA[contato]['email']
        arquivo.write("{}, {}, {}\n".format(contato, telefone, email))
    print('Contatos exportados com sucesso')
  except Exception as error:
    print('Algum erro ocorreu ao exportar contatos')
    print(error)

def importar_contatos(nome_arquivo):
  try:
    with open(nome_arquivo, 'r') as arquivo:
      linhas = arquivo.readlines()
      for linha in linhas:
        detalhes = linha.strip().split(',')
        contato = detalhes[0]
        telefone = detalhes[1]
        email = detalhes[2]
        incluir_editar_contato(contato, telefone, email)
    print('Contatos importados com sucesso')
  except FileNotFoundError:
    print('Arquivo não encontrado')
  except Exception as error:
    print('Algum erro ocorreu ao importar contatos')
    print(error)

def imprimir_menu():
  print('1 - Mostrar todos os contatos')
  print('2 - Buscar contato')
  print('3 - Incluir contato')
  print('4 - Excluir contato')
  print('5 - Editar contato')
  print('6 - Exportar contatos para CSV')
  print('7 - Importar contatos de um arquivo CSV')
  print('0 - Sair')
  print()

while True:
  imprimir_menu()
  opcao = input('Escolha uma opção: ')
  print()

  if opcao == '1':
    mostrar_contatos()
  elif opcao == '2':
    contato = input('Nome do contato: ')
    buscar_contato(contato)
  elif opcao == '3' or opcao == '5':
    contato = input('Nome do contato: ')
    telefone = input('Telefone do contato: ')
    email = input('Email do contato: ')
    incluir_editar_contato(contato, telefone, email)
  elif opcao == '4':
    contato = input('Nome do contato: ')
    excluir_contato(contato)

  elif opcao == '6':
    nome_arquivo = input('Digite o nome do arquivo CSV: ')
    exportar_contatos(nome_arquivo)

  elif opcao == '7':
    nome_arquivo = input('Digite o nome do arquivo CSV: ')
    importar_contatos(nome_arquivo)

  elif opcao == '0':
    print('Até mais!')
    break
  else:
    print('Opção inválida')
    print()