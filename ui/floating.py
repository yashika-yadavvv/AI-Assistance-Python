# ============================================
# JARVIS — FLOATING UI (Wave Style)
# ============================================

import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QTimer
from PyQt5.QtGui import (QFont, QPainter, QColor, QPen,
                          QBrush, QLinearGradient, QRadialGradient, QPainterPath)
from config import ASSISTANT_NAME

class Signals(QObject):
    update_status = pyqtSignal(str)
    update_subtitle = pyqtSignal(str)
    update_color = pyqtSignal(str)

class FloatingUI(QWidget):
    def __init__(self):
        super().__init__()
        self.signals = Signals()
        self.signals.update_status.connect(self.set_status)
        self.signals.update_subtitle.connect(self.set_subtitle)
        self.signals.update_color.connect(self.set_color)
        self.old_pos = None
        self.is_active = False
        self.wave_offset = 0
        self.wave_amplitude = 8
        self.user_text = f"Say '{ASSISTANT_NAME}'..."
        self.ai_text = ""
        self.pulse = 0
        self.pulse_dir = 1

        self.wave_timer = QTimer()
        self.wave_timer.timeout.connect(self.animate)
        self.wave_timer.start(25)

        self.init_ui()

    def init_ui(self):
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(340, 440)

        screen = QApplication.primaryScreen().geometry()
        self.move(screen.width() // 2 - 170, screen.height() - 500)

    def animate(self):
        self.wave_offset += 0.1
        self.pulse += 0.05 * self.pulse_dir
        if self.pulse >= 1: self.pulse_dir = -1
        if self.pulse <= 0: self.pulse_dir = 1
        if self.is_active:
            self.wave_amplitude = min(self.wave_amplitude + 1.2, 30)
        else:
            self.wave_amplitude = max(self.wave_amplitude - 1, 5)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        w, h = self.width(), self.height()



        # === CARD BACKGROUND ===
        card_grad = QLinearGradient(0, 0, w, h)
        card_grad.setColorAt(0.0, QColor(10, 10, 10, 252))
        card_grad.setColorAt(0.5, QColor(18, 16, 5, 252))
        card_grad.setColorAt(1.0, QColor(25, 20, 0, 252))
        painter.setBrush(QBrush(card_grad))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(6, 6, w-12, h-12, 22, 22)

        # === TOP ACCENT LINE ===
        accent_grad = QLinearGradient(20, 0, w-20, 0)
        accent_grad.setColorAt(0, QColor(0, 0, 0, 0))
        accent_grad.setColorAt(0.5, QColor(34, 197, 94, 200))
        accent_grad.setColorAt(1, QColor(0, 0, 0, 0))
        painter.setPen(QPen(QBrush(accent_grad), 2))
        painter.drawLine(30, 18, w-30, 18)

        # === JARVIS LABEL ===
        painter.setFont(QFont("Segoe UI", 7, QFont.Bold))
        painter.setPen(QColor(255, 200, 0, 150))
        painter.drawText(0, 22, w, 20, Qt.AlignCenter,
                         "● J A R V I S   A I ●")

        # === USER TEXT ===
        painter.setFont(QFont("Segoe UI", 10))
        painter.setPen(QColor(255, 255, 255, 210))
        painter.drawText(22, 48, w-44, 90,
                         Qt.AlignLeft | Qt.TextWordWrap,
                         self.user_text)

        # === AI RESPONSE ===
        if self.ai_text:
            # Separator
            sep_grad = QLinearGradient(20, 0, w-20, 0)
            sep_grad.setColorAt(0, QColor(0, 0, 0, 0))
            sep_grad.setColorAt(0.5, QColor(255, 200, 0, 80))
            sep_grad.setColorAt(1, QColor(0, 0, 0, 0))
            painter.setPen(QPen(QBrush(sep_grad), 1))
            painter.drawLine(30, 138, w-30, 138)

            painter.setFont(QFont("Segoe UI", 9))
            painter.setPen(QColor(255, 200, 0, 200))
            painter.drawText(22, 145, w-44, 80,
                             Qt.AlignLeft | Qt.TextWordWrap,
                             f"⚡ {self.ai_text}")

        # === WAVE AREA BACKGROUND ===
        wave_bg = QRadialGradient(w//2, h//2 + 40, 120)
        wave_bg.setColorAt(0, QColor(255, 200, 0, 15))
        wave_bg.setColorAt(1, QColor(0, 0, 0, 0))
        painter.setBrush(QBrush(wave_bg))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(w//2-120, h//2-20, 240, 160)

        # === SOUND WAVES ===
        wave_y = int(h * 0.62)
        waves = [
            (QColor(255, 200, 0), 200, 1.6, 1.0),
            (QColor(255, 255, 255), 80, 2.2, 0.6),
            (QColor(255, 160, 0), 140, 1.0, 0.8),
            (QColor(255, 220, 50), 100, 2.8, 0.4),
        ]
        for color, alpha, freq, amp_mult in waves:
            color.setAlpha(alpha)
            pen = QPen(color, 2)
            pen.setCapStyle(Qt.RoundCap)
            painter.setPen(pen)
            path = QPainterPath()
            for i in range(201):
                x = 28 + (w - 56) * i / 200
                y = wave_y + (self.wave_amplitude * amp_mult) * math.sin(
                    freq * (i / 200 * 3.5 * math.pi + self.wave_offset)
                )
                if i == 0:
                    path.moveTo(x, y)
                else:
                    path.lineTo(x, y)
            painter.drawPath(path)

        # === BOTTOM GLOW ===
        bottom_rad = QRadialGradient(w//2, h-40, 80)
        pulse_alpha = int(40 + self.pulse * 40)
        bottom_rad.setColorAt(0, QColor(255, 200, 0, pulse_alpha))
        bottom_rad.setColorAt(1, QColor(0, 0, 0, 0))
        painter.setBrush(QBrush(bottom_rad))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(w//2-80, h-110, 160, 90)

        # === MIC BUTTON ===
        mic_x, mic_y = w//2, h - 52
        # Outer pulse ring
        ring_alpha = int(30 + self.pulse * 50)
        painter.setBrush(QBrush(QColor(255, 200, 0, ring_alpha)))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(mic_x-32, mic_y-32, 64, 64)
        # Inner circle
        mic_bg = QRadialGradient(mic_x, mic_y, 22)
        mic_bg.setColorAt(0, QColor(34, 197, 94))
        mic_bg.setColorAt(1, QColor(200, 150, 0))
        painter.setBrush(QBrush(mic_bg))
        painter.setPen(QPen(QColor(255, 230, 100, 200), 1))
        painter.drawEllipse(mic_x-22, mic_y-22, 44, 44)
        # Mic icon
        pen = QPen(QColor(10, 10, 10), 2.5)
        pen.setCapStyle(Qt.RoundCap)
        painter.setPen(pen)
        painter.setBrush(Qt.NoBrush)
        painter.drawRoundedRect(mic_x-7, mic_y-15, 14, 20, 7, 7)
        painter.drawArc(mic_x-11, mic_y+3, 22, 14, 0, -180*16)
        painter.drawLine(mic_x, mic_y+17, mic_x, mic_y+22)
        painter.drawLine(mic_x-5, mic_y+22, mic_x+5, mic_y+22)

        # === CLOSE BUTTON ===
        painter.setBrush(QBrush(QColor(255, 200, 0, 20)))
        painter.setPen(QPen(QColor(255, 200, 0, 80), 1))
        painter.drawEllipse(w-42, 26, 24, 24)
        painter.setPen(QPen(QColor(255, 200, 0, 180), 1.5))
        painter.drawLine(w-36, 32, w-25, 43)
        painter.drawLine(w-36, 43, w-25, 32)

        # === BOTTOM ACCENT ===
        painter.setPen(QPen(QBrush(accent_grad), 1))
        painter.drawLine(30, h-18, w-30, h-18)

    def set_status(self, text):
        self.user_text = text
        self.update()

    def set_subtitle(self, text):
        if text and text.startswith("You:"):
            self.user_text = text
            self.ai_text = ""
        elif text and text.startswith("Jarvis:"):
            self.ai_text = text.replace("Jarvis: ", "")
        elif text == "":
            self.ai_text = ""
        self.update()

    def set_color(self, color):
        self.is_active = color != "#22c55e"
        self.update()

    def mousePressEvent(self, event):
        if (self.width()-42 <= event.x() <= self.width()-18 and
                26 <= event.y() <= 50):
            QApplication.quit()
        self.old_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.old_pos:
            delta = event.globalPos() - self.old_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPos()

    def mouseReleaseEvent(self, event):
        self.old_pos = None