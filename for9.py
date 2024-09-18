stipendia  = int(input("введите сумму стипендии"))
rashodi = int(input("введите сумму затрат"))
months = int(input("введите количество месяцев"))

if stipendia<rashodi:
    print(f"чтобы прожить {months} месяцев необходимо {(rashodi*months)-(stipendia*months)} рублей")
else:
    pass