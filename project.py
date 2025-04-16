def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100  
    bmi = weight / (height_m ** 2)
    
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"
    
    return bmi, category

try:
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in centimeters: "))
    
    bmi, category = calculate_bmi(weight, height)
    
    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"Category: {category}")

except ValueError:
    print("Please enter valid numeric inputs.")
