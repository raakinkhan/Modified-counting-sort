#  my own sorting algorithm

#  so the algorithm is that we will find the min value, then instead of checking yes or no .., we will generate our own future number and check using set whether it exists inside or not


#  version 2 using flaps... genrates dummies for that many numbers and if nothing found its gonna change its pivot or hook to the new min and repeat the algorithm

s = {9, 8, 7, 6, 5, 4, 3, 2, 1, -1, -2, -3, -4}

maxv = max(s)  # max for entire program
flaps = 0  # the amt to check
limit = 2

sorted_list = []
sorted_ = set()


def raakin(set_=s):
    global flaps, limit
    set_f = set_ - sorted_
    print(set_f)
    minv = min(set_f)
    gen = minv
    for i in range(minv, maxv + 1):
        if gen in s:
            sorted_.add(gen)
            sorted_list.append(gen)
            flaps = 0
        else:
            flaps += 1
        if flaps > limit:
            raakin(set_=s)
            break
        gen += 1


raakin()

print(sorted_list)

