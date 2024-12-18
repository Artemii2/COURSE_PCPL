import random 

def gen_random(col, mini, maxi):
    result = []
    for i in range(col):
        result.append(random.randint(mini, maxi))
    return result 

print(*gen_random(5, 1, 3))
