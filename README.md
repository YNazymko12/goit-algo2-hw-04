# Домашнє завдання до теми «Префіксні дерева»

Вітаємо в домашньому завданні до теми «Префіксні дерева»! 🙂

Домашнє завдання буде складатися з двох незалежних завдань.

Занурившись у роботу з префіксними деревами через ці практичні завдання, ви
відкриєте для себе потужний інструмент обробки текстових даних. Розширивши
функціонал Trie-дерева, ви не просто вивчите теорію, а зрозумієте, як ця
структура даних допомагає розв’язувати реальні задачі пошуку й аналізу тексту.

Реалізувавши методи для роботи із суфіксами та префіксами, ви побачите, як
працюють сучасні системи автодоповнення й перевірки правопису. А завдання з
пошуку найдовшого спільного префікса навчить вас оптимізувати алгоритми, з
урахуванням як швидкодії, так і використання пам'яті.

Досвід роботи з префіксними деревами стане вашим надійним фундаментом для
вивчення складніших алгоритмів і структур даних, особливо якщо ви плануєте
працювати з обробкою природної мови чи пошуковими системами.

Це не просто навчальна вправа — це ваш крок до розуміння, як створюються сучасні
системи обробки тексту, які ми використовуємо щодня.

## Задача 1. Розширення функціоналу префіксного дерева

Реалізуйте два додаткових методи для класу Trie:

- count_words_with_suffix(pattern) для підрахунку кількості слів, що
  закінчуються заданим шаблоном;
- has_prefix(prefix) для перевірки наявності слів із заданим префіксом.

### Технічні умови

- Клас Homework має успадковувати базовий клас Trie.
- Методи повинні опрацьовувати помилки введення некоректних даних.
- Вхідні параметри обох методів мають бути рядками.
- Метод count_words_with_suffix має повертати ціле число.
- Метод has_prefix має повертати булеве значення.

### Критерії прийняття

📌Критерії прийняття домашнього завдання є обов’язковою умовою розгляду завдання
ментором. Якщо якийсь із критеріїв не виконано, ментор надішле ДЗ на
доопрацювання без оцінювання. Якщо вам «тільки уточнити»😉 або ви застопорилися
на якомусь з етапів виконання — звертайтеся до ментора у Slack).

1. Метод count_words_with_suffix повертає кількість слів, що закінчуються на
   заданий pattern. За відсутності слів повертає 0. Враховує регістр символів
   (10 б).

2. Метод has_prefix повертає True, якщо існує хоча б одне слово із заданим
   префіксом. Повертає False, якщо таких слів немає. Враховує регістр символів
   (10 б).

3. Код проходить усі тести (10 б).

4. Обробляються некоректні вхідні дані (10 б).

5. Методи працюють ефективно на великих наборах даних (10 б).

### Шаблон програми

```python
from trie import Trie

class Homework(Trie): def count_words_with_suffix(self, pattern) -> int: pass

    def has_prefix(self, prefix) -> bool:
       pass

if **name** == "**main**": trie = Homework() words = ["apple", "application",
"banana", "cat"] for i, word in enumerate(words): trie.put(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    # Перевірка наявності префікса
    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat
```

## Задача 2. Пошук найдовшого спільного префікса

Створіть клас LongestCommonWord, який наслідує клас Trie, та реалізуйте метод
find_longest_common_word, який знаходить найдовший спільний префікс для всіх
слів у вхідному масиві рядків strings.

### Технічні умови

- Клас LongestCommonWord має успадковувати Trie.
- Вхідний параметр методу find_longest_common_word, strings — масив рядків.
- Метод find_longest_common_word має повертати рядок — найдовший спільний
  префікс.
- Час виконання — O ( S ) O(S), де S S — сумарна довжина всіх рядків.

### Критерії прийняття

1. Метод find_longest_common_word:

- повертає найдовший префікс, спільний для всіх слів (10 б),
- повертає пустий рядок, якщо спільного префікса немає (10 б),
- коректно обробляє порожній масив або некоректні вхідні дані (10 б).

2. Код проходить усі тести (20 б).

### Шаблон програми

```python
from trie import Trie

class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        pass

if **name** == "**main**": # Тести trie = LongestCommonWord() strings =
["flower", "flow", "flight"] assert trie.find_longest_common_word(strings) ==
"fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""
```

## Підготовка та завантаження домашнього завдання

1. Створіть публічний репозиторій goit-algo2-hw-04.

2. Виконайте завдання та відправте його у свій репозиторій.

3. Завантажте робочі файли на свій комп’ютер і прикріпіть їх в LMS у форматі
   zip. Назва архіву повинна бути у форматі ДЗ4_ПІБ.

4. Прикріпіть посилання на репозиторій goit-algo2-hw-04 та відправте на
   перевірку.

## Формат здачі

- Прикріплені файли репозиторію у форматі zip із назвою ДЗ4_ПІБ.
- Посилання на репозиторій.

## Формат оцінювання

Оцінка від 0 до 100.

Завдання 1 оцінюється у 50 балів.

Завдання 2 оцінюється у 50 балів.

Докладний розподіл балів зазначений у критеріях прийняття.

☝🏻УВАГА!! У вас є можливість обрати підхід до виконання та можливого
доопрацювання домашнього завдання: задовольнитися першою отриманою оцінкою
(звісно ж, якщо вона вища за прохідний бал), намагатися отримати вищий бал
шляхом можливого подальшого доопрацювання роботи відповідно до фідбеку ментора.
Обраний підхід до виконання ДЗ необхідно зазначити в полі для здачі до
прикріпленого завдання. За відсутності коментаря ментор дотримується першого
підходу й виставляє отриману оцінку.

💡 Відправляйте ДЗ на перевірку, коли зроблено все можливе, адже кількість спроб
здачі завдання впливає на отриманий бал! За кожну наступну спробу після другої
(тобто з третьої) максимально можлива кількість балів зменшується на 5. Критерії
оцінювання робіт у магістратурі GoIt Neoversity

### Результат виконаного ДЗ

#### Завдання 1

![Results](./assets/task01.png)

#### Завдання 2

![Results](./assets/task02.png)
