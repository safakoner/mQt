#
# Copyright 2020 Safak Oner.
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------
## @file    mQtWidgets/paletteLib.py @brief [ FILE   ] - Custom palettes for Qt widget.
## @package mQtWidgets.paletteLib    @brief [ MODULE ] - Custom palettes for Qt widget.


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from Qt import QtGui, QtWidgets


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ CLASS ] - Dark palette class.
class Dark(QtGui.QPalette):
    #
    # ------------------------------------------------------------------------------------------------
    # PRIVATE METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Constructor.
    #
    #  @exception N/A
    #
    #  @return None - None.
    def __init__(self):

        QtGui.QPalette.__init__(self)

        self.setColor(QtGui.QPalette.Window       , QtGui.QColor(50, 50, 50))
        self.setColor(QtGui.QPalette.Base         , QtGui.QColor(70, 70, 70))

        self.setColor(QtGui.QPalette.Text         , QtGui.QColor(180, 180, 180))
        self.setColor(QtGui.QPalette.WindowText   , QtGui.QColor(180, 180, 180))
        self.setColor(QtGui.QPalette.Foreground   , QtGui.QColor(180, 180, 180))

        self.setColor(QtGui.QPalette.Button       , QtGui.QColor(48 , 48 , 48))
        self.setColor(QtGui.QPalette.ButtonText   , QtGui.QColor(180, 180, 180))

        self.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(0, 0  , 255))
        self.setColor(QtGui.QPalette.ToolTipBase  , QtGui.QColor(0, 255, 0))
        self.setColor(QtGui.QPalette.ToolTipText  , QtGui.QColor(0, 0  , 255))

        self.setColor(QtGui.QPalette.BrightText   , QtGui.QColor(255, 0, 0))
