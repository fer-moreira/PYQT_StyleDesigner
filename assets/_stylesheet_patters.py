_all ='''
/*  ---------------------------- ALL OTHERS WIDGETS ---------------------------- */
*{
    font-family: Arial, Helvetica, sans-serif;
    selection-background-color: #9C9C9B;
}
'''

_mainWidget = '''
/*  ---------------------------- MAIN WINDOW, WIDGET ---------------------------- */
QMainWindow,QWidget
{

}
'''

_menuBar = '''
/*  ---------------------------- MENU BAR ---------------------------- */
QMenuBar,QMenu
{

}
QMenuBar::item:selected,QMenu::item:selected 
{

}
QMenu::separator {

}
'''

_tabWidget = '''
/*  ---------------------------- TAB WIDGET ---------------------------- */
QTabWidget::tab-bar 
{

}
QTabBar::tab {

}
QTabBar::tab:selected, QTabBar::tab:hover {

}
'''

_textInput = '''
/*  ---------------------------- LINE_EDIT TEXT BROWSER TEXT_EDIT PLAIN_TEXT ---------------------------- */
QLineEdit,QTextBrowser,QTextEdit,QPlainTextEdit 
{

}
'''

_comboBoxCheckBox = '''
/*  ---------------------------- CHECK/COMBO BOX ----------------------------*/
QCheckBox,QComboBox
{

}
'''

_toolBox = '''
/* ----------------------------  TOOL BOX  ----------------------------  */
QToolBox
{

}
QToolBox::tab
{

}
QToolBox::tab::selected,QToolBox::tab::hover
{

}
'''

_progressBar = '''
/*  ---------------------------- PROGRESS BAR ---------------------------- */
QProgressBar {

}
QProgressBar::chunk {

}
'''

_pushButton = '''
/*  ---------------------------- PUSHBUTTON ---------------------------- */
QPushButton
{

}
QPushButton:hover, QPushButton:pressed 
{

}
'''

_lcdNumber = '''
/*  ----------------------------  LCD NUMBER ---------------------------- */
QLCDNumber
{
    
}
'''

_TableList = '''
/*  ---------------------------- TABLE_LIST_TABLE ---------------------------- */
QTreeView,QListView,QTableView
{

}
QTableView::item:selected, QListView::item:selected 
{

}
QTableView::item:hover, QListView::item:hover, QTreeView::item:hover 
{

}
QTableView::item, QListView::item, QTreeView::item 
{

}
QTreeView::item:selected 
{

}
'''

_headerView = '''
/*  ---------------------------- HEADER VIEW ---------------------------- */
QHeaderView::section 
{

}
'''
