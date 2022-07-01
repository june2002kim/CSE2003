#이진탐색
def binary_search(L, item):
    start=0
    finish=len(L)-1
    
    while start<=finish:
        index=(start+finish)//2
        if L[index]==item:
            return index
        elif L[index]>item:
            #start=start
            finish=index-1
        else:
            start=index+1
            #finish=finish
        
    return -1

L=[1,2,3,4,5,6,7,8,9,10]
item=int(input("찾고자 하는 정수 입력 : "))


if binary_search(L,item)!=-1:
    print(f"{item}은 L[{binary_search(L,item)}]에 존재")
else:
    print(f"{item}은 L[]에 존재하지 않음")

'''
target = 25
m_list = [30, 94, 27, 92, 21, 37, 25, 47, 25, 53, 98, 19, 32, 32, 7]
length = len(m_list)

m_list.sort()
left = 0 
right = length-1

while left<=right:
    mid = (left+right)//2
    if m_list[mid] == target:
        print(mid+1)
        break
    elif m_list[mid]>target:
        right = mid-1
    else :
        left = mid+1
'''

'''
def binarySearch(array, target, left, right):
    middle_idx = (left+right)//2
    print(middle_idx)
    middle = array[middle_idx]
    if target == middle:
        print('answer {}'.format(middle_idx))
    elif middle > target:
        binarySearch(array, target,left,middle_idx-1)
    elif middle < target:
        binarySearch(array, target,middle_idx+1,right)
    else: 
        return False

target = 25
m_list = [30, 94, 27, 92, 21, 37, 25, 47, 25, 53, 98, 19, 32, 32, 7]
length = len(m_list)

m_list.sort()
left = 0 
right = length-1

binarySearch(m_list,target,0,right)
'''
