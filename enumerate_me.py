# Without enumeration 
words = ("You", "Love", "Yourself")

for i in range(len(words)): 
  print(f"{words[i]} has {len(words[i])} letters")

# With enumeration 
words = ("You", "Love", "Yourself")

for word in words:
  print(f"{word} has {len(word)} letters")

-----------------------------------------------------------------------------------------------

# With enumeration you can also esaily access the index and the element at the same time 
words = ["You", "Love", "Yourself"]

for i, word in enumerate(words, 1):
  print(f"Word #{i}: <{word}> has {len(word)} letters")

# Enumerating directly over the list makes your code easier to write and more understandable
# Here’s the main takeaway of this chapter, for you, on a silver platter:
# enumerate is your best friend if you need to traverse an iterator to deal with its data and also
# need access to information about its index.
