from itertools import combinations

class Podlisty():
    def __init__(self,l:list):
        self.l = l            
    def subl(self):
        self.lists = []
        self.spr = []
        self.spr += [list(j) for j in combinations(self.l, 3)]
        for i in self.spr:
            if sum(i) == 0:
                self.lists.append(i)
        return self.lists

test = Podlisty([-1,1,0,-2,3])
print(test.subl())