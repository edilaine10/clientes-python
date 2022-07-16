# View: o que vai para o usuário
usuario_digitado = input("Informe o seu usuário: ")
senha_digitada = input("Informe sua senha: ")

# Model: O que vem do banco de dados (BD)
usuarioBD = 'joao'
senhaBD = '123'

# Controller: a validação
if usuario_digitado == usuarioBD and senha_digitada == senhaBD:
    print("Pode entrar")
else:
    print("Usuário ou senha inválido")