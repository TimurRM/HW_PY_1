# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет



def week_day(num):
    
 if num == 6 or num == 7:
    return('Yes')
 elif 1 <= num < 6: 
    return('No')
 else:
    return('Please, input number from 1 to 7')

num_day = int(input("Input week's day number: "))
           
print(week_day(num = num_day))