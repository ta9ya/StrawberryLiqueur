#!/usr/bin/env python
# -*- encoding:utf-8 -*-


class Levenshtein:
#ここで配列を立ち上げて、初期値を入れる
    def initArray(self,str1,str2):
        distance = []
        for i in range(len(str1)+1):
            distance.append([0]*(len(str2)+1))
            distance[i][0] = i
        for j in range(len(str2)+1):
            distance[0][j] = j
        return distance
#セルに値を入れる
    def editDist(self,str1,str2,distance):
        dist = [0]*3
        for i in range(1,len(str1)+1):
            for j in range(1,len(str2)+1):
                dist[0] = distance[i-1][j-1] if str1[i-1]==str2[j-1] else distance[i-1][j-1]+1
                dist[1] = distance[i][j-1]+1
                dist[2] = distance[i-1][j]+1
                distance[i][j]=min(dist)
        return distance[i][j]

    def __init__(self,str1,str2):
        self.str1 = str1
        self.str2 = str2
        Levenshtein.distance = self.initArray(str1,str2)
        Levenshtein.dist = self.editDist(str1,str2,Levenshtein.distance)


def minimumEditDistance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for index2, char2 in enumerate(s2):
        newDistances = [index2+1]
        for index1,char1 in enumerate(s1):
            if char1 == char2:
                newDistances.append(distances[index1])
            else:
                newDistances.append(1 + min((distances[index1],
                                             distances[index1+1],
                                             newDistances[-1])))
        distances = newDistances
    return distances[-1]

if __name__ == '__main__':
    str1 = 'sitting'
    str2 = 'kitten'
    leven = Levenshtein(str1,str2)
    print('class : {}'.format(str(leven.dist)))


    print('module2 : {}'.format(minimumEditDistance(str1, str2)))