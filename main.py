# View: o que vai para o usuário
def view():
    usuario_digitado = input("Informe o seu usuário: ")
    senha_digitada = input("Informe sua senha: ")
    controller(usuario_digitado, senha_digitada)

# Model: O que vem do banco de dados (BD)
def model_usuario():
    usuarioBD = 'joao'
    return usuarioBD

def model_senha():
    senhaBD = '123'
    return senhaBD

# Controller: a validação
def controller(usuario_digitado, senha_digitada):
    usuarioBD = model_usuario()
    senhaBD = model_senha()
    if usuario_digitado == usuarioBD and senha_digitada == senhaBD:
        print("Pode entrar")
    else:
        print("Usuário ou senha inválido")


view()
