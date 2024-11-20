from src.utils.auth import encode_jwt, decode_jwt

token = encode_jwt({"username": "Ruslan Shevyrev"})

print(token)

data = decode_jwt(token)

print(data)
