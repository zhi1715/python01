print("--請輸入三科成績--")
chinese_score=int(input("請輸入國文成績:"))
english_score=int(input("請輸入英文成績:"))
math_score=int(input("請輸入數學成績:"))

total_score=chinese_score+english_score+math_score
average_score=total_score/3

print("\n成績計算結果")
print(f"總分:{total_score:.1f}")
print(f"平均分數:{average_score:.1f}")


