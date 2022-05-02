from PySide2.QtCore import QElapsedTimer, QCoreApplication


def qt_sleep(millis: int):
    timer = QElapsedTimer()
    timer.start()
    while timer.elapsed() < millis:
        QCoreApplication.processEvents()
