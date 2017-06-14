import random
recipe_list = []
recipe_file = open('recipe_list.txt','r')
# Get all the recipes from the file
for recipe in recipe_file:
    # Put each recipe into the recipe_list
    recipe_list.append(recipe.strip())
    #print (line.strip())
def random_gen():
    if len(choice_list) > 0:

    # from remaining list generate random sample
        recipe_list.remove(choice_list[-1])
    r1= random.sample(recipe_list,5)
    # remove user chioce from list

    # print out sample out sign the numbers
    for i in range(5):
        print(str(i+1) + ' ' + r1[i])

    return r1
#random_list = random_gen()

# user_choice = input('\n Choose a Recipe Using Number1-5, (Q) to Quit:')

# ans = user_chioce.lower()

choice_list = []

quit_list = ["q", "quit", "end", "finished", "finish"]

first_run = True

while first_run == True or ans not in quit_list:
    first_run = False
    # generate a new random list
    random_list = random_gen()

    user_choice = input('\n Choose a Recipe Using Number1-5, (Q) to Quit:')
    try:
    # store user input as a list
        choice_list.append(random_list[int(user_choice)-1])
    except ValueError as e:
        pass
    #generate new radom list
    ans = user_choice.lower()

    # ask user to choose a recipe,


# print a new line before printing recipe
# print recipe in a  new line
print ('\n you choose:')
for recipe in choice_list:
     print (recipe)



