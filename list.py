#
# Learning Lists
# Mikel Manitius
# Mon Jan 22 16:32:33 EST 2018
#
# Pre-Nika
#
# Define initial family members
#
manitius = [ 'mikel', 'marjon', 'carina', 'natalie' ]

#
# show the list
#
print(manitius)

#
# how many members are there?
#
family_members = len(manitius)
print("There are", family_members, "members in the family.")

#
# print each name individually, capitalizing each name
#
for first_name in manitius:
	print(first_name.title())

#
# break
#
print("--- let's try that again ---")

#
# now print the list again, numbered
# just learning the for construct in Phyton
#
for n in range(0,family_members):
	print(n+1, manitius[n].title())

if 'nika' in manitius:
	print("Nika has been born!")
else:
	print("Nika has not yet been born")

print("\n--- now comes one more ---\n")

#
# Post Nika
#
# Add Nika to the list of family members
#
manitius.append("nika")
print(manitius)

family_members = len(manitius)
print("There are", family_members, "members in the family.")
for first_name in manitius:
	print(first_name.title())

print("--- let's try that again ---")

for n in range(0,family_members):
	print(n+1, manitius[n].title())

if 'nika' in manitius:
	print("Nika has been born!")
else:
	print("Nika has not yet been born")
