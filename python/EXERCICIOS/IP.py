file = open("IP_Lista.txt", "r")

content = file.read()

file.close()

ls_ip = content.split()
print(ls_ip)
ls_valida = ['200135809', '19216811', '8356774', '1234']
print(ls_valida)

file_val = open('End_Validos.txt', 'w+')
file_inv = open('End_Invalido.txt', 'w+')
for ip in ls_ip:
    if ip in ls_valida:
        file_val.write(ip + '\n')
    else:
        file_inv.write(ip + '\n')
file_inv.close()
file_val.close()