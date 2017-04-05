#!/usr/bin/python
# -*- coding: utf-8 -*-

import collections

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        graph = [[] for i in range(n)]
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        p1 = self.FindLongestPath(graph, 0)
        p2 = self.FindLongestPath(graph, p1[-1])

        if len(p2) % 2: return [p2[len(p2)/2]]
        else:           return [p2[len(p2)/2 - 1], p2[len(p2)/2]]

    def FindLongestPath(self, graph, root):
        queue = collections.deque([[root]])
        traversed = set([root])
        while queue:
            path = queue.pop()
            for v in graph[path[-1]]:
                if v not in traversed:
                    queue.appendleft(path + [v])
                    traversed.add(v)
        return path

print(Solution().findMinHeightTrees(147,[[0,1],[1,2],[0,3],[3,4],[2,5],[5,6],[1,7],[2,8],[0,9],[1,10],[8,11],[8,12],[6,13],[11,14],[12,15],[9,16],[14,17],[4,18],[4,19],[15,20],[20,21],[2,22],[8,23],[14,24],[15,25],[21,26],[18,27],[21,28],[24,29],[14,30],[27,31],[20,32],[21,33],[29,34],[27,35],[0,36],[19,37],[3,38],[19,39],[26,40],[17,41],[40,42],[24,43],[29,44],[31,45],[8,46],[10,47],[5,48],[33,49],[18,50],[3,51],[17,52],[34,53],[0,54],[2,55],[16,56],[46,57],[53,58],[27,59],[1,60],[21,61],[44,62],[9,63],[40,64],[12,65],[63,66],[27,67],[62,68],[7,69],[24,70],[34,71],[26,72],[20,73],[35,74],[48,75],[73,76],[65,77],[0,78],[6,79],[74,80],[70,81],[39,82],[23,83],[28,84],[56,85],[56,86],[49,87],[8,88],[56,89],[14,90],[9,91],[43,92],[65,93],[84,94],[75,95],[28,96],[5,97],[49,98],[94,99],[8,100],[92,101],[93,102],[77,103],[83,104],[63,105],[61,106],[32,107],[54,108],[44,109],[29,110],[68,111],[110,112],[12,113],[49,114],[31,115],[53,116],[53,117],[39,118],[90,119],[2,120],[114,121],[69,122],[110,123],[120,124],[90,125],[121,126],[61,127],[9,128],[47,129],[123,130],[25,131],[89,132],[77,133],[127,134],[12,135],[63,136],[84,137],[101,138],[98,139],[40,140],[112,141],[19,142],[55,143],[88,144],[49,145],[95,146]]))