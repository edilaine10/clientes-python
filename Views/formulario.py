import Controllers.validacao as validacao

# View: o que vai para o usuário
def formulario_login():
    usuario_digitado = input("Informe o seu usuário: ")
    senha_digitada = input("Informe sua senha: ")
    validacao.validar_login(usuario_digitado, senha_digitada)
