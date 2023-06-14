preco = float(input('Digite o preço do produto: R$'))
desconto = float(input('Digite a porcentagem de desconto: '))

desc = 100 - desconto
precofinal = (preco/100) * desc

print(f'O preço final do produto com {desconto:.0f}% de desconto é: R${precofinal:.2f}')
