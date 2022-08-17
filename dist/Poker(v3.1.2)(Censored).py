import os
import tkinter as tk
import random
from tkinter import *
from PIL import ImageTk, Image


# функция для раздачи случайных карт обоим игрокам
def two_players1(event):
    global deck_cards, general_list, xx1, xx2, tmp_value
    opp_cards.config(font = ('JetBrains Mono', 50), text = 'X X', width = 9, height = 1)
    if enter_my_card_flag != 1:
        general_list = []
    tmp_value = [[], [], []]
    clear_tmp()
    for h in [winerrr1, winerrr2, mouth1, mouth2, flop1, tern1, river1,
              my_combination, opp_combination, xx1, xx2]:
        h.place_forget()
    # если мы не выставляли себе карты вручную
    if enter_my_card_flag != 1:
        general_list.append(random.choice(deck_cards)); deck_cards.remove(general_list[0])
        general_list.append(random.choice(deck_cards)); deck_cards.remove(general_list[1])
    # если мы не выставляли карты оппонента вручную
    if enter_opp_card_flag != 1:
        if len(general_list) > 2:
            deck_cards.append(general_list.pop(2)); deck_cards.append(general_list.pop(2))
        general_list.append(random.choice(deck_cards)); deck_cards.remove(general_list[2])
        general_list.append(random.choice(deck_cards)); deck_cards.remove(general_list[3])
    my_cards.config(text = general_list[0] + ' ' + general_list[1])
    len_deck.configure(text = 'карт в колоде: 48')


# функция для показа мема
def fck_mouth1(event):
    global mouth2, mouth1, fck_mouth1_flag, fck_mouth1_flag1
    mouth2.configure(image = image_collection[fck_mouth1_flag])
    mouth2.place(x = 30, y = 30)
    mouth1.configure(font = ('JetBrains Mono', 20), text = words_collection[fck_mouth1_flag],
                     width = 26, height = 1)
    mouth1.place(x = 25, y = 350)
    if fck_mouth1_flag == 2:
        fck_mouth1_flag = 0
    else:
        fck_mouth1_flag += 1
    winerrr1.place_forget(); winerrr2.place_forget()
    fck_mouth1_flag1 = 1


# функция для скрытия мема
def delete_mouth(event):
    global fck_mouth1_flag1
    mouth2.place_forget(); mouth1.place_forget()
    if len_deck['text'] == 'карт в колоде: 43' and opp_cards['text'] != 'X X':
        winerrr1.place(x = 30, y = 30); winerrr2.place(x = 50, y = 350)
    fck_mouth1_flag1 = 0


# функция для открытия карт флопа
def open_flop(event):
    global general_list, deck_cards
    if len_deck['text'] == 'карт в колоде: 48':
        general_list.append(random.choice(deck_cards)); deck_cards.remove(general_list[4])
        general_list.append(random.choice(deck_cards)); deck_cards.remove(general_list[5])
        general_list.append(random.choice(deck_cards)); deck_cards.remove(general_list[6])
        flop1.config(font = ('JetBrains Mono', 45), text = general_list[4] +
                     general_list[5] + general_list[6], width = 9, height = 1)
        flop1.place(x = 450, y = 320)
        len_deck.configure(text = 'карт в колоде: 45')


# функция для открытия карты тёрна
def open_tern(event):
    global general_list, deck_cards
    if len_deck['text'] == 'карт в колоде: 45':
        general_list.append(random.choice(deck_cards))
        deck_cards.remove(general_list[7])
        tern1.config(font = ('JetBrains Mono', 45), text = general_list[7], width = 3, height = 1)
        tern1.place(x = 794, y = 320)
        len_deck.configure(text = 'карт в колоде: 44')


# функция для открытия карты ривера
def open_river(event):
    global general_list, deck_cards
    if len_deck['text'] == 'карт в колоде: 44':
        general_list.append(random.choice(deck_cards))
        deck_cards.remove(general_list[8])
        river1.config(font = ('JetBrains Mono', 45), text = general_list[8], width = 3, height = 1)
        river1.place(x = 920, y = 320)
        len_deck.configure(text = 'карт в колоде: 43')


# функция вычисляет комбинацию из карт борда и карманных карт для заданного игрока
def combinations(boardd, q):
    global tmp_list, tmp_value
    board1 = [x for x in boardd]
    if q == 1:
        board1 += [general_list[0], general_list[1]]
    if q == 2:
        board1 += [general_list[2], general_list[3]]
    # cr - список для хранения рангов наших карт (card rank)
    # cs - список для хранения мастей наших карт (card suit)
    cr, cs = [], []
    # заполняем список с рангами
    for x in board1:
        for x1 in x:
            for y in tmp_board2:
                if x1 == y:
                    cr.append(int(tmp_board1[tmp_board2.index(y)]))
    # заполняем список с мастями
    for x in board1:
        for x1 in x:
            for y in suit:
                if x1 == y:
                    cs.append(x1)
    street = [[2, 3, 4, 5, 14], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8],
              [5, 6, 7, 8, 9], [6, 7, 8, 9, 10], [7, 8, 9, 10, 11],
              [8, 9, 10, 11, 12], [9, 10, 11, 12, 13], [10, 11, 12, 13, 14]]
    kiker1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    # список для вывода текста на виджет
    kiker2 = ['двойка', 'тройка', 'четвёрка', 'пятёрка', 'шестёрка', 'семёрка', 'восьмёрка',
              'девятка', 'десятка', 'валет', 'дама', 'король', 'туз']
    # удаляем все дубликаты, сортируем список
    cr1 = list(set(x for x in cr)); cr1.sort()
    # ищем стрит и если нашли, то сохраняем
    for x in range(9, -1, -1):
        if list(y in cr1 for y in (v for v in street[x])).count(True) == 5:
            # зафиксировали наличие стрита
            tmp_list[4][2] = 1
            # сохраняем сам стрит
            tmp_list[4][0] = street[x]
            # вычисляем силу стрита (по кикеру)
            tmp_list[4][1] = x
            break
    # ищем флэш и стрит флэш
    for x in range(4):
        if cs.count(suit[x]) > 4:
            # фиксируем наличие флэша
            tmp_list[3][2] = 1
            # сохраняем все ранги одномастных карт и находим кикер
            cr1 = []
            for f in range(7):
                if cs[f] == suit[x]:
                    cr1.append(cr[f])
            cr1.sort(reverse=True)
            # вычисляем старшинство флэша
            tmp_list[3][1] = cr1[:5]
            # вычисляем наличие стрит флэша
            if tmp_list[4][2] == 1:
                for v in range(9, -1, -1):
                    # в нашем списке одномастных карт ищем наибольшее вхождение в список street
                    if list(y in cr1 for y in (x for x in street[v])).count(True) == 5:
                        # фиксируем наличие стрит флэша, силу комбинации и её старшинство
                        tmp_list[0][1] = v; tmp_list[0][2] = 1
                        tmp_value[2].append(8); tmp_value[2].append(tmp_list[0][1])
                        tmp_value[2].append(8)
                        if tmp_list[3][1][0] == 14:
                            return 'роял флеш'
                        else:
                            return 'стрит флэш'
            break
    cr1 = [x for x in cr]; cr1.sort()
    # ищем каре, фул хаус, сеты, пары
    while len(cr1) > 1:
        # ищем каре
        if cr1.count(cr1[0]) == 4:
            # фиксируем наличие каре, силу комбинации и её старшинство
            tmp_list[1][1] = cr1[0]; tmp_list[1][2] = 1
            tmp_value[2].append(7); tmp_value[2].append(tmp_list[1][1])
            # находим кикер для каре
            # удаляем все 4 карты каре
            cr1 = list(set(cr1)); cr1.remove(tmp_list[1][1])
            # записываем старшую из оставшихся карт
            tmp_value[2].append(cr1)
            return 'каре'
        # ищем сеты
        if cr1.count(cr1[0]) == 3:
            # фиксируем наличие сета, силу комбинации и её старшинство
            tmp_list[5][0] = cr1[0]; tmp_list[5][1] = cr1[0]; tmp_list[5][2] = 1
            cr1.remove(tmp_list[5][0]); cr1.remove(tmp_list[5][0]); cr1.remove(tmp_list[5][0])
            continue
        # ищем пары
        if cr1[:5].count(cr1[0]) == 2 or cr1[1:6].count(cr1[0]) == 2 or cr1[2:].count(cr1[0]) == 2:
            # фиксируем наличие пары, силу комбинации и её старшинство
            tmp_list[6][1].append(cr1[0]); tmp_list[6][2] = 1
            tmp_list[6][0].append(cr1[0])
            cr1.remove(tmp_list[6][1][-1]); cr1.remove(tmp_list[6][1][-1])
            continue
        if cr1.count(cr1[0]) == 1:
            cr1.remove(cr1[0])
    # если нашли больше двух пар, тогда удаляем меньшую из них
    if len(tmp_list[6][0]) > 2:
        tmp_list[6][0].remove(min(tmp_list[6][0]))
        tmp_list[6][1] = tmp_list[6][0]
    # если пара только одна, то переносим её в соответствующий список и меняем флаги
    if len(tmp_list[6][0]) == 1:
        tmp_list[7][0] = tmp_list[6][0][0]; tmp_list[6][2] = 0
        tmp_list[7][1] = tmp_list[7][0]; tmp_list[7][2] = 1
    # проверяем наличие фул хауса
    # сначала проверяем наличие сета
    if tmp_list[5][2] == 1:
        # если найден сет и только одна пара, то фиксируем наличие фул хауса и его старшинство
        if tmp_list[7][2] == 1:
            tmp_list[2][0].append(tmp_list[5][1]); tmp_list[2][1].append(tmp_list[5][1])
            tmp_list[2][0].append(tmp_list[7][1]); tmp_list[2][1].append(tmp_list[7][1])
            tmp_list[2][2] = 1
            tmp_value[2].append(6); tmp_value[2].append(tmp_list[2][1]); tmp_value[2].append(6)
            return 'фул хаус'
        # если найден сет и две пары, тогда берём большую из пар и
        # фиксируем наличие фул хауса и его старшинство
        if tmp_list[6][2] == 1:
            tmp_list[2][0].append(tmp_list[5][1]); tmp_list[2][1].append(tmp_list[5][1])
            tmp_list[2][0].append(max(tmp_list[6][1])); tmp_list[2][1].append(max(tmp_list[6][1]))
            tmp_list[2][2] = 1
            tmp_value[2].append(6); tmp_value[2].append(tmp_list[2][1]);  tmp_value[2].append(6)
            return 'фул хаус'
    # возвращаем старшую из найденных выше комбинаций
    if tmp_list[3][2] == 1:
        tmp_value[2].append(5); tmp_value[2].append(tmp_list[3][1]); tmp_value[2].append(5)
        return 'флэш'
    if tmp_list[4][2] == 1:
        tmp_value[2].append(4); tmp_value[2].append(tmp_list[4][1]); tmp_value[2].append(4)
        return 'стрит'
    if tmp_list[5][2] == 1:
        # определяем кикер для сета
        cr.remove(tmp_list[5][1]); cr.remove(tmp_list[5][1]); cr.remove(tmp_list[5][1])
        cr.sort(reverse = True)
        tmp_value[2].append(3); tmp_value[2].append(tmp_list[5][1]); tmp_value[2].append(cr[:2])
        return 'сет'
    if tmp_list[6][2] == 1:
        # определяем кикер для двух пар
        cr.remove(tmp_list[6][1][0]); cr.remove(tmp_list[6][1][0])
        cr.remove(tmp_list[6][1][1]); cr.remove(tmp_list[6][1][1])
        tmp_value[2].append(2); tmp_value[2].append(tmp_list[6][1]); tmp_value[2].append(max(cr))
        return 'две пары'
    if tmp_list[7][2] == 1:
        # определяем кикер для пары
        cr.remove(tmp_list[7][1]); cr.remove(tmp_list[7][1]); cr.sort(reverse = True)
        tmp_value[2].append(1); tmp_value[2].append(tmp_list[7][1]); tmp_value[2].append(cr[:3])
        return 'пара'
    # если не нашли ни одну комбинацию, то определяем кикер
    cr1 = [x for x in cr]
    kiker_part_1 = kiker2[kiker1.index(max(cr1))]
    cr1.remove(max(cr1))
    kiker_part_2 = kiker2[kiker1.index(max(cr1))]
    cr.sort(reverse = True)
    tmp_value[2].append(0); tmp_value[2].append(cr[:5]); tmp_value[2].append(0)
    return kiker_part_1 + ' с кикером ' + kiker_part_2


# функция для шоудауна по риверу
def show_cards1(event):
    global general_list, deck_cards, my_value, opp_value, tmp_value, variable, variable1, \
        my_card_select1, my_card_select2, royal_flush1, straight_flush1, four_of_a_kind1, \
        full_house1, flush1, straight1, three_of_a_kind1, two_pairs1, one_pair1, empty_combination1
    if len_deck['text'] == 'карт в колоде: 43':
        # вычисляем нашу комбинацию, показываем её название
        my_value.append(combinations(general_list[4:], 1))
        my_combination.configure(text = my_value[0])
        my_combination.place(x = 525, y = 445)
        # заполняем и показываем индикатор старшинства нашей комбинации
        tmp_value[0] = list(tmp_value[2])
        xx1.configure(text = tmp_value[0][0])
        if xx1['text'] == 8:
            if my_combination['text'] == 'ROYAL FLUSH !!!':
                royal_flush1 += 1
            else:
                straight_flush1 += 1
        elif xx1['text'] == 7:
            four_of_a_kind1 += 1
        elif xx1['text'] == 6:
            full_house1 += 1
        elif xx1['text'] == 5:
            flush1 += 1
        elif xx1['text'] == 4:
            straight1 += 1
        elif xx1['text'] == 3:
            three_of_a_kind1 += 1
        elif xx1['text'] == 2:
            two_pairs1 += 1
        elif xx1['text'] == 1:
            one_pair1 += 1
        elif xx1['text'] == 0:
            empty_combination1 += 1
        xx1.place(x = 970, y = 445)
        # очищаем временный лист, который использовали при вычислении комбинации
        clear_tmp()
        # вычисляем комбинацию оппонента, показываем её название
        opp_value.append(combinations(general_list[4:], 2))
        opp_combination.configure(text = opp_value[0])
        opp_combination.place(x = 525, y = 180)
        # заполняем и показываем индикатор старшинства комбинации оппонента
        tmp_value[1] = list(tmp_value[2])
        xx2.configure(text = tmp_value[1][0])
        xx2.place(x = 970, y = 180)
        # определяем победителя
        winner1()
        clear_tmp()
        # заглушка на случай открытого мема (чтобы скрыть его)
        mouth1.place_forget(); mouth2.place_forget()
        close_opp_card1(0)
        deck_cards = ['2♠', '2♥', '2♦', '2♣', '3♠', '3♥', '3♦', '3♣', '4♠', '4♥', '4♦',
                      '4♣', '5♠', '5♥', '5♦', '5♣', '6♠', '6♥', '6♦', '6♣', '7♠', '7♥',
                      '7♦', '7♣', '8♠', '8♥', '8♦', '8♣', '9♠', '9♥', '9♦', '9♣', '10♠',
                      '10♥', '10♦', '10♣', 'J♠', 'J♥', 'J♦', 'J♣', 'Q♠', 'Q♥', 'Q♦', 'Q♣',
                      'K♠', 'K♥', 'K♦', 'K♣', 'A♠', 'A♥', 'A♦', 'A♣']


# функция для автоматического открытия флопа, тёрна, ривера, карт оппонента и рассчёта исхода раздачи
def all_in1(event):
    global win_count, loose_count, draw_count, deals_count1, royal_flush1, \
        straight_flush1, four_of_a_kind1, full_house1, flush1, straight1,  \
        three_of_a_kind1, two_pairs1, one_pair1, empty_combination1
    win_count, loose_count, draw_count, royal_flush1, straight_flush1, \
        four_of_a_kind1, full_house1, flush1, straight1, three_of_a_kind1, \
        two_pairs1, one_pair1, empty_combination1 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    if deals_count_entry.get().isdigit():
        deals_count1 = int(deals_count_entry.get())
    for x in range(deals_count1):
        two_players1(0)
        open_flop(0); open_tern(0); open_river(0)
        show_cards1(0)
        opp_cards.config(text = general_list[2] + ' ' + general_list[3])
        if winerrr2['text'] == 'Flawless victory !' or winerrr2['text'] == 'ROYAL FLUSH !!!':
            win_count += 1
        elif winerrr2['text'] == 'Теплотрасса ждёт !':
            loose_count += 1
        else:
            draw_count += 1
    statistic.deiconify()
    deals_count.configure(text = f'  count: {deals_count1}')
    win_label.configure(text = f'  win: {win_count} ({round(win_count / deals_count1 * 100, 2)} %)')
    loose_label.configure(text = f'  loose: {loose_count} ({round(loose_count / deals_count1 * 100, 2)} %)')
    draw_label.configure(text = f'  draw: {draw_count} ({round(draw_count / deals_count1 * 100, 2)} %)')
    royal_flush.configure(text = f'роял флэш: {royal_flush1} ({round(royal_flush1 / deals_count1 * 100, 2)} %)')
    straight_flush.configure(text = f'стрит флэш: {straight_flush1} ({round(straight_flush1 / deals_count1 * 100, 2)} %)')
    four_of_a_kind.configure(text = f'каре: {four_of_a_kind1} ({round(four_of_a_kind1 / deals_count1 * 100, 2)} %)')
    full_house.configure(text = f'фул хаус: {full_house1} ({round(full_house1 / deals_count1 * 100, 2)} %)')
    flush.configure(text = f'флэш: {flush1} ({round(flush1 / deals_count1 * 100, 2)} %)')
    straight.configure(text = f'стрит: {straight1} ({round(straight1 / deals_count1 * 100, 2)} %)')
    three_of_a_kind.configure(text = f'сет: {three_of_a_kind1} ({round(three_of_a_kind1 / deals_count1 * 100, 2)} %)')
    two_pairs.configure(text = f'две пары: {two_pairs1} ({round(two_pairs1 / deals_count1 * 100, 2)} %)')
    one_pair.configure(text = f'одна пара: {one_pair1} ({round(one_pair1 / deals_count1 * 100, 2)} %)')
    empty_combination.configure(text = f'кикер: {empty_combination1} ({round(empty_combination1 / deals_count1 * 100, 2)} %)')


# функция для очистки некоторых временных списков
def clear_tmp():
    global tmp_value, tmp_list, my_value, opp_value
    my_value, opp_value, tmp_value[2] = [], [], []
    tmp_list = [[[], [], 0], [[], [], 0], [[], [], 0], [[], [], 0],
                [[], [], 0], [[], [], 0], [[], [], 0], [[], [], 0]]


# функция для определения исхода раздачи
def winner1():
    global win_count
    # если наши с оппонентом комбинации не равны
    if tmp_value[0][0] != tmp_value[1][0]:
        # если наша комбинация старше
        if tmp_value[0][0] > tmp_value[1][0]:
            winerrr1.configure(image = win1)
            winerrr2.configure(font = ('JetBrains Mono', 20), text = 'Flawless victory !',
                               width = 20, height = 1)
        # если комбинация оппонента старше
        if tmp_value[0][0] < tmp_value[1][0]:
            winerrr1.configure(image = loose)
            winerrr2.configure(font = ('JetBrains Mono', 20), text = 'Теплотрасса ждёт !',
                               width = 20, height = 1)
    # если наши с оппонентом комбинации равны
    if tmp_value[0][0] == tmp_value[1][0]:
        # если сила нашей комбы больше, то мы выиграли
        if tmp_value[0][1] > tmp_value[1][1]:
            winerrr1.configure(image = win1)
            winerrr2.configure(font = ('JetBrains Mono', 20), text = 'Flawless victory !',
                               width = 20, height = 1)
        # если сила комбы оппонента больше, то он выиграл
        if tmp_value[0][1] < tmp_value[1][1]:
            winerrr1.configure(image = loose)
            winerrr2.configure(font = ('JetBrains Mono', 20), text = 'Теплотрасса ждёт !',
                               width = 20, height = 1)
        # если сила комбинаций равна
        if tmp_value[0][1] == tmp_value[1][1]:
            # если наш кикер больше
            if tmp_value[0][2] > tmp_value[1][2]:
                winerrr1.configure(image = win1)
                winerrr2.configure(font = ('JetBrains Mono', 20), text = 'Flawless victory !',
                                   width = 20, height = 1)
            # если кикер оппонента больше
            if tmp_value[0][2] < tmp_value[1][2]:
                winerrr1.configure(image = loose)
                winerrr2.configure(font = ('JetBrains Mono', 20), text = 'Теплотрасса ждёт !',
                                   width = 20, height = 1)
            # если кикеры равны, тогда делёжка
            if tmp_value[0][2] == tmp_value[1][2]:
                winerrr1.configure(image = draw)
                winerrr2.configure(font = ('JetBrains Mono', 20), text = 'Боевая ничья',
                                   width = 20, height = 1)
    if my_combination['text'] == 'роял флеш':
        winerrr1.configure(image = royal)
        winerrr2.configure(font = ('JetBrains Mono', 20), text = 'ROYAL FLUSH !!!',
                           width = 20, height = 1)
    # так как картинка при поражении по ширине сильно меньше картинок для
    # победы и делёжки, то задаём ей отдельное позиционирование
    if winerrr2['text'] == 'Flawless victory !' or winerrr2['text'] == 'Боевая ничья':
        winerrr1.place(x = 30, y = 30)
    else:
        winerrr1.place(x = 100, y = 30)
    winerrr2.place(x = 50, y = 350)


# функция для подтверждения выбора наших карт
def enter_my_card1(event):
    global general_list, tmp_value, enter_my_card_flag, deck_cards, variable, variable1
    # удаляем первую выбранную карту из колоды
    if my_card_select1['text'] in deck_cards:
        deck_cards.remove(my_card_select1['text'])
    # удаляем вторую выбранную карту из колоды
    if my_card_select2['text'] in deck_cards:
        deck_cards.remove(my_card_select2['text'])
    # ставим блокировку на случай, если выбранные карты совпадают с картами вышедшими из колоды
    if my_card_select1['text'] == my_card_select2['text'] or my_card_select1['text'] \
            in general_list[2:] or my_card_select2['text'] in general_list[2:]:
        return False
    my_cards.configure(text = str(my_card_select1['text']) + ' ' + str(my_card_select2['text']))
    # если был шоудаун
    if len_deck['text'] == 'карт в колоде: 43':
        general_list[0] = my_cards['text'].split(sep = ' ')[0]
        general_list[1] = my_cards['text'].split(sep = ' ')[1]
        tmp_value = [[], [], [], []]
        opp_cards['text'] = 'X X'
        show_cards1(event)
    # если шоудауна не было
    if len_deck['text'] == 'карт в колоде: 52' or len_deck['text'] == 'карт в колоде: 48':
        general_list = []
        enter_my_card_flag = 1
        general_list.append(my_cards['text'].split(sep = ' ')[0])
        general_list.append(my_cards['text'].split(sep = ' ')[1])
    len_deck.configure(text = 'карт в колоде: 50')


# функция для подтверждения выбора карт оппонента
def enter_opp_card1(event):
    global general_list, tmp_value, enter_opp_card_flag, deck_cards, variable2, variable3
    if len(general_list) < 2:
        return False
    # удаляем первую выбранную карту из колоды
    if opp_card_select1['text'] in deck_cards:
        deck_cards.remove(opp_card_select1['text'])
    # удаляем вторую выбранную карту из колоды
    if opp_card_select2['text'] in deck_cards:
        deck_cards.remove(opp_card_select2['text'])
    # ставим блокировку на случай, если выбранные карты совпадают с картами вышедшими из колоды
    if opp_card_select1['text'] == opp_card_select2['text'] or opp_card_select1['text'] \
            in general_list[2:] or opp_card_select2['text'] in general_list[2:]:
        return False
    opp_cards.configure(text = str(opp_card_select1['text']) + ' ' + str(opp_card_select2['text']))
    # если был шоудаун
    if len_deck['text'] == 'карт в колоде: 43':
        general_list[2] = opp_cards['text'].split(sep = ' ')[0]
        general_list[3] = opp_cards['text'].split(sep = ' ')[1]
        tmp_value = [[], [], [], []]
        opp_cards['text'] = 'X X'
        show_cards1(event)
    # если шоудауна не было
    if len_deck['text'] == 'карт в колоде: 52' or len_deck['text'] == 'карт в колоде: 48':
        general_list = []
        enter_opp_card_flag = 1
        general_list.append(my_cards['text'].split(sep = ' ')[0])
        general_list.append(my_cards['text'].split(sep = ' ')[1])


# функция для сброса всех значений до исходных
def clear_all1(event):
    global tmp_value, general_list, enter_my_card_flag, fck_mouth1_flag, fck_mouth1_flag1, \
        enter_my_card_flag, enter_opp_card_flag, len_deck
    clear_tmp()
    tmp_value = [[], [], []]
    general_list = []
    my_cards.configure(text = 'X X'); opp_cards.configure(text = 'X X')
    if fck_mouth1_flag1 == 1:
        mouth1.place_forget(); mouth2.place_forget()
    if len_deck['text'] == 'карт в колоде: 43' and opp_cards['text'] == 'X X':
        for x in [winerrr1, winerrr2, my_combination, opp_combination, xx1, xx2, flop1, tern1, river1]:
            x.place_forget()
    enter_my_card_flag, enter_opp_card_flag, fck_mouth1_flag, fck_mouth1_flag1 = 0, 0, 0, 0
    len_deck.configure(text = 'карт в колоде: 52')
    statistic.withdraw()


# функция закрывающая/открывающая наши карты
def close_my_card1(event):
    if my_cards['text'] == 'X X' and len_deck['text'] != 'карт в колоде: 52':
        my_cards.configure(text = str(general_list[0]) + ' ' + str(general_list[1]))
    else:
        my_cards.configure(text = 'X X')


# функция закрывающая/открывающая карты оппонента
def close_opp_card1(event):
    if opp_cards['text'] == 'X X' and len_deck['text'] != 'карт в колоде: 52' and \
            len_deck['text'] != 'карт в колоде: 50':
        opp_cards.configure(text = str(general_list[2]) + ' ' + str(general_list[3]))
    else:
        opp_cards.configure(text = 'X X')


# функция для выбора фона стола
def select_background1(event):
    global select_background1_flag
    fon.configure(image = background_image_collection[select_background1_flag])
    if select_background1_flag == 11:
        select_background1_flag = 0
    else:
        select_background1_flag += 1


# функция закрывает все окна
def close_windows():
    statistic.destroy()
    main.destroy()


# функция нахождения полного адреса до иконки приложения
def map_to_ico():
    path = os.path.abspath(os.path.abspath('dist/Poker-icon.ico'))
    path2 = ''
    for i in path:
        if i == "/":
            path2 += '\\'
        else:
            path2 += i
    return path2


# списки с готовой колодой, мастями и рангами
deck_cards = ['2♠', '2♥', '2♦', '2♣', '3♠', '3♥', '3♦', '3♣', '4♠', '4♥', '4♦',
              '4♣', '5♠', '5♥', '5♦', '5♣', '6♠', '6♥', '6♦', '6♣', '7♠', '7♥',
              '7♦', '7♣', '8♠', '8♥', '8♦', '8♣', '9♠', '9♥', '9♦', '9♣', '10♠',
              '10♥', '10♦', '10♣', 'J♠', 'J♥', 'J♦', 'J♣', 'Q♠', 'Q♥', 'Q♦', 'Q♣',
              'K♠', 'K♥', 'K♦', 'K♣', 'A♠', 'A♥', 'A♦', 'A♣']
suit = ['♠', '♥', '♦', '♣']
rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# список для хранения названий комбинаций (не используется, возможно можно удалить)
combinations1 = ['стрит флэш', 'каре', 'фул хаус', 'флэш', 'стрит', 'две пары', 'пара']

general_list = []         # список для хранения всех вышедших из колоды карт
my_value = []             # моя комбинация
opp_value = []            # комбинация оппонента
tmp_value = [[], [], []]  # временный список для хранения сгенерированных функцией значений
fck_mouth1_flag = 0       # флаг для функции fck_mouth1()
fck_mouth1_flag1 = 0      # флаг для функции fck_mouth1()
enter_my_card_flag = 0    # флаг для функции enter_my_card1
enter_opp_card_flag = 0   # флаг для функции enter_opp_card1
select_background1_flag = 1  # флаг для функции background1_flag1() для смены фона стола
deals_count1 = 1          # переменная для хранения количества раздач для розыгрыша
win_count = 0             # количество выигранных раздач
loose_count = 0           # количество проигранных раздач
draw_count = 0            # количество делёжек
royal_flush1 = 0          # количество роял флешей
straight_flush1 = 0       # количество стрит флэшей
four_of_a_kind1 = 0       # количество стрит каре
full_house1 = 0           # количество фул хаусов
flush1 = 0                # количество фэшей
straight1 = 0             # количество стритов
three_of_a_kind1 = 0      # количество сетов
two_pairs1 = 0            # количество двух пар
one_pair1 = 0             # количество одной пары
empty_combination1 = 0    # количество раздач без комбинации

# стрит флэш, каре, фул хаус, флэш, стрит, сет, две пары, пара
# формат вложенных списков: [[сама комбинация], [сила комбинации], [флаг]]
tmp_list = [[[], [], 0], [[], [], 0], [[], [], 0], [[], [], 0],
            [[], [], 0], [[], [], 0], [[], [], 0], [[], [], 0]]
# вспомогательные списки для перевода букв в числа
tmp_board1 = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
tmp_board2 = ['2', '3', '4', '5', '6', '7', '8', '9', '1', 'J', 'Q', 'K', 'A']

# создаём окно прогаммы
main = tk.Tk()
main.title('Покерррррр')
main.geometry('1050x800+800+200')
main.resizable(False, False)
main.iconbitmap(map_to_ico())

# создаём окно статистики и скрываем его
statistic = tk.Tk()
statistic.title('Статистика')
statistic.geometry('650x500+140+200')
statistic.resizable(False, False)
statistic.withdraw()

# назначаем ширину первой колонки в окне статистики
statistic.grid_columnconfigure(0, minsize=200)

# сохраняем все фоны для стола и добавляем их в список
fon1 = ImageTk.PhotoImage(Image.open('Изображения/fon1.jpg'))
fon2 = tk.PhotoImage(file= 'Изображения/fon2.gif')
fon3 = ImageTk.PhotoImage(Image.open('Изображения/fon3.jpg'))
fon4 = ImageTk.PhotoImage(Image.open('Изображения/fon4.jpg'))
fon5 = ImageTk.PhotoImage(Image.open('Изображения/fon5.jpg'))
fon6 = ImageTk.PhotoImage(Image.open('Изображения/fon6.jpg'))
fon7 = ImageTk.PhotoImage(Image.open('Изображения/fon7.jpg'))
fon8 = ImageTk.PhotoImage(Image.open('Изображения/fon8.jpg'))
fon9 = ImageTk.PhotoImage(Image.open('Изображения/fon9.jpg'))
fon10 = ImageTk.PhotoImage(Image.open('Изображения/fon10.jpg'))
fon11 = ImageTk.PhotoImage(Image.open('Изображения/fon11.jpg'))
fon12 = ImageTk.PhotoImage(Image.open('Изображения/fon12.jpg'))
background_image_collection = [fon1, fon2, fon3, fon4, fon5, fon6, fon7,
                               fon8, fon9, fon10, fon11, fon12]

# сохраняем изображения для мемов и вариантов исхода раздачи и добавляем их в список
rot0 = ImageTk.PhotoImage(Image.open('Изображения/rot0.jpg'))
rot1 = ImageTk.PhotoImage(Image.open('Изображения/rot1.jpg'))
rot2 = ImageTk.PhotoImage(Image.open('Изображения/rot2.jpg'))
win1 = ImageTk.PhotoImage(Image.open('Изображения/win1.jpg'))
royal = ImageTk.PhotoImage(Image.open('Изображения/royal.jpg'))
loose = ImageTk.PhotoImage(Image.open('Изображения/loose.jpg'))
draw = ImageTk.PhotoImage(Image.open('Изображения/draw.jpg'))
image_collection = [rot0, rot1, rot2, win1, loose, draw, royal]
words_collection = ['Кто вы такой, сударь !?', 'Я очень возмущён !', 'Да что ж такое !']

# создаём виджет для показа фона стола
fon = tk.Label(main, image = fon1); fon.pack()

# создаём меню выбора наших карт в виде выпадающего списка
variable = StringVar(main); variable.set(deck_cards[10])

variable1 = StringVar(main); variable1.set(deck_cards[15])

my_card_select1 = OptionMenu(main, variable, *deck_cards)
my_card_select1.configure(font=('JetBrains Mono', 15)); my_card_select1.place(x=890, y=500)

my_card_select2 = OptionMenu(main, variable1, *deck_cards)
my_card_select2.configure(font=('JetBrains Mono', 15)); my_card_select2.place(x=890, y=547)

# создаём кнопку подтверждения выбора наших карт, связываем её с функцией
enter_my_card = tk.Button(main, text='OK', font=('JetBrains Mono', 12), bd=5, width=2, height=1)
enter_my_card.bind('<Button-1>', enter_my_card1); enter_my_card.place(x=980, y=500)

# кнопка для скрытия/показа наших карт
close_my_card = tk.Button(main, text='\u2BBF', font=('JetBrains Mono', 12), bd=5, width=2, height=1)
close_my_card.bind('<Button-1>', close_my_card1); close_my_card.place(x=980, y=547)

# создаём меню выбора карт оппонента в виде выпадающего списка
variable2 = StringVar(main); variable2.set(deck_cards[10])

variable3 = StringVar(main); variable3.set(deck_cards[15])

opp_card_select1 = OptionMenu(main, variable2, *deck_cards)
opp_card_select1.configure(font=('JetBrains Mono', 15)); opp_card_select1.place(x=890, y=75)

opp_card_select2 = OptionMenu(main, variable3, *deck_cards)
opp_card_select2.configure(font=('JetBrains Mono', 15)); opp_card_select2.place(x=890, y=122)

# создаём кнопку подтверждения выбора карт оппонента, связываем её с функцией
enter_opp_card = tk.Button(main, text='OK', font=('JetBrains Mono', 12), bd=5, width=2, height=1)
enter_opp_card.bind('<Button-1>', enter_opp_card1); enter_opp_card.place(x=980, y=75)

# кнопка для скрытия/показа карт оппонента
close_opp_card = tk.Button(main, text='\u2BBF', font=('JetBrains Mono', 12), bd=5, width=2, height=1)
close_opp_card.bind('<Button-1>', close_opp_card1); close_opp_card.place(x=980, y=122)

# создаём кнопку раздачи карманных карт, связываем её с функцией
btn1 = tk.Button(main, text='раздать карты', font=('JetBrains Mono', 15), bd=5, width=26, height=1)
btn1.bind('<Button-1>', two_players1); btn1.place(x=51, y=540)

# создаём кнопку открытия флопа, связываем её с функцией
flop = tk.Button(main, text='флоп', font=('JetBrains Mono', 15), bd=5, width=26, height=1)
flop.bind('<Button-1>', open_flop); flop.place(x=51, y=600)

# создаём виджет для отображения карт флопа
flop1 = tk.Label(main); flop1.pack()

# создаём кнопку открытия тёрна, связываем её с функцией
tern = tk.Button(main, text='тёрн', font=('JetBrains Mono', 15), bd=5, width=26, height=1)
tern.bind('<Button-1>', open_tern); tern.place(x=51, y=660)

# создаём виджет для отображения карты тёрна
tern1 = tk.Label(main); tern1.pack()

# создаём кнопку открытия ривера, связываем её с функцией
river = tk.Button(main, text='ривер', font=('JetBrains Mono', 15), bd=5, width=26, height=1)
river.bind('<Button-1>', open_river); river.place(x=51, y=720)

# создаём виджет для отображения карты ривера
river1 = tk.Label(main); river1.pack()

# создаём виджет для отображения наших карт
my_cards = tk.Label(main, font=('JetBrains Mono', 50), text='X X', width=9, height=1)
my_cards.place(x=510, y=500)

# создаём виджет для отображения карт оппонента
opp_cards = tk.Label(main, font=('JetBrains Mono', 50), text='X X', width=9, height=1)
opp_cards.place(x=510, y=75)

# создаём виджет со счётчиком карт в колоде
len_deck = tk.Label(main, font=('JetBrains Mono', 20), text='карт в колоде: 52', width=20, height=1)
len_deck.place(x=50, y=450)

# создаём кнопку для шоудауна, связываем её с функцией
show_cards = tk.Button(main, text='вскрываемся', font=('JetBrains Mono', 15), bd=5, width=24, height=1)
show_cards.bind('<Button-1>', show_cards1); show_cards.place(x=494, y=660)

# создаём кнопку для показа мема, связываем её с функцией
fck_mouth = tk.Button(main, text='... этого казино', font=('JetBrains Mono', 15), bd=5,
                      width=24, height=1)
fck_mouth.bind('<Button-1>', fck_mouth1); fck_mouth.place(x=494, y=720)

# создаём кнопку для закрытия мема, связываем её с функцией
close_mouth = tk.Button(main, text='\u2BBF', font=('JetBrains Mono', 15), bd=5, width=2, height=1)
close_mouth.bind('<Button-1>', delete_mouth); close_mouth.place(x=820, y=720)

# создаём кнопку для выбора фона стола, связываем её с функцией
select_background = tk.Button(main, font=('JetBrains Mono', 15),
                              text='сменить фон', width=12, bd=5, height=1)
select_background.bind('<Button-1>', select_background1); select_background.place(x=872, y=720)

# создаём кнопку для сброса всех значений до исходных, связываем её с функцией
clear_all = tk.Button(main, font=('JetBrains Mono', 15), text='очистить', width=8, bd=5, height=1)
clear_all.bind('<Button-1>', clear_all1); clear_all.place(x=920, y=660)

# создаём виджет для показа картинки мема
mouth2 = tk.Label(main, image = rot1); mouth2.pack()

# создаём виджет для показа текста мема
mouth1 = tk.Label(main, font = ('JetBrains Mono', 20), text = 'Ты кто такой, сука !?', width = 27, height = 1)
mouth1.pack()

# создаём виджет для показа моей комбинации
my_combination = tk.Label(main, font=('JetBrains Mono', 20), text='пусто', width=27, height=1)
my_combination.pack()

# создаём виджет для показа комбинации оппонента
opp_combination = tk.Label(main, font=('JetBrains Mono', 20), text='пусто', width=27, height=1)
opp_combination.pack()

# создаём кнопку для олына, связываем её с функцией
all_in = tk.Button(main, text='all in', font=('JetBrains Mono', 15), bd=5, width=6, height=1)
all_in.bind('<Button-1>', all_in1); all_in.place(x=820, y=660)

# создаём виджет для отображения индикатора старшинства нашей комбинации
xx1 = tk.Label(main, font=('JetBrains Mono', 20), width=2, height=1)

# создаём виджет для отображения индикатора старшинства комбинации оппонента
xx2 = tk.Label(main, font=('JetBrains Mono', 20), width=2, height=1)

# создаём виджет для показа изображения исхода раздачи
winerrr1 = tk.Label(main); winerrr1.pack()

# создаём виджет для показа текста исхода раздачи
winerrr2 = tk.Label(main); winerrr2.pack()

# поле для ввода количества раздач для розыгрыша
deals_count_entry = Entry(main, font=('JetBrains Mono', 15), width=10, bd = 5)
deals_count_entry.place(x = 690, y = 610)

# виджет с текстовым пояснением для поля ввода количества раздач для розыгрыша
deals_count_entry1 = tk.Label(main, text = 'кол-во раздач:',
                              font=('JetBrains Mono', 15), width=14, bd = 5)
deals_count_entry1.place(x = 494, y = 610)

# виджет, показывающий количество раздач
deals_count = tk.Label(statistic, font=('JetBrains Mono', 15), anchor='w', width=25, height=1)
deals_count.grid(row = 0, column = 0)

# виджет, показывающий сколько раз выиграли
win_label = tk.Label(statistic, font=('JetBrains Mono', 15), anchor='w', width=25, height=1)
win_label.grid(row = 1, column = 0)

# виджет, показывающий сколько раз проиграли
loose_label = tk.Label(statistic, font=('JetBrains Mono', 15), anchor='w', width=25, height=1)
loose_label.grid(row = 2, column = 0)

# виджет, показывающий сколько раз поделили
draw_label = tk.Label(statistic, font=('JetBrains Mono', 15), anchor='w', width=25, height=1)
draw_label.grid(row = 3, column = 0)

# виджет, в котором отображается количество роял флешей
royal_flush = tk.Label(statistic, font=('JetBrains Mono', 15), anchor='w', width=60, height=1)
royal_flush.grid(row = 0, column = 1)

# виджет, в котором отображается количество стрит-флешей
straight_flush = tk.Label(statistic, font=('JetBrains Mono', 15), anchor='w', width=60, height=1)
straight_flush.grid(row = 1, column = 1)

# виджет, в котором отображается количество каре
four_of_a_kind = tk.Label(statistic, font=('JetBrains Mono', 15), anchor='w', width=60, height=1)
four_of_a_kind.grid(row = 2, column = 1)

# виджет, в котором отображается количество фул хаусов
full_house = tk.Label(statistic, font=('JetBrains Mono', 15), anchor='w', width=60, height=1)
full_house.grid(row = 3, column = 1)

# виджет, в котором отображается количество флэшей
flush = tk.Label(statistic, font=('JetBrains Mono', 15), anchor='w', width=60, height=1)
flush.grid(row = 4, column = 1)

# виджет, в котором отображается количество стритов
straight = tk.Label(statistic, font=('JetBrains Mono', 15), anchor='w', width=60, height=1)
straight.grid(row = 5, column = 1)

# виджет, в котором отображается количество сетов
three_of_a_kind = tk.Label(statistic, font=('JetBrains Mono', 15), anchor='w', width=60, height=1)
three_of_a_kind.grid(row = 6, column = 1)

# виджет, в котором отображается количество двух пар
two_pairs = tk.Label(statistic, font=('JetBrains Mono', 15), anchor='w', width=60, height=1)
two_pairs.grid(row = 7, column = 1)

# виджет, в котором отображается количество одной пары
one_pair = tk.Label(statistic, font=('JetBrains Mono', 15), anchor='w', width=60, height=1)
one_pair.grid(row = 8, column = 1)

# виджет, в котором отображается количество раздач без комбинаций
empty_combination = tk.Label(statistic, font=('JetBrains Mono', 15), anchor='w', width=60, height=1)
empty_combination.grid(row = 9, column = 1)

# программируем кнопку закрытия окна статистики, чтобы она лишь скрывала его
statistic.protocol("WM_DELETE_WINDOW", statistic.withdraw)

# программируем закрытие (уничтожение) всех окон при закрытии главного окна
main.protocol("WM_DELETE_WINDOW", close_windows)

main.mainloop()
