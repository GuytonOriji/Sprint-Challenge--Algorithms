'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #if theres any text at all
    if len(word) < 1:
        return 0
        #checks if the 1st 2 char's are th
    elif word[0:2] == 'th':
        return 1 + count_th(word[2:])
        #if not skip em an start from char's after them an
        #run it back through to check those
    else:
        return count_th(word[1:])