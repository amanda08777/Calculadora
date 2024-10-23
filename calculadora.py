def somar_numeros(a, b):
    """Função que soma dois números."""
    return a + b

def obter_numero(mensagem):
    """Função para obter um número do usuário, garantindo que seja um valor válido."""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def main():
    print("Bem-vindo ao programa de soma!")
    
    
    num1 = obter_numero("Digite o primeiro número: ")
    num2 = obter_numero("Digite o segundo número: ")
    
    
    resultado = somar_numeros(num1, num2)
    
    
    print(f"A soma de {num1} e {num2} é: {resultado}")

if __name__ == "__main__":
    main()
