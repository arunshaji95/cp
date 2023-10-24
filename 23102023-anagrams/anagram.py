# A word w is an anagram of a word v if a permutation of the letters transforming w into v exists. 
# Given a set of n words of length at most k, we would like to detect all possible anagrams
# Average time complexity is O(nk log k), worst case is O(n2k log k)
input_str = "below the car is a rat drinking cider and bending its elbow while this thing is an arc that can act like a cat which cried during the night caused by pain in its bowel"
dictionary = dict()
for w in list(set(input_str.split(" "))):
    s = ''.join(sorted(w))
    if s in dictionary:
        dictionary[s].append(w)
    else:
        dictionary[s] = [w]
st = [dictionary[s] for s in dictionary if len(dictionary[s]) > 1]
print(st)
