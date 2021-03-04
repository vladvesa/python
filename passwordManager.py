from hashlib import sha256

master_password = "1234"
password_file = open("PasswordStorage.txt", "a+")


def create_pass(key, service, master_pass):
    return sha256(master_pass.encode("utf-8") + service.lower().encode("utf-8") + key.encode("utf-8")).hexdigest()[:10]


def add_pass(master_pass, service):
    hex_key = sha256(master_pass.encode("utf-8") + service.lower().encode("utf-8")).hexdigest()
    password_file.write(hex_key + "\n")
    return create_pass(hex_key, service, master_pass)


def get_pass(master_pass, service):
    pass_from_file = ""
    hex_key = sha256(master_pass.encode("utf-8") + service.lower().encode("utf-8")).hexdigest()
    for line in password_file:
        if line == hex_key:
            pass_from_file = line
    return create_pass(pass_from_file, service, master_pass)


connection = input("Give master password: ")
while connection != master_password:
    connection = input("Give master password: ")

if connection == master_password:
    while True:
        print("What would you like to do?")
        print("1. Create and store password")
        print("2. Get password")
        print("0. Exit")
        print()
        option = input("Give desired command: ")
        print()

        if option == "1":
            service = input("Give app or website for which you want to store password: ")
            print("Generated password: " + add_pass(service, master_password))
        if option == "2":
            service = input("Give app or website for which you want to retrieve password:")
            print("Retrieved password: " + get_pass(service, master_password))
        if option == "0":
            break

password_file.close()
