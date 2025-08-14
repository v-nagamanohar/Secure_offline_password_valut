import base64
import os

VAULT_FILE = "vault.txt"

def encode(text):
    return base64.b64encode(text.encode()).decode()

def decode(text):
    return base64.b64decode(text.encode()).decode()

def password_strength(password):
    lenght = len(password)
    has_upper = any(c.isupper() for c in password )
    has_lower = any(c.islower() for c in password )
    has_digit  = any(c.isdigit() for c in password )
    has_sepical_char = any( c in "!@#$%^&*().,<>" for c in password)

    score = sum([lenght >= 8,has_upper,has_lower,has_digit,has_sepical_char])
    return ['Weak','Medium','Stong','Very Strong'][min(score,3)]


def add_credential():
    website = input("Website: ").strip()
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    strenght = password_strength(password)

    line = f"{website}||{username}||{password}"
    encoded_line = encode(line)

    with open(VAULT_FILE,"a",encoding="utf-8") as file:
        file.write(encoded_line + "\n")

    print("✅ Credential Saved")


def view_credential():
    if not os.path.exists(VAULT_FILE):
        print("File Not Found")
        return
    
    with open(VAULT_FILE,'+w',encoding="utf-8") as file:
        for line in file:
            decoded = decode(line.strip())
            website,username,password = decoded.split("||")
            hidden_password = "*" * len(password)
            print(f"{website} | {username} | {password}")

def update_credential():
    website_name = input("Enter the website name for updation: ").strip()

    with open(VAULT_FILE,'r',encoding="utf-8") as file:
        for line in file:
            decoded = decode(line.strip())
            website,username,password = decoded.split("||")
            if website == website_name:
                choice = input("Enter 1.For Username Update 2.For Password Update").strip
                match choice:
                    case "1":
                        print("Enter the changes now")
                        username == input("Enter New Username").strip()
                    case "2":
                        password == input("Enter New Password").strip()
            else:
                return decoded
            encoded = encode(line.strip())


def main():
    while True:
        print("\n🔒 Credential Manager")
        print("1. Add Credentials")        
        print("2. View Credentials")        
        print("3. Update Credentials")        
        print("4. Exit")        

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                add_credential()
            case "2":
                view_credential()
            case "3":
                print("Coming Soon..")
            case "4":
                print("Exiting the Program")
                break
            case _ :
                print("Choose a Valid Option") 


if __name__ == "__main__":
    main()
        

