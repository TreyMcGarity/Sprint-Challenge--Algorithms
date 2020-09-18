'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #if no word, no th's
    if len(word) == 0:
        return 0
    # if last 2 characters are "th"
    if word[:2] == "th":
        # increment count and 
        # recall without first character
        return 1 + count_th(word[1:])
    # if not don't increment count and
    # recall without first character
    return 0 + count_th(word[1:])
    
print(count_th("ththhellothth"))