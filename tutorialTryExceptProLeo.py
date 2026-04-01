# oi leo 👋👋👋
# esse aqui é o tutorial oficial de try except ok
# ----------------------------------------------------------

# As vezes que eu utilizei o try catch foram para prevenir que o programa pare de rodar
# quando o usuário faz algo de errado.

# Por exemplo:

inteiro = int(input("Digite um valor\n"))

# Se o usuário digitar um valor que não é inteiro, o programa inteiro vai parar de funcionar

# Para contornar esse problema, a gente usa try e except!
# Exemplo:

try: # Você coloca a linha de código que pode gerar um erro dentro do "try"...
    inteiro = int(input("\nDigite um inteiro porfas\n"))
# ... E no except, você vai tratar dos possíveis erros que podem ocorrer com
# a linha de código dentro do try
except ValueError: # "ValueError" é um dos vários erros que você pode "especificar". Ao inserí-lo
                   # junto ao except, você diz ao código para tratar aquele erro específico (nesse
                   # caso, o erro que ocorre quando um valor inválido é digitado, como uma string 
                   # num tipo int)
    print("\nDigita certo zeee!")
    input()
except Exception as e: # E eu tenho quase certeza que o "Exception" só representa qualquer erro.
                       # O "as e" do lado serve para inserir uma string dentro da varíavel "e"
                       # para armazenar o erro e, se você quiser, mostrá-lo ao usuário.
    print(f"\nErro da silva: {e}")
    input()
finally: # POR ÚLTIMO, o "finally" é só um bloco que roda independente de erros ocorrerem ou não.
         # Ele vai sempre rodar no fim e é opcional tá!!!?
    print("\ntchau leo bom aprendizado 👋👋")

# O código limpo, sem comentários, fica assim:

try:
    inteiro = int(input("\nDigite um inteiro porfas\n"))
except ValueError:
    print("\nDigita certo zeee")
except Exception as e:
    print(f"\nErro da silva: {e}")
finally:
    print("\ntchau leo bom aprendizado 👋👋")

# Espero que te ajude 🎉