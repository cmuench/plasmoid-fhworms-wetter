# -*- coding: iso-8859-15 -*

from PyQt4.QtCore import QLocale, QTranslator
from PyQt4.QtGui import *
from PyKDE4.plasma import Plasma
from PyKDE4 import plasmascript
from service.weather import MeasurementReader

class FHWormsWetterApplet(plasmascript.Applet):
    def __init__(self, parent, args=None):
        plasmascript.Applet.__init__(self, parent)
        self.reader = MeasurementReader()
        self.width = 200            
        self.height = 100        
    
    def _create_temperture_row(self):
        # Temperature
        self.temperatureLabel = Plasma.Label(self.applet)
        self.temperatureLabel.setText(self.tr('Temperature:'))
        self.layout.addItem(self.temperatureLabel, 0, 0)
        self.temperatureValue = Plasma.Label(self.applet)
        self.layout.addItem(self.temperatureValue, 0, 1)    

    def _create_wind_row(self):
        # Wind
        self.windLabel = Plasma.Label(self.applet)
        self.windLabel.setText(self.tr('Wind:'))
        self.layout.addItem(self.windLabel, 1, 0)
        self.windValue = Plasma.Label(self.applet)
        self.layout.addItem(self.windValue, 1, 1)

    def _create_pressure_row(self):
        # Pressure
        self.pressureLabel = Plasma.Label(self.applet)
        self.pressureLabel.setText(self.tr('Pressure:'))
        self.layout.addItem(self.pressureLabel, 2, 0)
        self.pressureValue = Plasma.Label(self.applet)
        self.layout.addItem(self.pressureValue, 2, 1)

    def _init_translations(self):
        # Translation system        
        self.locale = QLocale.system().name()
        self.translator = QTranslator()
        if self.translator.load('lang_' + self.locale, ':/'):
            QApplication.installTranslator(self.translator)

    def init(self):
        """
        Init's applet
        """
        self.setHasConfigurationInterface(False)

        self.theme = Plasma.Svg(self)
        self.theme.setImagePath('images/background')
        self.setBackgroundHints(Plasma.Applet.DefaultBackground)
        self.setAspectRatioMode(Plasma.IgnoreAspectRatio)

        self._init_translations()
        self.layout = QGraphicsGridLayout(self.applet)
        self._create_temperture_row()
        self._create_wind_row()
        self._create_pressure_row()
        self.setLayout(self.layout)
        self.resize(self.width, self.height)
        self.update_gui()
        self.time = self.startTimer(60000)

    def update_gui(self):
        """
        Update GUI elements (triggered by timer)
        """
        try:
            data = self.reader.read()
            self.temperatureValue.setText("%s °C" % data.temperature)
            self.pressureValue.setText("%s hPa" % data.pressure)
            self.windValue.setText("%s Km/h %s" % (data.wind_speed, data.wind_direction))
        except Exception:
            self.temperatureValue.setText("%s °C" % '-')
            self.pressureValue.setText("%s hPa" % '-')
            self.windValue.setText("%s Km/h %s" % '-')
            
    def timerEvent(self, event):
        """
        Timer event of applet
        """
        self.update_gui()

def CreateApplet(parent):
    return FHWormsWetterApplet(parent)