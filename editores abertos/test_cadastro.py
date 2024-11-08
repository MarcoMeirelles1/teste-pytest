from cliente import Cliente
from cadastro_clientes import CadastroCliente
def test_cadastro_cliente_com_sucesso():

    cliente = Cliente('will',20,'will@teste.com')
    cadastro_cliente = CadastroCliente()
    resposta = cadastro_cliente.cadastrar_cliente(cliente)
    assert resposta == "Cadastro ok,criado"
