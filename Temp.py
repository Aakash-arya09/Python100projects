# # with open ("movies1.txt", "w") as file:
# #     content = file.write("New movie added.")             
# #     print(content)


# with open ("movies.txt", "a") as file:
#     content = file.write("New movie added. may i come in")             
#     print(content)


#Note taking app 

FILE_NAME = "notes.txt"

def show_menu():
    print("1. Add a new note")
    print("2. View all notes")
    print("3. Delete all notes")
    print("4. Exit")
    
def add_note():
    note = input("enter your note: ")
    with open(FILE_NAME, "a") as file:
        file.write(note + "\n")
    print("Note added successfully.")
    
def view_notes():
    try:
        with open(FILE_NAME, "r") as file:
            content = file.read()
            if content:
                print("Your notes:")
                print(content)
            else:
                print("No notes found.")
    except FileNotFoundError:
        print("No notes found.")