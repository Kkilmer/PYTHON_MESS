#DICIONÁRIO

filmes = {
    1: ['Outono em NY','Romance', 789, 120],
    2: ['Exorcista', 'Terror', 456, 130],
    3: ['Jhon Whik', 'Acao', 123, 120]
}

for indice in filmes: #pesquisar como trazer dois valores?
    print(f'Filme: {filmes[indice][0]}')
    print(f'Gênero: {filmes[indice][1]}')
    print(f'Duração: {filmes[indice][3]}')
    print('-------')