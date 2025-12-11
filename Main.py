from cryptography.fernet import Fernet


def GetFilePath():
    file_path = input("Input the file path: ")
    return file_path

def Add():
    file_path = GetFilePath()
    application = input("Application: ")
    password = input("Password: ")

    try:
        with open(file_path, "a") as file:
            file.write(f"{application} : {password} \n")
            print(f"{application} password saved. ")
    except Exception as e:
        print("Some error", e)

def Remove():
    file_path = GetFilePath()
    application = input("Name of website to delete: ")

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
        removed_pass = False

        with open(file_path, "w") as file:
            for line in lines:
                if not line.startswith(application + " :"):
                    file.write(line)
                else:
                    removed_pass = True
        if removed_pass:
            print(f"{application} password removed.")
        else:
            print(f"No password saved for {application}")

    except Exception as e:
        print("Error", e)

def View(): # file is getting saved but this function isn't printing it
    file_path = GetFilePath()

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            
            if not lines:
                print("No passwords yet.")
                return
            
            print("\n ----- Saved Passwords ------")
            for line in lines:
                print(line.strip()) # removes the new line char

    except Exception as e:
        print("Error", e)
    
    print("\n")
    print("\n")

def main():

    print("******* Password Manager *********")
    print("******* Version 1.0 **************")

    while True:
        print("Add password(1)")
        print("Delete Password(2)")
        print("View Password(3)")
        print("Exit(4)")
        choice = int(input("Select an option: "))

        if choice == 1:
            Add()
        elif choice == 2:
            Remove()
        elif choice == 3:
            View()
        else: 
            print("Exiting...")
            break

if __name__ == "__main__":
    main()

