#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ������������¶���
���ڣ�2021.11.27
"""
import numbers
import random #���������ģ��1



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name=="ʯͷ":
        return 0#�������
    elif name=="ʷ����":
        return 1#�������
    elif name =="��":
        return 2#�������
    elif name =="����":
        return 3#�������
    elif name=="����":
        return 4#�������
    else :
        print("Error:NO Correct Name")#else ֱ���������������ִ��
        return "Error:NO Correct Name"
    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��


    pass #��дִ�д���,������ɺ�passɾ��


def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number==0:#==Ϊ���ڣ�˫�����������뺺��
        return "ʯͷ" #�������
    elif number==1:
        return "ʷ����"#�������
    elif number ==2:
        return "��"#�������
    elif number ==3:
        return "����"#�������
    else :
        return "����"#�������

    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��

    # pass #��дִ�д���,������ɺ�passɾ��


def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
    """
    calculation = player_choice#��calculation��ֵ
    p=name_to_number(calculation)#���ú���  ���ֵ���
    answer=random.randint(0,5)#��������
    big=number_to_name(answer)
    print("�������ѡ��Ϊ��"+str(big))#�ں����г�����������ѡ��
    if p==0 :
        if answer in {3,4}:
            print("��Ӯ��")
        elif answer in range(1,3):
            print("����Ӯ��")
        else :
            print("ƽ��")
    if p==1:
        if answer in {0,4}:
            print("��Ӯ��")
        elif answer in {2,3}:#elif:Ϊ��if�µ���������������������
            print("����Ӯ��")
        else:
            print("ƽ��")
    if p==2:
        if answer in {0,1}:
            print("��Ӯ��")
        elif answer in {3,4}:
            print("����Ӯ��")
        else :
            print("ƽ��")
    if p==3:
        if answer in {1,2}:
            print("��Ӯ��")
        elif answer in {0,4}:
            print("����Ӯ��")
        else :
            print("ƽ��")
    if p==4:
        if answer in {2,3}:
            print("��Ӯ��")
        elif answer in {0,1}:
            print("����Ӯ��")
        else :
            print("ƽ��")






    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

    # pass #����������ʾ��дִ�д��룬������ɺ�ɾ����pass


# �Գ�����в���

print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)


