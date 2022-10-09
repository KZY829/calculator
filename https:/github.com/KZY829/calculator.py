sentaku = input('どの計算をしますか? 足し算:+ 引き算:- 掛け算:* 割り算:// 少数足し算:+. 少数引き算:-. 少数掛け算:*. 少数割り算:/.>>')

# 足し算
if sentaku == '+':
    one = input('足される数を入力してください。>>')
    two = input('足す数を入力してください。>>')
    print(int(one) + int(two))

# 引き算
if sentaku == '-':
    one = input('引かれる数を入力してください。>>')
    two = input('引く数を入力してください。>>')
    print(int(one) - int(two))

# 掛け算(面積、体積)
if sentaku == '*':
    sentaku2 = input('九九もしくは面積を求める場合は"1"を入力、体積を求める場合は"2"を押してください。>>')
    if sentaku2 == '1':
        one = input('かけられる数を入力してください。>>')
        two = input('かける数を入力してください。>>')
        print(int(one) * int(two))
    else:
        one = input('縦の値を入力してください。>>')
        two = input('横の値を入力してください。>>')
        three = input('高さの値を入力してください。')
        print(int(one) * int(two) * int(three))

# 割り算
if sentaku == '//':
    one = input('割られる数を入力してください。>>')
    two = input('割る数を入力してください。>>')
    print(int(one) / int(two))

# 少数足し算
if sentaku == '+.':
    one = input('足される少数を入力してください。>>')
    two = input('足す少数を入力してください。>>')
    print(float(one) + float(two))

# 少数引き算
if sentaku == '-':
    one = input('引かれる少数を入力してください。>>')
    two = input('引く少数を入力してください。>>')
    print(float(one) - float(two))

# 少数掛け算(面積、体積)
if sentaku == '*':
    sentaku2 = input('九九もしくは面積を求める場合は"1"を入力、体積を求める場合は"2"を押してください。>>')
    if sentaku2 == '1':
        one = input('かけられる少数を入力してください。>>')
        two = input('かける少数を入力してください。>>')
        print(float(one) * float(two))
    else:
        one = input('縦の値を入力してください。(少数)>>')
        two = input('横の値を入力してください。(少数)>>')
        three = input('高さの値を入力してください。(少数)')
        print(float(one) * float(two) * float(three))

# 少数割り算
if sentaku == '//':
    one = input('割られる少数を入力してください。>>')
    two = input('割る少数を入力してください。>>')
    print(float(one) / float(two))
