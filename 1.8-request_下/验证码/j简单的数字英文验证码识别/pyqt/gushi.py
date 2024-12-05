import sys
from PyQt6.QtWidgets import QApplication ,QMainWindow
# 必须使用两个类: QApplication和QMainWindow。都在PyQt6.QtWidgets。
# 第一个类表示应用程序，第二个类表示窗口(有三种类型QMainWindow，Qwidget)

from Ui_gyshi import Ui_MainWindow #从模块Ui_gyshi.py导入Ui_MainWindow类

if __name__=="__main__":

    #创建QApplication类的实例
    app=QApplication(sys.argv)

    #创建一个QMainWindow对象
    main_window=QMainWindow()

    #将Ui_MainWindow()类实例化
    ui=Ui_MainWindow()

    #在ui中调用setupUi方法，创建初始组件
    ui.setupUi(main_window)

    #创建窗口
    main_window.show()
    
    #进入程序的主循环，并通过exit函数确保主循环安全结束(该释放资源的一定要释放)
    sys.exit(app.exec())