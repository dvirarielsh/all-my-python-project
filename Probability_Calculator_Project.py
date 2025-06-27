import copy
import random

class Hat:
    def __init__(self,**kwargs):
        self.contents =[]
        for key,value in kwargs.items():
            for i in range(value):
                self.contents.append(key)
    def draw(self,num):
        if num > len(self.contents):
            d = copy.deepcopy(self.contents)
            self.contents = []
            return d
        return [self.contents.pop(self.contents.index(random.choice(self.contents))) for _ in range(num)]
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    N=num_experiments
    M=0
    for i in range(N):
        hat1 = copy.deepcopy(hat)
        list_draw = hat1.draw(num_balls_drawn)
        d= True
        for  j in expected_balls:
            if expected_balls[j]> list_draw.count(j) and d ==True:
                d = False
        if d == True:
            M +=1
    return M/N
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)