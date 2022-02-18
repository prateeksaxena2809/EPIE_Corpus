idioms=open("Formal_idioms.txt")
meanings=open("Formal_idioms_meanings_final.txt")
complexities=[]
for idiom,meaning in zip(idioms,meanings):
    print(idiom)
    print(meaning)
    complexity=None
    while complexity not in ["1","2","3","4"]:
        complexity=input("does this idiom require 1.pruning, 2. agreement, 3. replacement 4.others: ")
    complexities.append(complexity)

with open("Formal_idioms_complexities.txt",'w') as fp:
    fp.write("\n".join(complexities))

