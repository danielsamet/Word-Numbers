def word_calc(string):
    total_val = int()

    for char in string.lower():
        try:
            total_val += alphabet[char]
        except KeyError:
            try:
                total_val += int(char) if int(char) in numbers else None
            except ValueError:
                pass

    return total_val


print("Welcome to Word Numbers!\n")

alphabet = {}
for letter in range(97, 123):
    alphabet[chr(letter)] = letter - 97 + 1

numbers = list(range(0, 10))

with open("words.txt") as f:
    words = f.read()
words = words.split("\n")

nums = {}

for word in words:
    total = word_calc(word)
    nums[total] = [] if total not in nums.keys() else nums[total]
    nums[total].append(word)

print("Please type in a number to see all of the words with that value.\n"
      "Alternatively, type a word to see its numerical value and all those in the dictionary with the same value.\n")
choice = input("")

try:
    print(nums[int(choice)]) if int(choice) in nums.keys() else print("No words found with that value.")
except (KeyError, ValueError):
    total = word_calc(choice)
    print("Your word ({choice}) has a numerical value of {value}. Here is a list of all words in the English dictionary"
          " with the same value.".format(choice=choice, value=total))
    print(nums[total]) if total in nums.keys() else print("No words found with that value.")
