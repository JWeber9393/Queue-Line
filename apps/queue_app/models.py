from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    age = models.IntegerField(default=0)

    def __repr__(self):
        return f'User id {User.id} is {User.first_name} {User.last_name}.'

class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def enqueue(self, x):
        while len(self.s1) != 0:
            self.s2.push(self.s1[-1])
            self.s1.pop()
        
        self.s1.append(x)

        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop() 
    
    
    def dequeue(self):

        if len(self.s1) == 0:
            print('*'*100)
            print('The queue is empty...')

        x = self.s1[-1]
        self.s1.pop()
        return x

