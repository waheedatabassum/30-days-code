N = int(input())
phone_book = {}

for i in range(N):
    a = input().split()
    phone_book[a[0]] = a[1]
  
for j in range(N):
    b = str(input())
    if b not in phone_book:
        print ("Not found")
    else:
        print (str(b) + "=" + str(phone_book[b]))
