l = [
    {"goal": 15, "assists": 29},
    {"goal": 18, "assists": 39},
    {"goal": 13, "assists": 42},
    {"goal": 5, "assists": 43},
    {"goal": 33, "assists": 45},
    {"goal": 15, "assists": 61}
]

for i,p in enumerate(l):
    s = p["assists"]+p["goal"]
    print(f"index = {i}, score={s}")
    print(p)

# r = l[0:len(l)]
l = [ 56,44, 57, 55, 48, 78, 76 ]
r = [ 56,44, 57, 55, 48, 78, 76 ]
# 0 = 44, 0 = 44
# 0 = 44, 1 = 57
# [57, 44, ...]
# 0 =  44, 2 = 55
# [57, 55, 44 ...]
# ...
# [ 57, 55, 48, 78, 76, 44 ]
# 1 = 57, 1 = 57
# 1 = 57, 2 = 55
# 1 = 57, 3 = 48
print("-----------------------------------------")
print("-----------------------------------------")
print("-----------------------------------------")
print("-----------------------------------------")

for i in range(len(r)):
    for j in range(len(r)-1-i,0,-1):
        n = len(r)-j-i-1
        s = n+1
        if(r[s] > r[n]):
            t = r[n]
            r[n] = r[s]
            r[s] = t
            print("-----------------------------------------")
            print(r)
            print("-----------------------------------------")
            

for i,p in enumerate(r):
    print(f"index = {i}, score={p}")