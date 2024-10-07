# Only integer can be entered 
list = []
store_value = int(input('Enter how many you need to store in the list: '))

for i in range(store_value):
    val = int(input('Enter the value: '))  # Move input inside the loop
    list.append(val)

print(list)
