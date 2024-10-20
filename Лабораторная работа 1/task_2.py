pages = 100
lines = 50
symbols = 25
memory_for_one_book = (4 * pages * lines * symbols)/(1024*1024)
max_V = 1.44

print("Количество книг, помещающихся на дискету:", int(max_V//memory_for_one_book))
