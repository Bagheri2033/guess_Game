import random

play = "y"

while play == "y":
    secret = random.randint(1, 100)
    tries = 0
    won = False

    while tries < 5:
        print("تلاش", tries + 1, "از 5")
        print("جان باقی‌مانده:", 5 - tries)
        text = input("یه عدد بین 1 تا 100 وارد کن: ")

        # اگه عدد نبود، دوباره می‌پرسیم و از فرصت‌ها کم نمی‌کنیم
        if not text.isdigit():
            print("باید عدد وارد کنی!")
            continue

        guess = int(text)

        # اگه بیرون از بازه بود هم همینطور
        if guess < 1 or guess > 100:
            print()
            continue

        # از اینجا به بعد حدس معتبره، یه فرصت مصرف میشه
        tries = tries + 1

        if guess == secret:
            print("آفرین، درست حدس زدی!")
            if tries == 1:
                print("رتبه: نمونه ای")
            elif tries == 2:
                print("رتبه: بسیار خوبی")
            elif tries == 3:
                print("رتبه: خوب")
            elif tries == 4:
                print("رتبه: قبول")
            else:
                print("رتبه: با شانس بردی!")
            won = True
            break

        # جهت درست
        if guess > secret:
            print("کوچک‌تر وارد کن")
        else:
            print("بزرگ‌تر وارد کن")

        # نزدیک یا دور
        diff = abs(guess - secret)
        if diff <= 5:
            print("خیلی نزدیکی!")
        elif diff <= 15:
            print("نزدیکی، ولی هنوز فاصله داری!")
        else:
            print("خیلی دوری!")
        print()

    if won == False:
        print("باختی!")
        print("عدد مخفی این بود:", secret)

    # می‌پرسیم دوباره بازی کنه یا نه
    while True:
        play = input("دوباره بازی می‌کنی؟ (y/n): ")
        if play == "y" or play == "n":
            break
        print("فقط y یا n بنویس")

print("خداحافظ!")
