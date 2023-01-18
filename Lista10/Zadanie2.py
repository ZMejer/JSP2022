from itertools import combinations

class Podlisty():
    def __init__(self,l:list):
        self.l = l
        self.lists = []
        for i in range(len(l)+1):
            self.lists += [list(j) for j in combinations(self.l, i)]
    def subl(self):
        return self.lists
        
                

test = Podlisty([1,2,3])
print(test.subl())