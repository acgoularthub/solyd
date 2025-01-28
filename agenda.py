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
  for contato in AGENDA:
    buscar_contato(contato)

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

def imprimir_menu():
  print('1 - Mostrar todos os contatos')
  print('2 - Buscar contato')
  print('3 - Incluir contato')
  print('4 - Excluir contato')
  print('5 - Editar contato')
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
  elif opcao == '0':
    print('Até mais!')
    break
  else:
    print('Opção inválida')
    print()