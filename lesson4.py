#linear search
l = list(map(int,input('enter a number').split(' ')))
print(l)
target = int(input('enter the target'))
for i in range(0, len(l)):
    if l[i] == target:
        print('key exists')
    else:
        print('key doesnt exist')
#time complextity is 0(n)


#binary search
def binarysearch(l1, low, high, target):
    mid = (low+high)//2
    if low<=high:
        if l1[mid] == target:
            return target
        elif l1[mid] < target:
            return binarysearch(l1, mid+1, high, target)
        elif l1[mid] > target:
            return binarysearch(l1, low, mid-1, target)
    else:
        return -1
print(binarysearch([1, 2, 3, 4, 5], 1, 5, 4))
# time comlexity is 0(logn)

# Method - 2 Iterative
arr = list(map(int, input("Enter the numbers - ").split(' ')))
key = int(input())

start = 0
end = len(arr)-1

flag = False

while start <= end:
  mid = (start + end)//2

  if arr[mid] == key:
    print("Key Found")
    flag = True
    break
  elif arr[mid] > key:
    end = mid - 1
  else:
    start = mid + 1

if flag == False:
  print("No Key Found")