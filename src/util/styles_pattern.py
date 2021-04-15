_all = '''
*{

}
'''

_QMainWindow = '''
QMainWindow,QWidget
{
}
'''

_QMenuBar = '''
_QMenuBar
{
}
QMenuBar::item:selected
{
}
'''

_QMenu = '''
QMenu
{
}
QMenu::item:selected 
{
}
QMenu::separator 
{
}

'''

_QTabBar = '''
QTabBar::tab 
{
}

QTabBar::tab:selected 
{
}
QTableWidget QTableCornerButton::section 
{
}
'''


_QLineEdit = '''
QLineEdit
{
}
QLineEdit:disabled
{
}
'''

_QTextBrowser = '''
QTextBrowser
{
}
QTextBrowser:disabled
{
}
'''

_QTextEdit = '''
QTextEdit
{
}
QTextEdit:disabled
{
}
'''

_QPlainTextEdit  = '''
QPlainTextEdit 
{
}
QPlainTextEdit :disabled
{
}
'''

_QComboBox = '''
QComboBox 
{
}

QComboBox:hover
{
}

QComboBox:selected
{
}

QComboBox::drop-down
{
}

QComboBox::down-arrow 
{
}
'''

_QCheckBox = '''
QCheckBox
{
}
'''


_QToolBox = '''
QToolBox::tab
{
}
QToolBox::tab::selected
{
}
QToolBox::tab::hover
{
}
'''

_QProgressBar = '''
QProgressBar 
{
}
QProgressBar::chunk 
{
}
'''

_QPushButton = '''
QPushButton
{
}
QPushButton:hover
{
}
QPushButton:pressed
{
}
'''

_QLCDNumber = '''
QLCDNumber
{
}
'''

_QTable = '''
QTableView,
QTableWidget,
QTreeView
{
}
QTableView::item:selected, QTableView::item:hover,
QListView::item:selected , QListView::item:hover,
QTreeView::item:selected , QTreeView::item:hover 
{
}
QTableView::item, 
QListView::item, 
QTreeView::item
{
}
QTreeView::item:selected,
QListView::item:selected,
QTableView::item:selected
{
}
QTreeView::item:has-children
{
}
'''
_QHeaderView = '''
QHeaderView::section 
{
}
'''

_QCalendarView = '''
QCalendarView
{ 
}
QAbstractItemView
{
}
'''

_QSlider = '''
QSlider::groove:horizontal,QSlider::add-page:horizontal 
{
}
QSlider::sub-page:horizontal 
{
}
QSlider::handle:horizontal 
{
}
QSlider::handle:horizontal:hover 
{
}
QSlider::handle
{
}
QSlider::groove:vertical,QSlider::add-page:vertical,QSlider::sub-page:vertical 
{
}
QSlider::handle:vertical 
{
}
QSlider::handle:vertical:hover 
{
}
'''

_QScrollBar = '''
QScrollBar::groove:horizontal
{
}
QScrollBar::sub-page:horizontal,QScrollBar::add-page:horizontal  
{
}
QScrollBar::handle:horizontal 
{
}
QScrollBar::handle:horizontal:hover 
{
}
QScrollBar:vertical 
{
}
QScrollBar::handle:vertical 
{
}
QScrollBar::up-arrow:vertical 
{
}
QScrollBar::down-arrow:vertical 
{
}
QScrollBar::sub-line:vertical 
{
}
QScrollBar::add-line:vertical 
{
}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical 
{
}
'''

_QToolBar = '''
QToolBar 
{
}
QToolBar:separator 
{
}
QToolBar QToolButton 
{ 
}
QToolButton
{
}
QToolButton:hover,QToolButton:pressed     
{ 
}
QMessageBox QLabel
{
}
'''