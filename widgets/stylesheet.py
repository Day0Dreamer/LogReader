stylesheet_orange = '''QToolTip
{
     border: 1px solid black;
     background-color: #ffa02f;
     padding: 1px;
     border-radius: 3px;
     opacity: 100;
}

QWidget
{
    color: #b1b1b1;
    background-color: #323232;
}

QWidget:item:hover
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);
    color: #000000;
}

QWidget:item:selected
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
}

QMenuBar::item
{
    background: transparent;
}

QMenuBar::item:selected
{
    background: transparent;
    border: 1px solid #ffaa00;
}

QMenuBar::item:pressed
{
    background: #444;
    border: 1px solid #000;
    background-color: QLinearGradient(
        x1:0, y1:0,
        x2:0, y2:1,
        stop:1 #212121,
        stop:0.4 #343434/*,
        stop:0.2 #343434,
        stop:0.1 #ffaa00*/
    );
    margin-bottom:-1px;
    padding-bottom:1px;
}

QMenu
{
    border: 1px solid #000;
}

QMenu::item
{
    padding: 2px 20px 2px 20px;
}

QMenu::item:selected
{
    color: #000000;
}

QWidget:disabled
{
    color: #404040;
    background-color: #323232;
}

QAbstractItemView
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);
}

QWidget:focus
{
    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/
}

QLineEdit
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);
    padding: 1px;
    border-style: solid;
    border: 1px solid #1e1e1e;
    border-radius: 5;
}

QPushButton
{
    color: #b1b1b1;
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);
    border-width: 1px;
    border-color: #1e1e1e;
	border-style: solid;
    padding: 3px;
    font-size: 12px;
    padding-left: 5px;
    padding-right: 5px;
}

QPushButton:pressed
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);
}

QComboBox
{
    selection-background-color: #ffaa00;
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);
    border-style: solid;
    border: 1px solid #1e1e1e;
    border-radius: 5;
}

QComboBox:hover,QPushButton:hover
{
    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
}


QComboBox:on
{
    padding-top: 3px;
    padding-left: 4px;
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);
    selection-background-color: #ffaa00;
}

QComboBox QAbstractItemView
{
    border: 2px solid darkgray;
    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
}

QComboBox::drop-down
{
     subcontrol-origin: padding;
     subcontrol-position: top right;
     width: 15px;
     border-style: inset;
     border-radius: 6;
     border-left-width: 0px;
     border-left-color: darkgray;
     border-left-style: solid; /* just a single line */
     border-top-right-radius: 3px; /* same radius as the QComboBox */
     border-bottom-right-radius: 3px;
 }

QComboBox::down-arrow
{
     image: url(:/down_arrow.png);
}

QGroupBox:focus
{
border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
}

QTextEdit:focus
{
    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
}

QScrollBar:horizontal {
     border: 1px solid #222222;
     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);
     height: 7px;
     margin: 0px 16px 0 16px;
}

QScrollBar::handle:horizontal
{
      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);
      min-height: 20px;
      border-radius: 2px;
}

QScrollBar::add-line:horizontal {
      border: 1px solid #1b1b19;
      border-radius: 2px;
      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);
      width: 14px;
      subcontrol-position: right;
      subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal {
      border: 1px solid #1b1b19;
      border-radius: 2px;
      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);
      width: 14px;
     subcontrol-position: left;
     subcontrol-origin: margin;
}

QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal
{
      border: 1px solid black;
      width: 1px;
      height: 1px;
      background: white;
}

QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
{
      background: none;
}

QScrollBar:vertical
{
      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);
      width: 7px;
      margin: 16px 0 16px 0;
      border: 1px solid #222222;
}

QScrollBar::handle:vertical
{
      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);
      min-height: 20px;
      border-radius: 2px;
}

QScrollBar::add-line:vertical
{
      border: 1px solid #1b1b19;
      border-radius: 2px;
      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
      height: 14px;
      subcontrol-position: bottom;
      subcontrol-origin: margin;
}

QScrollBar::sub-line:vertical
{
      border: 1px solid #1b1b19;
      border-radius: 2px;
      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);
      height: 14px;
      subcontrol-position: top;
      subcontrol-origin: margin;
}

QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical
{
      border: 1px solid black;
      width: 1px;
      height: 1px;
      background: white;
}


QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
{
      background: none;
}

QTextEdit
{
    background-color: #242424;
}

QPlainTextEdit
{
    background-color: #242424;
}

QHeaderView::section
{
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);
    color: white;
    padding-left: 4px;
    border: 1px solid #6c6c6c;
}

QCheckBox:disabled
{
color: #414141;
}

QDockWidget::title
{
    text-align: center;
    spacing: 3px; /* spacing between items in the tool bar */
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);
}

QDockWidget::close-button, QDockWidget::float-button
{
    text-align: center;
    spacing: 1px; /* spacing between items in the tool bar */
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);
}

QDockWidget::close-button:hover, QDockWidget::float-button:hover
{
    background: #242424;
}

QDockWidget::close-button:pressed, QDockWidget::float-button:pressed
{
    padding: 1px -1px -1px 1px;
}

QMainWindow::separator
{
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);
    color: white;
    padding-left: 4px;
    border: 1px solid #4c4c4c;
    spacing: 3px; /* spacing between items in the tool bar */
}

QMainWindow::separator:hover
{

    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);
    color: white;
    padding-left: 4px;
    border: 1px solid #6c6c6c;
    spacing: 3px; /* spacing between items in the tool bar */
}

QToolBar::handle
{
     spacing: 3px; /* spacing between items in the tool bar */
     background: url(:/images/handle.png);
}

QMenu::separator
{
    height: 2px;
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);
    color: white;
    padding-left: 4px;
    margin-left: 10px;
    margin-right: 5px;
}

QProgressBar
{
    border: 2px solid grey;
    border-radius: 5px;
    text-align: center;
}

QProgressBar::chunk
{
    background-color: #d7801a;
    width: 2.15px;
    margin: 0.5px;
}

QTabBar::tab {
    color: #b1b1b1;
    border: 1px solid #444;
    border-bottom-style: none;
    background-color: #323232;
    padding-left: 10px;
    padding-right: 10px;
    padding-top: 3px;
    padding-bottom: 2px;
    margin-right: -1px;
}

QTabWidget::pane {
    border: 1px solid #444;
    top: 1px;
}

QTabBar::tab:last
{
    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */
    border-top-right-radius: 3px;
}

QTabBar::tab:first:!selected
{
 margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */


    border-top-left-radius: 3px;
}

QTabBar::tab:!selected
{
    color: #b1b1b1;
    border-bottom-style: solid;
    margin-top: 3px;
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);
}

QTabBar::tab:selected
{
    border-top-left-radius: 3px;
    border-top-right-radius: 3px;
    margin-bottom: 0px;
}

QTabBar::tab:!selected:hover
{
    /*border-top: 2px solid #ffaa00;
    padding-bottom: 3px;*/
    border-top-left-radius: 3px;
    border-top-right-radius: 3px;
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);
}

QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{
    color: #b1b1b1;
    background-color: #323232;
    border: 1px solid #b1b1b1;
    border-radius: 6px;
}

QRadioButton::indicator:checked
{
    background-color: qradialgradient(
        cx: 0.5, cy: 0.5,
        fx: 0.5, fy: 0.5,
        radius: 1.0,
        stop: 0.25 #ffaa00,
        stop: 0.3 #323232
    );
}

QCheckBox::indicator{
    color: #b1b1b1;
    background-color: #323232;
    border: 1px solid #b1b1b1;
    width: 9px;
    height: 9px;
}

QRadioButton::indicator
{
    border-radius: 6px;
}

QRadioButton::indicator:hover, QCheckBox::indicator:hover
{
    border: 1px solid #ffaa00;
}

QCheckBox::indicator:checked
{
    image:url(:/images/checkbox.png);
}

QCheckBox::indicator:disabled, QRadioButton::indicator:disabled
{
    border: 1px solid #444;
}'''
stylesheet_cyan = '''QWidget{
    background-color: #323232;
    color: #b1b1b1;
}
QLineEdit{
    background-color: rgb(100,100,100);
    border: 1px solid grey;
    border-radius: 2px;
    color: #cacaca;
    padding: 3px;
    font-size: 14px;
}
QPushButton{
    background-color: QLinearGradient(x1:0, y1:0,
    x2:0, y2:1,
    stop: 0 #4a4a4a, stop: 0.1 #3a3a3a, stop: 0.5 #323232,stop: 1 #2b2b2b
    );
    border-radius: 2px;
    border-width: 1px;
    border-style: solid;
    border-color: grey;
    padding: 5px;
}
QPushButton:pressed{
    background-color: black;
}
QPushButton:hover:!pressed{
    background-color: QLinearGradient( x1:0, y1:0, x2:0, y2:1, stop: 0 #595959, stop: 0.1 #464646, stop: 0.5 #383838, stop: 1 #2b2b2b);;
}

QSlider::groove:horizontal {
    border: 1px solid grey;
    height: 4px;
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #878787, stop:1 #545454);
    margin: 2px 0;
}

QSlider::handle:horizontal {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);
    border: 1px solid grey;
    width: 10px;
    margin: -6 0 -6 0;
    border-radius: 2px;
}
QCheckBox:indicator{
    image: url(ico/cb_unchecked.png);
}
QCheckBox:indicator:checked{
    image: url(ico/cb_checked.png);
}
QRadioButton:indicator{
    image: url(ico/rb_unchecked.png);
}
QRadioButton:indicator:checked{
    image: url(ico/rb_checked.png);
}
QAbstractItemView
{
    background-color: #353535;
    alternate-background-color: #282828;
    outline: 0;
}
QTreeView:item,
QAbstractItemView:item
{
    height: 22px;
}
QAbstractItemView:item:hover
{
    background-color: #9e9d99;
    color: black;
}
QAbstractItemView:item::selected
{
    background-color: orange;
    color: #000000;
}

QHeaderView::section
{
   background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #393939, stop: 1 #272727);
   color: #b1b1b1;
   border: 1px solid #191919;
   border-top-width: 0px;
   border-left-width: 0px;
   padding-left: 10px;
   padding-right: 10px;
   padding-top: 3px;
   padding-bottom: 3px;

}

QTreeView:branch:has-siblings:!adjoins-item
{
    border-image: url(ico/tree/vline.png) 0;
}
QTreeView:branch:has-siblings:adjoins-item
{
    border-image: url(ico/tree/more.png) 0;
}
QTreeView:branch:!has-children:!has-siblings:adjoins-item
{
    border-image: url(ico/tree/end.png) 0;
}

QTreeView:branch:closed:has-children:has-siblings
{
    border-image: url(ico/tree/closed.png) 0;
}

QTreeView:branch:closed:has-children:!has-siblings
{
    border-image: url(ico/tree/closed_end.png) 0;
}

QTreeView:branch:open:has-children:!has-siblings
{
    border-image: url(ico/tree/open_end.png) 0;
}

QTreeView:branch:open:has-children:has-siblings
{
    border-image: url(ico/tree/open.png) 0;
}

QComboBox {
     border: 1px solid gray;
     border-radius: 2px;
     padding: 2px 18px 2px 3px;
     min-width: 2em;
}
QComboBox:drop-down {
     subcontrol-origin: padding;
     subcontrol-position: top right;
     width: 20px;
     border-left-width: 1px;
     border-left-color: #808080;
     border-left-style: solid;
     border-top-right-radius: 3px;
     border-bottom-right-radius: 3px;
}
QComboBox::down-arrow {
    image: url(ico/arrow_down.png);
}

QSpinBox, QDubleSpinBox{
    border: 1px solid #808080;
}
QSpinBox:up-button{
    subcontrol-origin: border;
    subcontrol-position: top right;
    width: 16px;
}
QSpinBox:down-button{
    subcontrol-origin: border;
    subcontrol-position: bottom right;
    width: 16px;
}
QSpinBox::down-button,QSpinBox::up-button
{
    border: 1px solid #808080;
    border-bottom: none;
    border-top: none;
    border-radius: 0;
}
QSpinBox::up-button:pressed, QSpinBox::down-button:pressed
{
    background-color: #828282;
}
QSpinBox::up-button  {
    image: url(ico/spin_up.png);
}

QSpinBox::down-button {
    image: url(ico/spin_down.png);
}
QProgressBar
{
    border: 1px solid grey;
    border-radius: 2px;
    text-align: right;
    font-weight: bold;
    font-size: 14px;
}
QProgressBar:chunk
{
    background-color: #858585;
    width: 3px;
    margin: 1px;
}

QMenuBar::item
{
    background: transparent;
}
QMenuBar::item:selected
{
    background-color: #555555;
    color: #fff;
}
QMenuBar::item:pressed
{
    border: 1px solid #000;
    background-color: #252525;
}

QMenu
{
    border: 1px solid #000;
}
QMenu::item
{
    padding: 2px 20px 2px 20px;
}
QMenu::item:selected
{
    color: #fff;
    background-color: #555555;
}
'''
dark = '''/*
 * QDarkStyle - A dark style sheet for Qt applications
 *
 * Copyright 2012, 2013 Colin Duquesnoy <colin.duquesnoy@gmail.com>
 *
 * This software is released under the LGPLv3 license.
 * You should have received a copy of the GNU Lesser General Public License
 * along with this program. If not, see <http://www.gnu.org/licenses/>.
 */

QProgressBar:horizontal {
    border: 1px solid #3A3939;
    text-align: center;
    padding: 1px;
    background: #201F1F;
}
QProgressBar::chunk:horizontal {
    background-color: qlineargradient(spread:reflect, x1:1, y1:0.545, x2:1, y2:0, stop:0 rgba(28, 66, 111, 255), stop:1 rgba(37, 87, 146, 255));
}

QToolTip
{
    border: 1px solid #3A3939;
    background-color: rgb(90, 102, 117);
    color: white;
    padding: 1px;
    opacity: 200;
}

QWidget
{
    color: silver;
    background-color: #302F2F;
    selection-background-color:#78879b;
    selection-color: black;
}

QWidget:item:hover
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,
    stop: 0 #78879b, stop: 1 #78879b);
    color: black;
}

QWidget:item:selected
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,
    stop: 0 #78879b, stop: 1 #78879b);
}

QMenuBar
{
    background-color: #302F2F;
    color: silver;
}

QMenuBar::item
{
    background: transparent;
}

QMenuBar::item:selected
{
    background: transparent;
    border: 1px solid #3A3939;
;
}

QMenuBar::item:pressed
{
    border: 1px solid #3A3939;
    background-color: #78879b;
    color: black;
    margin-bottom:-1px;
    padding-bottom:1px;
}

QMenu
{
    border: 1px solid #3A3939;
    color: silver;
}

QMenu::item
{
    padding: 2px 20px 2px 20px;
}

QMenu::item:selected
{
    color: black;
}

QWidget:disabled
{
    color: #404040;
    background-color: #302F2F;
}

QAbstractItemView
{
    alternate-background-color: #3A3939;
    color: silver;
    border: 1px solid 3A3939;
    border-radius: 3px;
    padding: 1px;
}

QWidget:focus, QMenuBar:focus
{
    border: 1px solid rgba(48, 86, 111);
}

QTabWidget:focus, QCheckBox:focus
{
    border: none;
}

QLineEdit
{
    background-color: #201F1F;
    padding: 2px;
    border-style: solid;
    border: 1px solid #3A3939;
    border-radius: 3px;
    color: silver;
}

QGroupBox {
    border:1px solid #3A3939;
    border-radius: 7px;
    margin-top: 2ex;
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top center;
    padding-left: 10px;
    padding-right: 10px;
}

QAbstractScrollArea
{
    border-radius: 3px;
    border: 1px solid #3A3939;
}

QScrollBar:horizontal
{
    height: 15px;
    margin: 0px 11px 0px 11px;
    border: 1px solid #3A3939;
    border-radius: 6px;
    background-color: QLinearGradient( x1: 0, y1: 1, x2: 0, y2: 0,
    stop: 0 #302F2F, stop: 1 #484846);
}

QScrollBar::handle:horizontal
{
    background-color: QLinearGradient( x1: 0, y1: 1, x2: 0, y2: 0,
    stop: 0 #605F5F, stop: 1 #787876);
    min-width: 5px;
    border-radius: 5px;
}

QScrollBar::sub-line:horizontal
{
    border-image: url(:/qss_icons/rc/right_arrow_disabled.png);
    width: 10px;
    height: 10px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}

QScrollBar::add-line:horizontal
{
    border-image: url(:/qss_icons/rc/left_arrow_disabled.png);
    height: 10px;
    width: 10px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal:hover,QScrollBar::sub-line:horizontal:on
{
    border-image: url(:/qss_icons/rc/right_arrow.png);
    height: 10px;
    width: 10px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}


QScrollBar::add-line:horizontal:hover, QScrollBar::add-line:horizontal:on
{
    border-image: url(:/qss_icons/rc/left_arrow.png);
    height: 10px;
    width: 10px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}

QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal
{
    background: none;
}


QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
{
    background: none;
}

QScrollBar:vertical
{
    background-color: QLinearGradient( x1: 1, y1: 0, x2: 0, y2: 0,
    stop: 0 #302F2F, stop: 1 #484846);
    width: 15px;
    margin: 11px 0 11px 0;
    border: 1px solid #3A3939;
    border-radius: 6px;
}

QScrollBar::handle:vertical
{
    background-color: QLinearGradient( x1: 1, y1: 0, x2: 0, y2: 0,
    stop: 0 #605F5F, stop: 1 #787876);
    min-height: 5px;
    border-radius: 5px;
}

QScrollBar::sub-line:vertical
{
    border-image: url(:/qss_icons/rc/up_arrow_disabled.png);
    height: 10px;
    width: 10px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}

QScrollBar::add-line:vertical
{

    border-image: url(:/qss_icons/rc/down_arrow_disabled.png);
    height: 10px;
    width: 10px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on
{

    border-image: url(:/qss_icons/rc/up_arrow.png);
    height: 10px;
    width: 10px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}


QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on
{
    border-image: url(:/qss_icons/rc/down_arrow.png);
    height: 10px;
    width: 10px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical
{
    background: none;
}


QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
{
    background: none;
}

QTextEdit
{
    background-color: #302F2F;
    color: silver;
    border: 1px solid #3A3939;
}

QPlainTextEdit
{
    background-color: #201F1F;;
    color: silver;
    border-radius: 3px;
    border: 1px solid #3A3939;
}

QHeaderView::section
{
    background-color: #3A3939;
    color: silver;
    padding-left: 4px;
    border: 1px solid #6c6c6c;
}

QCheckBox:disabled
{
    color: #404040;
}

QSizeGrip {
    image: url(:/qss_icons/rc/sizegrip.png);
    width: 12px;
    height: 12px;
}


QMainWindow::separator
{
    background-color: #302F2F;
    color: white;
    padding-left: 4px;
    spacing: 2px;
    border: 1px dashed #3A3939;
}

QMainWindow::separator:hover
{

    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #58677b,
      stop:0.5 #78879b stop:1 #58677b);
    color: white;
    padding-left: 4px;
    border: 1px solid #3A3939;
    spacing: 2px;
}


QMenu::separator
{
    height: 1px;
    background-color: #3A3939;
    color: white;
    padding-left: 4px;
    margin-left: 10px;
    margin-right: 5px;
}



QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{
    color: #b1b1b1;
    background-color: #302F2F;
    border: 1px solid silver;
    border-radius: 5px;
}



QRadioButton::indicator:checked
{
    background-color: qradialgradient(
    cx: 0.5, cy: 0.5,
    fx: 0.5, fy: 0.5,
    radius: 1.0,
    stop: 0.25 #78879b,
    stop: 0.3 #302F2F
    );
}

QCheckBox::indicator{
    color: #b1b1b1;
    background-color: #302F2F;
    border: 1px solid silver;
    width: 9px;
    height: 9px;
}

QRadioButton::indicator
{
    border-radius: 7px;
    width: 9px;
    height: 9px;
}

QRadioButton::indicator:hover, QCheckBox::indicator:hover
{
    border: 1px solid #78879b;
}

QCheckBox::indicator:checked
{
    image:url(:/qss_icons/rc/checkbox.png);
}

QCheckBox::indicator:disabled, QRadioButton::indicator:disabled
{
    border: 1px solid #444;
}

QFrame
{
    border-radius: 3px;
}

QStackedWidget
{
    border: none;
}

QToolBar {
    border: 1px solid #393838;
    background: 1px solid #302F2F;
    font-weight: bold;
}

QToolBar::handle:horizontal {
    image: url(:/qss_icons/rc/Hmovetoolbar.png);
}
QToolBar::handle:vertical {
    image: url(:/qss_icons/rc/Vmovetoolbar.png);
}
QToolBar::separator:horizontal {
    image: url(:/qss_icons/rc/Hsepartoolbar.png);
}
QToolBar::separator:vertical {
    image: url(:/qss_icons/rc/Vsepartoolbars.png);
}

QPushButton
{
    color: silver;
    background-color: QLinearGradient( x1: 0, y1: 1, x2: 0, y2: 0,
    stop: 0 #302F2F, stop: 1 #484846);
    border-width: 1px;
    border-color: #4A4949;
    border-style: solid;
    padding-top: 5px;
    padding-bottom: 5px;
    padding-left: 5px;
    padding-right: 5px;
    border-radius: 5px;
}

QPushButton:disabled
{
    background-color: QLinearGradient( x1: 0, y1: 1, x2: 0, y2: 0,
    stop: 0 #302F2F, stop: 1 #484846);
    border-width: 1px;
    border-color: #3A3939;
    border-style: solid;
    padding-top: 5px;
    padding-bottom: 5px;
    padding-left: 10px;
    padding-right: 10px;
    /*border-radius: 3px;*/
    color: #3A3939;
}

QComboBox
{
    selection-background-color: #78879b;
    background-color: #201F1F;
    border-style: solid;
    border: 1px solid #3A3939;
    border-radius: 3px;
    padding: 2px;
}

QComboBox:hover,QPushButton:hover,QAbstractSpinBox:hover,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QAbstractView:hover,QTreeView:hover
{
    border: 1px solid #78879b;
    color: silver;
}

QComboBox:on
{
    background-color: #626873;
    padding-top: 3px;
    padding-left: 4px;
    selection-background-color: #4a4a4a;
}

QComboBox QAbstractItemView
{
    background-color: #201F1F;
    border-radius: 3px;
    border: 1px solid #3A3939;
    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,
      stop: 0 #78879b, stop: 1 #78879b);
}

QComboBox::drop-down
{
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 15px;

    border-left-width: 0px;
    border-left-color: darkgray;
    border-left-style: solid;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px;
}

QComboBox::down-arrow
{
    image: url(:/qss_icons/rc/down_arrow_disabled.png);
}

QComboBox::down-arrow:on, QComboBox::down-arrow:hover,
QComboBox::down-arrow:focus
{
    image: url(:/qss_icons/rc/down_arrow.png);
}

QPushButton:pressed
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,
    stop: 0 #302F2F, stop: 1 #484846);
}

QAbstractSpinBox {
    padding-top: 2px;
    padding-bottom: 2px;
    border: 1px solid #3A3939;
    background-color: #201F1F;
    color: silver;
    border-radius: 3px;
}

QAbstractSpinBox:up-button
{
    background-color: transparent;
    subcontrol-origin: border;
    subcontrol-position: center right;
}

QAbstractSpinBox:down-button
{
    background-color: transparent;
    subcontrol-origin: border;
    subcontrol-position: center left;
}

QAbstractSpinBox::up-arrow,QAbstractSpinBox::up-arrow:disabled,QAbstractSpinBox::up-arrow:off {
    image: url(:/qss_icons/rc/up_arrow_disabled.png);
    width: 10px;
    height: 10px;
}
QAbstractSpinBox::up-arrow:hover
{
    image: url(:/qss_icons/rc/up_arrow.png);
}


QAbstractSpinBox::down-arrow,QAbstractSpinBox::down-arrow:disabled,QAbstractSpinBox::down-arrow:off
{
    image: url(:/qss_icons/rc/down_arrow_disabled.png);
    width: 10px;
    height: 10px;
}
QAbstractSpinBox::down-arrow:hover
{
    image: url(:/qss_icons/rc/down_arrow.png);
}


QLabel
{
    border: 0px solid black;
}

QTabBar::tab {
    color: #b1b1b1;
    border: 1px solid #3A3939;
    background-color: #302F2F;
    padding-left: 5px;
    padding-right: 5px;
    padding-top: 3px;
    padding-bottom: 2px;
    margin-right: -1px;
}


QTabWidget::pane {
    border: 1px solid #3A3939;
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1,
      stop:1 #302F2F, stop:0 #3A3939);
}

QTabBar::tab:last
{
    margin-right: 0;
    border-top-right-radius: 3px;
}

QTabBar::tab:first:!selected
{
    margin-left: 0px;
    border-top-left-radius: 3px;
}

QTabBar::tab:!selected
{
    color: #b1b1b1;
    border-bottom-style: solid;
    margin-top: 3px;
}

QTabBar::tab:selected
{
    border-top-left-radius: 3px;
    border-top-right-radius: 3px;
    margin-bottom: 0px;

    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1,
      stop:1 #302F2F, stop:0 #5A5959);
}

QTabBar::tab:!selected:hover
{
    color:white;
}

QTabBar::tab:selected:hover
{
    color:white;
    border-top-left-radius: 3px;
    border-top-right-radius: 3px;
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1,
    stop:1 #302F2F, stop:0 #5A5959);
}

QDockWidget
{
    color: silver;
    titlebar-close-icon: url(:/qss_icons/rc/close.png);
    titlebar-normal-icon: url(:/qss_icons/rc/undock.png);
}

QDockWidget::title
{
    border: 1px solid #3A3939;
    border-bottom: #302F2F;
    text-align: left;
    spacing: 2px;
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1,
    stop:1 #302F2F, stop:0 #3A3939);;
    background-image: none;
    padding-left: 10px;
}

QDockWidget {
    border: 1px solid lightgray;
    titlebar-close-icon: url(:/qss_icons/rc/close.png);
    titlebar-normal-icon: url(:/qss_icons/rc/undock.png);
}

QDockWidget::close-button, QDockWidget::float-button {
    border: 1px solid transparent;
    border-radius: 5px;
    background: transparent;
    icon-size: 10px;
}

QDockWidget::close-button:hover, QDockWidget::float-button:hover {
    background: #3A3939;
}

QDockWidget::close-button:pressed, QDockWidget::float-button:pressed {
    padding: 1px -1px -1px 1px;
}

QTreeView, QListView, QTableView
{
    border: 1px solid #3A3939;
    background-color: #201F1F;
}

QTreeView:branch:selected, QTreeView:branch:hover
{
    background: url(:/qss_icons/rc/transparent.png);
}

QTreeView::branch:has-siblings:!adjoins-item {
    border-image: url(:/qss_icons/rc/transparent.png);
}

QTreeView::branch:has-siblings:adjoins-item {
    border-image: url(:/qss_icons/rc/transparent.png);
}

QTreeView::branch:!has-children:!has-siblings:adjoins-item {
    border-image: url(:/qss_icons/rc/transparent.png);
}

QTreeView::branch:has-children:!has-siblings:closed,
QTreeView::branch:closed:has-children:has-siblings {
    image: url(:/qss_icons/rc/branch_closed.png);
}

QTreeView::branch:open:has-children:!has-siblings,
QTreeView::branch:open:has-children:has-siblings  {
    image: url(:/qss_icons/rc/branch_open.png);
}

QTreeView::branch:has-children:!has-siblings:closed:hover,
QTreeView::branch:closed:has-children:has-siblings:hover {
    image: url(:/qss_icons/rc/branch_closed-on.png);
    }

QTreeView::branch:open:has-children:!has-siblings:hover,
QTreeView::branch:open:has-children:has-siblings:hover  {
    image: url(:/qss_icons/rc/branch_open-on.png);
    }

QSlider::groove:horizontal {
    border: 1px solid #3A3939;
    height: 8px;
    background: #201F1F;
    margin: 2px 0;
    border-radius: 4px;
}

QSlider::handle:horizontal {
    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,
      stop: 0.0 silver, stop: 0.2 #a8a8a8, stop: 1 #727272);
    border: 1px solid #3A3939;
    width: 14px;
    height: 14px;
    margin: -4px 0;
    border-radius: 7px;
}

QSlider::groove:vertical {
    border: 1px solid #3A3939;
    width: 8px;
    background: #201F1F;
    margin: 0 0px;
    border-radius: 4px;
}

QSlider::handle:vertical {
    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 silver,
      stop: 0.2 #a8a8a8, stop: 1 #727272);
    border: 1px solid #3A3939;
    width: 14px;
    height: 14px;
    margin: 0 -4px;
    border-radius: 7px;
}


QToolButton {
    background-color: #302F2F;
}

QToolButton:pressed {
    background-color: #3A3939;
}
QToolButton:hover {
    background-color: #3A3939;
}'''
houdini = '''/******* QWidget ********/

QWidget
{
    color: #b1b1b1;
    background-color:#3a3a3a;
}

QWidget:disabled
{
    color: #b1b1b1;
    background-color: #252525;
}

QAbstractScrollArea,QTableView
{
 border: 1px solid #222;
}

/************** QMainWindow *************/

QMainWindow::separator
{
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);
    color: white;
    padding-left: 4px;
    border: 1px solid #4c4c4c;
    spacing: 2px; 
}

QMainWindow::separator:hover
{

    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);
    color: white;
    padding-left: 4px;
    border: 1px solid #6c6c6c;
    spacing: 3px; 
}


/************** QToolTip **************/

QToolTip
{
     border: 1px solid black;
     background-color: #eeeeee;
     padding: 1px;
     padding-left: 4px;
     padding-right: 4px;
     border-radius: 3px;
     color: black;
     opacity: 100;
}

/***************** QMenuBar *************/

QMenuBar::item
{
    background: transparent;
}

QMenuBar::item:selected
{
    background-color: #555555;
    color: #fff;
}

QMenuBar::item:pressed
{
    background: #444;
    border: 1px solid #000;
    background-color: QLinearGradient(
        x1:0, y1:0,
        x2:0, y2:1,
        stop:1 #212121,
        stop:0.4 #343434
    );
    margin-bottom:-1px;
    padding-bottom:1px;
}

/**************** QMenu **********/

QMenu
{
    border: 1px solid #000;
}

QMenu::item
{
    background-color: #3a3a3a;
    padding: 2px 20px 2px 20px;
}

QMenu::item:selected
{
    color: #fff;
    background-color: #555555;
}

QMenu::separator
{
    height: 2px;
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);
    color: white;
    padding-left: 4px;
    margin-left: 20px;
    margin-right: 5px;
}



/************* QAbstractItemView ***********/

QAbstractItemView
{
    background-color: #353535;
    alternate-background-color: #323232;
    outline: 0;
    height: 20px;
}


/************ QTreeView **********/

QTreeView::item:alternate,
QListView::item:alternate  {
     background-color: #323232;
 }

QTreeView::branch:has-siblings:!adjoins-item
{
    border-image: url(:/vline.png) 0;
}
QTreeView::branch:has-siblings:adjoins-item
{
    border-image: url(:/more.png) 0;
}
QTreeView::branch:!has-children:!has-siblings:adjoins-item
{
    border-image: url(:/end.png) 0;
}

QTreeView::branch:closed:has-children:has-siblings
{
    border-image: url(:/closed.png) 0;
}

QTreeView::branch:closed:has-children:!has-siblings
{
    border-image: url(:/closed_end.png) 0;
}

QTreeView::branch:open:has-children:!has-siblings
{
    border-image: url(:/open_end.png) 0;
}

QTreeView::branch:open:has-children:has-siblings
{
    border-image: url(:/open.png) 0;
}

/********************* QListView ************

QListView::item,
QTreeView::item 
{
    color: rgb(220,220,220);
    border-color: rgba(0,0,0,0);
    border-width: 1px;
    border-style: solid;
}

QListView::item:selected,
QTreeView::item:selected
{
    background: #605132;
    border-color: #b98620;
 }
/*************** QTableView ********/

QHeaderView::section
{
   background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #393939, stop: 1 #272727);
   color: #b1b1b1;
   border: 1px solid #191919;
   border-top-width: 0px;
   border-left-width: 0px;
   padding-left: 10px;
   padding-right: 10px;
   padding-top: 3px;
   padding-bottom: 3px;

}

QTableView::item:selected {
    background: #605132;
    border: 1px solid #b98620;

    color: rgb(220,220,220);
 }

  QTableView QTableCornerButton::section {
     background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #393939, stop: 1 #272727);
     border: 1px solid #191919;
     border-top-width: 0px;
     border-left-width: 0px;
 }

/*************** QlineEdit ************/

QLineEdit,QDateEdit,QDateTimeEdit,QSpinBox
{
    background-color: #000;
    padding: 1px;
    border-style: solid;
    border: 2px solid #2b2b2b;
    border-radius: 0;
    color:rgb(255,255,255);
    min-height: 18px;
    selection-background-color: rgb(185,134,32);
    selection-color: rgb(0,0,0);
}


/*************** QPushButton ***********/

QPushButton
{
    color: #b1b1b1;
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #535353, stop: 0.1 #515151, stop: 0.5 #474747, stop: 0.9 #3d3d3d, stop: 1 #3a3a3a);
    border: 2px solid #232323;
    border-top-width: 2px;
    border-left-width: 2px;
    border-top-color:  QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #101010, stop: 1 #818181);
    border-left-color:  QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #101010, stop: 1 #818181);
    border-radius: 0;
    padding: 3px;
    font-size: 12px;
    padding-left: 10px;
    padding-right: 10px;
}


QPushButton:disabled
{
    background-color:   #424242;
    border: 2px solid #313131;
    border-top-width: 2px;
    border-left-width: 2px;
    border-top-color:  QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #151515, stop: 1 #777777);
    border-left-color:  QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #151515, stop: 1 #777777);
    color: #777;
}

QPushButton:checked
{   
    border-color: #000;
    background-color: #2d2d2d;
    color: #cacaca;
    border-width: 1px;
}

 QPushButton:hover
{   
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #606060, stop: 0.1 #585858, stop: 0.5 #545454, stop: 0.9 #3d3d3d, stop: 1 #3a3a3a);

}
QPushButton:pressed
{
    background-color: #af8021;
    color: #fff;
}
/*********** QScrollBar ***************/

QScrollBar:horizontal {
     border: 1px solid #222222;
     background: #222;
     height: 15px;
     margin: 0px 14px 0 14px;
}
QScrollBar:vertical
{
      border: 1px solid #222222;
      background: #222;
      width: 15px;
      margin: 14px 0 14px 0;
      border: 1px solid #222222;
}

QScrollBar::handle:vertical
{
    background:  QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #535353, stop: 0.1 #515151, stop: 0.5 #474747, stop: 0.9 #3d3d3d, stop: 1 #3a3a3a);
    min-height: 20px;
    border-radius: 0px;
    border: 1px solid #222222;
    border-left-width: 0px;
    border-right-width: 0px;
}
QScrollBar::handle:horizontal
{
      background:  QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #535353, stop: 0.1 #515151, stop: 0.5 #474747, stop: 0.9 #3d3d3d, stop: 1 #3a3a3a);
    min-height: 20px;
    border-radius: 0px;
    border: 1px solid #222222;
    border-top-width: 0px;
    border-bottom-width: 0px;
}


QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal 
{
      border: 1px solid #1b1b19;
      border-radius: 0px;
      background:QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #535353, stop: 0.1 #515151, stop: 0.5 #474747, stop: 0.9 #3d3d3d, stop: 1 #3a3a3a);
      width: 14px;
      subcontrol-origin: margin;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical
{
      border: 1px solid #1b1b19;
      border-radius: 1px;
      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #535353, stop: 0.1 #515151, stop: 0.5 #474747, stop: 0.9 #3d3d3d, stop: 1 #3a3a3a);
      height: 14px;
      subcontrol-origin: margin;
}
QScrollBar::add-line:horizontal:pressed, QScrollBar::sub-line:horizontal:pressed ,
QScrollBar::add-line:vertical:pressed, QScrollBar::sub-line:vertical:pressed
{
      background:  #5b5a5a;
}

QScrollBar::sub-line:vertical
{
      subcontrol-position: top;
}
QScrollBar::add-line:vertical
{
      subcontrol-position: bottom;
}

QScrollBar::sub-line:horizontal 
{
     subcontrol-position: left;
}
QScrollBar::add-line:horizontal
{
      subcontrol-position: right;
}

QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
{
      background: none;
}

QScrollBar::up-arrow:vertical
{
     border-image: url(:/arrow_up.png) 1;
}
QScrollBar::down-arrow:vertical
{
     border-image: url(:/arrow_down.png) 1;
}
QScrollBar::right-arrow:horizontal
{
     border-image: url(:/arrow_right.png) 1;
}
QScrollBar::left-arrow:horizontal
{
     border-image: url(:/arrow_left.png) 1;
}


QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
{
      background: none;
}
/********* QSlider **************/

QSlider::groove:horizontal {
    border: 1px solid #000;
    background: #000;
    height: 3px;
    border-radius: 0px;
}

QSlider::sub-page:horizontal {
    background:  #404040;
    border: 1px solid #000;
    height: 10px;
    border-radius: 0px;
}


QSlider::add-page:horizontal {
    background: #626262;
    border: 1px solid #000;
    height: 10px;
    border-radius: 0px;
}


QSlider::handle:horizontal {
background: qlineargradient(x1:0, y1:0, x2:1, y2:1,   stop:0 #696969, stop:1 #505050);
border: 1px solid #000;
width: 5px;
margin-top: -8px;
margin-bottom: -8px;
border-radius: 0px;
}

QSlider::hover
{
    background: #3f3f3f;	
}

QSlider::groove:vertical {
border: 1px solid #ffaa00;
background: #ffaa00;
width: 3px;
border-radius: 0px;
}


QSlider::add-page:vertical {
background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,   stop: 0 #ffaa00, stop: 1 #ffaa00);
background:#404040;
border: 1px solid #000;
width: 8px;
border-radius: 0px;
}

QSlider::sub-page:vertical {
background: #626262;
border: 1px solid #000;
width: 8px;
border-radius: 0px;
}


QSlider::handle:vertical {
background: qlineargradient(x1:0, y1:0, x2:1, y2:1,   stop:0 #696969, stop:1 #505050);
border: 1px solid #000;
height: 5px;
margin-left: -8px;
margin-right: -8px;
border-radius: 0px;
}

/* disabled */

QSlider::sub-page:disabled, QSlider::add-page:disabled 
{
border-color: #3a3a3a;
background: #414141;
border-radius: 0px;
}
QSlider::handle:disabled {
background: #3a3a3a;
border: 1px solid #242424;

}

QSlider::disabled {
background: #3a3a3a;
}


/********* QProgressBar ***********/
QProgressBar
{
    border: 1px solid #6d6c6c;
    border-radius: 0px;
    
    text-align: center;
    background:#262626;
    color: gray;
    border-bottom: 1px #545353;
}

QProgressBar::chunk
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, 
	stop: 0 #f0d66e,
	stop: 0.09 #f0d66e,
	stop: 0.1 #ecdfa8, 
	stop: 0.7 #d9a933, 
	stop: 0.91 #b88822);

}

/************ QComboBox ************/

QComboBox
{
    selection-background-color: #ffaa00;
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #515151,  stop: 0.5 #484848, stop: 1 #3d3d3d);
    border-style: solid;
    border: 1px solid #000;
    border-radius: 0;
    padding-left: 9px;
    min-height: 20px;
    font: 10pt;

}

QComboBox:hover
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #555555,  stop: 0.5 #4d4d4d, stop: 1 #414141);
   /* font: 14pt;*/
}

QComboBox:on
{
    background-color: #b98620;
    color:#fff;
    selection-background-color: #494949;
}

QComboBox::drop-down
{
     subcontrol-origin: padding;
     subcontrol-position: top right;
     width: 25px;
     background-color:QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3d3d3d,  stop: 1 #282828);
     border-width: 0px;
 }

QComboBox::down-arrow
{
    image: url(:/arrow_up_down.png);
}

QComboBox QAbstractItemView
{
    background-color: #3a3a3a;
    border-radius: 0px;
    border: 1px solid #101010;
    border-top-color:  #818181;
    border-left-color: #818181;
    selection-background-color: #606060;
    padding: 2px;

}

QComboBox QAbstractItemView::item 
{
    margin-top: 3px;
}

QListView#comboListView {
    background: rgb(80, 80, 80);
    color: rgb(220, 220, 220);
    min-height: 90px;
    margin: 0 0 0 0;
}

QListView#comboListView::item {
    background-color: rgb(80, 80, 80);
}

QListView#comboListView::item:hover {
    background-color: rgb(95, 95, 95);
}


/************ QCheckBox *********/

QCheckBox::indicator:unchecked {
    background:black;
    image: url(:/unchecked.png);
}
QCheckBox::indicator:checked {
    image: url(:/checked.png);
}
/****** QRadioButton ***********/

QRadioButton::indicator:unchecked 
{
    image: url(:/rb_unchecked.png);
}

QRadioButton::indicator:checked 
{
    image: url(:/rb_checked.png);
}
QTableView { alternate-background-color: #2e2e2e }


/****** QTabWidget *************/

QTabWidget::pane  { 
    border: 1px solid #111111;
    margin-top:-1px; /* hide line under selected tab*/

}

QTabWidget::tab-bar  {
    left: 0px; /* move to the right by 5px */
}
 
QTabBar::tab  {
    border: 1px solid #111;
    border-radius: 0px;
    min-width: 15ex;
    padding-left: 3px;
    padding-right: 5px;
    padding-top: 3px;
    padding-bottom: 2px;
    background-color:QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #313131,  stop: 1 #252525);
     
}

QTabBar::tab:selected  {
    border-bottom: 0px;
    background-color:QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4b4b4b,  stop: 1 #3a3a3a)
}

 
QTabBar::tab:only-one  {
    margin: 0;
}

/************** QGroupBox *************/
 QGroupBox {
    border-left-color:QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #4b4b4b,  stop: 1 #3a3a3a);
    border-right-color:QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #111,  stop: 1 #3a3a3a);
    border-top-color:QLinearGradient( x1: 0, y1: 0, x2: 0, y2:1, stop: 0 #4b4b4b,  stop: 1 #3a3a3a);
    border-bottom-color:QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #111,  stop: 1 #3a3a3a);
    border-width: 2px; 
    border-style: solid; 
    border-radius: 0px;
    padding-top: 10px;
}
QGroupBox::title { 
    background-color: transparent;
     subcontrol-position: top left;
     padding:4 10px;
 } 


/************************ QSpinBox *******************/
/*,QDoubleSpinBox*/

QSpinBox::up-button, QDoubleSpinBox::up-button, QTimeEdit::up-button  {
    /*background:QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #535353, stop: 1 #3a3a3a);*/
    subcontrol-origin: border;
    subcontrol-position: top right;
    width: 16px;
    /*border: 1px solid #333;*/
} 
QSpinBox::down-button, QDoubleSpinBox::down-button,  QTimeEdit::down-button{
   /* background:QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #535353, stop: 1 #3a3a3a);*/
    subcontrol-origin: border;
    subcontrol-position: bottom right;
    width: 16px;
   /* border: 1px solid #333;*/
}

QSpinBox::down-button,QDoubleSpinBox::down-button,  QTimeEdit::down-button,
QSpinBox::up-button, QDoubleSpinBox::up-button,QTimeEdit::up-button 
{
    color: #b1b1b1;
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #535353, stop: 0.1 #515151, stop: 0.5 #474747, stop: 0.9 #3d3d3d, stop: 1 #3a3a3a);
    border: 2px solid #232323;
    border-top-width: 2px;
    border-left-width: 2px;
    border-top-color:  QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #101010, stop: 1 #818181);
    border-left-color:  QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #101010, stop: 1 #818181);
    border-radius: 0;

}


QSpinBox::up-button:pressed, QDoubleSpinBox::up-button:pressed, QSpinBox::down-button:pressed,
QTimeEdit::up-button:pressed ,QDoubleSpinBox::up-button:pressed , QTimeEdit::down-button:pressed 
{
    background-color: #828282;
}

QSpinBox::up-button, QDoubleSpinBox::up-button  {
    image: url(:/spin_up.png);
}

QSpinBox::down-button, QDoubleSpinBox::down-button  {
    image: url(:/spin_down.png);
}


QPlainTextEdit, QTextEdit {
    background: #000;
    color: white;
}
QTextBrowser {
   background-color:#3a3a3a;
}
QTabBar::close-button {
     image: url(:/tab_close.png);
     subcontrol-position: right;
 }
QTabBar::close-button:hover {
     image: url(:/tab_close_hover.png);
 }'''
pwblack = '''/*******WIDGET********/

QWidget
{
    color: #b1b1b1;
    background-color:#323232;
}
QWidget:item:hover
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #b3b3b3, stop: 1 #686767);
    color: #000000;
}
QWidget:item:selected
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
}
QWidget:disabled
{
    color: #404040;
    background-color: #323232;
}
QWidget:focus
{
    border: 1px solid  rgb(80,80,80);
}

/**************MAINWINDOW*************/

QMainWindow::separator
{
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);
    color: white;
    padding-left: 4px;
    border: 1px solid #4c4c4c;
    spacing: 2px; 
}

QMainWindow::separator:hover
{

    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);
    color: white;
    padding-left: 4px;
    border: 1px solid #6c6c6c;
    spacing: 3px; 
}


/**************Tooltip**************/

QToolTip
{
     border: 1px solid black;
     background-color: #ffa02f;
     padding: 1px;
     border-radius: 3px;
     opacity: 100;
}

/*****************MENUBAR*************/

QMenuBar::item
{
    background: transparent;
}

QMenuBar::item:selected
{
    background: transparent;
    border: 1px solid #ffaa00;
}

QMenuBar::item:pressed
{
    background: #444;
    border: 1px solid #000;
    background-color: QLinearGradient(
        x1:0, y1:0,
        x2:0, y2:1,
        stop:1 #212121,
        stop:0.4 #343434
    );
    margin-bottom:-1px;
    padding-bottom:1px;
}

/*********************MENU************/

QMenu
{
    border: 1px solid #000;
}

QMenu::item
{
    padding: 2px 20px 2px 20px;
}

QMenu::item:selected
{
    color: #000000;
}

QMenu::separator
{
    height: 2px;
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);
    color: white;
    padding-left: 4px;
    margin-left: 20px;
    margin-right: 5px;
}

/***************ITEM**************/

QAbstractItemView
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);
}

/***************LINEEDIT************/

QLineEdit
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);
    padding: 1px;
    border-style: solid;
    border: 1px solid #1e1e1e;
    border-radius: 2;
}

/***************PUSHBUTTON***********/

QPushButton
{
    color: #b1b1b1;
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);
    border-width: 1px;
    border-color: #1e1e1e;
    border-style: solid;
    border-radius: 2;
    padding: 3px;
    font-size: 12px;
    padding-left: 1px;
    padding-right: 1px;
}

QPushButton:pressed
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);
}

/*************COMBOBOX***************/

QComboBox
{
    selection-background-color: #ffaa00;
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);
    border-style: solid;
    border: 1px solid #1e1e1e;
    border-radius: 2;
}

QComboBox:hover,QPushButton:hover
{
    border: 1px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
}


QComboBox:on
{
    padding-top: 3px;
    padding-left: 4px;
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);
    selection-background-color: #ffaa00;
}

QComboBox QAbstractItemView
{
    border: 2px solid darkgray;
    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
}

QComboBox::drop-down
{
     subcontrol-origin: padding;
     subcontrol-position: top right;
     width: 15px;

     border-left-width: 0px;
     border-left-color: darkgray;
     border-left-style: solid;
     border-top-right-radius: 3px; 
     border-bottom-right-radius: 3px;
 }

QComboBox::down-arrow
{

width:0px; 
width:0px; 
  height:3px; 
  border-left:5px solid transparent;
  border-right:5px solid transparent;
  border-top:4px solid #2f2f2f;
  font-size:10px;
  line-height:0px;
}


QGroupBox:focus
{
border: 1px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
}

/**********************GROUPBOX**********/

QGroupBox
{
   border: 1px solid gray;
   border-radius: 4px;
   padding:7 -4px;
}
QGroupBox::title {
     subcontrol-position: top center;
     padding: 0 7px;
 }
 
 /******************TEXTEDIT****************/

QTextEdit
{
    background-color: #242424;
    border: 1px solid gray;
} 

QTextEdit:focus
{
    border: 1px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
}

QPlainTextEdit
{
    background-color: #242424;
}

/***********SCROLLBAR***************/

QScrollBar:horizontal {
     border: 1px solid #222222;
     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);
     height: 15px;
     margin: 0px 16px 0 16px;
}

QScrollBar::handle:horizontal
{
      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);
      min-height: 20px;
      border-radius: 2px;
}

QScrollBar::add-line:horizontal {
      border: 1px solid #1b1b19;
      border-radius: 2px;
      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);
      width: 14px;
      subcontrol-position: right;
      subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal {
      border: 1px solid #1b1b19;
      border-radius: 2px;
      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);
      width: 14px;
     subcontrol-position: left;
     subcontrol-origin: margin;
}

QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal
{
      border: 1px solid black;
      width: 1px;
      height: 1px;
      background: white;
}

QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
{
      background: none;
}

QScrollBar:vertical
{
      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);
      width: 15px;
      margin: 16px 0 16px 0;
      border: 1px solid #222222;
}

QScrollBar::handle:vertical
{
      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);
      min-height: 20px;
      border-radius: 2px;
}

QScrollBar::add-line:vertical
{
      border: 1px solid #1b1b19;
      border-radius: 2px;
      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
      height: 14px;
      subcontrol-position: bottom;
      subcontrol-origin: margin;
}

QScrollBar::sub-line:vertical
{
      border: 1px solid #1b1b19;
      border-radius: 2px;
      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);
      height: 15px;
      subcontrol-position: top;
      subcontrol-origin: margin;
}

QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical
{
      border: 1px solid black;
      width: 5px;
      height: 1px;
      background: white;
}


QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
{
      background: none;
}

/***************HEADER*************/

QHeaderView::section
{
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);
    color: white;
    padding-left: 4px;
    border: 1px solid #6c6c6c;
}

/****************DOCKWIDGET***********/

QDockWidget::title
{
    text-align: center;
    spacing: 3px; /* spacing between items in the tool bar */
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);
}

QDockWidget::close-button, QDockWidget::float-button
{
    text-align: center;
    spacing: 1px; /* spacing between items in the tool bar */
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);
}

QDockWidget::close-button:hover, QDockWidget::float-button:hover
{
    background: #242424;
}

QDockWidget::close-button:pressed, QDockWidget::float-button:pressed
{
    padding: 1px -1px -1px 1px;
}

/***************TOOLBAR*************/

QToolBar::handle
{
     spacing: 3px; 
    /* background: url(:/images/handle.png);*/
}

/***************PROGRESSBAR***********/

QProgressBar
{
    border: 2px solid grey;
    border-radius: 3px;
    text-align: center;
}

QProgressBar::chunk
{
    background-color: #d7801a;
    width: 2.15px;
    margin: 0.5px;
}

/*************TABBAR**********/

QTabBar::tab {
    color: #b1b1b1;
    border: 1px solid #444;
    border-bottom-style: none;
    background-color: #323232;
    padding-left: 15px;
    padding-right: 15px;
    padding-top: 3px;
    padding-bottom: 2px;
    margin-right: -1px;
}

QTabWidget::pane {
    border: 1px solid #444;
    top: 1px;
}

QTabBar::tab:last
{
    margin-right: 0;
    border-top-right-radius: 3px;
}

QTabBar::tab:first:!selected
{
    margin-left: 0px; 
    border-top-left-radius: 3px;
}

QTabBar::tab:!selected
{
    color: #b1b1b1;
    border-bottom-style: solid;
    margin-top: 3px;
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);
}

QTabBar::tab:selected
{
    border-top-left-radius: 3px;
    border-top-right-radius: 3px;
    margin-bottom: 0px;
}

QTabBar::tab:!selected:hover
{
    border-top-left-radius: 3px;
    border-top-right-radius: 3px;
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);
}

/**************RADIOBUTTON*************/

QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{
    color: #b1b1b1;
    background-color: #323232;
    border: 1px solid #b1b1b1;
    border-radius: 4px;
}

QRadioButton::indicator:checked
{
    background-color: qradialgradient(
        cx: 0.5, cy: 0.5,
        fx: 0.5, fy: 0.5,
        radius: 1.0,
        stop: 0.25 #ffaa00,
        stop: 0.3 #323232
    );
}

QRadioButton::indicator
{
    border-radius: 6px;
}

QRadioButton::indicator:hover, QCheckBox::indicator:hover
{
    border: 1px solid #ffaa00;
}

/**************CHECKBOX***************/

QCheckBox::indicator:checked
{
    background-color: qradialgradient(
        cx: 0.5, cy: 0.5,
        fx: 0.5, fy: 0.5,
        radius: 1.0,
        stop: 0.25 #ffaa00,
        stop: 0.3 #323232
    );

}

QCheckBox:disabled
{
color: #414141;
}

QCheckBox::indicator
{
    color: #b1b1b1;
    background-color: #323232;
    border: 1px solid #b1b1b1;
    width: 9px;
    height: 9px;
}

QCheckBox::indicator:disabled, QRadioButton::indicator:disabled
{
    border: 1px solid #444;
}

/*********HORIZONTAL SLIDER**************/

QSlider::groove:horizontal {
border: 1px solid #ffaa00;
background: #ffaa00;
height: 6px;
border-radius: 2px;
}


QSlider::sub-page:horizontal {
background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,
    stop: 0 #ffaa00, stop: 1 #ffaa00);
background:#ffaa00;
border: 1px solid #777;
height: 10px;
border-radius: 2px;
}

QSlider::add-page:horizontal {
background: rgb(40,40,40);
border: 1px solid #777;
height: 10px;
border-radius: 2px;
}

QSlider::handle:horizontal {
background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
    stop:0 #eee, stop:1 #ccc);
border: 1px solid #777;
width: 5px;
margin-top: -8px;
margin-bottom: -8px;
border-radius: 2px;
}

QSlider::handle:horizontal:hover {
background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
    stop:0 #fff, stop:1 #ddd);
border: 1px solid #444;
border-radius: 2px;
}

QSlider::sub-page:horizontal:disabled {
background: #bbb;
border-color: #999;
}

QSlider::add-page:horizontal:disabled {
background: #eee;
border-color: #999;
}

QSlider::handle:horizontal:disabled {
background: #eee;
border: 1px solid #aaa;
border-radius: 2px;
}

/*********VERTICAL SLIDER**************/

QSlider::groove:vertical {
border: 1px solid #ffaa00;
background: #ffaa00;
width: 6px;
border-radius: 2px;
}


QSlider::add-page:vertical {
background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,
    stop: 0 #ffaa00, stop: 1 #ffaa00);
background:#ffaa00;
border: 1px solid #777;
width: 10px;
border-radius: 2px;
}

QSlider::sub-page:vertical {
background: rgb(40,40,40);
border: 1px solid #777;
width: 10px;
border-radius: 2px;
}

QSlider::handle:vertical {
background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
    stop:0 #eee, stop:1 #ccc);
border: 1px solid #777;
height: 5px;
margin-left: -8px;
margin-right: -8px;
border-radius: 2px;
}

QSlider::handle:vertical:hover {
background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
    stop:0 #fff, stop:1 #ddd);
border: 1px solid #444;
border-radius: 2px;
}

QSlider::add-page:vertical:disabled {
background: #bbb;
border-color: #999;
}

QSlider::sub-page:vertical:disabled {
background: #eee;
border-color: #999;
}

QSlider::handle:vertical:disabled {
background: #eee;
border: 1px solid #aaa;
border-radius: 2px;
}
/*******************SPINBOX***************/

QSpinBox, QDoubleSpinBox {
  font-size: 12px;
  color: #ccc;
  background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);;
  border: 1 solid #515151;
  padding-right: 10px;
}
QSpinBox::up-button, QDoubleSpinBox::up-button {
subcontrol-origin: border;
subcontrol-position: top right;
width: 19px;

}
QSpinBox::down-button, QDoubleSpinBox::down-button 
{
subcontrol-origin: border;
subcontrol-position: bottom right;
width: 19px;
}'''
win32 = '''/* Basic Palette
border styles: dashed | dot-dash | dot-dot-dash | dotted | double | groove | inset | outset | ridge | solid | none
*/

/* Set the selection colors for all widgets. */
QWidget
{
	color: #111111;
	border: 0px solid #737373;
	background: #727272;
	selection-color: #cccccc;
	selection-background-color: #686868;
	padding: 0px;
	margin: 0px;
}

QMainWindow
{
	background: #727272;
	padding: 0px;
	margin: 0px;
	border: 0px solid #1a1a1a;
}

QMainWindow::separator:horizontal
{
    background: #ff0000;
    max-width: 2px;
	width: 2px;
	border-top: 1px solid #393939;
	border-bottom: 1px solid #959595;
}

QMainWindow::separator:vertical
{
    background: #ff0000;
    max-height: 2px;
	height: 2px;
	border-left: 1px solid #393939;
	border-right: 1px solid #959595;
}

QMainWindow::separator:hover
{
    background: #686868;
}

/* Customize check boxes. */
QCheckBox
{
    spacing: 5px;
   	border: 1px solid #242424;
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #535353, stop:1 #373737);
	max-width: 13px;
    max-height: 13px;
}

QCheckBox::indicator
{
    width: 13px;
    height: 13px;
}


QCheckBox::indicator:checked
{
    image: url(:/checkbox_checked);
}

QCheckBox::indicator:checked:hover
{
    image: url(:/checkbox_checked_hover);
}

QCheckBox::indicator:checked:pressed
{
    image: url(:/checkbox_checked_pressed);
}

/* Combobox */
QComboBox
{
	border: 1px solid #242424;
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #535353, stop:1 #373737);
	color: #c8c8c8;
	border-top-left-radius: 4px; /* same radius as the QComboBox */
	border-bottom-left-radius: 4px;
	border-top-right-radius: 4px;
	border-bottom-right-radius: 4px;
	padding: 1px 18px 1px 13px;
	min-width: 6em;
	max-height: 15px;
}

/* The popup */
QComboBox QAbstractItemView {
	border: 1px solid #303030;
	background: #212121;
	selection-background-color: #484848;
	selection-color: #ffffff;
	color: #c8c8c8;
}

QComboBox:editable
{
	border: 1px solid #242424;
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #535353, stop:1 #373737);
}

QComboBox:!editable, QComboBox::drop-down:editable
{
	border: 1px solid #242424;
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #535353, stop:1 #373737);

}

/* QComboBox gets the "on" state when the popup is open */
QComboBox:!editable:on, QComboBox::drop-down:editable:on
{
	border: 1px solid #242424;
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #535353, stop:1 #373737);

}

QComboBox:on
{
	/* shift the text when the popup opens */
	padding-top: 3px;
	padding-left: 4px;
	border: 1px solid #242424;
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #535353, stop:1 #373737);
}

/* Drop down button */
QComboBox::drop-down
{
	subcontrol-origin: padding;
	subcontrol-position: top right;
	width: 15px;
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #535353, stop:1 #373737);
	border: 0px solid #818181;
	border-top-right-radius: 6px; /* same radius as the QComboBox */
	border-bottom-right-radius: 6px;
}

QComboBox::down-arrow
{
     image: url(:/arrow_down);
     width: 11px;
     height: 6px;
}

QComboBox::up-arrow
{
     image: url(:/arrow_up);
     width: 11px;
     height: 6px;
}

QDockWidget
{
    border-top: 1px solid #1a1a1a;
	border-bottom: 1px solid #1a1a1a;
	border-radius: 0px;
}

QDockWidget::title
{
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #4c4c4c, stop:1 #434343);
}

QFrame
{
     border: 0px solid #737373;
     border-radius: 0px;
     padding: 0px;
     background-color: transparent;
}

QGroupBox
 {
     border: 1px solid #3a3a3a;
     background: #808080;
     border-radius: 5px;
     margin-top: 13px;
 }

QGroupBox::title
{
     subcontrol-origin: margin;
     subcontrol-position: top left;
     padding: 0px 10px;
     color: #0b0b0b;
}

/* Header for ... */
QHeaderView::section
{
	color: #cccccc;
	background: transparent;
	padding-left: 4px;
	border-top: 0px solid #393939;
	border-bottom: 0px solid #959595;
	min-height: 15px;
}

/* Text input box */
QLineEdit
{
	color: #c8c8c8;
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #808080, stop:1 #8c8c8c);
    border: 1px solid #4d4d4d;
	padding: 0 8px;
	selection-background-color: #222222;
	selection-color: #f5f5f5;
	margin-left: 5px;
	margin-right: 5px;
	border-radius: 5px;
	max-height: 14px;
	height: 14px;
}

QLabel
{
	margin-left: 5px;
	margin-right: 5px;
	background: none;
	border: 0px;
}

/* Drop down style */
QMenu
{
	background: #212121;
	border: 1px solid #303030;
	color: #eaeaea;
}

QMenu::separator
{
     image: none;
     border-top: 1px solid #262626;
}

QMenu::item
{
	/* sets background of menu item. set this to something non-transparent
	if you want menu color and menu item color to be different */
	background-color: transparent;
}

QMenu::item:selected
{
	/* when user selects item using mouse or keyboard */
	background: #3e3e3e;
	color: #ffffff;
}

QMenuBar
{
    border-top: 1px solid #8b8b8b;
	border-left: 0px solid #606060;
	border-bottom: 1px solid #939393;
	border-right: 0px solid #303030;
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #686868, stop:0.8 #686868, stop:0.9 #474747, stop:1 #000000);
	min-height: 20px;
}

QMenuBar::item
{
	spacing: 3px; /* spacing between menu bar items */
	padding: 1px 4px;
	background: transparent;
	color: #111111;
	max-height: 16px;
}

/* when selected using mouse or keyboard */

QMenuBar::item:selected
{
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #565656, stop:1 #464646);
	color: #ffffff;
	border-radius: 5px;
	border:	1px solid #222222;
}

QMenuBar::item:pressed
{
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #565656, stop:1 #464646);
	color: #ffffff;
	border-radius: 5px;
	border:	1px solid #222222;
}

QPushButton
{
    color: #0b0b0b;
    border: 1px solid #353535;
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #a6a6a6, stop:1 #8a8a8a);
	border-radius: 3px;
	padding-left: 5px;
	padding-right: 5px;
}

/* all types of push button */
QPushButton:hover
{
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #565656, stop:1 #464646);
	color: #ffffff;
}

QPushButton:pressed
{
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #565656, stop:1 #464646);
	color: #e5e5e5;
}

/* Customize radio buttons. */
QRadioButton
{
    spacing: 5px;
}

QRadioButton::indicator
{
    width: 13px;
    height: 13px;
}

QRadioButton::indicator::unchecked
{
    image: url(:/radiobutton_unchecked);
}

QRadioButton::indicator:unchecked:hover
{
    image: url(:/radiobutton_unchecked_hover);
}

QRadioButton::indicator:unchecked:pressed
{
    image: url(:/radiobutton_unchecked_pressed);
}

QRadioButton::indicator::checked
{
    image: url(:/radiobutton_checked);
}

QRadioButton::indicator:checked:hover
{
    image: url(:/radiobutton_checked_hover);
}

QRadioButton::indicator:checked:pressed
{
    image: url(:/radiobutton_checked_pressed);
}

/* Customize arrows.
*::down-arrow, *::menu-indicator {
    image: url(:/arrow_down);
    width: 9px;
    height: 9px;
}

*::down-arrow:disabled, *::down-arrow:off {
   image: url(:/down_arrow_disabled.png);
}

*::up-arrow {
    image: url(:/arrow_up);
    width: 9px;
    height: 9px;
}

*::up-arrow:disabled, *::up-arrow:off {
   image: url(:/up_arrow_disabled.png);
}

*/

QScrollBar QAbstractScrollArea
{
	background: transparent;
}

QScrollBar:horizontal
{
	max-height: 12px;
	min-height: 12px;
	margin: 0px 22px 0px 22px;
    border: 0px solid #474747;
    border-radius: 0px;
    background: transparent;
}

QScrollBar::handle:horizontal
{
	border: 1px solid #383838;
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #969696, stop:1 #7b7b7b);
	border-radius: 3px;
	min-height: 8px;
	max-height: 8px;
	height: 8px;
}

QScrollBar::add-line:horizontal
{
	border: 0px solid #1e1e1e;
    background-color: transparent;
    width: 0px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal
{
	border: 0px solid #1e1e1e;
    background-color: transparent;
    width: 0px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}

QScrollBar::left-arrow:horizontal
{
	background-color: transparent;
    width: 0px;
    height: 0px;
}

QScrollBar::right-arrow:horizontal
{
	background-color: transparent;
    width: 0px;
    height: 0px;
}

QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
{
    background-color: transparent;
}

QScrollBar:vertical
{
    border: 0px solid #1e1e1e;
    border-radius: 0px;
    background: transparent;
    max-width: 12px;
	min-width: 12px;
	margin: 22px 0px 22px 0px;
}

QScrollBar::handle:vertical
{
	border: 1px solid #383838;
	background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #969696, stop:1 #7b7b7b);
	border-radius: 3px;
	min-width: 8px;
	max-width: 8px;
	min-height: 20px;
	max-height: 20px;
	width: 8px;

}

QScrollBar::add-line:vertical
{
    subcontrol-position: top;
    subcontrol-origin: margin;
	border: 0px solid #1e1e1e;
	background-color: transparent;
	height: 0px;
}

QScrollBar::sub-line:vertical
{
    subcontrol-position: bottom;
    subcontrol-origin: margin;
	border: 0px solid #1e1e1e;
	background-color: transparent;
	height: 0px;
}

QScrollBar::up-arrow:vertical
{
	background-color: transparent;
    width: 0px;
    height: 0px;
}

QScrollBar::down-arrow:vertical
{
	background-color: transparent;
    width: 0px;
    height: 0px;
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
{
	background-color: transparent;
}

QSlider
{
	background-color: #808080;
}

QSlider::groove:vertical
{
	background-color: transperant;
	position: absolute;
	left: 4px; right: 4px;
}

QSlider::handle:vertical
{
     height: 10px;
     background: #ff7603;
     border: 1px solid #62340e;
     margin: 0 -4px; /* expand outside the groove */
}

QSlider::add-page:vertical
{
     background: #222222;
}

QSlider::sub-page:vertical
{
     background: #222222;
}

QSpinBox
{
    padding-right: 15px; /* make room for the arrows */
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #808080, stop:1 #8c8c8c);
    border: 1px solid #4d4d4d;
    color: #ffffff;
   	border-top-left-radius: 3px; /* same radius as the QComboBox */
	border-bottom-left-radius: 3px;
}

QSpinBox::up-button
{
    subcontrol-origin: border;
    subcontrol-position: top right; /* position at the top right corner */
    width: 16px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #a6a6a6, stop:1 #979797);
    border: 1px solid #323232;
	border-bottom-width: 0;
}

QSpinBox::up-button:hover
{
	background: #3e3e3e;
}

QSpinBox::up-button:pressed
{
	background: #3e3e3e;
}

QSpinBox::up-arrow
{
     image: url(:/arrow_up);
     width: 11px;
     height: 6px;
}

QSpinBox::up-arrow:disabled, QSpinBox::up-arrow:off
{ /* off state when value is max */
    image: url(:/arrow_up);
}

QSpinBox::down-button
{
    subcontrol-origin: border;
    subcontrol-position: bottom right; /* position at bottom right corner */
    width: 16px;
	border-top: 0px solid #323232;
	border-left: 1px solid #323232;
	border-bottom: 1px solid #323232;
	border-right: 1px solid #323232;
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #979797, stop:1 #8a8a8a);
    border-top-width: 0;
}

QSpinBox::down-button:hover
{
	background: #3e3e3e;
}

QSpinBox::down-button:pressed
{
	background: #3e3e3e;
}

QSpinBox::down-arrow
{
     image: url(:/arrow_down);
     width: 11px;
     height: 6px;
}

QSpinBox::down-arrow:disabled,
QSpinBox::down-arrow:off
{ /* off state when value in min */
    image: url(:/arrow_down);
}

QSplitter::handle
{
    background: transparent;
}

QSplitter::handle:horizontal
{
 	background: transparent;
 	min-width: 2px;
	max-width: 2px;
	width: 2px;
	border-left: 1px solid #393939;
	border-right: 1px solid #959595;
	padding: 0px;
	margin: 0px;
}

QSplitter::handle:vertical
{
   	background: transparent;
   	max-height: 2px;
	min-height: 2px;
	height: 2px;
	border-top: 1px solid #393939;
	border-bottom: 1px solid #959595;
	padding: 0px;
	margin: 0px;
}

QStatusBar
{
   	border: 0px solid #262626;
	background: #686868;
}

/* Table View */
QTableView
{
	background: #727272;
	selection-background-color: #787878;
	selection-color: #f5f5f5;
	padding-left: 5px;
	padding-right: 5px;
	color: #000000;
	margin: 5px;
}

QTreeView
{
	margin-top: 1px;
	border: 0px solid #434343;
	border-radius: 0px;
	padding: 0px;
	background: #727272;
	paint-alternating-row-colors-for-empty-area: 1;
	show-decoration-selected: 1;
	alternate-background-color: #727272;
}

QTreeView::item
{
	color: #cccccc;
	padding-left: 10px;
}

QTreeView::item:hover
{
	color: #e5e5e5;
}

QTreeView::item:selected
{
	color: #ffffff;
	background: #686868;
}

QTreeView::item:selected:active
{
	color: #f5f5f5;
	background: #686868;
}

QTreeView::item:selected:!active
{
	color: #f5f5f5;
	background: #686868;
}

QTreeView::branch:has-siblings:!adjoins-item
{
     border-image: url(:/vline) 0;
}

QTreeView::branch:has-siblings:adjoins-item
{
     border-image: url(:/branch-more) 0;
}

QTreeView::branch:!has-children:!has-siblings:adjoins-item
{
     border-image: url(:/branch-end) 0;
}

QTreeView::branch:has-children:!has-siblings:closed,
QTreeView::branch:closed:has-children:has-siblings
{
         image: url(:/branch-closed);
}

QTreeView::branch:open:has-children:!has-siblings,
QTreeView::branch:open:has-children:has-siblings
{
         border-image: none;
         image: url(:/branch-open);
}

/* The tab widget frame */
QTabWidget::pane
{
    border: 1px solid #353535;
	margin: 0px;
	padding: 0px;

}

QTabWidget::tab-bar
{
	background: #323232;
	border: 1px solid #1e1e1e;
}

/* Style the tab using the tab sub-control. */
QTabBar::tab
{
	border: 1px solid #353535;
	border-bottom: 0px solid #242424;
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #535353, stop:1 #373737);
	color: #aaaaaa;
	padding: 3px;
	border-top-left-radius: 4px;
    border-top-right-radius: 4px;
	margin-top: 1px;
	margin-bottom: 0px;
	margin-left: 5px;
}

QTabBar::tab:hover
{
	color: #ffffff;
}

QTabBar::tab:selected
{
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #a6a6a6, stop:1 #8a8a8a);
	color: #010101
}

/* Style for main toolbar */
QToolBar
{
    border: 0px solid #8b8b8b;
	background-color: transparent;
	spacing: 2px; /* spacing between items in the tool bar */
	margin-left: 3px;
	color: #e5e5e5;
	max-height: 22px;
}

QToolBar::handle
{
     image: none;
     background-color: transparent;
}

QToolBar::separator
{
     width: 5px;
     border: 0px;
     background-color: transparent;
}

/* All types of tool button */
QToolButton
{
	border: 1px solid #353535;
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #a6a6a6, stop:1 #8a8a8a);
	color: #e5e5e5;
	border-radius: 5px;
	max-height: 18px;
	min-width: 18px;
}

QToolButton[popupMode="1"]
{
	/* only for MenuButtonPopup */
	padding-right: 20px; /* make way for the popup button */
	/* max-width: 32px; */
}

QToolButton::menu-button
{
     /* 16px width + 4px for border = 20px allocated above */
	border-top: 1px solid #323232;
	border-left: 1px solid #222222;
	border-bottom: 1px solid #323232;
	border-right: 1px solid #323232;
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #a6a6a6, stop:1 #8a8a8a);
	color: #111111;
}

QToolButton:hover
{
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #e5e5e5, stop:0.2 #a6a6a6, stop:0.8 #8a8a8a, stop:1 #4a4a4a);
	color: #c8c8c8;
}

QToolButton:pressed
{
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #e5e5e5, stop:0.2 #a6a6a6, stop:0.8 #8a8a8a, stop:1 #4a4a4a);
	color: #c8c8c8;
}

QToolTip
{
	border: 1px solid #111111;
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #363636, stop:0.2 #e5e5e5, stop:0.8 #ffffff, stop:1 #262626);
	padding: 3px;
	border-radius: 0px;
	opacity: 150;
	color: #000000;
}

QDoubleSpinBox
{
    padding-right: 15px; /* make room for the arrows */
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #808080, stop:1 #8c8c8c);
    border: 1px solid #4d4d4d;
    color: #ffffff;
   	border-top-left-radius: 3px; /* same radius as the QComboBox */
	border-bottom-left-radius: 3px;
}

QDoubleSpinBox::up-button
{
    subcontrol-origin: border;
    subcontrol-position: top right; /* position at the top right corner */
    width: 16px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #a6a6a6, stop:1 #979797);
    border: 1px solid #323232;
	border-bottom-width: 0;
}

QDoubleSpinBox::up-button:hover
{
	background: #3e3e3e;
}

QDoubleSpinBox::up-button:pressed
{
	background: #3e3e3e;
}

QDoubleSpinBox::up-arrow
{
     image: url(:/arrow_up);
     width: 11px;
     height: 6px;
}

QDoubleSpinBox::up-arrow:disabled, QDoubleSpinBox::up-arrow:off
{ /* off state when value is max */
    image: url(:/arrow_up);
}

QDoubleSpinBox::down-button
{
    subcontrol-origin: border;
    subcontrol-position: bottom right; /* position at bottom right corner */
    width: 16px;
	border-top: 0px solid #323232;
	border-left: 1px solid #323232;
	border-bottom: 1px solid #323232;
	border-right: 1px solid #323232;
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #979797, stop:1 #8a8a8a);
    border-top-width: 0;
}

QDoubleSpinBox::down-button:hover
{
	background: #3e3e3e;
}

QDoubleSpinBox::down-button:pressed
{
	background: #3e3e3e;
}

QDoubleSpinBox::down-arrow
{
     image: url(:/arrow_down);
     width: 11px;
     height: 6px;
}

QDoubleSpinBox::down-arrow:disabled,
QDoubleSpinBox::down-arrow:off
{ /* off state when value in min */
    image: url(:/arrow_down);
}
'''