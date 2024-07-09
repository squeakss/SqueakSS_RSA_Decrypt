def List_M_Values(d, n):
    cipher_textblocks = [, , , , , , , , , , , , ]
    m_values = []  # Initialize an empty list to store the plaintext blocks
    for i in cipher_textblocks:
        m = (i ** d) % n
        m_values.append(m)  # Append the decrypted block to the list
    return m_values  # Return the list of decrypted blocks

d = 
n = 
m_values = List_M_Values(d, n)
print(m_values)