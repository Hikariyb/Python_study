#FizzBuzz(3の倍数ならばFizz,5の倍数ならばBuzz,3及び5の両方の倍数ならばFizzBuzzを表示し、それ以外ならば数字を表示するプログラム)を作ろう！！
num = int(input("最後の数字を入力してください。"))

for i in range(1, num+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
