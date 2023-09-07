import string
import secrets
import time


def generator_password():
    comb_password = string.ascii_letters + string.digits + string.punctuation
    length_password = int(input("Digite o comprimento da sua senha:"))

    while True:
        try:
            if length_password < 8:
                print("o Número de caracteres está inválido:(O minimo é:8)")
                length_password = int(input("Digite o comprimento da sua senha:"))
                continue

            password = ''.join(secrets.choice(comb_password) for i in range(length_password))

            if any(c.islower() for c in password) and any(c.isupper() for c in password) and sum(
                    c.isdigit() for c in password) >= 3:
                time.sleep(1)
                print("Aguarde(1)...")
                time.sleep(1)
                print("Aguarde(2)...")
                time.sleep(1)
                print("Aguarde(3)...")
                time.sleep(2)
                print(
                    f"A sua senha atual foi gerada:\n-{password}(A sua senha atual contém:{len(password)} caracteres.)")
                break

        except ValueError as Error:
            print(Error)


generator_password()




