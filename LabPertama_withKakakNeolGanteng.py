secret_letter = ["z", "Z"]

while True:
    input_letter = input("Ketik 1 huruf: ")
    if input_letter in secret_letter:
        print("Benar!")
        break
    elif len(input_letter) != 1 and input_letter.isalpha():
        print("INVALID - Masukkan hanya 1 huruf!")
        continue
    elif len(input_letter) == 1 and not input_letter.isalpha():
        print("INVALID - Masukkan huruf saja!")
        continue
    elif len(input_letter) != 1 and not input_letter.isalpha():
        print("INVALID - Masukkan huruf saja dan hanya 1 huruf!")
        continue
    elif len(input_letter) == 1 and input_letter not in secret_letter:
        print("Salah!")
        break

print("~Selesai~")

