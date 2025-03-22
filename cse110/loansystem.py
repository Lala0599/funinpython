#function to get rating from 1 to 10
def get_rating(prompt) :
    while True:
        try:
            rating = int(input(prompt))
            if 1 <= rating <= 10:
                return rating
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 10.")
            
#get user inputs
loan_size = get_rating("How large is the loan? (1-10): ")
credit_history = get_rating("How good is your credit history? (1-10): ")
income = get_rating("How high is your income? (1-10): ")
down_payment = get_rating("How large is your down payment? (1-10): ")

#decision logic
decision = False

if loan_size >= 5:
    if credit_history >= 7 and income >= 7:
        decision = True
    elif credit_history >= 7 or income >=7:
        if down_payment >= 5:
            decision = True
        else:
            decision = False
    else:
        decision = False
else:
    if credit_history < 4:
        decision = False
    else:
        if income >= 7 or down_payment >= 7:
            decision = True
        elif income >= 4 and down_payment >=4:
            decision = True
        else:
            decision = False

#display
if decision:
    print("Decision: Yes, you qualify for the loan!")
else:
    print("Decision: No, you do not qualify for the loan.")
    
        