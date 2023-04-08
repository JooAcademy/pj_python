
# dataset = ["abcabc", "bbab", "cccc", "abaaa", "bdfad"]
# total = 0
# for data in dataset:
#     count = data.count('a')
#     total = total + count

# print ('a의 개수는', total)

# data, dataset, count, total 모두 그냥 변수임


dataset = ["abcabc", "bbab", "cccc", "abaaa", "bdfad"]

total = 0

for data in dataset:
    for i in range(len(data)):
        if data[i] == 'a':
            total += 1
            
print ('a의 개수는', total)


itemA = [ "abcabc", "bbab", "cccc", "abaaa", "bdfad"]
hap = 0

for i in itemA:
    su = i.count("a")
    hap = hap + su
    
print("a의 개수는 " , hap)



