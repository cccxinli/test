git add  file 添加
git commit -m "xxx"  提交
git diff      查看修改
git log       查看提交历史
git reflog    查看命令历史
git reset --hard HEAD^ (HEAD~n) 或commit id   回退
cat file      查看文件内容
命令git checkout -- readme.txt意思就是，把readme.txt文件在工作区的修改全部撤销，让这个文件回到最近一次git commit或git add时的状态。
git push origin master 推送到GitHub