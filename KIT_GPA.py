#金沢工業大学のGPAを計算するシステムを作ろう！！
#【条件】
# 1. 関数(関数名をchangerとすること)を使うこと(GPAの評価ポイントと評価の変換)
# 2. GPAと正課学習ポイントを表示しよう
# 【参照】
# https://www.kanazawa-it.ac.jp/campus_guide/2025/chapter_3/list_3/page_3.html
# https://www.kanazawa-it.ac.jp/campus_guide/2025/chapter_3/list_3/page_4.html


grade = str(input("成績を入力してください(ex.S,A,B..)"))
credit = int(input("単位数を入力してください(合否科目含まない)"))
credit_total = int(input("単位数を入力してください(合否科目含む)"))