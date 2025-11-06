# --- Python Basics: Dictionaries, Classes, and File Operations (Consolidated Code) ---

# --- 1. Dictionaries Examples ---

# Example 1: Creating and Accessing a Student Scores Dictionary
print("--- Dictionary Example 1: Basic Student Scores Dictionary Creation and Access ---")
student_scores = {
    "Alice": 95,
    "Bob": 88,
    "Charlie": 72,
    "Diana": 90
}
print(f"Alice's score: {student_scores['Alice']}")
print(f"Charlie's score: {student_scores['Charlie']}")
non_existent_student_score = student_scores.get("Eve", "N/A")
print(f"Eve's score (using .get()): {non_existent_student_score}")


# Example 2: Modifying and Adding Elements in a Student Scores Dictionary
print("\n--- Dictionary Example 2: Modifying and Adding Elements in a Student Scores Dictionary ---")
student_scores = {
    "Alice": 95,
    "Bob": 88,
    "Charlie": 72
}
student_scores["Bob"] = 90
print(f"Updated Bob's score: {student_scores['Bob']}")
student_scores["Eve"] = 85
print(f"Added Eve's score: {student_scores['Eve']}")
print("Current student scores dictionary:", student_scores)


# Example 3: Iterating Through a Student Scores Dictionary
print("\n--- Dictionary Example 3: Iterating Through a Student Scores Dictionary ---")
student_scores = {
    "Alice": 95,
    "Bob": 88,
    "Charlie": 72,
    "Diana": 90
}
print("Student names and their scores:")
for name, score in student_scores.items():
    print(f"{name}: {score}")

print("\nStudents who scored 90 or above:")
for name, score in student_scores.items():
    if score >= 90:
        print(f"{name} (Score: {score})")

print("\nOnly student names (keys):")
for name in student_scores.keys():
    print(name)

print("\nOnly scores (values):")
for score in student_scores.values():
    print(score)


# Example 4: Managing Student Data with Two Separate Lists (Mimicking Dictionary)
print("\n--- Dictionary Example 4: Using Two Separate Lists for Student Data ---")
student_names_list = ["Alice", "Bob", "Charlie", "Diana"]
student_scores_list = [95, 88, 72, 90]

try:
    bob_index = student_names_list.index("Bob")
    print(f"Bob's score: {student_scores_list[bob_index]}")
except ValueError:
    print("Bob not found in the list.")

new_student_name = "Eve"
new_student_score = 85
student_names_list.append(new_student_name)
student_scores_list.append(new_student_score)
print(f"Added {new_student_name} with score {new_student_score}.")

try:
    charlie_index = student_names_list.index("Charlie")
    student_scores_list[charlie_index] = 75
    print(f"Updated Charlie's score: {student_scores_list[charlie_index]}")
except ValueError:
    print("Charlie not found in the list.")

print("\nAll student names:", student_names_list)
print("All student scores:", student_scores_list)

print("\nIterating through names and scores (using indices):")
for i in range(len(student_names_list)):
    print(f"{student_names_list[i]}: {student_scores_list[i]}")


# --- 2. Classes Examples ---

# Example: The 'Cow' Class
print("\n--- Class Example: The 'Cow' Class ---")
class Cow:
    def __init__(self, name, color, age_years, milk_produced_liters_per_day, is_milking_cow):
        self.name = name
        self.color = color
        self.age_years = age_years
        self.milk_produced_liters_per_day = milk_produced_liters_per_day
        self.is_milking_cow = is_milking_cow

    def speak(self):
        print(f"{self.name} says: Moo!")

    def eat(self, food_type):
        print(f"{self.name} is eating {food_type}.")

    def produce_milk(self):
        if self.is_milking_cow:
            print(f"{self.name} produced {self.milk_produced_liters_per_day} liters of milk today.")
            return self.milk_produced_liters_per_day
        else:
            print(f"{self.name} is not a milking cow.")
            return 0.0

cow1 = Cow("Daisy", "black and white", 4, 28.5, True)
cow2 = Cow("Bessie", "brown", 2, 0.0, False)

print(f"{cow1.name} is a {cow1.color} cow, {cow1.age_years} years old.")
print(f"{cow2.name} is a {cow2.color} cow, {cow2.age_years} years old.")

cow1.speak()
cow2.eat("hay")

cow1.produce_milk()
cow2.produce_milk()


# Example 1: Basic Class as a "Structure"
print("\n--- Class Example 1: Basic Class as a 'Structure' ---")
class Point:
    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord

point1 = Point(10, 20)
point2 = Point(-5, 0)

print(f"Point 1 coordinates: ({point1.x}, {point1.y})")
print(f"Point 2 coordinates: ({point2.x}, {point2.y})")


# Example 2: Class with Methods (Adding Behavior)
print("\n--- Class Example 2: Class with Methods ---")
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_read = False

    def display_info(self):
        read_status = "Read" if self.is_read else "Unread"
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}, Status: {read_status}")

    def mark_as_read(self):
        self.is_read = True
        print(f"'{self.title}' has been marked as read.")

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
book2 = Book("1984", "George Orwell", 328)

book1.display_info()
book2.display_info()

book1.mark_as_read()
book1.display_info()


# --- 3. File Operations Examples ---

# Example 1: Writing to a File ('w' mode - write, overwrites existing file)
file_name_write = "my_notes.txt"
content_to_write = "This is the first line of my notes.\nThis is the second line.\nAnd this is the third."

print(f"\n--- File Operations Example 1: Writing to '{file_name_write}' ---")
try:
    with open(file_name_write, 'w') as file:
        file.write(content_to_write)
    print(f"Successfully wrote content to '{file_name_write}'.")
except IOError as e:
    print(f"Error writing to file: {e}")


# Example 2: Appending to a File ('a' mode - append)
file_name_append = "my_notes.txt"
content_to_append = "\n\nAdding a new line at the end."

print(f"\n--- File Operations Example 2: Appending to '{file_name_append}' ---")
try:
    with open(file_name_append, 'a') as file:
        file.write(content_to_append)
    print(f"Successfully appended content to '{file_name_append}'.")
except IOError as e:
    print(f"Error appending to file: {e}")


# Example 3: Reading from a File ('r' mode - read)
file_name_read = "my_notes.txt"

print(f"\n--- File Operations Example 3: Reading from '{file_name_read}' ---")
try:
    with open(file_name_read, 'r') as file:
        full_content = file.read()
        print("\n--- Full Content ---")
        print(full_content)

    with open(file_name_read, 'r') as file:
        print("\n--- Content Line by Line ---")
        for line_num, line in enumerate(file, 1):
            print(f"Line {line_num}: {line.strip()}")
except FileNotFoundError:
    print(f"Error: The file '{file_name_read}' was not found.")
except IOError as e:
    print(f"Error reading file: {e}")


# Example 4: Reading Line by Line with readline()
file_name_readline = "my_notes.txt"

print(f"\n--- File Operations Example 4: Reading Line by Line with readline() ---")
try:
    with open(file_name_readline, 'r') as file:
        line1 = file.readline()
        line2 = file.readline()
        line3 = file.readline()
        print(f"First line: {line1.strip()}")
        print(f"Second line: {line2.strip()}")
        print(f"Third line: {line3.strip()}")
except FileNotFoundError:
    print(f"Error: The file '{file_name_readline}' was not found.")
except IOError as e:
    print(f"Error reading file: {e}")


# Example 5: Reading All Lines into a List with readlines()
file_name_readlines = "my_notes.txt"

print(f"\n--- File Operations Example 5: Reading All Lines into a List with readlines() ---")
try:
    with open(file_name_readlines, 'r') as file:
        all_lines = file.readlines()
        print("All lines as a list:")
        for i, line in enumerate(all_lines):
            print(f"List item {i}: {line.strip()}")
except FileNotFoundError:
    print(f"Error: The file '{file_name_readlines}' was not found.")
except IOError as e:
    print(f"Error reading file: {e}")


# Example 6: Writing a List of Strings with writelines()
file_name_writelines = "new_list_content.txt"
lines_to_write = [
    "Item 1: Apple\n",
    "Item 2: Banana\n",
    "Item 3: Cherry\n"
]

print(f"\n--- File Operations Example 6: Writing a List of Strings with writelines() ---")
try:
    with open(file_name_writelines, 'w') as file:
        file.writelines(lines_to_write)
    print(f"Successfully wrote list of strings to '{file_name_writelines}'.")

    with open(file_name_writelines, 'r') as file:
        print("\nContent of new_list_content.txt:")
        print(file.read())
except IOError as e:
    print(f"Error writing to file: {e}")
