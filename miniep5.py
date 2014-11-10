import ply.lex as lex

#Lista de nome dos tokens
tokens = (
	'NUMBER',
	'PLUS',
	'MINUS',
	'TIMES',
	'DIVIDE',
)

#Regras de definicoes de operadores
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

#Caracteres a serem ignorados
t_ignore  = ' \t'

#Regra para definicao de numeros
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

#Regra para lidar com erro
def t_error(t):
    print ("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

#Contruir o lexer
lexer = lex.lex()

#Inicializa a pilha
stack = []

#Pede a expressão pela entrada padrão
data = input('Entre com uma expressao em notacao posfixa:\n' )

#Entra com a expressão no analizador lexico
lexer.input(data)

value = 0

while True:
	tok = lexer.token()
	
	#Para sair do loop
	if not tok: break
	
	#Coloca um token de numero na pilha
	if tok.type == 'NUMBER':
		stack.append(tok.value)
	
	#Caso seja um operador, devemos realizar a conta com os ultimos dois numeros da pilha
	elif tok.type == 'PLUS':
		value = stack.pop() + stack.pop()
		stack.append(value)
	elif tok.type == 'MINUS':
		value = stack.pop() - stack.pop()
		stack.append(value)
	elif tok.type == 'TIMES':
		value = stack.pop() * stack.pop()
		stack.append(value)
	elif tok.type == 'DIVIDE':
		value = 1/stack.pop() * stack.pop()
		stack.append(value)
		
print(stack[0])

