last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

gradebook = [
  ["physics", 98], 
  ["calculus", 97], 
  ["poetry", 85], 
  ["history", 88]
]

print("1. Original List")
print(gradebook)
print("\n")

gradebook.append(["computer science", 100])
print("2. Add Computer Science to List")
print(gradebook)
print("\n")

gradebook.append(["visual arts", 93])
print("3. Add Visual Arts to List")
print(gradebook)
print("\n")

gradebook[-1][-1] = 98
print("4. Modify grade for Visual Arts")
print(gradebook)
print("\n")

gradebook[2].remove(85)
print("5. Remove numerical grade from Poetry")
print(gradebook)
print("\n")

gradebook[2].append("Pass")
print("6. Append Pass grade to Poetry")
print(gradebook)
print("\n")