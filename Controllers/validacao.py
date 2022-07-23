import Models.banco as banco

# Controller: a validação
def validar_login(usuario_digitado, senha_digitada):
    usuarioBD = banco.model_usuario()
    senhaBD = banco.model_senha()
    if usuario_digitado == usuarioBD and senha_digitada == senhaBD:
        print("Pode entrar")
    else:
        print("Usuário ou senha inválido")