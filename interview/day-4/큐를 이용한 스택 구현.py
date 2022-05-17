import collections
class MyStack:
    def __init__(self):
        self.q = collections.deque()

    def push(self, x:int):
        return self.q.append(x)

    def top(self):
        return self.q[-1]

    def pop(self):
        return self.q.pop()


    def empty(self):
        return not self.q

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

