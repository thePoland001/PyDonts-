# Without enumeration 
words = ("You", "Love", "Yourself")

for i in range(len(words)): 
  print(f"{words[i]} has {len(words[i])} letters")

# With enumeration 
words = ("You", "Love", "Yourself")

for word in words:
  print(f"{word} has {len(word)} letters")

# Enumerating directly over the list makes your code easier to write and more understandable
