from cgi import print_environ_usage
from operator import index
from re import I, X
from typing import List
from unittest import result


# def sumsol(h):
#     sum = 0
#     for i in h :
#         sum =sum+ i 
#     return sum
# k =(2,4,3,6,8)
# print(sumsol(k))


def runningsum(nums:List[int])->List[int]:
    output= []
    previous_sum =0
    for num in nums:
        previous_sum = previous_sum+num
        output.append(previous_sum)
    return output
k = (4,6,7)
print(runningsum(k))

# def twosums(nums,target):
#     fin =[]

#     for num in range(len(nums)):
#         for i in range(num+1,len(nums)):
#             sum = nums[num] + nums[i]
#             if sum == target:
#                 fin.append(index(num))
#                 fin.append(index(i))
#                 return fin
                

# p =5

# print(twosums(k,p))

# def palindrome(x):
#     x = str(x)
#     reversedx = x[::-1] 
#     if x == reversedx:
#         return True
#     else:
#         return False

# print(palindrome(102))



# def longest_subString(x):
#     charset = set()
#     lent = 0
#     result=0
#     for i in range(len(x)):
#         while x[i] in charset:
#             charset.remove(x[i])
#             lent+=1
#         charset.add(x[i])
#         result = max (result,i-lent+1)
#     return result ,i,lent

        
# print(longest_subString("pwwkew"))

    
