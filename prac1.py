#Find the Rotation Count in Rotated Sorted array
min1=arr[0]
for i in range(len(arr)):
    if min1>arr[i]:
        min1=arr[i]
        place=i
print(place)

#just find the position of min element
