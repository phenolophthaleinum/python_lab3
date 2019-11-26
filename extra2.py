names = []
percents = []
bases = {'a', 'g', 't', 'c'}
gc_pairs = 0
base_count = 0
file_names = ['seq{}.genbank.txt'.format(x) for x in range (1,11)]
for file_name in file_names:
    f = open(file_name, 'r')
    names.append(f.readline().split()[1])
    f2 = f.read().split('ORIGIN')[1]
    for base in f2:
        if base in bases:
            base_count += 1
            if base == 'g' or base == 'c':
                gc_pairs += 1
    percents.append(gc_pairs/base_count)
    f.close()
for name, percent in zip(names, percents):
    print('NAME: {} G/C PERCENT: {}'.format(name, percent*100))