import math
def BMI_calc(name , height ,weight):
    Ans = weight / (math.sqrt(height))
    print (f"Hi {name} your height is {height} and your weight is {weight} BMI calculation is {abs(Ans)}")
    if Ans > 27 :
        print("You are overweight")
    else :
        print("You are not overweight")

#N1  = BMI_calc ("YK", 2 , 90)
#N2  = BMI_calc ("YK sister", 1.8 , 70)
N3  = BMI_calc("YK brother" , 2.5, 160)

#print(N1)