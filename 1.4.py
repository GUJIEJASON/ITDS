text="数据科学与工程导论"
star= chr(0x2605)
total_len=int(len(text)+2)
for i in range(total_len):
    print(star,end=" ")
print("\n"+star,end=" ")
print(text,end="")
print(star,end="\n")
for j in range(total_len):
    print(star,end=" ")