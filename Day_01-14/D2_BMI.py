#BMI Calculator
#100 Days of Code ! Day 2
# Don't change the code below
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
# Don't change the code above

#Write your code below this line


_BMI = weight/height**2
print(round(_BMI, 2))

if _BMI < 18.5:
    print('You are Underweight')
elif _BMI < 25:
    print('You have a Normal weight')
elif _BMI <30:
        print('You are overweight')
elif _BMI < 35:
        print('You are obese')
else:
    print('You are clinically obese')
    
weight_loss = weight - round(24.9*height**2)
weight_gain = round(18.5*height**2) - weight

max_weight = round(24.9*height**2)
min_weight = round(18.5*height**2)

if _BMI < 18.5:
    print(f"You need to gain atleast {weight_gain} kgs to be {min_weight}kg")
elif _BMI < 25:
    print(f"Continue the fitness to not go beyond {max_weight} kgs or below {min_weight} kgs")
else:
    print(f"You need to shed atleast {weight_loss} kgs to be {max_weight}kg")