## QUESTÃO 5 ##
# Escreva um programa para calcular a redução do tempo de vida de um fumante.
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
# Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule
# quantos dias de vida um fumante perderá. Exiba o total em dias.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!!
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    cif_dia = int(input('quantos fumados por dia?'))
    anos = int(input('informe ha quanto  tempo vc ja fuma em anos'))
    anos = anos * 365
    cig = cif_dia * anos
    cig = cig *10
    cig = int(cig /1440)
    print('vc tem {} dias a menos de vida meu bom'.fomat(cig))


if __name__ == '__main__':
    main()
