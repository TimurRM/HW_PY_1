# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

def predicate(x: int, y: int, z: int) -> bool:
     if  not (x or y or z) == (not x and not y and not z):
         return True
     else:
         return False

for X in range(2):
    for Y in range(2):
        for Z in range(2):
            print(X, Y, Z)
            print(predicate(x = X, y = Y, z = Z))