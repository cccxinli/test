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

�鿴Զ�̿���Ϣ��ʹ��git remote -v��
�����½��ķ�֧��������͵�Զ�̣��������˾��ǲ��ɼ��ģ�
�ӱ������ͷ�֧��ʹ��git push origin branch-name���������ʧ�ܣ�����git pullץȡԶ�̵����ύ��
�ڱ��ش�����Զ�̷�֧��Ӧ�ķ�֧��ʹ��git checkout -b branch-name origin/branch-name�����غ�Զ�̷�֧���������һ�£�
�������ط�֧��Զ�̷�֧�Ĺ�����ʹ��git branch --set-upstream branch-name origin/branch-name��
��Զ��ץȡ��֧��ʹ��git pull������г�ͻ��Ҫ�ȴ����ͻ��

����git tag <name>�����½�һ����ǩ��Ĭ��ΪHEAD��Ҳ����ָ��һ��commit id��
git tag -a <tagname> -m "blablabla..."����ָ����ǩ��Ϣ��
git tag -s <tagname> -m "blablabla..."������PGPǩ����ǩ��
����git tag���Բ鿴���б�ǩ��
����git push origin <tagname>��������һ�����ر�ǩ��
����git push origin --tags��������ȫ��δ���͹��ı��ر�ǩ��
����git tag -d <tagname>����ɾ��һ�����ر�ǩ��
����git push origin :refs/tags/<tagname>����ɾ��һ��Զ�̱�ǩ��