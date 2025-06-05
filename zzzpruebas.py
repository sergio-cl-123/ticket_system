from werkzeug.security import check_password_hash, generate_password_hash

a= generate_password_hash("hola", method='pbkdf2:sha256', salt_length=8)
print(a)

