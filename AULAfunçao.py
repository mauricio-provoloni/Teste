def pegar_notas():
    n1 = float(input("Digite sua nota 1: "))
    n2 = float(input("Digite sua nota 2: "))
    n3 = float(input("Digite sua nota 3: "))
    return n1, n2, n3

def calcular_media(n1, n2, n3):
    return (n1+n2+n3)/3

def verificar_situacao(media):
    if media >= 7:
        return "aprovado"
    
    elif media >= 5 and media < 7:
        return "Recuperaçao"
    
    else:
        return "reprovado"

nome = input("Nome do aluno: ")
notas = pegar_notas()
media = calcular_media(*notas)
situacao = verificar_situacao(media)

print(f"\nAluno: {nome}")
print(f"media: {media:.2f} - situaçao: {situacao}.")