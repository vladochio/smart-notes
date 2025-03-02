from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from file_helper import *

app = QApplication([])


notes = read_from_file()
window = QWidget()
window.setWindowTitle('Розумні замітки')
window.resize(900, 600)

list_notes = QListWidget()
list_notes.addItems(notes)

list_notes_label = QLabel('Список заміток')

button_note_create = QPushButton('Створити замітку ')
button_note_del = QPushButton('Видалити замітку')
button_note_save = QPushButton('Зберегти замітку')

field_tag = QLineEdit('')
field_tag.setPlaceholderText('Введіть тег...')
field_text = QTextEdit()
button_tag_add = QPushButton('Добавити до змітки')
button_tag_del = QPushButton('Відкріпити від змітки')
button_tag_search = QPushButton('Шукати замітку по тегу')
list_tags = QListWidget()
list_tags_label = QLabel('Список тегів')

layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)

col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)

col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)
row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(button_tag_del)
row_4 = QHBoxLayout()
row_4.addWidget(button_tag_search)

col_2.addLayout(row_3)
col_2.addLayout(row_4)

layout_notes.addLayout(col_1, stretch=2)
layout_notes.addLayout(col_2, stretch=1)
window.setLayout(layout_notes)

def show_note():
    key = list_notes.currentItem().text()
    field_text.setText(notes[key]["текст"])
    list_tags.clear()
    list_tags.addItems(notes[key]["теги"])
    print(notes[key])

list_notes.itemClicked.connect(show_note)

def create_note_func():
    note_name, ok = QInputDialog.getText(window, 
                        "Створення замітки",
                        "Назва замітку")
    if ok == True:
        notes[note_name] = {
            "текст": "купити пельмені ",
            "теги": [1111]
        }
        list_notes.clear()
        list_notes.addItems(notes)
        write_in_file(notes)

def delete_note_func():
    key = list_notes.currentItem().text()
    notes.pop(key)
    list_notes.clear()
    list_notes.addItems(notes)
    write_in_file(notes)

button_note_create.clicked.connect(create_note_func)

def save_note_func():
    (button_note_save)
    list_notes.itemClicked.connect(show_note)
    button_note_create.clicked.connect(button_note_save)

def add_tag():
    key = list_notes.currentItem().text()
    notes.pop(key)
    notes[key]["текст"] = field_text.toPlainText()
    list_notes.addItems(notes)
    write_in_file(notes)

def delete_tags():
    key_note = list_notes.currentItem().text()
    tag = list_tags.currentItem().text()
    notes[key_note]["теги"].remove(tag)
    list_notes.clear()
    list_notes.addItems(notes)
    write_in_file(notes)

button_tag_add.clicked.connect(add_tag)
button_note_create.clicked.connect(create_note_func)
list_notes.itemClicked.connect(show_note)

window.show()
app.exec_()