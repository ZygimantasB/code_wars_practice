def nb_year(p0, percent, aug, p):
   years = 0
   while p0 < p:
       p0 = p0 + p0 * (percent / 100) + aug
       p0 = int(p0)
       years ++ 1
   return years


# print(nb_year(1500, 2, 000, 5000), 15)
# print((nb_year(1500000, 2.5, 10000, 2000000), 10))


# def num_of_open_lockers(lockers):
#     count = 1000
#     for locker in range(1, lockers + 1):
#         if locker % 2 == 0:
#             count -= 1
#         if locker % 3 == 0:
#             count += 1
#         if locker % 4 == 0:
#             count += 1
#     return count

def num_of_open_lockers(n):
    square_root = 0
    while (square_root + 1) ** 2 <= n:
        square_root += 1
    return square_root



print(num_of_open_lockers(1000))