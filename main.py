weight = input("What is your weight:")
kg_lb = input("Is it in Kg(K) or Lbs(L): ")
lbcon = float(weight) * 2.205
kgcon = float(weight) / 2.205
if kg_lb.lower() == "l":
    print("Your weight in kg is " + str(kgcon))
elif kg_lb.lower() == "k":
    print("Your weight in lb is " + str(lbcon))
