#check if person qualified or disqualified
def interview(ll, total):
    d = "disqualified"
    q = "qualified"
    if total> 120:
        return d
    for i in ll[:2]: #very easy
        if i >5 :
            return d
    for i in ll[2:4]: #easy
        if i >10:
            return d
    for i in ll[4:6]: #medium
        if i >15:
            return d
    for i in ll[6:8]: #hard
        if i >20:
            return d
    return q

print(interview([5,5,10,10,15,15,20,20], 120))
print(interview([2,3,8,6,5,12,10,18], 64))
print(interview([5,5,10,10,15,15,20,20], 200))
print(interview([1,1,1,1,1,50,2,2], 60))