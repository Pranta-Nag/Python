# set is the collection of unorder items
# each element in the set must be unique & immutable

collections = {1, 3, 3, 6, 4, "hello", "world", "Pranta"}        # set ignore duplicate value

print(collections)
print(type(collections))        # print type

null_set = set()                # empty set : syntax
null_set.add("Pranta")
null_set.add("Shuvo")           # add value in the empty set
null_set.add("Nag")
null_set.add((1,2,3))           # add tuple into the set

print(null_set)

null_set.remove("Nag")          # remove value to the set
print(null_set)

print(collections.union(null_set))              # union set1(collections) and set2(null_set)
                                                # combine both set values & returns new
print(collections.intersection(null_set))       # intersection set1(collections) and set2(null_set)
                                                # combine common values & returns new

null_set.pop()                  # pop random value to the set
print(null_set)

null_set.clear()                # empties the set
print(null_set)


a = (4, 6,7, 3)

print({6,3}.issubset(a))            # subset

