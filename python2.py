# Group 19; Artem Babiienko and Sireesha Kuppampati; Nov 1, 2023.

# - - - Task:

# Create a loop to execute 100 times. For each value if the number is divisible by 5 display the word
# - Fizz. If the value is divisible by 8 display the word Buzz. If the value is divisible by both 5 and 8 display
# -- the word FizzBizz – be careful of the order of the if’s in this problem. Otherwise display just the
# --- number. A sample of the output is shown.

# To be sincere didn't expect it to be that easy and hard at the same time. After some time on stackoverflow
# got something like that. Seems small, seems to be working.

for i in range(1, 101):
    output = ""
    
    if i % 5 == 0:
        output += "Fizz"
    
    if i % 8 == 0:
        output += "Buzz"
    
    if not output:
        output = i
    
    print(output)
