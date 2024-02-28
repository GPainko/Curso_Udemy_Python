from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help = 'mostra "Olá mundo na tela',
    #type=str, tipo do argumento
    metavar='STRING',
    #default='Olá Mundo', valor padrao
    required=True,
    #nargs='+' recebe mais de um valor
    action='append',
    )
args = parser.parse_args()


if args.basic is None:
    print('Voce nao passou o valor de b.')
    print(args.basic)
else:
    print(f'o valor de basic = {args.basic}')

