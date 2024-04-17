import ply.yacc as yacc
from analizador_lexico import tokens

resultado_gramatica = []


def p_expresion(p):
    '''
    expresion : MENORQUE NOT RESERVADA RESERVADA MAYORQUE MENORQUE RESERVADA MAYORQUE MENORQUE RESERVADA MAYORQUE MENORQUE RESERVADA MAYORQUE IDENTIFICADOR IDENTIFICADOR IDENTIFICADOR MENORQUE DIV RESERVADA MAYORQUE MENORQUE DIV RESERVADA MAYORQUE MENORQUE RESERVADA MAYORQUE MENORQUE IDENTIFICADOR MAYORQUE IDENTIFICADOR IDENTIFICADOR NOT MENORQUE DIV IDENTIFICADOR MAYORQUE MENORQUE DIV RESERVADA MAYORQUE MENORQUE DIV RESERVADA MAYORQUE MAYORQUE
    '''

def p_error(p):
    global resultado_gramatica
    if p:
        resultado = "Error sintactico de tipo {} en el valor {}".format(str(p.type), str(p.value))
        print(resultado)
    else:
        resultado = "EL CODIGO ES CORRECTO".format(p)
        print(resultado)
    resultado_gramatica.append(resultado)


# instanciamos el analizador sintáctico
parser = yacc.yacc()


def prueba_sintactica(data):
    global resultado_gramatica
    resultado_gramatica.clear()

    if data.strip():
                gram = parser.parse(data)
                if gram:
                    resultado_gramatica.append(str(gram))
    else:
                print("data vacia")

    print("result: ", resultado_gramatica)
    return resultado_gramatica

# ---//aqui le movi
if __name__ == '__main__':
    while True:
        try:
            s = input(''' <!DOCTYPE html>
<HTML>
    <head>
        <title>Mi primer web</title>
    </head>
    <body>
        <h1>Hola mundo!</h1>
      </body>
</HTML> ''')
        except EOFError:
            continue
        if not s:
            continue

        prueba_sintactica(s)
