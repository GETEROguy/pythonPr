import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTableView
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel

# Устанавливаем соединение с базой данных
def create_connection():
    connection = None
    try:
        connection = sqlite3.connect("coffee.sqlite")
        print("Connection to SQLite DB successful")
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")

    if connection:
        return connection

# Создаем модель данных для отображения в таблице
class CoffeeTableModel(QSqlTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTable("coffee")  # Указываем, что модель будет работать с таблицей "coffee"
        self.select()  # Выбираем все записи из таблицы

# Создаем окно приложения и размещаем в нем таблицу
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Coffee Viewer")

        # Создаем виджет таблицы
        table_view = QTableView()
        # Создаем модель данных
        model = CoffeeTableModel()
        # Устанавливаем модель данных для таблицы
        table_view.setModel(model)

        # Создаем вертикальный layout и устанавливаем в него таблицу
        layout = QVBoxLayout()
        layout.addWidget(table_view)

        # Создаем центральный виджет и устанавливаем в него layout
        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

# Запускаем приложение
if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    # Создаем соединение с базой данных
    connection = create_connection()
    if connection:
        main_window = MainWindow()
        main_window.show()

        sys.exit(app.exec_())
    else:
        print("Database connection failed")