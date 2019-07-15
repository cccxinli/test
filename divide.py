import os,shutil
import random
def mymovefile(srcfile,dstfile):
    if not os.path.isfile(srcfile):           #判断文件是否存在
        print ("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.move(srcfile,dstfile)          #移动文件
        print ("move %s -> %s"%( srcfile,dstfile))

trainDirRoot = './total-data/train/'
valDirRoot = './total-data/val/'
list = os.listdir(trainDirRoot)  # 列出文件夹下所有的目录名与文件名，不包含二级文件
print(list)
for i in range(0, len(list)):
    srcPath = trainDirRoot + list[i]
    valDir = valDirRoot + list[i]
    if not os.path.exists(valDir):
        os.makedirs(valDir)            # 创建路径
    imgList = os.listdir(srcPath)
    for j in range(len(imgList)//3):
        index = random.randint(0,len(imgList)-1-j)
        srcImgPath = os.path.join(srcPath,imgList[index])
        valImgPath = os.path.join(valDir,imgList[index])
        #print(len(imgList))
        #print(srcImgPath, valImgPath)
        mymovefile(srcImgPath, valImgPath)
        j += 1
    # imgList = os.listdir(valDir)
    # for j in range(len(imgList)):
    #     srcImgPath = os.path.join(srcPath, imgList[j])
    #     valImgPath = os.path.join(valDir, imgList[j])
    #     mymovefile(valImgPath, srcImgPath)
    #     j += 1
    i += 1
    # if i == 2:
    #     break

