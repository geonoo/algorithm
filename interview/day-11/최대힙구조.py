class BinanryMaxHeap:
    def __init__(self):
        self.item = [None]

    def __len__(self):
        return len(self.item)-1

    def percolate_up(self):
        cur = len(self)
        parent = cur // 2

        while parent > 0:
            if self.item[cur] > self.item[parent]:
                self.item[cur], self.item[parent] = self.item[parent], self.item[cur]

            cur = parent
            parent = cur//2

    def percolate_down(self, cur):
        big = cur
        left = cur * 2
        right = cur * 2 + 1

        if left <= len(self) and self.item[big] < self.item[left]:
            big = left
        if right <= len(self) and self.item[big] < self.item[right]:
            big = right

        if cur != big:
            self.item[cur], self.item[big] = self.item[big], self.item[cur]
            self.percolate_down(big)

    def insert(self, k):
        self.item.append(k)
        self.percolate_up()

    def extract(self):
        if len(self) < 1:
            return None
        root = self.item
        self.item[1] = self.item[-1]
        self.item.pop()
        self.percolate_down(1)
        return root