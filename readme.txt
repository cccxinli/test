git add  file 添加
git commit -m "xxx"  提交
git diff      查看修改
git log       查看提交历史
git reflog    查看命令历史
git reset --hard HEAD^ (HEAD~n) 或commit id   回退
cat file      查看文件内容
命令git checkout -- readme.txt意思就是，把readme.txt文件在工作区的修改全部撤销，让这个文件回到最近一次git commit或git add时的状态。
git push origin master 推送到GitHub

Git鼓励大量使用分支：
查看分支：git branch
创建分支：git branch <name>
切换分支：git checkout <name>
创建+切换分支：git checkout -b <name>
合并某分支到当前分支：git merge <name>
删除分支：git branch -d <name>

分支合并冲突
主支修改
解决冲突