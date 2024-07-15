import time
def seven_segment_display(number):
    # Dictionary mapping digits to their seven-segment display representation
    segments = {
        '0': [' _ ', '| |', '|_|'],
        '1': ['   ', '  |', '  |'],
        '2': [' _ ', ' _|', '|_ '],
        '3': [' _ ', ' _|', ' _|'],
        '4': ['   ', '|_|', '  |'],
        '5': [' _ ', '|_ ', ' _|'],
        '6': [' _ ', '|_ ', '|_|'],
        '7': [' _ ', '  |', '  |'],
        '8': [' _ ', '|_|', '|_|'],
        '9': [' _ ', '|_|', ' _|']
    }
    
    # Convert the number to a string
    number_str = str(number)
    
    # Prepare the lines for the seven-segment display
    lines = ['', '', '']
    
    # Build the seven-segment display for each digit
    for digit in number_str:
        for i in range(3):
            lines[i] += segments[digit][i] + ' '
    for line in lines:
        print(line)
        


print("Red light")
# You can change the duration by changing th first element in for loop
for i in range(20,-1,-1):
    seven_segment_display(i)
    time.sleep(1)
time.sleep(1)
print()
print("Yellow light")
for i in range(5,-1,-1):
    seven_segment_display(i)
    time.sleep(1)

print()
time.sleep(1)
print("Green light")
for i in range(20,-1,-1):
    seven_segment_display(i)
    time.sleep(1)
