# Here’s the main takeaway of this chapter, for you, on a silver platter:
# zip is your friend whenever you need to traverse two or more iterables at the same time.

# Without zip 
firsts = ["Walker", "Josh", "Peter"]
lasts = ["McGilvary", "Gibson", "Zwahlen"]

for i in range(len(firsts)):
  print(f"{firsts[i]} {lasts[i]}")

# With zip
firsts = ["Walker", "Josh", "Peter"]
lasts = ["McGilvary", "Gibson", "Zwahlen"]

for firsts, lasts in zip(firsts, lasts):
  print(firsts, lasts)

# Zip makes your code easier to write, and it makes it more clear what your code is doing.
