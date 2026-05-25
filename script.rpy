# Игра "Логика чувств: Тайна старой лаборатории"
# Образовательная новелла + симулятор свиданий + головоломки
# Автор: [Ваше имя]
# Версия: 1.0

init python:
    style.window.background = Solid("#00000080")
    style.window.xalign = 0.5
    style.window.yalign = 1.0
    style.window.ysize = 200
    style.window.xsize = 1920
    
    style.choice_vbox.xalign = 0.5
    style.choice_vbox.yalign = 0.5
    style.choice_vbox.spacing = 15
    
    style.choice_button.xminimum = 300
    style.choice_button.xfill = True
    
    style.choice_button_text.size = 36
    style.choice_button_text.color = "#ffffff"
    style.choice_button_text.hover_color = "#ffcc88"

init python:
    # Переменные для отношений и знаний
    anna_relation = 0
    dmitry_relation = 0
    knowledge = 0

# Определение персонажей (с цветами для текста)
define a = Character("Анна", color="#c8a2c8", who_outlines=[(1, "#8a2be2")])
define d = Character("Дмитрий", color="#a2c8a2", who_outlines=[(1, "#228b22")])
define e = Character("Елена", color="#c8c8a2", who_outlines=[(1, "#b8860b")])
define g = Character("Алексей", color="#ffffff", who_outlines=[(1, "#555555")])

# Объявление изображений (заглушки – замените на свои файлы)
image bg corridor = Transform("images/bg_corridor.jpeg", size=(1920,  1080))  # или Solid("#3a3a5a")
image bg lab = Transform("images/bg_lab.jpeg", size=(1920, 1080))
image bg library = Transform("images/bg_library.jpeg", size=(1920, 1080))
image bg room = Transform("images/bg_room.jpeg", size=(1920, 1080))
image bg park = Transform("images/bg_park.jpeg", size=(1920, 1080))
image bg archive = Transform("images/bg_archive.jpeg", size=(1920, 1080))

# Спрайты персонажей (временно используем цветные квадраты)
image anna smile = "images/anna_smile.png"
image anna think = "images/anna_think.png"
image anna surprise = "images/anna_surprize.png"

image dmitry neutral = "images/dmitry_neutral.png"
image dmitry happy = "images/dmitry_happy.png"
image dmitry sad = "images/dmitry_sad.png"

image elena serious = "images/elena_serious.png"
image elena warm = "images/elena_warm.png"
image elena strict = "images/elena_strict.png"

# Иллюстрации (ключевые сцены)
image ill diary = Transform("images/ill_diary.png", size=(500, 500))
image ill puzzle = "images/ill_puzzle.jpg"
image ill ending = "images/ill_ending.png"

# Звуки и музыка (заглушки, но можно добавить реальные файлы)
define audio.music_main = "audio/music_main.mp3"
define audio.sound_click = "audio/click.mp3"
define audio.sound_page = "audio/page.mp3"
define audio.sound_success = "audio/success.mp3"
define audio.sound_fail = "audio/fail.mp3"
init python:
    config.say_allow_dismiss = lambda: renpy.play("audio/click.mp3", channel="sound") or True
# Начало игры
label start:
    # Включаем фоновую музыку
    play music audio.music_main fadein 1.0

    scene bg corridor
    show ill diary at truecenter
    with fade

    g "Я, Алексей, аспирант исторического факультета. Сегодня в старом крыле университета нашёл нечто невероятное..."
    g "Пыльный дневник, перевязанный кожаным ремешком. На обложке вытиснено: «Профессор Лебедев, 1937»."
    hide ill diary
    g "Внутри – странные записи, химические формулы и чертежи. А в конце – недописанное письмо..."
    play sound audio.sound_page
    g "{i}«...если ты читаешь это, значит, моя тайна ещё не погибла. Ищи ключи в трёх испытаниях...»{/i}"
   

    scene bg corridor
    show anna smile at left
    show dmitry neutral at right
    a "Алексей! Ты что, нашёл лабораторию Лебедева? Говорят, он пропал вместе со всеми записями."
    d "Брось, Анна. Это, скорее всего, подделка. Слишком хорошо сохранился."
    menu:    
        "Верю, что это настоящее открытие.":
            g "Нет, я чувствую – здесь есть что-то реальное. Давайте хотя бы проверим."
            $ knowledge += 1
        "Сомневаюсь, но любопытно.":
            g "Может, вы и правы. Но проверить стоит, правда?"
    d "Ладно. Если хочешь, я помогу с физической частью."
    a "А я – с химической. Но сначала нужно попасть в старую лабораторию."

    scene bg lab
    g "Мы пробираемся в заброшенную лабораторию на третьем этаже. Всё покрыто пылью, но на столе – мензурки и непонятный прибор."
    a "Смотри! Здесь указан номер партии – 118. И таблица символов."
    g "{i}«Первое испытание: вода и огонь. Ответ даст начало пути.»{/i}"
    g "Нужно решить химическую загадку."

    # ---------- ГОЛОВОЛОМКА 1 (химия) ----------
    label puzzle_chemistry:
        scene bg lab
        show anna think at left
        show dmitry neutral at right
        g "На столе лежит записка: «Что тяжелее – литр воды или литр льда?»"
        menu:
            "Литр воды":
                $ answer1 = "вода"
            "Литр льда":
                $ answer1 = "лед"
            "Они одинаковы":
                $ answer1 = "одинаково"
        if answer1 == "вода":
            g "Верно! Лёд легче, потому что его плотность ниже."
            $ knowledge += 1
            play sound audio.sound_success
            a "Молодец! Первый ключ получен."
        else:
            g "Неверно. На самом деле литр воды тяжелее – лёд плавает, значит, он менее плотный."
            play sound audio.sound_fail
            a "Ничего, дальше будет проще."
        "Вы получаете кусочек пазла. На нём цифра {b}7{/b}."

    # ---------- ВЫБОР 1 (влияет на отношения) ----------
    scene bg library
    show anna smile at left
    show dmitry neutral at right
    g "Следующая подсказка ведёт в библиотеку. Нужно найти книгу по физике."
    a "Давай я помогу – я знаю, где раздел с термодинамикой."
    d "А я могу объяснить любую формулу. Но решать тебе."
    menu:
        "Кого позвать на помощь?"
        "Анну (она быстрее найдёт книгу)":
            $ anna_relation += 1
            a "Отлично, идём к стеллажам!"
            g "Анна быстро отыскала нужный фолиант."
        "Дмитрия (он лучше объяснит физику)":
            $ dmitry_relation += 1
            d "Пойдём, покажу, как читать эти графики."
            g "Дмитрий углубился в формулы."

    # ---------- ГОЛОВОЛОМКА 2 (физика) ----------
    label puzzle_physics:
        scene bg library
        show elena serious at right
        g "Внезапно появляется библиотекарь Елена."
        e "Вы ищете книгу «Теплота и движение»? Она хранится в особом отделе. Но сначала ответьте: какую температуру показывает уличный термометр, если в тени 10°C, а на солнце 25°C?"
        menu:
            "10°C":
                $ answer2 = "10"
            "25°C":
                $ answer2 = "25"
            "Среднее арифметическое":
                $ answer2 = "среднее"
        if answer2 == "10":
            g "Правильно! В тени измеряется настоящая температура воздуха. На солнце термометр нагревается."
            $ knowledge += 1
            play sound audio.sound_success
            e "Хорошо. Вот ваша книга."
        else:
            g "Нет, официальная температура всегда измеряется в тени. На солнце прибор врет."
            play sound audio.sound_fail
            e "В следующий раз подумайте. Держите книгу, но запомните."
        g "В книге найден второй кусочек пазла – цифра {b}3{/b}."

    # ---------- ВЫБОР 2 (романтический / научный уклон) ----------
    scene bg room
    g "Поздно вечером я разбираю записи у себя в комнате. Стук в дверь."
    if anna_relation > dmitry_relation:
        show anna smile at left
        a "Не спишь? Пришла проверить, как идут дела."
    else:
        show dmitry neutral at left
        d "Я всё думаю про эти цифры. Может, это координаты?"
    menu:
        "Пригласить на чай и поговорить по душам":
            if anna_relation > dmitry_relation:
                $ anna_relation += 1
                g "Заходи, как раз кипячу чайник."
                a "Расскажи о своей семье…"
            else:
                $ dmitry_relation += 1
                g "Заходи, Дим, у меня есть печенье."
                d "Спасибо. Ты знаешь, я редко с кем-то делюсь мыслями…"
        "Сказать, что устал, и попросить прийти завтра":
            g "Извини, сегодня уже нет сил. Давай завтра."
            # Отношения не меняются, но лёгкая грусть
    g "Мы сблизились. Осталось последнее испытание."

    # ---------- ГОЛОВОЛОМКА 3 (исторический шифр) ----------
    label puzzle_history:
        scene bg archive
        show elena warm at left
        e "Третье испытание – расшифровать старый текст. Вот вам отрывок: «17 10 22 1 15 1 10». Что это за слово?"
        g "Каждая цифра – позиция буквы в алфавите (1=А, 2=Б ...). Попробуем..."
        menu:
            "ПАНАМА":
                $ answer3 = "панама"
            "ПОБЕДА":
                $ answer3 = "победа"
            "ПУТЬ":
                $ answer3 = "путь"
        if answer3 == "победа" or answer3 == "ПОБЕДА":
            g "Верно! 17=П, 10=О, 22=В, 1=А, 15=Н, 1=А, 10=Й -> ПОБЕДА!"
            $ knowledge += 1
            play sound audio.sound_success
            e "Поздравляю. Вы достойны войти в секретную комнату."
        else:
            g "Нет. Расшифровка даёт слово «ПОБЕДА». Вы записываете его."
            play sound audio.sound_fail
            e "Попробуйте ещё раз в следующий раз. Но сейчас я открою дверь."

    # ---------- ФИНАЛ (зависит от отношений и знаний) ----------
    scene bg archive
    show ill ending at truecenter
    "Вы заходите в тайный архив. На стене портрет профессора Лебедева и три конверта."

    if knowledge >= 2 and (anna_relation >= 2 or dmitry_relation >= 2):
        # Хорошая концовка – научное открытие и романтика
        if anna_relation >= dmitry_relation:
            g "Анна, мы сделали это! Все формулы верны. Дневник расшифрован полностью."
            a "Это было потрясающе. Я так рада, что мы были вместе."
            g "Мы опубликуем статью и, может быть, откроем новый элемент."
            a "А ещё... я хочу быть не просто коллегой."
            "Вы целуетесь под звуки старого радио. Конец: {b}Научная любовь{/b}."
        else:
            g "Дмитрий, без твоей физики мы бы не поняли чертежи. Ты гений."
            d "Спасибо, что поверил. Это открытие изменит науку."
            g "И изменит нас. Давай работать вместе дальше."
            d "Ты лучший друг, который у меня был."
            "Вы обнимаетесь. Конец: {b}Дружба и открытие{/b}."
    elif knowledge >= 1 and (anna_relation + dmitry_relation >= 2):
        # Средняя концовка – тайна раскрыта, но одиночество
        g "Я всё понял! Дневник – это план забытой машины времени. Но никто не пришёл разделить радость."
        "Анна и Дмитрий заняты своими делами. Вы передаёте находку в музей и уходите в закат один."
        "Конец: {b}Одинокий учёный{/b}."
    else:
        # Плохая концовка – тайна не раскрыта
        scene bg corridor
        g "Я так и не смог собрать все кусочки. Дневник теряется в пыльных архивах."
        "Профессор Лебедев остаётся забытым. Моя научная карьера идёт под откос."
        "Конец: {b}Провал{/b}."

    "Спасибо за игру! Вы прошли «Логику чувств»."
    menu:
        "Начать заново?"
        "Да":
            jump start
        "Нет":
            return