import re

def padroniza_string(string):
    return string.apply(lambda x: " ".join(x.title().strip().split()))

# def padronizar_nomes(nomes):
#     # join junta as palavras dividias pelo split ('nome', 'sobrenome' ...)
#     # title coloca em UpperCamelCase
#     # strip tira os espaços antes e depois de cada palavra
#     return nomes.apply(lambda x: " ".join(x.title().strip().split()))

# def padronizar_cargo(cargos):
#     return cargos.apply(lambda x: " ".join(x.title().strip().split()))

# def padronizar_estado_civi(estado_civil):
    return estado_civil.apply(lambda x: " ".join(x.title().strip().split()))

def validar_email(email):
    # Padroniza o texto para minúsculo e evita qualquer espaço, inicio/meio/fim
    email = email.apply(lambda x: " ".join(x.lower().strip().split()))
    
    # Cria o padrão com regex para usar como parametro no re.match
    padrao = r'^[\w\.-]+@[\w\.-]+\.(com|com\.br|net|org|br)$'

    # Usa uma função Lambda que usa o padrão definido , voltando true se está certo, se não volta false
    return email.apply (lambda x: re.match(padrao, str(x)) is not None)

def normalizar_cfp (cpf):
    # Remover dados que não sejam números 
    cpf_ajustado = cpf.apply(lambda x: re.sub(r"\D", "", str(x)))
    # Verifica se tem 11 digitos, se não houver seta o campo para None
    return cpf_ajustado.apply(lambda x: None if len(x)!=11 else x)

def salario_para_float(salario):
    
    # Para evitar a inclusão indesejada de novos valores, verifica se já é float
    if salario.dtype == float:
        return salario
    
    # Função lambda para retirar R$
    salario = salario.apply(lambda x: re.sub(r'R\$', '', str(x)))
    # Função lambda para retirar os pontos de milhar
    salario =  salario.apply(lambda x: x.replace(".",''))
    # Função lambda para troca vírgula por ponto             
    salario =  salario.apply(lambda x: x.replace(",",'.'))
    # retorna o salario em tipo float
    return salario.str.strip().astype(float)

def formatar_salario(df):

    # Cria uma cópia do DF 
    copia_df = df.copy()

    # Faz as munças para String na cópia do DF, mudando para a apresentação em BRL
    copia_df['salario'] = copia_df['salario'].apply(
        lambda x: f'R$ {x:,.2f}'
        .replace(',', 'X')
        .replace('.', ',')
        .replace('X', '.')
    )
    print(copia_df[['nome', 'salario']])


def padronizar_data():
    print()

def padronizar_regime():
    print ()

def classificar_nivel():
    print ()


