#金沢工業大学のGPAを計算するシステムを作ろう！！
#【条件】
# 1. 関数(関数名をchangerとすること)を使うこと(GPAの評価ポイントと評価の変換)
# 2. GPAと正課学習ポイントを表示しよう
# 【参照】
# https://www.kanazawa-it.ac.jp/campus_guide/2025/chapter_3/list_3/page_3.html
# https://www.kanazawa-it.ac.jp/campus_guide/2025/chapter_3/list_3/page_4.html

num = int(input("科目数を入力してください"))

for i in range(num):
    grade = str(input("成績を入力してください(ex.S,A,B..)"))
    credit = int(input("単位数を入力してください"))
    is_pass = bool(input("合否科目かどうかを入力してください(True or False)"))





