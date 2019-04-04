import socket, psutil as p, pickle, shutil, platform, os, struct, ipaddress

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 7777))

print('Aguardando Conexão...')
package, destination = s.recvfrom(2048)

##opcao 1 do usuário
def memory_usage_percent():
    process = p.Process(os.getpid())
    mem = process.memory_percent()
    return mem

def cpu_usage_percent():
    percent_cpu = p.cpu_percent()
    return percent_cpu

def disk_usage_percent():
    disk_percent = p.disk_usage('/')[3]
    return disk_percent

def get_local_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address
    
def core_per_cpu_percent():
    cpu_core_usage = p.cpu_times_percent(interval=1, percpu=True)
    return cpu_core_usage

def name_model_cpu():
    model_name_cpu = platform.processor()
    return model_name_cpu

def architecture_cpu():
    architecture_cpu = platform.architecture()
    return architecture_cpu

def size_bit_cpu():
    size_cpu, so = platform.architecture()
    return size_cpu

def freq_cpu_usage():
    freq_cpu = p.cpu_freq(percpu=True)
    return freq_cpu

def cores_cpu():
    cpu_logical = p.cpu_count()
    cpu_fisic = p.cpu_count(logical=False)
    return cpu_logical, cpu_fisic

def current_dir():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    return current_dir

#poderia ter um tratamento melhor
def current_processes():
    process = [pr.info for pr in p.process_iter(attrs=['pid', 'name']) if 'python' in pr.info['name']]
    return process

## FIX IT!!!!!!!!!###############################
def ip_from_subnet():
    net = ipaddress.ip_network('192.0.2.0/23')
    for i in net.hosts():
        hosts = i
    return hosts

def interface_network():
    interfaces = p.net_if_addrs()
    names = []
    values_interfaces = []
    dict_name_value_interfaces = {}
    for i in interfaces:
        names.append(str(i))
    for j in interfaces[i]:
        for item in j:
            values_interfaces.append(item)
    dict_name_value_interfaces[i] = j
    return dict_name_value_interfaces

while True:
    package, destination = s.recvfrom(2048)
    print(f'A conexão foi estabelecida com {destination}')
    print(f'{destination} solicitou dados do servidor')
    answer = []

    ##Dou append em cada funcao para retornar no cliente
    answer.append(memory_usage_percent())
    answer.append(cpu_usage_percent())
    answer.append(disk_usage_percent())
    answer.append(get_local_ip())
    answer.append(core_per_cpu_percent())
    answer.append(name_model_cpu())
    answer.append(architecture_cpu())
    answer.append(size_bit_cpu())
    answer.append(freq_cpu_usage())
    answer.append(cores_cpu())
    answer.append(current_dir())
    answer.append(current_processes())
    answer.append(ip_from_subnet())
    answer.append(interface_network())

    bytes_resp = pickle.dumps(answer)
    s.sendto(bytes_resp, destination)