para = input("Enter a Paragraph : ")
unique = []
w = para.split()
repet=[]
#w_list = [w]

print("List of words ",w)

print("Number of words :-",len(w))

for i in w:
    count = w.count(i)
    if not count > 1 and i not in unique:
        unique.append(i)
print("Total Unique words ",unique)

longNum = [0]
smallnum = [0]
for i in w:
    if len(i) > len(longNum):
        longNum = i
    
print("Longest Word in Paragraph : ",longNum)

smallnum = w[0]
for i in w:
    if len(i) < len(smallnum):
        smallnum = i

print("Smallest Number in Paragraph : ",smallnum)

for i in w:
    count = w.count(i)

    if count > 1 and i not in repet:
        repet.append(i)

print("Repeted Words :- ",repet)




