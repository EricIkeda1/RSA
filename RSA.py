# Define o expoente da chave pública e o módulo para a criptografia RSA
e = 7  # Expoente da chave pública
n = 187  # Módulo da chave pública

texto = "ATACAR BASE NORTE"

# Convertendo a cada caracter do texto em seu valor ASCII usando a função ord()
ascii_values = [ord(char) for char in texto]

# Função que implementa a criptografia RSA
# Recebe o valor m (o número a ser criptografado), e (expoente) e n (módulo)
def rsa_encrypt(m, e, n):
    # Retorna o valor criptografado c, calculando m^e mod n
    return pow(m, e, n)

# Criptografando cada valor ASCII usando a função rsa_encrypt
# Printa a lista encrypted_values contendo os valores criptografados a cada valor ASCII
encrypted_values = [rsa_encrypt(m, e, n) for m in ascii_values]

# printa a lista de valores criptografados
print("Texto criptografado:", encrypted_values)
