secret_word = "tidur"
list_secret = ["t", "i", "d", "u", "r"]

print("~Hangman 2.0~")
print("Kata rahasia terdiri dari 5 huruf.")
print("Tebak kata dalam 6 kesempatan.\n")

lenght_secret = 5 * "_ "
print(lenght_secret)

print("\nMulai!\n")

chance = 6
guessed_letters = []

while chance > 0:
    guess = input("Masukan 1 huruf: ")
    if len(guess) != 1 or not guess.isalpha():
        print("Input invalid. Coba lagi.\n")
        continue
    
    if guess in guessed_letters:
        print("Kamu sudah menebak huruf", guess, "sebelumnya. Coba lagi.\n")
        continue
    guessed_letters.append(guess)
    
    if len(guess) == 1:
        chance = chance - 1
        if guess in list_secret:
            print("Huruf", guess, "ada dalam kata rahasia\n")
        else:
            print("Coba lagi\n")

        print("Kesempatan:", chance)

    if chance == 0:
        print("Kesempatan habis!") 
        last_guess = input("Kata rahasia adalah: ")
        if last_guess == secret_word:
            print("Selamat! Kamu menebak kata rahasia!")
        else:
            print("Salah! kata rahasia:", secret_word)
        break   

print("~Selesai~")