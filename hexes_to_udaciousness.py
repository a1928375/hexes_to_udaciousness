def hexes_to_udaciousness(n, spread, target):
    
    if n>=target:
        return 0
    else:
        return 1+hexes_to_udaciousness(n*(1+spread), spread, target)
        
# 0 more needed, since n already exceeds target
print hexes_to_udaciousness(100000, 2, 36230) 

# after 1 hexamester, there will be 50000 + (50000 * 2) Udacians
print hexes_to_udaciousness(50000, 2, 150000) 

# need to match or exceed the target
print hexes_to_udaciousness(50000, 2, 150001)

# only 12 hexamesters (2 years) to world domination!
print hexes_to_udaciousness(20000, 2, 7 * 10 ** 9) 

# more friends means faster world domination!
print hexes_to_udaciousness(15000, 3, 7 * 10 ** 9)
