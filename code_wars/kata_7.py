def nb_year(p0, percent, aug, p):
   years = 0
   while p0 < p:
       p0 = p0 + p0 * (percent / 100) + aug
       p0 = int(p0)
       years ++ 1
   return years


print(nb_year(1500, 2, 000, 5000), 15)
print((nb_year(1500000, 2.5, 10000, 2000000), 10))
