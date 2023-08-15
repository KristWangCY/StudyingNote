import pandas as pd
# Try to research pd.Series(Case, index=[] , name='') function.
# From my perspective, It is trivial.


FirstCase = [ 1, 2, 3 ]
FirstResult = pd.Series(FirstCase)
# Build the index.

print(FirstResult)
print("FirstResult[0] =",FirstResult[0])
print("\n")
# Output:
# 0    1
# 1    2
# 2    3
# dtype: int64
# FirstResult[0] = 1



SecondCase = ["Google", "Runoob", "Wiki"]
SecondResult = pd.Series(SecondCase, index = ["x", "y", "z"])
# Alter the index.

print(SecondResult)
print("SecondResult[0] =",SecondResult[0])
print("\n")
# print("SecondResult[x] =",SecondResult[x])
# It does not work, X is just an indece.
# It does not mean that X could be used to fetch list.
#Output:
#x    Google
#y    Runoob
#z      Wiki
#dtype: object
#SecondResult[0] = Google


#ThirdCase = {x: Google, y: Runoob, z: Wiki }
#Index can only be number.
ThirdCase = {1: "Google", 2: "Runoob", 3: "Wiki"}
ThirdResult = pd.Series(ThirdCase)
print(ThirdResult)
print("\n")
#Output:
#1    Google
#2    Runoob
#3      Wiki
#dtype: object


FourthCase = {1: "Google", 2: "Runoob", 3: "Wiki"}
FourthResult = pd.Series(FourthCase, index = [1, 3], name= "Google and Wiki Class")
print(FourthResult)
#Take a part from a dictionary and set the name parameter.
#Output:
#1    Google
#3      Wiki
#Name: Google and Wiki Class, dtype: object


