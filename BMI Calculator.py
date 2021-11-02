print('This program will calculate you BMI')
name = input("Please enter you name: ")
weight = float(input("Please enter you weight in KGs: "))
height = float(input("Please enter you height in CM: "))

bmi = weight / height**2

if bmi < 25:
    print('{} is underweight by {} BMI'.format(name, bmi))
else:
    print('{} is overweight by {} BMI'.format(name, bmi))