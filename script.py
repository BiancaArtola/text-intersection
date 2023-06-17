import sys

def find_intersecting_words(string1, string2):
    # Get the words from each string
    words1 = set(string1.split())
    words2 = set(string2.split())

    # Find the intersecting words
    intersecting_words = words1.intersection(words2)

    return intersecting_words

# Check if the required number of arguments is provided
if len(sys.argv) != 3:
    print("Usage: python script.py string1 string2")
else:
    string1 = sys.argv[1]
    string2 = sys.argv[2]
    result = find_intersecting_words(string1, string2)
    print(result)
