user_name = "Alice"       
user_age = 25             
user_height = 5.7         
is_active = True          

# Using f-strings (standard in 2026) for easy formatting
print(f"{user_name} is {user_age} years old.") 
fruits = ["apple", "banana", "cherry"]
fruits.append("orange") 
print(fruits[0])         


prices = [10.5, 20.0, 5.75]
print(len(prices))      
print(sum(prices))      
print(max(prices))      

def print_any_dimension(data):
   
    if isinstance(data, (list, tuple)) and not isinstance(data, str):
        for item in data:
         
            print_any_dimension(item)
    else:
      
        print(data)

my_array = [[12], [7, 8], 9,'tetr']
print_any_dimension(my_array)

file_path = "example.txt"

# Open the file in write mode ('w') and write content
with open(file_path, 'w') as file:
    file.write("Hello, world!\n")
    file.write("This is a new text file created using Python.")

print(f"File '{file_path}' created and written to successfully.")