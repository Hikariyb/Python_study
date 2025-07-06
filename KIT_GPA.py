#金沢工業大学のGPAを計算するシステムを作ろう！！
#【条件】
# 1. 関数(関数名をchangerとすること)を使うこと(GPAの評価ポイントと評価の変換)
# 2. GPAと正課学習ポイントを表示しよう
# 【参照】
# https://www.kanazawa-it.ac.jp/campus_guide/2025/chapter_3/list_3/page_3.html
# https://www.kanazawa-it.ac.jp/campus_guide/2025/chapter_3/list_3/page_4.html

num = int(input("科目数を入力してください"))

def changer(grade):
    if grade == 'S':
        return 4
    elif grade == 'A':
        return 3
    elif grade == 'B':
        return 2
    elif grade == 'C':
        return 1
    elif grade == 'D' and grade == 'F':
        return 0
    else:
        print('不正な入力')

for i in range(num):
    grade = str(input("成績を入力してください(ex.S,A,B..)"))
    credit = int(input("単位数を入力してください"))
    total_grade += grade * credit
    total_credit += credit
    
GPA = total_grade / total_credit
    


