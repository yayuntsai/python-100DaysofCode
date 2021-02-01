# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()
T = lower_case_name1.count("t")
R = lower_case_name1.count("r")
U = lower_case_name1.count("u")
E = lower_case_name1.count("e")
true = T + R + U + E
print(true)
L = lower_case_name1.count("l")
O = lower_case_name1.count("o")
V = lower_case_name1.count("v")
love = L + O + V + E
print(love)

love_score = true*10 + love


print("T scores " + str(T) + " times")
print("R scores " + str(R) + " times")
print("U scores " + str(U) + " times")
print("E scores " + str(E) + " times")
print("L scores " + str(L) + " times")
print("O scores " + str(O) + " times")
print("V scores " + str(V) + " times")
print("love score" + str(love_score))
