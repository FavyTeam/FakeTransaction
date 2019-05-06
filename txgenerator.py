from pyforms import settings as formSettings

formSettings.PYFORMS_STYLESHEET = "style.css"

import pyforms

from   pyforms.basewidget import BaseWidget
from   pyforms.controls import ControlText
from   pyforms.controls import ControlButton

class TxGenerator(BaseWidget):

    def __init__(self):
        super(TxGenerator,self).__init__('TxGenerator 1.0')
        self.setupUI()
    
    def setupUI(self) :
        #Definition of the forms fields
        self._firstname  = ControlText('First name', 'Default value')
        self._middlename = ControlText('Middle name')
        self._lastname   = ControlText('Lastname name')
        self._fullname   = ControlText('Full name')
        self._button     = ControlButton('Press this button')
        

#Execute the application
if __name__ == "__main__": pyforms.start_app( TxGenerator )
