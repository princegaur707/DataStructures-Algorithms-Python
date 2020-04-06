# - sign to signify desc

pairs = [(3,2),(4,5),(8,1),(1,8),(5,6)]

pairs.sort(key=lambda x: (x[0],x[1]))

print(pairs)

pairs.sort(key=lambda x: (-x[0],x[1]))

print(pairs)

pairs.sort(key=lambda x: (x[0],-x[1]))

print(pairs)

pairs.sort(key=lambda x: (-x[0],-x[1]))

print(pairs)