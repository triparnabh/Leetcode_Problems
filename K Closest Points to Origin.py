import math
import operator

class Solution(object):
    def kClosest(self, points, K):

        distance = {}
        c = 1
        output = []

        for i in points:
            dist = math.sqrt(math.pow(i[0] - 0, 2) + math.pow(i[1] - 0, 2))
            distance[str(i)] = dist

        # print (distance)

        sorted_x = sorted(distance.items(), key=operator.itemgetter(1))

        print(sorted_x)

        for i in sorted_x:
            if c <= K:
                output.append(i[0])
                c += 1
        return output
