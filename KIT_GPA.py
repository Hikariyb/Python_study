#金沢工業大学のGPAを計算するシステムを作ろう！！
#【条件】
# 1. 関数(関数名をchargerとすること)を使うこと(GPAの評価ポイントと評価の変換)
# 2. GPAと正課学習ポイントを表示しよう
# 【参照】
# https://www.kanazawa-it.ac.jp/campus_guide/2025/chapter_3/list_3/page_3.html
# https://www.kanazawa-it.ac.jp/campus_guide/2025/chapter_3/list_3/page_4.html

def charger(grade):
    if(grade == "S") | (grade == "s"):
        return 4
    elif(grade == "A") | (grade == "a"):
        return 3
    elif(grade == "B") | (grade == "b"):
        return 2
    elif(grade == "C") | (grade == "c"):
        return 1
    elif(grade == "D") | (grade == "d"):
        return 0
    elif(grade == "F") | (grade == "f"):
        return 0
    else:
        print("不正な成績です")
        grade = str(input("もう一度成績を入力してください(ex.S,A,B..)"))
        return charger(grade)

def is_pass_or_not(str_pass):
    #合否・認定科目かどうかを逆で判断させたいため
    if str_pass == "0":
        is_pass = True
    elif str_pass == "1":
        is_pass = False
    else:
        print("不正な入力です")
        str_pass = str(input("もう一度合否・認定科目かどうかを入力してください(True:1 or False:0)"))
        is_pass = is_pass_or_not(str_pass)
    return is_pass

def credit_num_check(credit):
    try:
        credit_num = int(credit)
    except ValueError:
        print("不正な入力です")
        credit = input("単位数を入力してください")
        credit_num = credit_num(credit)
    return credit_num

num = int(input("科目数を入力してください"))
total_credit = 0
total_credit_all = 0
total_grade_point = 0

for i in range(num):
    str_pass = input("合否・認定科目かどうかを入力してください(True:1 or False:0)")
    is_pass = is_pass_or_not(str_pass)
    
    #合否科目での動作変更
    if is_pass:
        #合否科目の成績を入力
        grade = input("成績を入力してください(ex.S,A,B..)")
        grade_num = charger(grade)
        
        credit = input("単位数を入力してください")
        credit_num = credit_num_check(credit)
        
        #評価ポイントの合計
        total_grade_point += grade_num * credit_num
        
        #合否科目の単位数を合計
        total_credit += credit_num
        total_credit_all += credit_num
    else:
        credit = input("単位数を入力してください")
        credit_num = credit_num_check(credit)
        #合否科目でない単位数を合計
        total_credit_all += credit_num

#GPAを計算
GPA = total_grade_point / total_credit
SP = GPA * total_credit_all
print(f"GPA: {GPA},正課学習ポイント: {SP}")
