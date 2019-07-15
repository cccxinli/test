# from sklearn import svm
# x = [[0,0],[1,1]]
# y = [0,1]
# clf = svm.SVC()
# clf.fit(x,y)

import csv

test = open('./test.csv','r+')
total = open('./total.csv','r+')
final = open('./final.csv','w+')
test_lines = test.readlines()
k = 0
for line in total:
    if k<=60 :
        a = test_lines[0].split(',')
        final.write('%s,%s,%s,%s,%s,%s' % (line.rstrip(), a[1], a[2], a[3], a[4], a[5]))
    else:
        a = test_lines[(k-1)//60].split(',')
        final.write('%s,%s,%s,%s,%s,%s'%(line.rstrip(),a[1],a[2],a[3],a[4],a[5]))
    k += 1
    if k ==185:
        break
final.close()
test.close()
total.close()
