
#czesto na rekrutacjach

def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 ==0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input

print(fizz_buzz(3))



# very important exercise
sentence = "This is a common interview question"

char_list = {}

for i in sentence:
    if i in char_list:
        char_list[i] += 1
    else:
        char_list[i] = 1
print(char_list)

print(sorted(char_list.items(), key=lambda kv:kv[1], reverse=True))