from werkzeug.security import generate_password_hash, check_password_hash

test = generate_password_hash("123qweasdzxcghost")

print(test)

print(check_password_hash(test, "123qweasdzxcghost"))

