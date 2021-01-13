import hashlib
import sys

letters = "abcdefghijklmnopqrstuvwxyz0123456789"

def word_permutations(word):
    if len(word) <= 1:
        return [word]
    else:
        perms = []
        for sub_word in word_permutations(word[1:]):
            for i in range(len(sub_word)+1):
                perms.append(sub_word[:i] + word[0] + sub_word[i:])
        return perms

# Dont go beyond 5
def generateRainbow(hash, n=5):
    if(n==0):
        return [""]
    else:
        words = []
        for word in generateRainbow(hash, n-1):
            for letter in letters:
                new_word = word+letter
                words.append(new_word)
                if hashlib.sha1(new_word.encode()).hexdigest() == hash:
                    raise Exception("Password is : " + new_word)
        return words



if __name__ == "__main__":
    try:
        generateRainbow(sys.argv[1])
    except Exception as exception:
        print(exception)
    else:
        print("Password not found")
