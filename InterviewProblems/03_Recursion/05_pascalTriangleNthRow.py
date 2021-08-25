
def pascal_print(line_number):

        if line_number == 0:
            return [1]

        else:
            line = [1]

            last_line = pascal_print(line_number - 1)

            for i in range(len(last_line) - 1):
                line.append(last_line[i] + last_line[i+1])

            line += [1]

        return line


print(pascal_print(3))
print(pascal_print(4))
print(pascal_print(5))