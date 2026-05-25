# screens.rpy – полная версия с кастомным главным меню
# Остальные экраны (загрузка, настройки) остаются стандартными
# В самом верху файла screens.rpy (перед любыми экранами)
transform fullscreen:
    xalign 0.5 yalign 0.5
    zoom max(1.0 * config.screen_width / renpy.image_size("gui/main_menu_bg.jpg")[0], 1.0 * config.screen_height / renpy.image_size("gui/main_menu_bg.jpg")[1])

screen main_menu():
    tag menu
    add "gui/main_menu_bg.jpg" at fullscreen
    text "Логика чувств" size 80 color "#ffcc88" outlines [(2, "#000000", 2, 2)] xalign 0.5 yalign 0.1
    vbox:
        xalign 0.5 yalign 0.7 spacing 15
        textbutton _("Начать игру") action Start() style "main_menu_button"
        textbutton _("Загрузить игру") action ShowMenu("load") style "main_menu_button"
        textbutton _("Настройки") action ShowMenu("preferences") style "main_menu_button"
        textbutton _("Выход") action Quit() style "main_menu_button"

style main_menu_button:
    size 40
    color "#dddddd"
    hover_color "#ffaa66"
    background Solid("#444444")
    hover_background Solid("#aa8866")
    xminimum 300
    ypadding 10

# Ниже идут все стандартные экраны Ren'Py – они должны быть, иначе игра сломается.
# Если вы не хотите их вручную копировать, просто скопируйте их из свежего проекта Ren'Py.
# Я приведу сокращённую, но полную версию (в Ren'Py 8.0 они выглядят так):

screen navigation():
    vbox:
        style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.5
        spacing gui.navigation_spacing
        textbutton _("Назад") action Return()
        textbutton _("Сохранить") action FileAction("Save")
        textbutton _("Загрузить") action FileAction("Load")
        textbutton _("Главное меню") action MainMenu()
        textbutton _("Выход") action Quit()

screen save():
    tag menu
    use file_slots(_("Сохранить игру"))

screen load():
    tag menu
    use file_slots(_("Загрузить игру"))

screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Страница {}"), auto=_("Автосохранения"), quick=_("Быстрые"))
    use game_menu(title):
        fixed:
            order_reverse True
            style_prefix "file_slots"
            textbutton _("{}".format(page_name_value)):
                style "page_label"
                xalign 0.5
                action NullAction()
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"
                xalign 0.5
                yalign 0.5
                spacing gui.slot_spacing
                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1
                    button:
                        action FileAction(slot)
                        has vbox
                        text FileTime(slot, empty=_("Пустой слот")):
                            style "slot_time_text"
                        text FileSaveName(slot):
                            style "slot_name_text"
                        key "save_delete" action FileDelete(slot)
            hbox:
                style_prefix "page"
                xalign 0.5
                spacing gui.page_spacing
                textbutton _("<") action FilePagePrevious()
                textbutton _("{#auto_page}A") action FilePage("auto")
                textbutton _("{#quick_page}Q") action FilePage("quick")
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)
                textbutton _(">") action FilePageNext()

screen preferences():
    tag menu
    use game_menu(_("Настройки")):
        vbox:
            style_prefix "preferences"
            label _("Дисплей")
            textbutton _("Оконный") action Preference("display", "window")
            textbutton _("Полный экран") action Preference("display", "fullscreen")
            label _("Язык")
            textbutton "Русский" action Language(None)
            textbutton "English" action Language("english")
            null height 20
            label _("Скролл текста")
            bar value Preference("text speed")
            label _("Авто-чтение")
            bar value Preference("auto-forward time")

screen game_menu(title):
    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background
    vbox:
        style_prefix "game_menu"
        xpos gui.game_menu_xpos
        ypos gui.game_menu_ypos
        spacing gui.game_menu_spacing
        label title
        use navigation
    key "game_menu" action ShowMenu("preferences")

style game_menu_outer_frame:
    background "gui/overlay/game_menu.png"
    padding (222, 0, 222, 0)

style game_menu_navigation_frame:
    xsize 360
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_content_frame:
    left_margin 30
    right_margin 30
    top_margin 15

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style game_menu_label:
    xpos 75
    ysize 90

screen choice(items):
    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5
        vbox:
            spacing 30
            for i in items:
                textbutton i.caption:
                    action i.action
                    xminimum 400
                    text_size 40
                    text_color "#fff"
                    text_hover_color "#ff0"


# И так далее – в оригинале много стилей и мелких экранов.
# Но для базовой работы этих достаточно.
