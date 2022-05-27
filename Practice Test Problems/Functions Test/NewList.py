#Finding unique elements in a list
def unique(ll):
    d = {}
    for i in ll:
        d[i] = ll.count(i)
    temp = min(d.values())
    uniq = [key for key in d if d[key] == temp]
    return uniq[0]
print(unique([1,1,1,1,2]))
print(unique([3,3,3,7,3,3,3,3]))
print(unique([0,0,0.85,0,0]))
print(unique([0,1,1,1,1,1,1,1]))
print(unique([1,1,1,111,1,1,1,1]))

print()

#Caluclating the century of a given year
def find_century(yr):
    year = str(yr)
    half1 = year[:2]
    half2 = year[2:]
    cen = int(half1)
    if half2 != "00":
        cen += 1
    return cen
print(find_century(2005))
print(find_century(1950))
print(find_century(1900))
print(find_century(2259))