set1 = set([1,2,3,4,5,6, 1, 1, 2])
set2 = {'hi', 456, 244, 6546}
set1.add(15)
set1.add('True')
set1.update({66,55,33,34}, set2)
set1.remove(5)
# discard does not give error when not present
set1.discard(555555555555)
print(set1)


sa = {1,2,3}
sb = {2,3,4}
sc = {3,4,5}

# identical values from each set with intersection
inter_sets = sa.intersection(sb, sc)
diff_sets = sa.difference(sb, sc)
diff_sets_sb = sb.difference(sa)
print(inter_sets)
print(diff_sets)
print(diff_sets_sb)

# get all different values from each set  
# 1 appears in sa and 4 appears in sb so these are unique and returns {1,4}

symmetric_sets = sa.symmetric_difference(sb)
print(symmetric_sets)

