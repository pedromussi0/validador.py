def cpf_validate(cpf):
    # verify if its only numbers and turning each iterable character into an int so that the isdigit function works:
    cpf = [int(char) for char in cpf if char.isdigit()]

    # verify if it has 11 digits:
    if len(cpf) != 11:
        return False

    # cross out exception cases (11111111111,22222222222,[...]) :
    if cpf == cpf[::-1]:
        return False
    
    #  Validate both verification digits:
    for i in range(9, 11):
        value = sum(cpf[num] * ((i + 1) - num) for num in range(0, i))
        digito = ((value * 10) % 11) % 10
        if digito != cpf[i]:
            return False
        else:
            return True

cpf = input("digite o cpf : ")

if cpf_validate(cpf):
    print("valido")
else:
    print("invalido")
