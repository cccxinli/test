import json
import os
import cv2
import time

print('- - - - - - step2 readcocoBegin- - - - - - ')
start = time.time()
f_instance = open('instances_val2017.json', encoding='utf-8')
data = json.loads(f_instance.read())
images = data['images']
idhash = {}
for i in range(len(images)):
    idhash[images[i]['id']] = images[i]['file_name']


f_bbox = open('results.pkl.bbox.json', encoding='utf-8')
databox = json.loads(f_bbox.read())
srcPathRoot = '../russ pic/pic total/'
savePathRoot = './test/'
k=1
thres_value = 0.85
for j in range(len(databox)):
    if databox[j]['score'] < thres_value:
        continue
    imageName = idhash[databox[j]['image_id']]
    srcPath = srcPathRoot + imageName
    xtl = int(databox[j]['bbox'][0])  
    ytl = int(databox[j]['bbox'][1])
    xbr = int(databox[j]['bbox'][0] + databox[j]['bbox'][2])
    ybr = int(databox[j]['bbox'][1] + databox[j]['bbox'][3])
    img = cv2.imread(srcPath)
    crop = img[ytl:ybr, xtl:xbr]  
    cropImgPath = savePathRoot + '/' + str(xtl) + '_' + str(ytl)+ '_' + str(xbr)+ '_' + str(ybr) + '_'+ imageName
    cv2.imwrite(cropImgPath, crop)  
    k+=1
end = time.time()
print('threshold value is : %f \n %d crop images saved in /root/chenxinli/test' % (thres_value,k))
print('=>  step2 time cost {:.2f} s'.format(end-start) )
print('- - - - - - step2 readcocoDown- - - - - - ')
print('\n')

