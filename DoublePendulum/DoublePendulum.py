import numpy as np

class DoublePendulum:
    
    def __init__(self, pos):
        self.pos = pos
        self.reset()
    
    def reset(self):
        self.r1 = 100
        self.r2 = 100
        self.m1 = 10
        self.m2 = 10
        self.t1 = np.pi / 2
        self.t2 = np.pi / 4
        self.t1_v = 0
        self.t2_v = 0
        self.t1_a = 0
        self.t2_a = 0
        self.g = 9.81
        self.res = 0.0002
   
    def update(self, dt):
        self.t1_v += self.t1_a * dt
        self.t2_v += self.t2_a * dt
        self.t1 += self.t1_v
        self.t2 += self.t2_v
        
        self.t1_v *= 1 - self.res
        self.t2_v *= 1 - self.res
        
        n1 = self.g * (2 * self.m1 + self.m2) * np.sin(self.t1)
        n2 = self.m2 * self.g * np.sin(self.t1 - 2 * self.t2)
        n3 = 2 * np.sin(self.t1 - self.t2) * self.m2
        n4 = self.t2_v * self.t2_v * self.r2 + self.t1_v * self.t1_v * self.r1 * np.cos(self.t1 - self.t2)
        n5 = self.r1 * (2 * self.m1 + self.m2 - self.m2 * np.cos(2 * self.t1 - 2 * self.t2))
        
        self.t1_a = (-n1 - n2 - n3 * n4) / n5
       
        n6 = 2 * np.sin(self.t1 - self.t2)
        n7 = self.t1_v * self.t1_v * self.r1 * (self.m1 + self.m2)
        n8 = self.g * np.cos(self.t1) * (self.m1 + self.m2)
        n9 = self.t2_v * self.t2_v * self.r2 * self.m2 * np.cos(self.t1 - self.t2)
        n10 = self.r2 * (2 * self.m1 + self.m2 - self.m2 * np.cos(2 * self.t1 - self.t2))
        
        self.t2_a = (n6 * (n7 + n8 + n9)) / n10
        
    def get_pos(self):
        x1 = self.pos[0] + self.r1 * np.sin(self.t1)
        y1 = self.pos[1] + self.r1 * np.cos(self.t1)
        x2 = x1 + self.r2 * np.sin(self.t2)
        y2 = y1 + self.r2 * np.cos(self.t2)
        
        return (x1, y1, x2, y2)