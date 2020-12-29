#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------
## @file    mQtWidgets/tests/iconLibTest.py [ FILE   ] - Unit test module.
## @package mQtWidgets.tests.iconLibTest    [ MODULE ] - Unit test module.


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
import os
import unittest

import mQtWidgets.iconLib


#-----------------------------------------------------------------------------------------------------
# CODE
#-----------------------------------------------------------------------------------------------------
class DirectoryTest(unittest.TestCase):

    def setUp(self):

        self._iconPath = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                      '..',
                                                      '..',
                                                      '..',
                                                      'resources',
                                                      'icons',
                                                      'dark'))

    def test_getFile(self):

        _icon = mQtWidgets.iconLib.Icon(__file__, mQtWidgets.iconLib.ColorScheme.kDark)

        iconFile = os.path.join(self._iconPath, mQtWidgets.iconLib.FeedbackIcon.kError)

        self.assertEqual(_icon.getFile(mQtWidgets.iconLib.FeedbackIcon.kError, False), iconFile)

    # def test_createIcon(self):
    #
    #     _app = QtWidgets.QApplication(sys.argv)
    #
    #     _window = QtWidgets.QWidget()
    #
    #     _icon = mQtWidgets.iconLib.Icon(__file__, mQtWidgets.iconLib.ColorScheme.kDark)
    #
    #     sys.stdout.write(_icon.createIcon(mQtWidgets.iconLib.FeedbackIcon.kError, False))
    #
    #     _window.show()
    #     _window.close()
    #
    #     sys.exit(_app.exec_())

#
#-----------------------------------------------------------------------------------------------------
# INVOKE
#-----------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    unittest.main()
