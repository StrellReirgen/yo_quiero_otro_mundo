import time
import random
import re

usuarios = []


def generate_password():
    verificador = True
    minus = "qwertyuiopasdfghjklñzxcvbnm"
    mayus = "QWERTYUIOPASDFGHJKLÑZXCVBNM"
    psw = ""
    for i in range(10):
        x = random.randint(1,3)
        if x == 1:
            psw += str(random.randint(0,9))
        elif x == 2:
            psw += minus[random.randint(0,len(minus)-1)]
        elif x == 3:
            psw += mayus[random.randint(0,len(mayus)-1)]
    if re.search('[0-9]',psw) is None:
        verificador = False
    if re.search('[A-Z]',psw) is None: 
        verificador = False
    if re.search('[a-z]',psw) is None: 
        verificador = False
    if verificador:
        return psw
    else:
        generate_password()

def add_phone(user):
    number : int
    try:
        number = int(input(f'Ingrese un numero telefonico para {user}: '))
    except:
        add_phone(user)
    if len(str(number)) < 8 or len(str(number)) > 8:
        print('El numero de telefono tiene que tener exactamente 8 digitos!')
        add_phone(user)
    else:
        return str(number)
    

def add_user(user,usuarios):
    new = {'nombre':user}
    new['password'] = generate_password()
    new['phone'] = add_phone(user)
    usuarios.append(new)

def mostrar_usuarios(usuarios):
    for user in usuarios:
        print(f"Usuario: {user['nombre']} Contraseña: {user['password']} Telefono: {user['phone']}")
        time.sleep(2)

def lista_de_usuarios(usuarios):
    for i in range(1, 11):
        add_user(f"Organizacion {i}",usuarios)
    
lista_de_usuarios(usuarios)
mostrar_usuarios(usuarios)