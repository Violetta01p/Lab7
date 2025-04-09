import random
import time
print("Ласкаво просимо до гри, яка логічна й нелогічна одночасно!")
print("Вибери, що хочеш вгадати: число, колір або тварину (але це не точно)")
category = input("Твій вибір: ").strip().lower()
possible_choices = {
   "число": [str(i) for i in range(1, 21)],
   "колір": ["червоний", "зелений", "синій", "жовтий"],
   "тварина": ["кіт", "пес", "слон", "жираф"]
}
if category not in possible_choices:
   print("Це щось дуже дивне... Але гаразд, продовжимо!")
   category = random.choice(list(possible_choices.keys()))
   print(f"Ми обрали за тебе: {category}")
secret = random.choice(possible_choices[category])
print("Починай вгадувати! (але ми не обіцяємо допомагати чесно)")
start_time = time.time()
attempts = 0
while True:
   if time.time() - start_time > random.randint(15, 30):
       break
   guess = input("Твоя здогадка: ").strip().lower()
   attempts += 1
   if not guess:
       print("Нічого? Ну окей...")
       continue
   if not guess.isalpha():
       print("Це виглядає підозріло. Але ми запам'ятаємо це.")
       continue
   if random.choice([True, False]):
       if guess == secret:
           print("Можливо, ти на правильному шляху...")
       else:
           print("Це точно не те. Або ні?")
   else:
       if guess == secret:
           print("Це абсолютно неправильно. Або ні?")
       else:
           print("Дуже близько. Можливо.")
print("Гру завершено. Чи виграв ти? Це знаєш лише ти.")
