#bmiを計算するプログラムを作ってください。

heigh = float(input("身長を入力してください(cm)："))
weight = float(input("体重を入力してください(kg)："))

heigh1 = heigh / 100
bmi = weight / heigh1 ** 2
print(f'身長が{heigh}cmで、体重が{weight}kgの人のbmiは{bmi:.2f}です')