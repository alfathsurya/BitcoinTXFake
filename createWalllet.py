import bitcore

# Generate a random 32-byte buffer
rand_buffer = bitcore.crypto.Random.getRandomBuffer(32)

# Convert the random buffer to a Bitcoin bignum
rand_number = bitcore.crypto.BN.fromBuffer(rand_buffer)

# Create a new bitcore PrivateKey object from the random bignum
private_key = bitcore.PrivateKey(rand_number)

# Convert the private key to a Bitcoin address for the mainnet network
address = private_key.to_address('mainnet')

# Print the private key and address to the console
print({
    "privatekey": private_key.to_string(),
    "address": address.to_string()
})
