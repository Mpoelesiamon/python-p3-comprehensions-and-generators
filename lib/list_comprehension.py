# list_comprehension.py

def return_evens(seq):
    return [num for num in seq if num % 2 == 0]

def make_exclamation(sentences):
    return [sentence + '!' for sentence in sentences]

# Test return_evens
evens_test = return_evens([0, 1, 3, 5, 7, 8, 9])
print(evens_test)

exclamation_test = make_exclamation(["Hello", "I'm doing great", "Python is fun"])
print(exclamation_test)
