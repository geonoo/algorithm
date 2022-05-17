class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None]*k
        self.maxlen = k
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.q[self.rear] is None:
            self.q[self.rear] = value
            # rear값이 +1 이되고, 원형이 때문에 rear 값이 maxlen를 초과했을때,
            # 다시 처음 인덱스로 시작해야 하기 때문에 maxlen으로 나눈 나머지 값을 넣어야 한다.
            self.rear = (self.rear + 1) % self.maxlen
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.q[self.front] is None:
            return False
        else:
            self.q[self.front] =None
            self.front = (self.front + 1) % self.maxlen
            return True


    def Front(self) -> int:
        return -1 if self.q[self.front] is None else self.q[self.front]

    def Rear(self) -> int:
        # rear 값은 enQueue할 때 현재 rear에서 값을 넣은 다음에 rear값을 +1 해주기 때문에,
        # rear 값을 -1 해줘야 마지막으로 들어간 데이터값을 확인할 수 있다.
        return -1 if self.q[self.rear - 1] is None else self.q[self.rear - 1]

    def isEmpty(self) -> bool:
        if self.front == self.rear and self.q[self.front] is None:
            return True
        return False

    def isFull(self) -> bool:
        return self.front == self.rear and self.q[self.front] is not None

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()