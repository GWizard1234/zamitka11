

from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit, QPushButton, QListWidget , QVBoxLayout )

app = QApplication([])
window  = QWidget()


but1 = QPushButton("Добавити")
but2 = QPushButton("Видалити")
but3 = QPushButton("Зберегти")

line  = QLineEdit()
line1 = QListWidget()

v = QVBoxLayout()
v.addWidget(line)
v.addWidget(but1)
v.addWidget(line1)
v.addWidget(but2)
v.addWidget(but3)
window.setLayout(v)

tasks = []
def add_task():
    t = line.text() 
    if t:
        tasks.append(t)  
        line1.addItem(t)
        line.clear()
but1.clicked.connect(add_task)

def remove_task():
    t = line1.currentRow()
    if t >= 0:
        del tasks[t]
        line1.takeItem(t)
but2.clicked.connect(remove_task)

def save_task():
    with open("tasks.txt",'w') as file:
        for t in tasks:
            file.write(t+'\n')
but3.clicked.connect(save_task)


window.show()
app.exec_()