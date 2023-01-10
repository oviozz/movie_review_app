
from PyQt5 import QtCore, QtGui, QtWidgets
from movie_api_call import MovieListLoad
from movie_detail import MovieDetail
from movie_gerne import GerneListLoad
from movie_search import SearchListLoad
from function_navigation import Navigation, Region
from functools import partial


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(1259, 734)
        main_window.setStyleSheet("background-color: rgb(23, 25, 52);")
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.top_background = QtWidgets.QLabel(self.centralwidget)
        self.top_background.setGeometry(QtCore.QRect(-10, -10, 1271, 91))
        self.top_background.setStyleSheet("background-color: rgb(12, 15, 38);")
        self.top_background.setText("")
        self.top_background.setObjectName("top_background")
        self.side_background = QtWidgets.QLabel(self.centralwidget)
        self.side_background.setGeometry(QtCore.QRect(0, 60, 191, 691))
        self.side_background.setStyleSheet("background-color: rgb(12, 15, 38);")
        self.side_background.setText("")
        self.side_background.setObjectName("side_background")
        self.list_sorting = QtWidgets.QComboBox(self.centralwidget)
        self.list_sorting.setGeometry(QtCore.QRect(1100, 20, 121, 41))
        self.list_sorting.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.list_sorting.setStyleSheet("\n"
                                        "\n"
                                        "QComboBox{\n"
                                        "background-color: rgb(23, 25, 52);\n"
                                        "color: rgb(118, 120, 251); \n"
                                        "font: 12pt \"MS Shell Dlg 2\";\n"
                                        "border-radius: 7px;\n"
                                        "padding: 8px;\n"
                                        "}\n"
                                        "\n"
                                        "QComboBox::drop-down:button{border-radius:7px; background-color: rgb(23, 25, 52)}\n"
                                        "\n"
                                        "QListView\n"
                                        "{\n"
                                        "background-color: rgb(23, 25, 52);\n"
                                        "font: 12pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(118, 120, 251); \n"
                                        "font: 12pt \"MS Shell Dlg 2\";\n"
                                        "padding: 5px;\n"
                                        "outline: 0px;\n"
                                        "border: 1px solid rgba(0,0,0,10%);\n"
                                        "\n"
                                        "\n"
                                        "}\n"
                                        "\n"
                                        "")
        self.list_sorting.setDuplicatesEnabled(False)
        self.list_sorting.setFrame(False)
        self.list_sorting.setObjectName("list_sorting")

        self.list_sorting.addItem("")
        self.list_sorting.addItem("")
        self.list_sorting.addItem("")
        self.list_sorting.addItem("")
        self.list_sorting.addItem("")
        self.list_sorting.addItem("")

        self.search_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.search_bar.setGeometry(QtCore.QRect(410, 20, 431, 41))
        self.search_bar.setStyleSheet("color: rgb(135, 151, 255);\n"
                                      "font: 12pt \"MS Shell Dlg 2\";\n"
                                      "border-radius: 15px;\n"
                                      "border: 0px\n"
                                      "\n"
                                      "\n"
                                      "")
        self.search_bar.setObjectName("search_bar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 20, 51, 41))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "border-radius: 15px;\n"
                                 "border: 0px")
        self.label.setText("")
        self.label.setObjectName("label")
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setGeometry(QtCore.QRect(820, 20, 51, 41))
        self.search_button.setStyleSheet("\n"
                                         "QPushButton {\n"
                                         "    color: rgb(255, 255, 255);\n"
                                         "    border-radius: 15px;\n"
                                         "    border: 0px\n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "QPushButton:hover,QPushButton:pressed  {\n"
                                         "    background-color: rgb(43, 47, 97);\n"
                                         "    \n"
                                         "}")
        self.search_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/search-line.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_button.setIcon(icon)
        self.search_button.setIconSize(QtCore.QSize(100, 100))
        self.search_button.setObjectName("search_button")
        self.title_box = QtWidgets.QLabel(self.centralwidget)
        self.title_box.setGeometry(QtCore.QRect(30, 20, 181, 41))
        self.title_box.setStyleSheet("color: rgb(250, 202, 49);\n"
                                     "font: 12pt \"MS Shell Dlg 2\";\n"
                                     "border: 1px solid rgb(250, 202, 49);")
        self.title_box.setObjectName("title_box")
        self.screens = QtWidgets.QTabWidget(self.centralwidget)
        self.screens.setGeometry(QtCore.QRect(200, 90, 1091, 711))
        self.screens.setStyleSheet("border: 0px;")
        self.screens.setTabPosition(QtWidgets.QTabWidget.South)
        self.screens.setObjectName("screens")
        self.movie_list_screen = QtWidgets.QWidget()
        self.movie_list_screen.setObjectName("movie_list_screen")
        self.movie_lists = QtWidgets.QListWidget(self.movie_list_screen)

        self.movie_lists.setGeometry(QtCore.QRect(0, 0, 1051, 641))
        self.movie_lists.setStyleSheet("\n"
                                       "QListWidget {background-color: rgb(23, 25, 52); color: rgb(255, 255, 255); font: 15pt \"MS Shell Dlg 2\"; border: 2px rgb(255, 255, 255); }\n"
                                       "\n"
                                       "\n"
                                       "QScrollBar:vertical { border: none; width: 10px; margin: 14px 0 14px 0; border-radius: 0px; } QScrollBar::handle:vertical { background-color: rgb(43, 71, 156); min-height: 30px; border-radius: 5px; } QScrollBar::handle:vertical:hover{ background-color: rgb(198, 198, 198); } QScrollBar::handle:vertical:pressed { background-color: rgb(182, 182, 182); } QScrollBar::sub-line:vertical { border: none; height: 15px; border-top-left-radius: 7px; border-top-right-radius: 7px; subcontrol-position: top; subcontrol-origin: margin; } QScrollBar::sub-line:vertical:hover { background-color: rgb(198, 198, 198); } QScrollBar::sub-line:vertical:pressed { background-color: rgb(182, 182, 182); } QScrollBar::add-line:vertical { border: none; ; height: 15px; border-bottom-left-radius: 7px; border-bottom-right-radius: 7px; subcontrol-position: bottom; subcontrol-origin: margin; } QScrollBar::add-line:vertical:hover { background-color: rgb(198, 198, 198); } QScrollBar::add-line:vertical:pressed { background-color: rgb(182, 182, 182); } QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical { background: rgb(12, 15, 38); } QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { background: rgb(12, 15, 38); } QListWidget::item:hover,QListWidget::item:selected {background-color: rgb(12, 15, 38); color: rgb(118, 120, 251); border-radius: 15px;}")
        self.movie_lists.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.movie_lists.setIconSize(QtCore.QSize(200, 200))
        #self.movie_lists.setViewMode(QtWidgets.QListView.IconMode)
        self.movie_lists.setSelectionRectVisible(True)
        self.movie_lists.setObjectName("movie_lists")

        self.movie_lists.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.movie_lists.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.NoSelection)

        self.screens.addTab(self.movie_list_screen, "")
        self.movie_detail_screen = QtWidgets.QWidget()
        self.movie_detail_screen.setObjectName("movie_detail_screen")
        self.movie_detail_poster = QtWidgets.QLabel(self.movie_detail_screen)
        self.movie_detail_poster.setGeometry(QtCore.QRect(30, 30, 231, 311))
        self.movie_detail_poster.setStyleSheet("border: 1px solid rgb(250, 202, 49);\n"
                                               "border-radius: 7px;\n"
                                               "")
        self.movie_detail_poster.setText("")
        self.movie_detail_poster.setPixmap(QtGui.QPixmap("../background.png"))
        self.movie_detail_poster.setScaledContents(True)
        self.movie_detail_poster.setWordWrap(False)
        self.movie_detail_poster.setObjectName("movie_detail_poster")
        self.movie_detail_title = QtWidgets.QLabel(self.movie_detail_screen)
        self.movie_detail_title.setGeometry(QtCore.QRect(310, 30, 471, 51))
        self.movie_detail_title.setStyleSheet("color: rgb(255, 255, 255);\n"
                                              "font: 25pt \"MS Shell Dlg 2\";")
        self.movie_detail_title.setObjectName("movie_detail_title")
        self.movie_detail_overview = QtWidgets.QLabel(self.movie_detail_screen)
        self.movie_detail_overview.setGeometry(QtCore.QRect(290, 100, 741, 181))
        self.movie_detail_overview.setStyleSheet("color: rgb(176, 176, 176);\n"
                                                 "font: 15pt \"MS Shell Dlg 2\";")
        self.movie_detail_overview.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.movie_detail_overview.setWordWrap(True)
        self.movie_detail_overview.setObjectName("movie_detail_overview")
        self.movie_detail_rating = QtWidgets.QLabel(self.movie_detail_screen)
        self.movie_detail_rating.setGeometry(QtCore.QRect(800, 60, 231, 31))
        self.movie_detail_rating.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";\n"
                                               "color: rgb(255, 255, 255);")
        self.movie_detail_rating.setObjectName("movie_detail_rating")
        self.movie_detail_releasedate = QtWidgets.QLabel(self.movie_detail_screen)
        self.movie_detail_releasedate.setGeometry(QtCore.QRect(800, 30, 231, 31))
        self.movie_detail_releasedate.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                    "font: 13pt \"MS Shell Dlg 2\";")
        self.movie_detail_releasedate.setObjectName("movie_detail_releasedate")
        self.movie_detail_language = QtWidgets.QLabel(self.movie_detail_screen)
        self.movie_detail_language.setGeometry(QtCore.QRect(30, 370, 180, 31))
        self.movie_detail_language.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                 "font: 14pt \"MS Shell Dlg 2\";")
        self.movie_detail_language.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.movie_detail_language.setObjectName("movie_detail_language")
        self.movie_detail_genre = QtWidgets.QLabel(self.movie_detail_screen)
        self.movie_detail_genre.setGeometry(QtCore.QRect(30, 350, 261, 31))
        self.movie_detail_genre.setStyleSheet("color: rgb(255, 255, 255);\n"
                                              "font: 14pt \"MS Shell Dlg 2\";")
        self.movie_detail_genre.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.movie_detail_genre.setObjectName("movie_detail_genre")

        self.movie_restrict = QtWidgets.QLabel(self.movie_detail_screen)
        self.movie_restrict.setGeometry(QtCore.QRect(950, 60, 71, 21))
        self.movie_restrict.setStyleSheet("color: rgb(250, 202, 49);\n"
                                          "font: 13pt \"MS Shell Dlg 2\";")
        self.movie_restrict.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.movie_restrict.setObjectName("movie_restrict")
        self.movie_tralier_button = QtWidgets.QPushButton(self.movie_detail_screen)
        self.movie_tralier_button.setGeometry(QtCore.QRect(290, 290, 81, 31))
        self.movie_tralier_button.setStyleSheet("\n"
                                                "\n"
                                                "QPushButton {\n"
                                                "    color: rgb(255, 255, 255);\n"
                                                "    \n"
                                                "    background-color: rgb(255, 0, 0);\n"
                                                "    font: 10pt \"MS Shell Dlg 2\";\n"
                                                "    border-radius: 7px;\n"
                                                " }\n"
                                                "\n"
                                                " QPushButton:hover {\n"
                                                "    \n"
                                                "    background-color: rgb(197, 6, 35);\n"
                                                "}\n"
                                                "\n"
                                                "\n"
                                                " QPushButton:pressed {\n"
                                                "    \n"
                                                "    background-color: rgb(126, 0, 0);\n"
                                                " }\n"
                                                "\n"
                                                "")
        self.movie_tralier_button.setObjectName("movie_tralier_button")
        self.add_to_list_button = QtWidgets.QPushButton(self.movie_detail_screen)
        self.add_to_list_button.setGeometry(QtCore.QRect(280, 20, 31, 31))
        self.add_to_list_button.setStyleSheet("\n"
                                              "\n"
                                              "QPushButton {\n"
                                              "    font: 20pt \"MS Shell Dlg 2\";\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              " }\n"
                                              "\n"
                                              "\n"
                                              "QPushButton:hover {\n"
                                              "    \n"
                                              "    color: rgb(250, 202, 49);\n"
                                              "\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:pressed {\n"
                                              "    \n"
                                              "    \n"
                                              "    color: rgb(198, 158, 39);\n"
                                              "\n"
                                              "}\n"
                                              "")
        self.add_to_list_button.setObjectName("add_to_list_button")

        self.back_button = QtWidgets.QPushButton(self.movie_detail_screen)
        self.back_button.setGeometry(QtCore.QRect(0, 0, 21, 31))
        self.back_button.setStyleSheet("\n"
                                       "\n"
                                       "QPushButton {\n"
                                       "    font: 25pt \"MS Shell Dlg 2\";\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(23, 25, 52);\n"
                                       "    color: rgb(118, 120, 251); \n"
                                       "    border-radius: 7px;\n"
                                       "    padding: 8px;    \n"
                                       "\n"
                                       " }\n"
                                       "\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    \n"
                                       "    background-color:rgb(32, 35, 72)\n"
                                       "\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    \n"
                                       "    \n"
                                       "    background-color: rgb(59, 66, 134);\n"
                                       "\n"
                                       "}\n"
                                       "")
        self.back_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/back_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_button.setIcon(icon1)
        self.back_button.setIconSize(QtCore.QSize(50, 50))
        self.back_button.setObjectName("back_button")


        self.movie_detail_title.raise_()
        self.movie_detail_overview.raise_()
        self.movie_detail_rating.raise_()
        self.movie_detail_releasedate.raise_()
        self.movie_detail_poster.raise_()
        self.movie_detail_genre.raise_()
        self.movie_detail_language.raise_()
        self.movie_restrict.raise_()
        self.movie_tralier_button.raise_()
        self.add_to_list_button.raise_()
        self.back_button.raise_()


        self.screens.addTab(self.movie_detail_screen, "")
        self.search_screen = QtWidgets.QWidget()
        self.search_screen.setObjectName("favorites")

        self.movie_search_lists = QtWidgets.QListWidget(self.search_screen)
        self.movie_search_lists.setGeometry(QtCore.QRect(0, 0, 1051, 641))
        self.movie_search_lists.setStyleSheet("\n"
                                       "QListWidget {background-color: rgb(23, 25, 52); color: rgb(255, 255, 255); font: 15pt \"MS Shell Dlg 2\"; border: 2px rgb(255, 255, 255); }\n"
                                       "\n"
                                       "\n"
                                       "QScrollBar:vertical { border: none; width: 10px; margin: 14px 0 14px 0; border-radius: 0px; } QScrollBar::handle:vertical { background-color: rgb(43, 71, 156); min-height: 30px; border-radius: 5px; } QScrollBar::handle:vertical:hover{ background-color: rgb(198, 198, 198); } QScrollBar::handle:vertical:pressed { background-color: rgb(182, 182, 182); } QScrollBar::sub-line:vertical { border: none; height: 15px; border-top-left-radius: 7px; border-top-right-radius: 7px; subcontrol-position: top; subcontrol-origin: margin; } QScrollBar::sub-line:vertical:hover { background-color: rgb(198, 198, 198); } QScrollBar::sub-line:vertical:pressed { background-color: rgb(182, 182, 182); } QScrollBar::add-line:vertical { border: none; ; height: 15px; border-bottom-left-radius: 7px; border-bottom-right-radius: 7px; subcontrol-position: bottom; subcontrol-origin: margin; } QScrollBar::add-line:vertical:hover { background-color: rgb(198, 198, 198); } QScrollBar::add-line:vertical:pressed { background-color: rgb(182, 182, 182); } QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical { background: rgb(12, 15, 38); } QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { background: rgb(12, 15, 38); } QListWidget::item:hover,QListWidget::item:selected {background-color: rgb(12, 15, 38); color: rgb(118, 120, 251); border-radius: 15px;}")

        self.movie_search_lists.setIconSize(QtCore.QSize(250, 250))
        self.movie_search_lists.setSelectionRectVisible(True)

        self.movie_search_lists.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.movie_search_lists.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.NoSelection)
        self.movie_search_lists.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.movie_search_lists.setObjectName("movie_favorites")
        self.screens.addTab(self.search_screen, "")

        self.favorite_list = QtWidgets.QPushButton(self.centralwidget)
        self.favorite_list.setGeometry(QtCore.QRect(30, 590, 121, 31))
        self.favorite_list.setStyleSheet("\n"
                                         "\n"
                                         "QPushButton {\n"
                                         "    font: 25pt \"MS Shell Dlg 2\";\n"
                                         "    color: rgb(255, 255, 255);\n"
                                         "    background-color: rgb(23, 25, 52);\n"
                                         "    color: rgb(118, 120, 251); \n"
                                         "    border-radius: 7px;\n"
                                         "    padding: 8px;    \n"
                                         "\n"
                                         " }\n"
                                         "\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "    \n"
                                         "    background-color:rgb(32, 35, 72)\n"
                                         "\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed {\n"
                                         "    \n"
                                         "    \n"
                                         "    background-color: rgb(59, 66, 134);\n"
                                         "\n"
                                         "}\n"
                                         "")
        self.favorite_list.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/receipt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.favorite_list.setIcon(icon2)
        self.favorite_list.setIconSize(QtCore.QSize(100, 100))
        self.favorite_list.setObjectName("favorite_list")

        self.back_button_favorite = QtWidgets.QPushButton(self.search_screen)
        self.back_button_favorite.setGeometry(QtCore.QRect(0, 0, 21, 31))
        self.back_button_favorite.setStyleSheet("\n"
                                       "\n"
                                       "QPushButton {\n"
                                       "    font: 25pt \"MS Shell Dlg 2\";\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(23, 25, 52);\n"
                                       "    color: rgb(118, 120, 251); \n"
                                       "    border-radius: 7px;\n"
                                       "    padding: 8px;    \n"
                                       "\n"
                                       " }\n"
                                       "\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    \n"
                                       "    background-color:rgb(32, 35, 72)\n"
                                       "\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    \n"
                                       "    \n"
                                       "    background-color: rgb(59, 66, 134);\n"
                                       "\n"
                                       "}\n"
                                       "")
        self.back_button_favorite.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/back_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_button_favorite.setIcon(icon3)
        self.back_button_favorite.setIconSize(QtCore.QSize(50, 50))
        self.back_button_favorite.setObjectName("back_button")



        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(30, 650, 121, 31))
        self.exit_button.setStyleSheet("\n"
                                       "\n"
                                       "QPushButton {\n"
                                       "    font: 25pt \"MS Shell Dlg 2\";\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(23, 25, 52);\n"
                                       "    color: rgb(118, 120, 251); \n"
                                       "    border-radius: 7px;\n"
                                       "    padding: 8px;    \n"
                                       "\n"
                                       " }\n"
                                       "\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    \n"
                                       "    background-color:rgb(32, 35, 72)\n"
                                       "\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    \n"
                                       "    \n"
                                       "    background-color: rgb(59, 66, 134);\n"
                                       "\n"
                                       "}\n"
                                       "")
        self.exit_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/sign-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_button.setIcon(icon4)
        self.exit_button.setIconSize(QtCore.QSize(50, 50))
        self.exit_button.setObjectName("exit_button")


        self.movie_lists_gerne = QtWidgets.QListWidget(self.centralwidget)
        self.movie_lists_gerne.setGeometry(QtCore.QRect(10, 80, 181, 451))
        self.movie_lists_gerne.setStyleSheet(
            "QListWidget {background-color: rgb(12, 15, 38); color: rgb(118, 120, 251); font: 12pt \"MS Shell Dlg 2\"; border: 2px rgb(255, 255, 255); }\n"
            "\n"
            "\n"
            "QScrollBar:vertical { border: none; width: 10px; margin: 14px 0 14px 0; border-radius: 0px; } QScrollBar::handle:vertical { background-color: rgb(43, 71, 156); min-height: 30px; border-radius: 5px; } QScrollBar::handle:vertical:hover{ background-color: rgb(198, 198, 198); } QScrollBar::handle:vertical:pressed { background-color: rgb(182, 182, 182); } QScrollBar::sub-line:vertical { border: none; height: 15px; border-top-left-radius: 7px; border-top-right-radius: 7px; subcontrol-position: top; subcontrol-origin: margin; } QScrollBar::sub-line:vertical:hover { background-color: rgb(198, 198, 198); } QScrollBar::sub-line:vertical:pressed { background-color: rgb(182, 182, 182); } QScrollBar::add-line:vertical { border: none; ; height: 15px; border-bottom-left-radius: 7px; border-bottom-right-radius: 7px; subcontrol-position: bottom; subcontrol-origin: margin; } QScrollBar::add-line:vertical:hover { background-color: rgb(198, 198, 198); } QScrollBar::add-line:vertical:pressed { background-color: rgb(182, 182, 182); } QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical { background: rgb(12, 15, 38); } QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { background: rgb(12, 15, 38); } QListWidget::item:hover,QListWidget::item:selected {background-color: rgb(23, 25, 52); color: rgb(118, 120, 251); border-radius: 7px;}")
        self.movie_lists_gerne.setObjectName("movie_lists_gerne")
        item = QtWidgets.QListWidgetItem()
        self.movie_lists_gerne.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.movie_lists_gerne.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.movie_lists_gerne.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.movie_lists_gerne.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.movie_lists_gerne.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.movie_lists_gerne.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.movie_lists_gerne.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.movie_lists_gerne.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.movie_lists_gerne.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.movie_lists_gerne.addItem(item)

        self.movie_lists_gerne.setSpacing(10)
        self.movie_lists_gerne.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.top_background.raise_()
        self.side_background.raise_()
        self.list_sorting.raise_()
        self.label.raise_()
        self.search_bar.raise_()
        self.search_button.raise_()
        self.title_box.raise_()
        self.screens.raise_()
        self.favorite_list.raise_()
        self.back_button_favorite.raise_()
        self.exit_button.raise_()
        self.movie_lists_gerne.raise_()
        main_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(main_window)
        self.screens.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_window)


        MovieListLoad(Region.region_code(self.list_sorting.currentText())).movie_list_load(self.movie_lists)

        # Switch to movie detail when item clicked
        self.movie_lists.itemClicked.connect(self.detail_screen)
        self.movie_search_lists.itemClicked.connect(self.detail_screen)

        # Exit
        self.exit_button.clicked.connect(lambda x: Navigation.exit())

        # Movie gerne change
        self.movie_lists_gerne.itemClicked.connect(self.gernes_movies)

        # yt_button
        self.movie_tralier_button.clicked.connect(MovieDetail.youtube_button)

        # back_button ( checks for previous screen )
        self.back_button.clicked.connect(lambda x: Navigation.screen_navigator(self.screens, Navigation.return_index()))

        # Region change ( movie language detail )
        self.list_sorting.currentTextChanged.connect(self.language_change)

        # detail back_button
        self.back_button_favorite.clicked.connect(partial(self.movie_navigation, 0))

        # Favorite
        #self.favorite_list.clicked.connect(partial(self.movie_navigation, 2))

        self.search_button.clicked.connect(partial(self.search_movies, self.search_bar))


        self.current_gerne = None
        self.next_gerne = None

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "MainWindow"))
        self.list_sorting.setItemText(0, _translate("main_window", "USA"))
        self.list_sorting.setItemText(1, _translate("main_window", "China"))
        self.list_sorting.setItemText(2, _translate("main_window", "Hindi"))
        self.list_sorting.setItemText(3, _translate("main_window", "Korean"))
        self.list_sorting.setItemText(4, _translate("main_window", "Japanese"))
        self.list_sorting.setItemText(5, _translate("main_window", "France"))

        self.search_bar.setPlaceholderText(_translate("main_window", "Search Movies"))
        self.title_box.setText(_translate("main_window", "  MOVIE BOX - prajwal"))
        self.screens.setTabText(self.screens.indexOf(self.movie_list_screen), _translate("main_window", "Tab 1"))
        self.movie_detail_title.setText(_translate("main_window", "Avatar the Way of Water"))
        self.movie_detail_overview.setText(_translate("main_window",
                                                      "Newly engaged Shelby John and Ruby Red want a fresh start after their struggles with addiction, but when Shelby discovers his beloved Ruby dead on their porch, he embarks on a vengeful killing spree of the dealers who supplied her. Armed with nothing but adrenaline and a nail gun, Shelby begins to unleash chaos on the town’s criminal underbelly, as he hunt’s down crime lord Coyote. Sheriff Church must race against the clock to put an end to Shelby\'s vigilante justice before the entire town descends into a bloodbath."))
        self.movie_detail_rating.setText(_translate("main_window", "Rating: 7.7"))
        self.movie_detail_releasedate.setText(_translate("main_window", "Release date: 2022-12-14"))
        self.movie_detail_language.setText(_translate("main_window", "Language: English"))
        self.movie_detail_genre.setText(_translate("main_window", "Genre : Action, Drama, Horror"))
        self.movie_restrict.setText(_translate("main_window", "PG-13"))
        self.movie_tralier_button.setText(_translate("main_window", "YOUTUBE"))
        self.add_to_list_button.setText(_translate("main_window", "★"))
        self.screens.setTabText(self.screens.indexOf(self.movie_detail_screen), _translate("main_window", "Tab 2"))
        self.screens.setTabText(self.screens.indexOf(self.search_screen), _translate("main_window", "Page"))
        __sortingEnabled = self.movie_lists_gerne.isSortingEnabled()
        self.movie_lists_gerne.setSortingEnabled(False)
        item = self.movie_lists_gerne.item(0)
        item.setText(_translate("main_window", "ACTION"))
        item = self.movie_lists_gerne.item(1)
        item.setText(_translate("main_window", "ADVENTURE"))
        item = self.movie_lists_gerne.item(2)
        item.setText(_translate("main_window", "ANIMATION"))
        item = self.movie_lists_gerne.item(3)
        item.setText(_translate("main_window", "COMEDY"))
        item = self.movie_lists_gerne.item(4)
        item.setText(_translate("main_window", "DRAMA"))
        item = self.movie_lists_gerne.item(5)
        item.setText(_translate("main_window", "FAMILY"))
        item = self.movie_lists_gerne.item(6)
        item.setText(_translate("main_window", "SCIENCE FICTION"))
        item = self.movie_lists_gerne.item(7)
        item.setText(_translate("main_window", "ROMANCE"))
        item = self.movie_lists_gerne.item(8)
        item.setText(_translate("main_window", "HORROR"))
        item = self.movie_lists_gerne.item(9)
        item.setText(_translate("main_window", "MYSTERY"))
        self.movie_lists_gerne.setSortingEnabled(__sortingEnabled)


    def movie_navigation(self, screen):
        return Navigation.screen_navigator(self.screens, screen)


    def detail_screen(self, title):
        Navigation.current_index(self.screens.currentIndex())
        MovieDetail(Region.region_code(self.list_sorting.currentText())).detail_apply(title.text(), self.movie_detail_title, self.movie_detail_poster, self.movie_detail_overview, self.movie_detail_rating, self.movie_detail_releasedate, self.movie_restrict, self.movie_detail_language, self.movie_detail_genre, self.screens)


    def gernes_movies(self, category):
        self.current_gerne = category.text()

        if self.current_gerne != self.next_gerne:
            self.next_gerne = category.text()

            self.movie_lists.clear()
            list_load = GerneListLoad(category.text(), Region.region_code(self.list_sorting.currentText()))
            list_load.thread(self.movie_lists, self.screens)


    def language_change(self, region):
        self.movie_lists.clear()

        movie_region = MovieListLoad(Region.region_code(region))
        movie_region.movie_list_load(self.movie_lists)


    def search_movies(self, movie_name):
        if movie_name.text():
            self.movie_search_lists.clear()

            SearchListLoad(movie_name.text(), Region.region_code(self.list_sorting.currentText())).thread(self.movie_search_lists)
            return self.movie_navigation(2)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
