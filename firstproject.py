


# My attempt at it


# What will be filled out in the print section, empty strings
phrase = ['']



# Create input of say something
def say_something(input):
    something = input('say something: ')
    while something in input:
        if input != 'done':
            phrase = phrase + something
        else:
# print out statement of whats  input
            print(phrase)
        





# Instructor solution
def sentence_maker(phrase):
    interrogatives = {'how', 'what', 'why'}
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)



results = []

while True:
    user_input = input('say something: ')
    if user_input == '\end':
        break
    else:
        results.append(user_input)


print(results)