import random

ANSI_GREEN = '\033[92m'
ANSI_YELLOW = '\033[93m'
ANSI_NORMAL = '\033[0m'

def bold_text(text):
    bold_start = '\033[1m'
    bold_end = '\033[0m'
    return bold_start + text + bold_end

flag = True
slova = ["������", "������", "������", "������", "������",
         "������", "������", "������", "������", "������",
         "�����", "�����", "�����", "�����", "�����",
         "�����", "�����", "�����", "�����", "�����",
         "�����", "�����", "�����", "�����", "�����",
         "�����", "�����", "����", "����", "����"]
count = 0
vivod = list()

# ���������� ����������

slovo = random.choice(slova)
slova.remove(slovo)

# ������ �����

while ((a := input()).lower) != slovo or count < 6:
    count += 1  # ������� �������
    print(bold_text(f"����� ����� ����� {len(slovo)} ������"))
    
    
    if a == "/restart":
        slovo = random.choice(slova)
        slova.remove(slovo)
        print(bold_text("���������� �����!"))   # ������� �����������


    elif a == "/pass":
        flag = False
        break   # ������� �������


    elif a == "/help":
        print("�������� �����. � ��� ���� 6 �������. ������� ������ ����, ����� ���������.")
        print("����� ������ ������� ���� ���� ��� ������� ����� ��������, ����� ��������, ��������� ���� ������������� ���� ������ � ����������� �����:")
        print("-������ ���� ����� �������� ��� ����� ����� �� ���� �����.")
        print("-Ƹ���� ���� ����� ��������, ��� ����� ���� � �����, �� ���� �� �� ���� �����.")
        print()
        print("������ ��������� ������:")
        print()
        print("+ /help - �������� ������")
        print("+ /pass - �������")
        print("+ /restart - ����������")
        print("+ /")    # ������� ������


    elif len(a) != len(slovo) or not a.isalpha():
        print(bold_text("����� �� ��������!"))    # �������� �����


    else:
        a1 = a.split("")
        slovo1 = slovo.split("")
        
        slovo_bukvi = slovo1.copy()

        for i in range(len(slovo)):
            if a1[i] == slovo1[i]:
                vivod.append(ANSI_GREEN, a1[i], ANSI_NORMAL)
            elif a1[i] in slovo_bukvi:
                slovo_bukvi.remove(a1[i])
                vivod.append(ANSI_YELLOW, a1[i], ANSI_NORMAL)
            else:
                vivod.append(a1[i])
    print(vivod)
if flag and count <= 6:
    print("����������, �� ��������!")
else:
    print("� ��������� � ��� �� ���������� ��������.")

# ����� ��������� � ������