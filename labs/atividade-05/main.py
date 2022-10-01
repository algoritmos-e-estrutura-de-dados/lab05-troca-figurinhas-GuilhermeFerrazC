def maximizar_troca_de_figurinhas(figurinhasDaMaria, figurinhasDoJoao):
    trocas = 0
   
   #verifica quem possue uma quantidade maior de figurinhas
    menorFigurinha = figurinhasDaMaria if len(figurinhasDaMaria) <= len(figurinhasDoJoao) else figurinhasDoJoao
    maiorFigurinha = figurinhasDaMaria if len(figurinhasDaMaria) >= len(figurinhasDoJoao) else figurinhasDoJoao
   
    for index, n_Figurinha in enumerate(menorFigurinha):
        if not n_Figurinha in maiorFigurinha:
            for n in range(index, len(maiorFigurinha)):
                if n_Figurinha != maiorFigurinha[n]:
                    aux = maiorFigurinha[n]
                    maiorFigurinha[n] = n_Figurinha
                    menorFigurinha[index] = aux
                    trocas = trocas + 1
                    break
    return trocas



if __name__ == '__main__':
    A, B = input().split(' ')
    figurinhasDaMaria = input().split(' ')
    figurinhasDoJoao = input().split(' ')
    maximizar_troca_de_figurinhas(figurinhasDaMaria, figurinhasDoJoao)
