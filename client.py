import socket, pickle, math, os

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.settimeout(0.005)
dest = (socket.gethostname(), 7777)

def menu():
    user_choose = input('Informe a opcao desejada:\n\
    1- Porcentagem do uso da memoria principal no servidor\n\
    2- Porcentagem de uso de CPU no servidor\n\
    3- Porcentagem do uso de disco no servidor\n\
    4- IP local do servidor\n\
    5- Porcentagem do uso da CPU para cada core do servidor\n\
    6- Nome e modelo da CPU do servidor\n\
    7- Tipo da arquitetura da CPU do servidor\n\
    8- Palavra do processador, em bits\n\
    9- Frequencia total e frequencia de uso da CPU do servidor\n\
    10- Quantidade de nucleos logicos e fisicos do servidor\n\
    11- Diretorio atual no servidor\n\
    12- Informacoes dos processos em execucao no servidor\n\
    13- Maquinas pertencentes a sub-rede de um determinado IP e informacoes sobre as portas\n\
    14- Informacoes sobre interfaces de rede do servidor\n\
    15- Para sair da apliacacao\n')
    return user_choose

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

input_value = str(menu())
def connection_server():
    s.sendto(input_value.encode('utf-8'), dest)
    accepted = False
    while not accepted:
        try:
            ACK, address = s.recvfrom(2048)
            accepted = True
        except socket.timeout:
            s.sendto(input_value.encode('utf-8'), dest)
    answer_server = pickle.loads(ACK)
    return answer_server

while input_value != '15':
    answer = connection_server()
    if input_value == '1':
        print(os.system('clear'))
        print('O uso da memoria principal e:')
        for i in range(20):
            print(answer[0], '%')
        print('-'*60)
        input_value = menu()
    elif input_value == '2':
        print(os.system('clear'))
        print('O uso da CPU e:')
        for i in range(20):
            print(answer[1], '%')
        print('-'*60)
        input_value = menu()
    elif input_value == '3':
        print(os.system('clear'))
        print('A porcentagem do uso de disco e:')
        for i in range(20):
            print(answer[2], '%')
        print('-'*60)
        input_value = menu()
    elif input_value == '4':
        print(os.system('clear'))
        print('O endereco de IP do servidor e:', answer[3])
        print('-'*60)
        input_value = menu()
    elif input_value == '5':
        print(os.system('clear'))
        print('Uso da CPU para cada nucleo:')
        for i in answer[4]:
            print(i)
        print('-'*60)
        input_value = menu()
    elif input_value == '6':
        print(os.system('clear'))
        print('O nome e modelo da CPU do servidor e:', answer[5])
        print('-'*60)
        input_value = menu()
    elif input_value == '7':
        print(os.system('clear'))
        print('A arquitetura e o tipo da CPU do servidor e:', answer[6])
        print('-'*60)
        input_value = menu()
    elif input_value == '8':
        print(os.system('clear'))
        print('A palavra da CPU do servidor e:', answer[7])
        print('-'*60)
        input_value = menu()
    elif input_value == '9':
        print(os.system('clear'))
        for i in range(20):
            print('A frequencia da CPU do servidor e:', answer[8])
        print('-'*60)
        input_value = menu()
    elif input_value == '10':
        print(os.system('clear'))
        core_logic, core_fisical = answer[9]
        print('Nucleos logicos', core_logic, '\nNucleos fisicos', core_fisical)
        print('-'*60)
        input_value = menu()
    elif input_value == '11':
        print(os.system('clear'))
        print('O diretorio atual em execucao no servidor e:', answer[10])
        print('-'*60)
        input_value = menu()
    elif input_value == '12':
        print(os.system('clear'))
        print('Os processos em execucao sao:\n')
        print(answer[11])
        print('-'*60)
        input_value = menu()
    elif input_value == '13':
        print(os.system('clear'))
        print('As maquinas que pertencem a sub-rede do IP 192.0.2.0/23 sao:\n')
        for i in range(20):
            print(answer[12])
        print('-'*60)
        input_value = menu()
    elif input_value == '14':
        print(os.system('clear'))
        ## também da pra melhorar essa forma de visualizar o código
        print('As informacoes sobre a interface de rede sao:\n')
        print(answer[13])
        print('-'*60)
        input_value = menu()
    else:
        print('Escolha uma opcao valida!\n')
        input_value = menu()
 
print(dest, 'finalizou a conexao...')
s.close()