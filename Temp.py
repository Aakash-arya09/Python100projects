# # # with open ("movies1.txt", "w") as file:
# # #     content = file.write("New movie added.")             
# # #     print(content)

# with open ("movies.txt", "a") as file:
#     content = file.write("New movie added. may i come in")             
# print(content)


# #Note taking app 

# FILE_NAME = "notes.txt"

# def show_menu():
#     print("1. Add a new note")
#     print("2. View all notes")
#     print("3. Delete all notes")
#     print("4. Exit")
    
# def add_note():
#     note = input("enter your note: ")
#     with open(FILE_NAME, "a") as file:
#         file.write(note + "\n")
#     print("Note added successfully.")
    
# def view_notes():
#     try:
#         with open(FILE_NAME, "r") as file:
#             content = file.read()
#             if content:
#                 print("Your notes:")
#                 print(content)
#             else:
#                 print("No notes found.")
#     except FileNotFoundError:
#         print("No notes found.")
        
# def delete_notes():
#     with open(FILE_NAME, "w") as file:
#         file.write("")
#     print("All notes deleted successfully.")        
    
# def main():
#     while True:
#         show_menu()
#         choice = input("Enter your choice (1-4): ")
        
#         if choice == "1":
#             add_note()
#         elif choice == "2":
#             view_notes()
#         elif choice == "3":
#             delete_notes()
#         elif choice == "4":
#             print("Exiting the program.")
#             break
#         else:
#             print("Invalid choice. Please try again.")
            
    


# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
#     print("Result: ", result)
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# except ValueError:
#     print("Error: Invalid input. Please enter a valid number.")      
              
              
def add_numbers(num1, num2):
     return num1 + num2

result = add_numbers(5, 10) 
print("The sum is:", result)






