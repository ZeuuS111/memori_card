'''Вікно для редагування'''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*

txt_Question = QLineEdit('')
txt_Answer = QLineEdit('')
txt_Wrong1 = QLineEdit('')
txt_Wrong2 = QLineEdit('')
txt_Wrong3 = QLineEdit('')

layout_from = QFormLayout()

layout_from.addRow('Питання:', txt_Question)
layout_from.addRow('Правильна відповідь:', txt_Answer)
layout_from.addRow('Неправельний варіант №1:', txt_Wrong1)
layout_from.addRow('Неправельний варіант №2:', txt_Wrong2)
layout_from.addRow('Неправельний варіант №3:', txt_Wrong3)