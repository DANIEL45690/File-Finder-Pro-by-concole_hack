#!/usr/bin/env python3
"""File Finder Pro by @concole_hack"""

import sys
import os
import subprocess
import time
import ctypes
from pathlib import Path

def install_dependencies():
    try:
        import PySide6
        return "PySide6"
    except ImportError:
        print("╔════════════════════════════════════════╗")
        print("║   Installing PySide6...               ║")
        print("╚════════════════════════════════════════╝")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
            subprocess.check_call([sys.executable, "-m", "pip", "install", "PySide6"])
            import PySide6
            return "PySide6"
        except:
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "PyQt6"])
                import PyQt6
                return "PyQt6"
            except:
                print("Failed to install Qt. Please install manually: pip install PySide6")
                sys.exit(1)

QT_API = install_dependencies()

if QT_API == "PySide6":
    from PySide6 import QtCore, QtGui, QtWidgets
    from PySide6.QtCore import Signal, Slot, Qt, QThread, QTimer
    from PySide6.QtGui import QFont, QFontDatabase, QPalette, QColor, QLinearGradient, QBrush, QAction
    from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QTextEdit, QFrame, QProgressBar, QMessageBox
elif QT_API == "PyQt6":
    from PyQt6 import QtCore, QtGui, QtWidgets
    from PyQt6.QtCore import pyqtSignal as Signal, pyqtSlot as Slot, Qt, QThread, QTimer
    from PyQt6.QtGui import QFont, QFontDatabase, QPalette, QColor, QLinearGradient, QBrush, QAction
    from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QTextEdit, QFrame, QProgressBar, QMessageBox

if os.name == 'nt':
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("filefinderpro")

STYLESHEET = """
QMainWindow {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #0a0e1a, stop:0.3 #141b2b, stop:0.7 #1a1f2f, stop:1 #0f1322);
}

#glassCard {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 rgba(255,255,255,0.12), stop:0.5 rgba(255,255,255,0.06), stop:1 rgba(255,255,255,0.02));
    border: 1px solid qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 rgba(255,255,255,0.25), stop:0.5 rgba(255,255,255,0.12), stop:1 rgba(255,255,255,0.05));
    border-radius: 24px;
    padding: 20px;
}

#glassCard:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 rgba(255,255,255,0.15), stop:0.5 rgba(255,255,255,0.08), stop:1 rgba(255,255,255,0.03));
    border: 1px solid qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #00f5ff, stop:0.5 #667eea, stop:1 #a855f7);
}

#titleLabel {
    font-size: 42px;
    font-weight: 900;
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #00f5ff, stop:0.3 #667eea, stop:0.7 #a855f7, stop:1 #00f5ff);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    letter-spacing: 2px;
    margin: 5px 0;
}

QPushButton {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 rgba(255,255,255,0.12), stop:0.5 rgba(255,255,255,0.06), stop:1 rgba(255,255,255,0.02));
    border: 1px solid qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 rgba(255,255,255,0.2), stop:0.5 rgba(255,255,255,0.1), stop:1 rgba(255,255,255,0.05));
    border-radius: 18px;
    padding: 12px 24px;
    color: white;
    font-weight: 700;
    font-size: 14px;
    letter-spacing: 1px;
    text-transform: uppercase;
}

QPushButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 rgba(255,255,255,0.18), stop:0.5 rgba(255,255,255,0.1), stop:1 rgba(255,255,255,0.05));
    border: 1px solid qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #00f5ff, stop:0.5 #667eea, stop:1 #a855f7);
    box-shadow: 0 0 25px rgba(0,245,255,0.3);
}

QPushButton:pressed {
    transform: translateY(2px);
}

#searchBtn, #openBtn {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #00f5ff, stop:0.3 #667eea, stop:0.7 #a855f7, stop:1 #00f5ff);
    border: none;
    font-weight: 800;
    min-width: 180px;
    box-shadow: 0 0 30px rgba(0,245,255,0.4);
}

#searchBtn:hover, #openBtn:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #00ffff, stop:0.3 #7c8eff, stop:0.7 #b86aff, stop:1 #00ffff);
    box-shadow: 0 0 45px rgba(0,245,255,0.7);
}

QLineEdit {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 rgba(0,0,0,0.4), stop:0.5 rgba(0,0,0,0.3), stop:1 rgba(0,0,0,0.4));
    border: 1px solid qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 rgba(255,255,255,0.2), stop:0.5 rgba(255,255,255,0.1), stop:1 rgba(255,255,255,0.05));
    border-radius: 18px;
    padding: 14px 20px;
    color: white;
    font-size: 15px;
}

QLineEdit:focus {
    border: 2px solid qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #00f5ff, stop:0.5 #667eea, stop:1 #a855f7);
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 rgba(0,0,0,0.5), stop:0.5 rgba(0,0,0,0.4), stop:1 rgba(0,0,0,0.5));
}

QLineEdit::placeholder {
    color: rgba(255,255,255,0.4);
    font-style: italic;
}

QTextEdit {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 rgba(0,0,0,0.4), stop:0.5 rgba(0,0,0,0.3), stop:1 rgba(0,0,0,0.4));
    border: 1px solid qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 rgba(255,255,255,0.15), stop:0.5 rgba(255,255,255,0.08), stop:1 rgba(255,255,255,0.03));
    border-radius: 18px;
    padding: 18px;
    color: white;
    font-family: 'Consolas', monospace;
    font-size: 13px;
    max-height: 200px;
}

QListWidget {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 rgba(0,0,0,0.3), stop:0.5 rgba(0,0,0,0.2), stop:1 rgba(0,0,0,0.3));
    border: 1px solid qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 rgba(255,255,255,0.15), stop:0.5 rgba(255,255,255,0.08), stop:1 rgba(255,255,255,0.03));
    border-radius: 18px;
    padding: 8px;
    color: white;
    font-size: 13px;
}

QListWidget::item {
    padding: 12px 16px;
    border-radius: 12px;
    margin: 4px;
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 rgba(255,255,255,0.03), stop:0.5 rgba(255,255,255,0.01), stop:1 rgba(255,255,255,0.03));
}

QListWidget::item:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 rgba(0,245,255,0.15), stop:0.5 rgba(102,126,234,0.1), stop:1 rgba(168,85,247,0.15));
    transform: translateX(3px);
}

QListWidget::item:selected {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #00f5ff, stop:0.5 #667eea, stop:1 #a855f7);
    color: white;
    font-weight: 600;
}

#statusLabel {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 rgba(0,245,255,0.15), stop:0.5 rgba(102,126,234,0.1), stop:1 rgba(168,85,247,0.15));
    border: 1px solid qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #00f5ff, stop:0.5 #667eea, stop:1 #a855f7);
    border-radius: 16px;
    padding: 10px 20px;
    color: white;
    font-weight: 600;
    font-size: 14px;
    min-width: 200px;
}

QProgressBar {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 rgba(0,0,0,0.4), stop:0.5 rgba(0,0,0,0.3), stop:1 rgba(0,0,0,0.4));
    border: 1px solid qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 rgba(255,255,255,0.15), stop:0.5 rgba(255,255,255,0.08), stop:1 rgba(255,255,255,0.03));
    border-radius: 12px;
    text-align: center;
    color: white;
    min-height: 22px;
    max-width: 250px;
}

QProgressBar::chunk {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #00f5ff, stop:0.4 #667eea, stop:0.7 #a855f7, stop:1 #00f5ff);
    border-radius: 12px;
}

QScrollBar:vertical {
    background: rgba(0,0,0,0.2);
    border-radius: 8px;
    width: 10px;
}

QScrollBar::handle:vertical {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #00f5ff, stop:1 #667eea);
    border-radius: 8px;
    min-height: 25px;
}

QScrollBar::handle:vertical:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #00ffff, stop:1 #7c8eff);
}
"""

class SearchWorker(QThread):
    result_found = Signal(str, str)
    finished = Signal(int)
    status = Signal(str)
    
    def __init__(self):
        super().__init__()
        self.search_term = ""
        self.search_path = "C:\\"
        self.running = True
        
    def setup(self, term, path):
        self.search_term = term.lower()
        self.search_path = path
        self.running = True
        
    def stop(self):
        self.running = False
        
    def run(self):
        count = 0
        try:
            for root, dirs, files in os.walk(self.search_path):
                if not self.running:
                    break
                    
                self.status.emit(f"📁 {os.path.basename(root)[:30]}")
                
                for file in files:
                    if not self.running:
                        break
                        
                    if self.search_term in file.lower():
                        full = os.path.join(root, file)
                        self.result_found.emit(file, full)
                        count += 1
                        
                if len(dirs) > 20:
                    dirs[:] = dirs[:15]
                    
                QThread.msleep(1)
                
        except Exception as e:
            self.status.emit(f"⚠️ Error")
            
        self.finished.emit(count)

class FileFinderPro(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🔍 File Finder Pro by @concole_hack")
        self.setMinimumSize(1200, 700)
        self.resize(1400, 800)
        
        self.results = []
        self.worker = SearchWorker()
        self.worker.result_found.connect(self.add_result)
        self.worker.finished.connect(self.search_finished)
        self.worker.status.connect(self.update_status)
        
        self.setup_ui()
        self.setup_menu()
        self.center_window()
        
    def setup_menu(self):
        menubar = self.menuBar()
        menubar.setStyleSheet("""
            QMenuBar {
                background: transparent;
                color: white;
                spacing: 10px;
                padding: 5px;
            }
            QMenuBar::item {
                padding: 8px 15px;
                border-radius: 10px;
                background: rgba(255,255,255,0.05);
            }
            QMenuBar::item:selected {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #00f5ff, stop:1 #667eea);
                color: white;
            }
            QMenu {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #0a0e1a, stop:1 #1a1f2f);
                color: white;
                border: 1px solid rgba(255,255,255,0.1);
                border-radius: 12px;
                padding: 8px;
            }
            QMenu::item {
                padding: 8px 25px;
                border-radius: 8px;
            }
            QMenu::item:selected {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #00f5ff, stop:1 #667eea);
            }
        """)
        
        file_menu = menubar.addMenu("📁 File")
        
        fullscreen_action = QAction("🔲 Full Screen", self)
        fullscreen_action.setShortcut("F11")
        fullscreen_action.triggered.connect(self.toggle_fullscreen)
        file_menu.addAction(fullscreen_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction("❌ Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        view_menu = menubar.addMenu("👁️ View")
        
        compact_action = QAction("📏 Compact Mode", self)
        compact_action.setShortcut("Ctrl+M")
        compact_action.triggered.connect(self.toggle_compact)
        view_menu.addAction(compact_action)
        
        view_menu.addSeparator()
        
        always_top_action = QAction("📌 Always on Top", self)
        always_top_action.setCheckable(True)
        always_top_action.triggered.connect(self.toggle_always_top)
        view_menu.addAction(always_top_action)
        
        help_menu = menubar.addMenu("❓ Help")
        
        about_action = QAction("ℹ️ About", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
        
    def toggle_fullscreen(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()
            
    def toggle_compact(self):
        if self.width() > 1000:
            self.resize(1000, 600)
        else:
            self.resize(1400, 800)
            
    def toggle_always_top(self, checked):
        if checked:
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        else:
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowStaysOnTopHint)
        self.show()
        
    def show_about(self):
        QMessageBox.about(self, "About File Finder Pro",
            "<h2>🔍 File Finder Pro</h2>"
            "<p>Version 1.0</p>"
            "<p>Created by @concole_hack</p>"
            "<p>A powerful file search utility with beautiful glassmorphism design.</p>"
            "<p>Features:</p>"
            "<ul>"
            "<li>Fast file searching</li>"
            "<li>Glass morphic UI</li>"
            "<li>Full screen support</li>"
            "<li>Always on top mode</li>"
            "</ul>")
        
    def setup_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        main = QVBoxLayout(central)
        main.setContentsMargins(25, 25, 25, 25)
        main.setSpacing(20)
        
        title = QLabel("FILE FINDER PRO")
        title.setObjectName("titleLabel")
        title.setAlignment(Qt.AlignCenter)
        main.addWidget(title)
        
        search_card = QFrame()
        search_card.setObjectName("glassCard")
        search_layout = QVBoxLayout(search_card)
        search_layout.setSpacing(15)
        
        input_row = QHBoxLayout()
        input_row.setSpacing(15)
        
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("🔍 Enter filename...")
        self.search_input.returnPressed.connect(self.start_search)
        input_row.addWidget(self.search_input)
        
        self.search_btn = QPushButton("🔍 SEARCH")
        self.search_btn.setObjectName("searchBtn")
        self.search_btn.clicked.connect(self.start_search)
        input_row.addWidget(self.search_btn)
        
        search_layout.addLayout(input_row)
        
        path_row = QHBoxLayout()
        path_row.setSpacing(15)
        
        path_label = QLabel("📁 Path:")
        path_label.setStyleSheet("font-size: 14px; font-weight: 600;")
        
        self.path_input = QLineEdit("C:\\")
        self.path_input.setPlaceholderText("Search path...")
        path_row.addWidget(path_label)
        path_row.addWidget(self.path_input)
        
        search_layout.addLayout(path_row)
        main.addWidget(search_card)
        
        content = QHBoxLayout()
        content.setSpacing(20)
        
        left = QWidget()
        left_layout = QVBoxLayout(left)
        left_layout.setContentsMargins(0, 0, 0, 0)
        
        list_label = QLabel("📋 Results:")
        list_label.setStyleSheet("font-size: 15px; font-weight: 600; margin: 5px 0;")
        left_layout.addWidget(list_label)
        
        self.results_list = QListWidget()
        self.results_list.itemDoubleClicked.connect(self.open_file)
        self.results_list.currentItemChanged.connect(self.show_path)
        left_layout.addWidget(self.results_list)
        
        content.addWidget(left, 2)
        
        right = QWidget()
        right_layout = QVBoxLayout(right)
        right_layout.setContentsMargins(0, 0, 0, 0)
        
        path_label2 = QLabel("📍 Path:")
        path_label2.setStyleSheet("font-size: 15px; font-weight: 600; margin: 5px 0;")
        right_layout.addWidget(path_label2)
        
        path_card = QFrame()
        path_card.setObjectName("glassCard")
        path_layout = QVBoxLayout(path_card)
        
        self.path_display = QTextEdit()
        self.path_display.setReadOnly(True)
        self.path_display.setPlaceholderText("File path...")
        path_layout.addWidget(self.path_display)
        
        right_layout.addWidget(path_card)
        content.addWidget(right, 1)
        
        main.addLayout(content)
        
        status_card = QFrame()
        status_card.setObjectName("glassCard")
        status_row = QHBoxLayout(status_card)
        status_row.setSpacing(15)
        
        self.status_label = QLabel("✨ Ready")
        self.status_label.setObjectName("statusLabel")
        status_row.addWidget(self.status_label)
        
        self.progress = QProgressBar()
        self.progress.setVisible(False)
        status_row.addWidget(self.progress)
        
        status_row.addStretch()
        
        self.open_btn = QPushButton("📁 OPEN")
        self.open_btn.setObjectName("openBtn")
        self.open_btn.clicked.connect(self.open_selected)
        self.open_btn.setEnabled(False)
        status_row.addWidget(self.open_btn)
        
        main.addWidget(status_card)
        
    def center_window(self):
        screen = QApplication.primaryScreen().geometry()
        self.move(
            (screen.width() - self.width()) // 2,
            (screen.height() - self.height()) // 2
        )
        
    def start_search(self):
        term = self.search_input.text().strip()
        if not term:
            QMessageBox.warning(self, "Error", "Enter filename!")
            return
            
        path = self.path_input.text().strip() or "C:\\"
        if not os.path.exists(path):
            QMessageBox.warning(self, "Error", f"Path not found: {path}")
            return
            
        if self.worker.isRunning():
            self.worker.stop()
            self.worker.wait()
            
        self.results_list.clear()
        self.results = []
        self.path_display.clear()
        self.open_btn.setEnabled(False)
        
        self.progress.setVisible(True)
        self.progress.setRange(0, 0)
        self.search_btn.setEnabled(False)
        self.status_label.setText("🔍 Searching...")
        
        self.worker.setup(term, path)
        self.worker.start()
        
    def add_result(self, filename, full_path):
        name = filename[:40] + "..." if len(filename) > 40 else filename
        item = QtWidgets.QListWidgetItem(f"📄 {name}")
        item.setData(Qt.UserRole, full_path)
        self.results_list.addItem(item)
        self.results.append(full_path)
        
    def search_finished(self, count):
        self.progress.setVisible(False)
        self.search_btn.setEnabled(True)
        if count > 0:
            self.status_label.setText(f"✅ Found: {count}")
        else:
            self.status_label.setText("❌ Not found")
            
    def update_status(self, text):
        self.status_label.setText(text)
        
    def show_path(self, current, previous):
        if current:
            path = current.data(Qt.UserRole)
            self.path_display.setText(path)
            self.open_btn.setEnabled(True)
            
    def open_file(self, item):
        path = item.data(Qt.UserRole)
        if path and os.path.exists(path):
            if os.name == 'nt':
                os.startfile(path)
            else:
                subprocess.Popen(['open', path])
                
    def open_selected(self):
        item = self.results_list.currentItem()
        if item:
            path = item.data(Qt.UserRole)
            if path and os.path.exists(path):
                if os.name == 'nt':
                    subprocess.Popen(f'explorer /select,"{path}"')
                else:
                    subprocess.Popen(['open', '-R', path])
                    
    def closeEvent(self, event):
        if self.worker.isRunning():
            self.worker.stop()
            self.worker.wait()
        event.accept()

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    app.setStyleSheet(STYLESHEET)
    
    font = app.font()
    font.setPointSize(9)
    app.setFont(font)
    
    window = FileFinderPro()
    window.show()
    
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

