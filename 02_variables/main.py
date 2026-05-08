# ==========================
# VARIABLES IN PYTHON
# ==========================

# A variable is a name used to store a value so we can reuse it later.

# ❌ Inefficient way (repeating same text)

print("Ella is learning Python.")
print("Ella practices Python daily!")
print("Ella is on the right path.")

# The above approach is not efficient because if the name changes, we must update it everywhere

# ==========================
# ✔ Better way using variables
# ==========================

name = "Ella"
print() 
print(name, "is learning Python.")

print(name, "practices Python daily!")

print(name, "is on the right path.")

# Now if the name changes, we only update it once

# ==========================
# VARIABLES IN REAL LIFE EXAMPLE
# ==========================

# Describing a student profile

student_name = "John"

course = "Python Programming"

level = "Beginner"

goal = "Become a Python Developer"

print("\n----------------") #\n adds a blank line before the sentence
print("Student Profile") 
print("----------------")

print("Name:", student_name)

print("Course:", course)

print("Level:", level)

print("Goal:", goal)

# Updating variable

level = "Intermediate (after practice)"

print("\nUpdated Progress")

print("----------------")

print(student_name, "is now at", level)


# ==========================
# GAME CHARACTER PROFILE
# ==========================

# Creating a game character using variables

character_name = "Nova"

level = 1

health = 100

attack_power = 25

magic_power = 10

print("\n-------------------------")
print("🎮 Game Character Profile")
print("-------------------------")

print("Name:", character_name)

print("Level:", level)

print("Health:", health)

print("Attack Power:", attack_power)

print("Magic Power:", magic_power)

# Updating variable to level up

level = level + 1

health = health + 20

attack_power = attack_power + 10

print("\n⚔ After Level Up!") 

print("------------------")

print("Name:", character_name)

print("Level:", level)

print("Health:", health)

print("Attack Power:", attack_power)

print("Magic Power:", magic_power)