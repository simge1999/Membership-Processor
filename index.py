name_box = "Alice Bentall"
age_box = 20
uni_box = True
subs_box = 1.95
mkt_box = 0
name_entered = bool(name_box)
if name_entered:
  name = name_box
else:
    name = "Unknown"
if age_box <= 18:
  print("You cannot be a member")
else:
  print("Welcome to our site.")
profile = name + ", " + str(age_box)
print(profile)
universty = bool(uni_box)
print("Is this person university student:")
print(universty)
if uni_box == True :
  print("You have a %20 discount.")
print("This persons marketing number is:")
print(mkt_box)
print("This persons subscription $ :")
print(subs_box)