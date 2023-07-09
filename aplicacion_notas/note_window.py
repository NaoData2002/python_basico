from PyQt5.QtWidgets import QMainWindow, QInputDialog, QTreeWidgetItem, QMessageBox, QListWidget, QPushButton, QVBoxLayout, QApplication, QWidget, QTextEdit, QLabel
from PyQt5.QtCore import QTimer, Qt
from database import Database
from note import Note
import sys

class NoteWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Conexión a la base de datos
        self.db = Database('notes.db')

        # Interfaz de usuario
        self.init_ui()

        # Cargar las notas
        self.load_notes()

        # Crear un timer para revisar las fechas límite
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_deadlines)
        self.timer.start(60000)  # Revisar cada minuto

    def init_ui(self):
        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('Aplicación de Notas')

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel('Mis Notas')
        self.layout.addWidget(self.label)

        self.list_widget = QListWidget()
        self.layout.addWidget(self.list_widget)

        self.add_button = QPushButton('Agregar Nota')
        self.add_button.clicked.connect(self.add_note)
        self.layout.addWidget(self.add_button)

        self.update_button = QPushButton('Actualizar Nota')
        self.update_button.clicked.connect(self.update_note)
        self.layout.addWidget(self.update_button)

        self.delete_button = QPushButton('Eliminar Nota')
        self.delete_button.clicked.connect(self.delete_note)
        self.layout.addWidget(self.delete_button)

    def load_notes(self):
        self.notes = self.db.get_all()
        self.list_widget.clear()
        for note in self.notes:
            self.list_widget.addItem(note.content)

    def add_note(self):
        text, ok = QInputDialog.getText(self, 'Agregar Nota', 'Ingrese el contenido de la nota:')
        if ok:
            note = Note(content=text)
            self.db.add(note)
            self.load_notes()

    def update_note(self):
        selected_note = self.list_widget.currentItem()
        if selected_note is None:
            QMessageBox.warning(self, 'Advertencia', 'Seleccione una nota para actualizar.')
            return
        text, ok = QInputDialog.getText(self, 'Actualizar Nota', 'Actualice el contenido de la nota:', text=selected_note.text())
        if ok:
            note = next((note for note in self.notes if note.content == selected_note.text()), None)
            if note is not None:
                note.content = text
                self.db.update(note)
                self.load_notes()

    def delete_note(self):
        selected_note = self.list_widget.currentItem()
        if selected_note is None:
            QMessageBox.warning(self, 'Advertencia', 'Seleccione una nota para eliminar.')
            return
        note = next((note for note in self.notes if note.content == selected_note.text()), None)
        if note is not None:
            self.db.delete(note)
            self.load_notes()

    def check_deadlines(self):
        # Asegurarse de que las notas están cargadas
        self.load_notes()

        # Buscar notas con fechas límite pasadas
        for note in self.notes:
            if note.is_deadline_passed():
                QMessageBox.warning(self, 'Recordatorio', f'La fecha límite para la nota "{note.content}" ha pasado.')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NoteWindow()
    window.show()
    sys.exit(app.exec_())
