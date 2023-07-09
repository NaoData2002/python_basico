import sys
from PyQt5.QtWidgets import QApplication
from note_window import NoteWindow

def main():
    app = QApplication(sys.argv)
    note_window = NoteWindow()
    note_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
