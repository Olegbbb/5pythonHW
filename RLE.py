with open('RLE_input.txt', 'r',  encoding = 'UTF-8') as data:
    reading_text = data.readline()
print(reading_text)

def Uncoding(my_string: str) -> str:
    help_string = ''
    for i in range(len(my_string)):
            if  my_string[i].isalpha() and not my_string[i - 1].isdigit() :
                help_string += my_string[i] 
            elif my_string[i].isdigit():
                help_string += my_string[i + 1] * int(my_string[i])
            elif my_string[i].isalpha() and my_string [i - 1].isalpha():
                help_string += my_string[i]
    return(help_string)


def Coding(my_string):
    count = 0
    new_string = ''
    for i in range (1,len(my_string)):
        if i == 1:
            if my_string[i - 1] != my_string[i]:
                new_string = my_string[i - 1]
                count += 1
            else:
                count += 2
        else:
            if my_string[i] == my_string[i - 1]:
                count += 1
            else:
                new_string = new_string + str(count) + my_string[i - 1]
                count = 1
                if i == len(my_string) :
                    new_string = new_string + my_string[i] 
        new_string = new_string.replace('1', '')
    return new_string


if any(map(str.isdigit,reading_text)):
    print(Uncoding(reading_text))
else: print(Coding(reading_text))


