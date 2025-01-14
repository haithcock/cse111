#I beleive this program exceeds requirements by
# not only being clearly labeled in the 
# volumes.txt file but also by being correctly
# labeled in English, Korean, and Chinese.  

from datetime import datetime
import math
시간 = datetime.now()
print(f"Currently it is: {시간}")



width = float(input("What is the width of the tire?  "))
aspectratio = float(input("What is the aspect ratio of the tire?  "))
diameter = float(input("What is the diameter of the tire?  "))

volume = (math.pi * width**2 * aspectratio * (width * aspectratio + 2540 * diameter)) / 10000000000
print(f"The approximate volume of the tire is {volume:.2f} liters.")
print(f"Don't forget the date and time is currently: {시간}")   

with open("volumes.txt", "a") as file: 
    file.write("\n")
    file.write(f"Date and Time / 날짜와 시간 / 日期和时间: {시간}\n")
    file.write(f"Tire Width / 타이어 폭 /轮胎宽度: {width:.1f}\n")
    file.write(f"Aspect Ratio / 비율 / 轮胎扁平比: {aspectratio:.1f}\n")
    file.write(f"Diameter / 직경 / 直径: {diameter:.1f}\n")
    file.write(f"Volume / 부피 / 体积: {volume:.2f} liters-리터-升\n")
    file.write("\n") 
print("A file has been created named 'volumes.txt' (if it doesn't exist) and data has been appended. ")