amount_of_subnets = ""
ip_address = ""
hosts_per_subnets = []
prefix = ""
last = 0


def ask_network_information():
    global ip_address, prefix, amount_of_subnets, hosts_per_subnets
    ip_address = input("Give the ipv4-adress (in dotted decimal): ")
    prefix = input("Give the prefix: ")
    amount_of_subnets = int(input("how many subnets are required: "))
    for i in range(amount_of_subnets):
        hosts_per_subnets.append(input(f"How many hosts does subnet {i + 1}"\
                                      " need to manage? "))
        
def calculate_adresses(hosts):
    global ip_address, prefix, last
    # calc amount of bits needed
    bits = 0; 
    i = 0
    while True:
        i += 1
        if(int(hosts) + 2 <= 2**i):
            bits = i
            break
    # calc network portion
    network_portion = str(ip_address)[0:int(int(prefix)/2)]
    # addresses
    network_address = ip_address
    first_host_address = network_portion + str(last) + ".1"
    last_host_address = network_portion + str((2 **(bits - 8)) - 1 + last) + ".254"
    broadcast_address = network_portion + str((2 **(bits - 8)) - 1 + last) + ".255"
    address_range = (2 ** bits) - 2
    last += (2 **(bits - 8)) 
    ip_address =  network_portion + str(last ) + ".0" 
    return [network_address, first_host_address, last_host_address, broadcast_address, address_range]


def main():
    global amount_of_subnets, hosts_per_subnets
    ask_network_information()
    for i in range(amount_of_subnets):
        addresses = calculate_adresses(hosts_per_subnets[i])
        print(f"Subnet {i + 1} - {hosts_per_subnets[i]} hosts : ")
        print(f"Network adress: {addresses[0]}\n\
First host adress: {addresses[1]}\n\
Last host adress: {addresses[2]}\n\
Broadcast adress: {addresses[3]}\n\
Adress range: {addresses[4]}\n")

if __name__ == "__main__":
    main()