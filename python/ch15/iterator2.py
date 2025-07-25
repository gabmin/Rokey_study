class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data - 1)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration

        result = self.data[self.index]
        self.index -= 1
        return result


if __name__ == "__main__":
    ri = ReverseIterator([1, 2, 3, 4, 5])
    for item in ri:
        print(item)
