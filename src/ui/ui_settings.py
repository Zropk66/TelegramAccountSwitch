# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_setting(object):
    def setupUi(self, setting):
        if not setting.objectName():
            setting.setObjectName(u"setting")
        setting.resize(450, 250)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(setting.sizePolicy().hasHeightForWidth())
        setting.setSizePolicy(sizePolicy)
        setting.setMinimumSize(QSize(450, 250))
        setting.setMaximumSize(QSize(450, 250))
        self.centralwidget = QWidget(setting)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.client_edit = QLineEdit(self.centralwidget)
        self.client_edit.setObjectName(u"client_edit")
        self.client_edit.setGeometry(QRect(90, 20, 261, 21))
        self.client_edit.setClearButtonEnabled(False)
        self.client_label = QLabel(self.centralwidget)
        self.client_label.setObjectName(u"client_label")
        self.client_label.setGeometry(QRect(20, 20, 54, 16))
        self.search_client_button = QPushButton(self.centralwidget)
        self.search_client_button.setObjectName(u"search_client_button")
        self.search_client_button.setGeometry(QRect(360, 20, 75, 51))
        self.path_label = QLabel(self.centralwidget)
        self.path_label.setObjectName(u"path_label")
        self.path_label.setGeometry(QRect(20, 50, 54, 16))
        self.path_edit = QLineEdit(self.centralwidget)
        self.path_edit.setObjectName(u"path_edit")
        self.path_edit.setGeometry(QRect(90, 50, 261, 21))
        self.path_edit.setClearButtonEnabled(False)
        self.default_edit = QLineEdit(self.centralwidget)
        self.default_edit.setObjectName(u"default_edit")
        self.default_edit.setGeometry(QRect(90, 80, 261, 21))
        self.default_edit.setClearButtonEnabled(False)
        self.default_label = QLabel(self.centralwidget)
        self.default_label.setObjectName(u"default_label")
        self.default_label.setGeometry(QRect(20, 80, 54, 16))
        self.tags_label = QLabel(self.centralwidget)
        self.tags_label.setObjectName(u"tags_label")
        self.tags_label.setGeometry(QRect(20, 110, 54, 16))
        self.tags_widget = QListWidget(self.centralwidget)
        self.tags_widget.setObjectName(u"tags_widget")
        self.tags_widget.setGeometry(QRect(90, 110, 261, 101))
        self.add_button = QPushButton(self.centralwidget)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setGeometry(QRect(360, 110, 75, 24))
        self.del_button = QPushButton(self.centralwidget)
        self.del_button.setObjectName(u"del_button")
        self.del_button.setGeometry(QRect(360, 140, 75, 24))
        self.finish_button = QPushButton(self.centralwidget)
        self.finish_button.setObjectName(u"finish_button")
        self.finish_button.setGeometry(QRect(360, 215, 75, 24))
        self.log_output = QCheckBox(self.centralwidget)
        self.log_output.setObjectName(u"log_output")
        self.log_output.setGeometry(QRect(360, 180, 82, 20))
        setting.setCentralWidget(self.centralwidget)

        self.retranslateUi(setting)

        QMetaObject.connectSlotsByName(setting)
    # setupUi

    def retranslateUi(self, setting):
        setting.setWindowTitle(QCoreApplication.translate("setting", u"\u8bbe\u7f6e", None))
#if QT_CONFIG(tooltip)
        self.client_edit.setToolTip(QCoreApplication.translate("setting", u"\u5728\u8fd9\u91cc\u8f93\u5165\u4f60\u6240\u4f7f\u7528\u7684Telegram\u5ba2\u6237\u7aef\u540d\u79f0", None))
#endif // QT_CONFIG(tooltip)
        self.client_edit.setPlaceholderText(QCoreApplication.translate("setting", u"\u8bf7\u8f93\u5165\u5ba2\u6237\u7aef\u7684\u540d\u79f0", None))
        self.client_label.setText(QCoreApplication.translate("setting", u"\u5ba2\u6237\u7aef", None))
#if QT_CONFIG(tooltip)
        self.search_client_button.setToolTip(QCoreApplication.translate("setting", u"\u81ea\u52a8\u83b7\u53d6\u5ba2\u6237\u7aef\u540d\u79f0", None))
#endif // QT_CONFIG(tooltip)
        self.search_client_button.setText(QCoreApplication.translate("setting", u"\u81ea\u52a8\u83b7\u53d6", None))
        self.path_label.setText(QCoreApplication.translate("setting", u"\u8def\u5f84", None))
#if QT_CONFIG(tooltip)
        self.path_edit.setToolTip(QCoreApplication.translate("setting", u"\u5728\u8fd9\u91cc\u8f93\u5165\u4f60\u6240\u4f7f\u7528\u7684Telegram\u5ba2\u6237\u7aef\u8def\u5f84", None))
#endif // QT_CONFIG(tooltip)
        self.path_edit.setPlaceholderText(QCoreApplication.translate("setting", u"\u8bf7\u8f93\u5165\u5ba2\u6237\u7aef\u8def\u5f84", None))
#if QT_CONFIG(tooltip)
        self.default_edit.setToolTip(QCoreApplication.translate("setting", u"\u5728\u8fd9\u91cc\u8f93\u5165\u9ed8\u8ba4\u767b\u5f55\u7684\u8d26\u6237\u6807\u7b7e", None))
#endif // QT_CONFIG(tooltip)
        self.default_edit.setPlaceholderText(QCoreApplication.translate("setting", u"\u8bf7\u8f93\u5165\u9ed8\u8ba4\u8d26\u6237\u6807\u7b7e", None))
        self.default_label.setText(QCoreApplication.translate("setting", u"\u9ed8\u8ba4", None))
        self.tags_label.setText(QCoreApplication.translate("setting", u"\u53c2\u6570", None))
#if QT_CONFIG(tooltip)
        self.tags_widget.setToolTip(QCoreApplication.translate("setting", u"\u5728\u8fd9\u91cc\u6dfb\u52a0\u5907\u7528\u767b\u5f55\u7684\u8d26\u6237\u6807\u7b7e", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.add_button.setToolTip(QCoreApplication.translate("setting", u"\u6dfb\u52a0\u53c2\u6570", None))
#endif // QT_CONFIG(tooltip)
        self.add_button.setText(QCoreApplication.translate("setting", u"\u6dfb\u52a0", None))
#if QT_CONFIG(tooltip)
        self.del_button.setToolTip(QCoreApplication.translate("setting", u"\u5220\u9664\u53c2\u6570", None))
#endif // QT_CONFIG(tooltip)
        self.del_button.setText(QCoreApplication.translate("setting", u"\u5220\u9664", None))
#if QT_CONFIG(tooltip)
        self.finish_button.setToolTip(QCoreApplication.translate("setting", u"\u4fdd\u5b58\u914d\u7f6e", None))
#endif // QT_CONFIG(tooltip)
        self.finish_button.setText(QCoreApplication.translate("setting", u"\u4fdd\u5b58", None))
#if QT_CONFIG(tooltip)
        self.log_output.setToolTip(QCoreApplication.translate("setting", u"\u63a7\u5236\u65e5\u5fd7\u662f\u5426\u5199\u5165\u5230\u6587\u4ef6", None))
#endif // QT_CONFIG(tooltip)
        self.log_output.setText(QCoreApplication.translate("setting", u"\u65e5\u5fd7\u8f93\u51fa", None))
    # retranslateUi

