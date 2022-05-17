import string
import turtle as tur

def print_info():
    print("""
          List of instruction:
          P [number] -- select color pen num [1-15] (default 1)
          D -- pen down
          U -- pen up           
          W [number] -- move to west by number
          N [number] -- move north by number           
          E [number] -- move east by number           
          S [number] -- move south by number
          """)
    
def parse_line(line: string):
    instrution = line.split('#')[0]
    instrution = instrution.split(' ')
    command = instrution[0]
    number = None
    if is_need_number(command):
        try:
            number = int(instrution[1].rstrip())
        except BaseException:
            raise SyntaxError(f"Command {command} need valid number")
        return (command, number)
    return (command,)
        
    
def is_need_number(command: string):
    if (command == "D" or command == "U"):
        return False
    return True

def from_instruction_to_turtle(instruction):
    command = instruction[0]
    number = None
    if is_need_number(command):
        number = instruction[1]
    
    match command:
        case 'P':
            tur.pencolor(num_to_color(number))
        case 'D':
            tur.pendown()
        case 'U':
            tur.penup()
        case 'W':
            tur.setheading(180)
            tur.forward(number * 100)
        case 'N':
            tur.setheading(90)
            tur.forward(number * 100)
        case 'E':
            tur.setheading(0)
            tur.forward(number * 100)
        case 'S':
            tur.setheading(270)
            tur.forward(number * 100)
        case _:
            raise SyntaxError(f"Command {command} not found")
        
def num_to_color(number):
    match ((number - 1) % 15) + 1:
        case 1:
            return "white"
        case 2:
            return "blue"
        case 3:
            return "cyan"
        case 4:
            return "teal"
        case 5:
            return "green"
        case 6:
            return "lime"
        case 7:
            return "yellow"
        case 8:
            return "brown"
        case 9:
            return "orange"
        case 10:
            return "red"
        case 11:
            return "coral"
        case 12:
            return "pink"
        case 13:
            return "purple"
        case 14:
            return "black"
        case 15:
            return "gray"