import sys
import json

from PyQt5.QtWidgets import QApplication

from src.routes.editor import Editor
from src.routes.preview import Preview


app = QApplication(sys.argv)
app.processEvents()

def main (config_path):
    editor_window  = Editor(app, config_path)
    editor_window.preview = Preview(app, config_path)

    sys.exit(app.exec_())


if __name__ == '__main__':
    try:
        config_path = sys.argv[1]
        main(config_path)
    except KeyboardInterrupt as r:
        sys.exit()
    except Exception as r:
        raise
    