#Temmp.p
#  # # with open ("movies1.txt", "w") as file:
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
#            print("Invalid choice. Please try again.")
            
    


# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
#     print("Result: ", result)
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# except ValueError:
#     print("Error: Invalid input. Please enter a valid number.")      
              
              
# def add_numbers(num1, num2):
#      return num1 + num2

# result = add_numbers(5, 10) 
# print("The sum is:", result)




# square = [x**2 for x in range(1,11)]
# print(square)



# name = ["John", "Alice", "Bob", "Eve", "Charlie"]
# short_name = [n for n in name if len(n) <= 4]
# print(short_name)


# import math
# print (math.sqrt(16))  # Output: 4.

# with open ("dairy.txt", "a") as file:
#     content = file.write("Day 2: I built a journal logger today.\n")


# JOURNAL_FILE = "daily_journal.txt"

# def add_entry():
#     entry = input("Enter your journal entry: ")
#     with open(JOURNAL_FILE, "a") as file:
#         file.write(entry + "\n")
#     print("Entry added successfully.")    
    
# def view_entries():
#     try:
#         with open(JOURNAL_FILE, "r") as file:
#             content = file.read()
#             if content:
#                 print("Your journal entries:")
#                 print(content)
#             else:
#                 print("No entries found.")
#     except FileNotFoundError:
#         print("No entries found.")

#json data handling


# # MINI TODO APP using JSON

# import json
# import os
 
# TODO_FILE = "todo_list.json")

# if not os.path.exists(TODO_FILE):
#     with open(TODO_FILE, "w") as file:
#         json.dump([], file)  # Initialize an empty list in the JSON file

# def load_todo_list():
#     with open(TODO_FILE, "r") as file:
#         return json.load(file)

# def save_task_list(todo_list):
#     with open(TODO_FILE, "w") as file:
#         json.dump(todo_list, file)


# from urllib import response

# import requests

# API_KEY = "3b95d5ceeb5fc644d66366733b450d5b"  #
# city = "London"  # Replace with your desired city
# url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

# response = requests.get(url)
# if response.status_code == 200:
#     print("Weather data fetched successfully!")
#     weather_data = response.json()
# else:
#     print("Failed to fetch weather data. Please check the city name or API key.")


# from datetime import datetime
# current_time = datetime.now()
# print("Current date and time:", current_time)

# event_date = datetime (2024, 6, 15, 10, 30)  # Example event date and time
# print("Event date and time:", event_date)

# current_time = datetime.now()
# formatted_time = current_time.strftime("%m-%d-%Y %H:%M:%S")
# print("Formatted time:", formatted_time)