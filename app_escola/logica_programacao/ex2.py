ano_nascimento = 2027
ano_atual = 2026
#pode votar a partir dos 16 e a partir dos 70 --> pode mas não é obrigatório
#obrigagorio entre 18 e 70

idade = ano_atual-ano_nascimento

if idade >= 18 and idade < 70:
    print("Idade da pessoa:", idade, "anos")
    print("O voto é obrigatório!")
elif idade < 0:
    print("Idade da pessoa:", idade, "anos")
    print("Idade Inválida")   
elif idade < 16:
    print("Idade da pessoa:", idade, "anos")
    print("A pessoa não pode votar")
else:
    print("Idade da pessoa:", idade, "anos")
    print("O voto não é obrigatório, mas a pessoa pode votar")


