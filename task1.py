import random
targets = ["собака", "крем", "єдиноріг"]
hints = {
   "собака": "Це жива істота, гавкає і вірний друг людини.",
   "крем": "Це неживий предмет, м'який і використовується для догляду.",
   "єдиноріг": "Це вигадана істота з рогом, чарівна і рідкісна."
}
secret = random.choice(targets)
print("Вгадай об'єкт: живий, неживий або вигаданий.")
print("У тебе є 5 спроб.")
attempts = 0
max_attempts = 5
while attempts < max_attempts:
   guess = input(f"Спроба {attempts + 1}: ").strip().lower()
   if not guess:
       print("Порожнє введення. Спробуй ще раз.")
       continue
   attempts += 1
   if guess == secret:
       print("Вітаю! Ти вгадав об'єкт!")
       break
   else:
       if attempts < max_attempts:
           print("Неправильно.", hints[secret])
       else:
           print(f"На жаль, ти програв. Правильна відповідь: {secret}")
