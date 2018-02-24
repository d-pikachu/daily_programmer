#https://www.reddit.com/r/dailyprogrammer/comments/7yyt8e/20180220_challenge_352_easy_making_imgurstyle/
def base2(x):
    res = []
    while(x!=0):
        res.append(str(x%2))
        x = int(x/2)
    res.reverse()
    return res

def base62(x):
    res = []
    while(x):
        res.append("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"[int(x%62)])
        x = int(x/62)
    res = "".join(res)
    return res

a = int(input("num : "))
print(base62(a))

