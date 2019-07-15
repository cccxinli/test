import json
import os
import cv2


f = open('final_data.json', encoding='utf-8')
data = json.loads(f.read())
srcPathRoot = '../russ pic/pic total/'
savePathRoot = './rus data/train/'
k = 1
for i in range(len(data)):
    imageName = data[i]['iamge_name']
    srcPath = srcPathRoot + imageName
    boxes = data[i]['bboxes']
    # for j in range(len(boxes)):
    folderName = data[i]['class']
    savePath = savePathRoot + folderName
    # if data[i]['temporary'] == 'True':
    #     folderName1 = 'temporary'
    # else:
    #     folderName1 = 'not_temporary'
    # if data[i]['occluded'] == 'True':
    #     folderName2 = 'occluded'
    # else:
    #     folderName2 = 'not_occluded'
    # if data[i]['data'] != '':
    #     folderName3 = 'data/' + data[i]['data'].replace(':','.')
    # else:
    #     folderName3 = 'not_data'
    # savePath1 = savePathRoot + folderName1
    # savePath2 = savePathRoot + folderName2
    # savePath3 = savePathRoot + folderName3
    # if not os.path.exists(savePath1):
    #     os.makedirs(savePath1)            # 创建路径
    # if not os.path.exists(savePath2):
    #     os.makedirs(savePath2)            # 创建路径
    # if not os.path.exists(savePath3):
    #     os.makedirs(savePath3)            # 创建路径
    if not os.path.exists(savePath):
        os.makedirs(savePath)  # 创建路径
    boxes = data[i]['bboxes']
    # for j in range(len(boxes)):
    xtl = int(boxes[0])  # 从文件中获取框信息，float型转int出错？直接用分割获取整数部分
    ytl = int(boxes[1])
    xbr = int(boxes[2])
    ybr = int(boxes[3])
    if (xbr-xtl)*(ybr-ytl) <200:
        continue
    img = cv2.imread(srcPath)
    crop = img[ytl:ybr, xtl:xbr]  # 裁剪图片[左上y：右下y，左上x：右下x]
    #cropImgPath = savePath + '/' + str(k).zfill(6) + '.jpg'
    cropImgPath1 = savePath1 + '/' + str(k).zfill(6) + '.jpg'
    cropImgPath2 = savePath2 + '/' + str(k).zfill(6) + '.jpg'
    cropImgPath3 = savePath3 + '/' + str(k).zfill(6) + '.jpg'
    #cv2.imwrite(cropImgPath, crop)  # 保存裁剪图
    cv2.imwrite(cropImgPath1, crop)  # 保存裁剪图
    cv2.imwrite(cropImgPath2, crop)  # 保存裁剪图
    cv2.imwrite(cropImgPath3, crop)  # 保存裁剪图
    print(k)
    k += 1
    # if k == 10:
    #     break