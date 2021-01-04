
n,m,k = map(int, input().split())
array = list(map(int, input().split()))

# sum=0
# array.sort(reverse=True)
# for i in range(0,(m//(k+1))):
#     for j in range(0,k):
#         sum += array[0]
#         print("k번반복:"+str(sum))
#     sum+=array[1]
#     print("m번반복:"+str(sum))


array.sort()
first = array[n-1]
second = array[n-2]

sum = 0

while True:
    for i in range(k):
        if m==0:
            break
        sum += first
        m -= 1
    if m==0:
        break
    sum += second
    m-=1

print(sum)