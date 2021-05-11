def get_answer(prompt):
    answer = input(prompt)
#1 while not (asnwer =="yes" or answer =="no"):
#2 while answer not in ("yes", "no"):
#3 while answer not in ["yes", "no"]:

    while answer not in ("yes", "no"):
        answer = input(prompt)

    return answer


#problem with above function - duplicating code!

print(get_answer("yes or no? "))



# Redoing the function
def get_answer2(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ('yes', 'no'):
            return answer


print(get_answer2("yes or no? "))

