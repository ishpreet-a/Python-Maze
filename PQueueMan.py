import random

class PriorityObject:
    obj = None
    priority = 0
    def __init__(self, o, p):
        self.obj = o
        self.priority = p
    #

    def Print(self):
        print(self.obj, ":", self.priority)
#

class PQueueMan:
    def __init__(self):
        self.q = []
        self.size = 0
    #

    def EnQ(self, obj, priority):
        print("Enqueued: obj:", obj, "  p:", priority)
        self.q.append(PriorityObject(obj, priority))
        self.size += 1
    #

    def DeQ(self):
        max = 0
        for obj in self.q:
            if obj.priority > max:
                max = obj.priority
            #
        #
        for obj in self.q:
            if obj.priority == max:
                self.q.remove(obj)
                obj.Print()
                self.size -= 1
                return obj
            #
        #
        return None
    #
#

# q = PQueueMan()
# q.EnQ("apple", random.randint(0, 100))
# 
# for i in range(0, 10):
#     q.EnQ(str(i), random.randint(0, 100))
# #
# 
# obj = q.DeQ()
# while (obj):
#     obj = q.DeQ()
# #
# print("end")
