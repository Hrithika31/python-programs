items = [("product1", 10),
         ("product2", 13),
         ("product3", 15)]

filtered = list(filter(lambda item: item[1] >= 13, items))
print(filtered) 