import os
# 标签转换
dataset = os.listdir('./rus data/train')
dataset.sort()
label_file = open('./label_trans.csv', "w")
for i in range(len(dataset)):
    label_file.write("%s,%s\n" % (i,dataset[i]))
label_file.close()