import sys
from pympler import asizeof
from pympler import classtracker

# Calculate memory usage for a list
list_obj = [1,2,3,'abc']
print(sys.getsizeof(list_obj))
print(asizeof.asizeof(list_obj))
print(asizeof.asized(list_obj, detail=1).format())


# track memory usage for a class
class C:
    def __init__(self, iterable):
        self.data = list(iterable)

tr = classtracker.ClassTracker()
tr.track_class(C)
tr.create_snapshot()
c1 = C([1,2,3])
c2 = C([1,2,3,4,5])
tr.create_snapshot()
tr.stats.print_summary()

# track memory usage for an instance
tracker = classtracker.ClassTracker()
obj = C([1,2,3])
tracker.track_object(obj)
tracker.create_snapshot('Before adding a whole heap of data')
obj.data.append(list(range(10000)))
tracker.create_snapshot('After adding a whole heap of data')
tracker.stats.print_summary()
