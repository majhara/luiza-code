from genericpath import exists
from math import prod
from operator import contains
import re
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel


app = FastAPI()

OK = "OK"
FALHA = "FALHA"


# Classes
## Classe representando os dados do endereço do cliente
class Endereco(BaseModel):
    rua: str
    cep: str
    cidade: str
    estado: str


## Classe representando os dados do cliente
class Usuario(BaseModel):
    id: int
    nome: str
    email: str
    senha: str


## Classe representando a lista de endereços de um cliente
class ListaDeEnderecosDoUsuario(BaseModel):
    usuario: Usuario
    enderecos: List[Endereco] = []


## Classe representando os dados do produto
class Produto(BaseModel):
    id: int
    nome: str
    descricao: str
    preco: float


# Classe representando o carrinho de compras de um cliente com uma lista de produtos
class CarrinhoDeCompras(BaseModel):
    id_usuario: int
    id_produtos: List[Produto] = []
    preco_total: float
    quantidade_de_produtos: int

#Coleções
## Coleção usuários
db_usuarios = {}
## Coleção produtos
db_produtos = {}
## Coleção endereços usuarios
db_end = {}        # enderecos_dos_usuarios
## Coleção carrinho
db_carrinhos = {}


# Persistências
## Persistências usuários
def persistencia_salvar_usuario(novo_usuario: Usuario):
    db_usuarios[novo_usuario.id] = novo_usuario.dict()
    return novo_usuario

def persistencia_deletar_usuario(id: int): 
    db_usuarios.pop(id)

def persistencia_buscar_usuario_pelo_id_usuario(id: int):
    if id in db_usuarios:
        return db_usuarios[id]
    return None

def persistencia_buscar_usuario_pelo_nome(nome: str):
    for usuario in db_usuarios.values():
        if usuario["nome"] == nome:
            return usuario
    return None

def persistencia_buscar_email_por_dominio(dominio: str):
    EMAILS_MESMO_DOMINIO = []
    ...


## Persistências endereços    
def persistencia_salvar_endereco(lista_endereco_usuario: ListaDeEnderecosDoUsuario):
    db_end[lista_endereco_usuario.usuario.id] = lista_endereco_usuario.dict()
    return lista_endereco_usuario

def persistencia_buscar_enderecos_pelo_id_usuario(id_usuario: int):
    if id_usuario in db_end:
        endereco_encontrado = db_end[id_usuario]
        return endereco_encontrado
    return None

def persistencia_buscar_enderecos_pelo_id_endereco(id_endereco: int):
    if id_endereco in db_end:
        endereco_encontrado = db_end[id_endereco]
        return endereco_encontrado
    return None
    
def persistencia_deletar_endereco_pelo_id_endereco(id_endereco: int):
    endereco = persistencia_buscar_enderecos_pelo_id_endereco(id_endereco)
    if endereco == None:
        return FALHA
    db_end.pop(endereco[id_endereco])
    return OK


## Persistências produtos
def persistencia_salvar_produto(novo_produto: Produto):
    db_produtos[novo_produto.id] = novo_produto.dict()
    return novo_produto

def persistencia_deletar_produto_pelo_id(id_produto: int):
    if id_produto not in db_produtos:
        return False
    db_produtos.pop(id_produto)
    return True
    
def persistencia_buscar_produto_pelo_id(id_produto: int):
    if id_produto in db_produtos:
        produto_encontrado = db_produtos[id_produto]
        return produto_encontrado
    return None



## Persistencias carrinho
def persistencia_salvar_carrinho(novo_carrinho: CarrinhoDeCompras):
    db_carrinhos[novo_carrinho.id_usuario] = novo_carrinho.dict()
    return novo_carrinho
    
def persistencia_buscar_carrinho_pelo_id_usuario(id_usuario: int):
    if id_usuario in db_carrinhos:
        carrinho_encontrado = db_carrinhos[id_usuario]
        return carrinho_encontrado
    return None


def persistencia_deletar_carrinho(id_usuario: int):
    db_carrinhos.pop(id_usuario)


# Serviços
## Serviços usuarios 

def servico_validar_cadastro_usuario(novo_usuario: Usuario):   
    usuario_existente = persistencia_buscar_usuario_pelo_id_usuario(novo_usuario.id)
    if(usuario_existente != None):
        return 'USUARIO JÁ EXISTE'
    valida_email = '@'
    if valida_email not in novo_usuario.email:
        return 'FALHA AO INSERIR EMAIL'
    if len(novo_usuario.senha) < 3:
        return 'AUMENTE SUA SENHA'
    novo_usuario = persistencia_salvar_usuario(novo_usuario)
    return novo_usuario

def servico_buscar_usuario_pelo_id(id: int):
    usuario_buscado = persistencia_buscar_usuario_pelo_id_usuario(id)
    if usuario_buscado == None:
        return False
    return usuario_buscado


def servico_buscar_usuario_pelo_nome(nome: str):
    usuario_buscado = persistencia_buscar_usuario_pelo_nome(nome)
    if usuario_buscado == None:
        return False
    return usuario_buscado
    
           
def servico_deletar_usuario_por_id(id: int):
    usuario = persistencia_buscar_usuario_pelo_id_usuario(id)
    if usuario == None:
         return False
    persistencia_deletar_usuario(id)
    return True

  
## Serviços endereços

def servico_validar_cadastro_endereco(endereco: Endereco, id_usuario: int): 
    usuario_buscado = persistencia_buscar_usuario_pelo_id_usuario(id_usuario)
    if usuario_buscado == None:
        return False
    lista_endereco_usuario = vincular_endereco_usuario(endereco, usuario_buscado)
    persistencia_salvar_endereco(lista_endereco_usuario)
    return True   
  
def vincular_endereco_usuario(endereco: Endereco, usuario: Usuario):
    lista_vinculada_ao_usuario = persistencia_buscar_enderecos_pelo_id_endereco(usuario["id"])
    if lista_vinculada_ao_usuario == None:       
        lista_vinculada_ao_usuario = ListaDeEnderecosDoUsuario(usuario=usuario)
        lista_vinculada_ao_usuario.enderecos.append(endereco)
        print(lista_vinculada_ao_usuario)
        return lista_vinculada_ao_usuario
    lista_vinculada_ao_usuario = ListaDeEnderecosDoUsuario.parse_obj(lista_vinculada_ao_usuario)
    lista_vinculada_ao_usuario.enderecos.append(endereco)
    return lista_vinculada_ao_usuario

def servico_deletar_endereco_pelo_id_endereco(id_endereco: int):
    endereco_encontrado = persistencia_buscar_enderecos_pelo_id_endereco(id_endereco)
    if endereco_encontrado == None:
        return False
    endereco_encontrado.pop(id_endereco)
    return True


# Serviços produtos
def servico_validar_regras_cadastro_produto(produto: Produto):
    if produto.id in db_produtos:
        return False
    persistencia_salvar_produto(produto)
    return True

def servico_buscar_produto_pelo_id(id_produto):
    produto_buscado = persistencia_buscar_produto_pelo_id(id_produto)
    if produto_buscado == None:
        return False
    return produto_buscado

def servico_deletar_produto_pelo_id(id_produto):
    produto_buscado = persistencia_buscar_produto_pelo_id(id_produto)
    if produto_buscado == None:
        return False
    persistencia_deletar_produto_pelo_id(id_produto)
    return True 


# Serviços carrinho
def servico_validar_cadastro_carrinho(id_usuario: int, id_produto: int):
    # Verificar se meu usuario existe
    usuario_buscado = servico_buscar_usuario_pelo_id(id_usuario)
    produto_buscado = servico_buscar_produto_pelo_id(id_produto)
    if usuario_buscado == False or produto_buscado == False:
        return False
    return True

def servico_criar_carrinho(id_usuario: int, id_produto: int):
    if servico_validar_cadastro_carrinho(id_usuario, id_produto) == False:
        return None
    produto_pedido = servico_buscar_produto_pelo_id(id_produto)
    produto_pedido = Produto.parse_obj(produto_pedido)
    carrinho_de_compras = CarrinhoDeCompras(id_usuario=id_usuario, preco_total=0, quantidade_de_produtos=0)
    servico_vincular_produto_ao_carrinho(carrinho_de_compras, produto_pedido)
    if persistencia_salvar_carrinho(carrinho_de_compras) == None:
        return False
    return True 
    
# Se não existir carrinho com o id_usuario retornar falha, 
# senão retorna o o número de itens e o valor total do carrinho de compras. 
def servico_buscar_qtd_e_valor_carrinho_pelo_id_usuario(id_usuario: int):
    carrinho_encontrado = servico_buscar_carrinho_pelo_id_usuario(id_usuario)
    if carrinho_encontrado == False:
        return False
    carrinho_encontrado = CarrinhoDeCompras.parse_obj(carrinho_encontrado)
    lista_valor_qtd_carrinho = {"preco_total": carrinho_encontrado.preco_total, "quantidade_produtos": carrinho_encontrado.quantidade_de_produtos}
    return lista_valor_qtd_carrinho
     
def servico_vincular_produto_ao_carrinho(carrinho_de_compras: CarrinhoDeCompras, produto: Produto):
    carrinho_de_compras.id_produtos.append(produto)
    carrinho_de_compras.preco_total += produto.preco 
    carrinho_de_compras.quantidade_de_produtos = carrinho_de_compras.quantidade_de_produtos + 1
    return carrinho_de_compras

def servico_adicionar_produto_ao_carrinho(carrinho_de_compras: CarrinhoDeCompras, id_produto: int):
    produto_buscado = servico_buscar_produto_pelo_id(id_produto)
    if produto_buscado is False: return False
    produto_buscado = Produto.parse_obj(produto_buscado)
    carrinho_de_compras = CarrinhoDeCompras.parse_obj(carrinho_de_compras)
    carrinho_com_produto = servico_vincular_produto_ao_carrinho(carrinho_de_compras, produto_buscado)
    carrinho_com_produto  = persistencia_salvar_carrinho(carrinho_com_produto)
    if carrinho_com_produto is None: return False
    return True


def servico_buscar_carrinho_pelo_id_usuario(id_usuario: Usuario):
    carrinho_buscado = persistencia_buscar_carrinho_pelo_id_usuario(id_usuario)
    if carrinho_buscado == None: return False
    return carrinho_buscado
    
# Remover produtos do carrinho
def servico_deletar_produto_carrinho(id_usuario: int, id_produto: int):
    carrinho_buscado = servico_buscar_carrinho_pelo_id_usuario(id_usuario)
    if carrinho_buscado == False: return False
    carrinho_buscado = CarrinhoDeCompras.parse_obj(carrinho_buscado)
    produto_buscado = servico_buscar_produto_pelo_id(id_produto)
    if produto_buscado == False: return False
    produto_buscado = Produto.parse_obj(produto_buscado)
    carrinho_buscado.id_produtos.remove(produto_buscado)
    carrinho_buscado.preco_total = carrinho_buscado.preco_total - produto_buscado.preco
    carrinho_buscado.quantidade_de_produtos = carrinho_buscado.quantidade_de_produtos - 1       
    persistencia_salvar_carrinho(carrinho_buscado)
    return True
       
def servico_deletar_carrinho(id_usuario: int):
    usuario_buscado = servico_buscar_usuario_pelo_id(id_usuario)
    if usuario_buscado == False:
        return False
    carrinho_buscado = servico_buscar_carrinho_pelo_id_usuario(id_usuario)
    if carrinho_buscado == False:
        return False
    persistencia_deletar_carrinho(id_usuario)
    return True

# Se não existir usuário com o id_usuario ou id_produto, retornar falha; 
# se não existir um carrinho vinculado ao usuário, crie o carrinho
# e retornar OK
# senão adiciona produto ao carrinho e retornar OK
    
    
# Criar um usuário,
# se tiver outro usuário com o mesmo ID retornar falha, 
# se o email não tiver o @ retornar falha, 
# senha tem que ser maior ou igual a 3 caracteres, 
# senão retornar OK
@app.post("/usuario/")
async def criar_usuario(novo_usuario: Usuario):
    return servico_validar_cadastro_usuario(novo_usuario)
     

# Se o id do usuário existir, retornar os dados do usuário
# senão retornar falha 
@app.get("/usuario/")
async def retornar_usuario_pelo_id(id: int):
    usuario_buscado = servico_buscar_usuario_pelo_id(id)
    if usuario_buscado == False:
        return FALHA
    return usuario_buscado

# Se existir um usuário com exatamente o mesmo nome, retornar os dados do usuário
# senão retornar falha OK
@app.get("/usuario/nome")
async def retornar_usuario_pelo_nome(nome: str):
    usuario = servico_buscar_usuario_pelo_nome(nome)
    if usuario is False:
        return FALHA
    return usuario

# Se o id do usuário existir, deletar o usuário e retornar
# senão retornar falha OK
# ao deletar o usuário, deletar também endereços e carrinhos vinculados a ele
@app.delete("/usuario/")
async def deletar_usuario(id: int):
    if servico_deletar_usuario_por_id(id) == False:
        return FALHA
    return OK
   

# Retornar todos os emails que possuem o mesmo domínio
# (domínio do email é tudo que vêm depois do @)
# senão retornar falha
@app.get("/usuarios/emails/")
async def retornar_emails(dominio: str):
    ...


# Se não existir usuário com o id_usuario retornar falha, 
# senão cria um endereço, vincula ao usuário e retornar OK
@app.post("/endereco/{id_usuario}/")
async def criar_endereco(endereco: Endereco, id_usuario: int):
    if servico_validar_cadastro_endereco(endereco, id_usuario) == False:
        return FALHA
    return OK


# Se não existir usuário com o id_usuario retornar falha,
# senão retornar uma lista de todos os endereços vinculados ao usuário
# caso o usuário não possua nenhum endereço vinculado a ele, retornar 
# uma lista vazia
### Estudar sobre Path Params (https://fastapi.tiangolo.com/tutorial/path-params/)
@app.get("/usuario/{id_usuario}/enderecos/")
async def retornar_enderecos_do_usuario(id_usuario: int):
    usuario = persistencia_buscar_usuario_pelo_id_usuario(id_usuario)
    if usuario == None:
        return FALHA
    return persistencia_buscar_enderecos_pelo_id_usuario(id_usuario)
    # return persistencia_buscar_enderecos_pelo_id_usuario(id_usuario)


# ---------------------------- FALTA FAZER --------------------------------------------  
# Se não existir endereço com o id_endereco retornar falha, 
# senão deleta endereço correspondente ao id_endereco e retornar OK
# (lembrar de desvincular o endereço ao usuário)
@app.delete("/endereco/{id_endereco}/")
async def deletar_endereco(id_endereco: int):
    servico_deletar_endereco_pelo_id_endereco(id_endereco)
    return OK


# Se tiver outro produto com o mesmo ID retornar falha, 
# senão cria um produto e retornar OK
@app.post("/produto/")
async def criar_produto(novo_produto: Produto):
    if servico_validar_regras_cadastro_produto(novo_produto) == False:
        return FALHA
    return OK


@app.get("/produto/{id_produto}/")
async def buscar_produto(id_produto: int):
    produto_buscado = servico_buscar_produto_pelo_id(id_produto)
    if produto_buscado == False:
        return FALHA
    return produto_buscado

# Se não existir produto com o id_produto retornar falha, 
# senão deleta produto correspondente ao id_produto e retornar OK
# (lembrar de desvincular o produto dos carrinhos do usuário)
@app.delete("/produto/{id_produto}/")
async def deletar_produto(id_produto: int):
    produto_buscado = servico_deletar_produto_pelo_id(id_produto)
    if produto_buscado == False:
        return FALHA
    return OK


# Se não existir usuário com o id_usuario ou id_produto, retornar falha; 
# se não existir um carrinho vinculado ao usuário, crie o carrinho
# e retornar OK
# senão adiciona produto ao carrinho e retornar OK
@app.post("/carrinho/{id_usuario}/{id_produto}/")
async def adicionar_carrinho(id_usuario: int, id_produto: int):
    carrinho_buscado = servico_buscar_carrinho_pelo_id_usuario(id_usuario)
    if carrinho_buscado == False:
        if servico_criar_carrinho(id_usuario, id_produto) == False:
            return FALHA
        return OK
    if servico_adicionar_produto_ao_carrinho(carrinho_buscado, id_produto) == False:
        return FALHA    
    return OK


# Se não existir carrinho com o id_usuario retornar falha, 
# senão retorna o carrinho de compras.
@app.get("/carrinho/{id_usuario}/")
async def retornar_carrinho(id_usuario: int):
    carrinho_buscado = servico_buscar_carrinho_pelo_id_usuario(id_usuario)
    if carrinho_buscado == False: return FALHA
    return carrinho_buscado


# Se não existir carrinho com o id_usuario retornar falha, 
# senão retorna o o número de itens e o valor total do carrinho de compras.
@app.get("/carrinho/{id_usuario}/valortotal")
async def retornar_total_carrinho(id_usuario: int):
    dados_qtd_valor_carrinho = servico_buscar_qtd_e_valor_carrinho_pelo_id_usuario(id_usuario)
    if dados_qtd_valor_carrinho == False:
        return FALHA
    return dados_qtd_valor_carrinho

#Deletar produto do carrinho de compras associado ao id_usuario
@app.delete("/carrinho/{id_usuario}/{id_produto}/")
async def remover_produto_carrinho(id_usuario: int, id_produto: int):
    produto_deletado = servico_deletar_produto_carrinho(id_usuario, id_produto)
    if produto_deletado == False:
        return FALHA
    return OK

# Se não existir usuário com o id_usuario retornar falha, 
# senão deleta o carrinho correspondente ao id_usuario e retornar OK
@app.delete("/carrinho/{id_usuario}/")
async def deletar_carrinho(id_usuario: int):
    if servico_deletar_carrinho(id_usuario) == False:
        return FALHA
    return OK
        

@app.get("/")
async def bem_vinda():
    site = "Seja bem vinda"
    return site.replace('\n', '')