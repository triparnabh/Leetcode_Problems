def nextGreaterElement(nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':

    output_list = []
    #counter = 0

    for element in nums1:
        if nums2.index(element) == len(nums2)-1:
            output_list.append(-1)
        else:
            for x in range(nums2.index(element)+1, len(nums2)):
                if nums2[x] > element:
                    output_list.append(nums2[x])
                    break

            output_list[] = (-1)

    return output_list


def main():

    nums1 = [1,3,5,2,4]
    nums3 = [-1,5,-1,4,5]
    nums2 = [2,4,3,5,1]

    result = nextGreaterElement(nums1, nums2)
    print(result)

main()

# abc = [10,20,30,4]
# efg = [10,30,6]
# #
# print (abc.index(4))
# print (len(abc)-1)