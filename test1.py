class Solution(object):
    def numComponents(self, head, G):
        connected = {}
        if head is None:
            return
        counter = 0
        temp = head
        while (temp):
            if temp.next == None:
                connected[temp.val] = "None"
                break
            connected[temp.val] = temp.next.val
            temp = temp.next

        for key in connected:
            if connected[key] == "None" and key in G:
                counter += 1

        for i in range(len(G) - 1):
            for j in range(i + 1, len(G)):
                if G[i] in connected and (G[j] == connected[G[i]]):
                    counter += 1
        return counter                              