import os
import string

# 作成先ディレクトリのパス（必要に応じて変更）
target_dir = "DailyTraining/20251113all"
testcase = 9

# ディレクトリが存在しない場合は作成
os.makedirs(target_dir, exist_ok=True)

# a.py から i.py まで作成
t = "abcdefghijklmnopqrstuvwxyz"
for char in t[:testcase]:  # 'a'〜'i' は最初の9文字
    filename = f'{char}.py'
    filepath = target_dir + '/' + filename
    # filepath = os.path.join(target_dir, filename)
    print(filepath)
    with open(filepath, 'w') as f:
        print(f"Creating file: {filename}")
        pass  # 空ファイルを作成
