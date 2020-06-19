'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # # TBC
    peep1 = word.find("th")
    peep2 = word.find("TH")

    if len(word) < 1:
    	return 0
    elif peep1 < 0:
    	peep1 = 100
    	# print('if the num is not here then yes p1 is in the negatives so increase amount overload so algorithm knows its the other answer to choose')
    elif peep2 < 0:
    	# print('if the num is not here then yes p2 is in the negatives so increase amount overload so algorithm knows its the other answer to choose')
    	peep2 = 100
    if peep1 < peep2:
    	return word.count("th")
    else:
    	return word.count("TH")
