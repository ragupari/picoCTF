from Crypto.Util.number import inverse, long_to_bytes

# The values from your challenge
n = 25765585224863259003932851570018748403772540662223164795084583484853946049918701161627151706962275184667683998233830549136798579109395731824931381444954454
e = 65537 # Common default, change if your challenge says otherwise

# The ciphertext from your 'flag.enc' or 'output.txt'
# PASTE YOUR CIPHERTEXT NUMBER HERE:
ct_value = 8719527020074987025768935916367832078854605560057721766176268083920574903579953978127614658669898866537766140520706440400890918499921077331867741337795967

# Step 1: Factors found previously
p = 2
q = n // p

# Step 2: Calculate Phi
phi = (p - 1) * (q - 1)

# Step 3: Calculate Private Key (d)
d = inverse(e, phi)

# Step 4: Decrypt
m = pow(ct_value, d, n)

# Step 5: Convert to readable flag
flag = long_to_bytes(m)
print(f"Decrypted Message: {flag.decode()}")