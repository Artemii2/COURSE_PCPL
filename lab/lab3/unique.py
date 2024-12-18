class Unique(object):
    def __init__(self, items, ignore_case=False):
        self.ignore_case = ignore_case
        self.items = set()
        self.index = 0
        
        for item in items:
            if ignore_case and isinstance(item, str):
                item = item.lower()
            self.items.add(item)
        
        self.unique_items = list(self.items)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.unique_items):
            result = self.unique_items[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
        
iter=Unique([1 , 2 ,2 ,4])

for i in iter:
    print(i)