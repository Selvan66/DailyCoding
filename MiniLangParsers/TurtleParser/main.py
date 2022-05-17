import tparser
import turtle as tur

if __name__ == '__main__':
    with open("inst.tur") as file:
        for line in file.readlines():
            try:
                instruciton = tparser.parse_line(line)
                tparser.from_instruction_to_turtle(instruciton)
            except SyntaxError as err:
                print(err.msg)
                tparser.print_info()
                break
        tur.done()