git add  file ���
git commit -m "xxx"  �ύ
git diff      �鿴�޸�
git log       �鿴�ύ��ʷ
git reflog    �鿴������ʷ
git reset --hard HEAD^ (HEAD~n) ��commit id   ����
cat file      �鿴�ļ�����
����git checkout -- readme.txt��˼���ǣ���readme.txt�ļ��ڹ��������޸�ȫ��������������ļ��ص����һ��git commit��git addʱ��״̬��
git push origin master ���͵�GitHub

Git��������ʹ�÷�֧��
�鿴��֧��git branch
������֧��git branch <name>
�л���֧��git checkout <name>
����+�л���֧��git checkout -b <name>
�ϲ�ĳ��֧����ǰ��֧��git merge <name>
ɾ����֧��git branch -d <name>

��֧�ϲ���ͻ
��֧�޸�
�����ͻ
��Git�޷��Զ��ϲ���֧ʱ���ͱ������Ƚ����ͻ�������ͻ�����ύ���ϲ���ɡ�
��git log --graph������Կ�����֧�ϲ�ͼ��

�޸�bugʱ�����ǻ�ͨ�������µ�bug��֧�����޸���Ȼ��ϲ������ɾ����
����ͷ����û�����ʱ���Ȱѹ����ֳ�git stashһ�£�Ȼ��ȥ�޸�bug���޸�����git stash pop���ص������ֳ���

����һ����feature������½�һ����֧��
���Ҫ����һ��û�б��ϲ����ķ�֧������ͨ��git branch -D <name>ǿ��ɾ����