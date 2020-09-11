import random

option_default = ['rock', 'paper', 'scissors']

new_name = input('Enter your name:')
print('Hello,', new_name)
names_scores = {}

file_ = open('rating.txt', 'r')
for line in file_:
        name_t, score_t = line.split()
        names_scores[name_t] = int(score_t)

if new_name in names_scores:
    new_score = names_scores[new_name]
else:
    new_score = 0
    names_scores[new_name] = new_score

new_option_string = input()
if new_option_string == '':
    option = option_default
else:
    option = new_option_string.split(',')

print("Okay, let's start")
indes = len(option)

score_list = [50, 0, 100]

input_ = input()
while input_ != '!exit':

    if input_ == '!rating':
        print('Your rating:', names_scores[new_name])

    elif input_ not in option:
        print('Invalid input')

    else:
        result = random.randint(0, indes - 1)

        comp = option[result]
        result_text = [f'There is a draw ({comp})', f'Sorry, but the computer chose {comp}',
                       f'Well done. The computer chose {comp} and failed']

        if input_ == comp:
            print(result_text[0])
            names_scores[new_name] += score_list[0]
                                                                         #   There is a draw and update the score
                                                                         #   There is not a draw in below
        else:

            index_ = 0
            condition = []
            for i in range(indes):                                        #  To get index for the input
                if option[i] == input_:
                    index_ = i

            if index_ == indes - 1:  # The input is the last option.
                for i in range(indes - 1):
                    condition.append(option[i])

            elif index_ == 0:       # The input is the first option
                for i in range(1, indes):
                    condition.append(option[i])

            else:
                for i in range(index_ + 1, indes):
                    condition.append(option[i])
                for i in range(index_ -1):
                    condition.append(option[i])

            if comp not in condition[0: int((indes - 1) / 2)]:
                print(result_text[2])
                names_scores[new_name] += score_list[2]
            else:
                print(result_text[1])
    input_ = input()
print('Bye!')
