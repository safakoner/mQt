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
## @file    mQtWidgets/iconLib.py @brief [ FILE   ] - Operate on icons.
## @package mQtWidgets.iconLib    @brief [ MODULE ] - Operate on icons.


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
import  os

from    Qt import QtGui, QtWidgets

import  mCore.enumAbs
import  mCore.platformLib

import  mFileSystem.directoryLib

import  mMecoPackage.enumLib
import  mMecoPackage.packageLib


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ ENUM CLASS ] - Color schemes.
class ColorScheme(mCore.enumAbs.Enum):

    ## [ str ] - Dark.
    kDark = 'dark'

#
## @brief [ ENUM CLASS ] - Common icons.
class CommonIcon(mCore.enumAbs.Enum):

    ## [ str ] - N/A.
    kNA = 'commonNA.png'

#
## @brief [ ENUM CLASS ] - Name of the icons.
class PlatformIcon(mCore.enumAbs.Enum):

    ## [ str ] - Mac.
    kDarwin  = 'platformDarwin.png'

    ## [ str ] - Linux.
    kLinux   = 'platformLinux.png'

    ## [ str ] - Windows.
    kWindows = 'platformWindows.png'

#
## @brief [ ENUM CLASS ] - Programming language icons.
class LanguageIcon(mCore.enumAbs.Enum):

    ## [ str ] - Python.
    kPython = 'languagePython.png'

    ## [ str ] - C++.
    kCPP    = 'languageCPP.png'

#
## @brief [ ENUM CLASS ] - File menu icons.
class FileMenuIcon(mCore.enumAbs.Enum):

    ## [ str ] - File new.
    kNew      = 'fileMenuNew.png'

    ## [ str ] - File open.
    kOpen     = 'fileMenuOpen.png'

    ## [ str ] - File save.
    kSave     = 'fileMenuSave.png'

    ## [ str ] - File save as.
    kSaveAs   = 'fileMenuSaveAs.png'

    ## [ str ] - File Exit.
    kExit     = 'fileMenuExit.png'

#
## @brief [ ENUM CLASS ] - Edit menu icons.
class EditMenuIcon(mCore.enumAbs.Enum):

    ## [ str ] - Delete all.
    kDeleteAll      = 'editMenuDeleteAll.png'

    ## [ str ] - Delete selected.
    kDeleteSelected = 'editMenuDeleteSelected.png'

    ## [ str ] - Refresh.
    kRefresh        = 'editMenuRefresh.png'

#
## @brief [ ENUM CLASS ] - Tab menu icons.
class TabMenuIcon(mCore.enumAbs.Enum):

    ## [ str ] - Tabify right.
    kTabifyRight    = 'tabMenuTabifyRight.png'

    ## [ str ] - Tabify left.
    kTabifyLeft     = 'tabMenuTabifyLeft.png'

#
## @brief [ ENUM CLASS ] - Help menu icons.
class HelpMenuIcon(mCore.enumAbs.Enum):

    ## [ str ] - Help.
    kHelp  = 'helpMenuHelp.png'

    ## [ str ] - About.
    kAbout = 'helpMenuAbout.png'

#
## @brief [ ENUM CLASS ] - Feedback icons.
class FeedbackIcon(mCore.enumAbs.Enum):

    ## [ str ] - Info.
    kInfo    = 'feedbackInfo.png'

    ## [ str ] - Success.
    kSuccess = 'feedbackSuccess.png'

    ## [ str ] - Warning.
    kWarning = 'feedbackWarning.png'

    ## [ str ] - Error.
    kError   = 'feedbackError.png'

#
## @brief [ ENUM CLASS ] - Splitter icons.
class SplitterIcon(mCore.enumAbs.Enum):

    ## [ str ] - Left.
    kLeft    = 'splitterLeft.png'

    ## [ str ] - Bottom.
    kBottom  = 'splitterBottom.png'

    ## [ str ] - Right.
    kRight   = 'splitterRight.png'

#
## @brief [ ENUM CLASS ] - Animated icons.
class AnimatedIcon(mCore.enumAbs.Enum):

    ## [ str ] - Activity.
    kActivity = 'animatedActivity.gif'

#
## @brief [ ENUM CLASS ] - Dot icons.
class DotIcon(mCore.enumAbs.Enum):

    ## [ str ] - Green.
    kGreen        = 'dotGreen.png'

    ## [ str ] - Yellow.
    kYellow       = 'dotYellow.png'

    ## [ str ] - Yellow hollow.
    kYellowHollow = 'dotYellowHollow.png'

    ## [ str ] - Red.
    kRed          = 'dotRed.png'

#
## @brief [ ENUM CLASS ] - Media icons.
class MediaIcon(mCore.enumAbs.Enum):

    ## [ str ] - Play.
    kPlay         = 'mediaPlay.png'

#
## @brief [ ENUM CLASS ] - File extension icons.
class FileExtensionIcon(mCore.enumAbs.Enum):

    ## [ str ] - File.
    kFile         = 'fileExtFILE.png'

    ## [ str ] - CSS.
    kCSS          = 'fileExtCSS.png'

    ## [ str ] - HTML.
    kHTML         = 'fileExtHTML.png'

    ## [ str ] - JavaScript.
    kJavaScript   = 'fileExtJS.png'

    ## [ str ] - Maya Ascii.
    kMayaAscii    = 'fileExtMA.png'

    ## [ str ] - Maya Binary.
    kMayaBinary   = 'fileExtMB.png'

    ## [ str ] - Nuke.
    kNuke         = 'fileExtNK.png'

    ## [ str ] - Photoshop.
    kPhotoshop    = 'fileExtPSD.png'

    ## [ str ] - Python.
    kPython       = 'fileExtPY.png'

#
#
#
## @brief [ CLASS ] - Class offers functionalities to find and create icons.
class Icon(object):
    #
    # ------------------------------------------------------------------------------------------------
    # PUBLIC STATIC MEMBERS
    # ------------------------------------------------------------------------------------------------
    #
    ## [ str ] - Icon file extension.
    ICON_FILE_EXTENSION = 'png'

    #
    # ------------------------------------------------------------------------------------------------
    # PRIVATE METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Constructor.
    #
    #  @param path         [ str  | None                                      | in  ] - Absolute path of the python module where this class is being used (i.e. __file__).
    #  @param colorScheme  [ enum | mQtWidgets.iconLib.Icon.ColorScheme.kDark | in  ] - Color scheme from mQtWidgets.iconLib.Icon.ColorScheme enum class.
    #
    #  @exception N/A
    #
    #  @return None - None.
    def __init__(self, path=None, colorScheme=ColorScheme.kDark):

        ## [ str ] - Color scheme.
        self._colorScheme = colorScheme

        ## [ str ] - Built-in icon path (mQtWidgets/resources/icons).
        self._builtInIconPath = mFileSystem.directoryLib.Directory.join(mFileSystem.directoryLib.Directory.navigateUp(__file__, level=3),
                                                                        mMecoPackage.enumLib.PackageFolderStructure.kResourcesIcons)

        packagePath = None
        if path:
            packagePath = mMecoPackage.packageLib.Package(path=path).path()

        if packagePath:
            ## [ str ] - Local package icon path (packageName/resources/icons).
            self._packageIconPath = mFileSystem.directoryLib.Directory.join(packagePath,
                                                                            mMecoPackage.enumLib.PackageFolderStructure.kResourcesIcons)
        else:
            self._packageIconPath = self._builtInIconPath

    #
    # ------------------------------------------------------------------------------------------------
    # PROPERTY METHODS
    # ------------------------------------------------------------------------------------------------
    ## @name PROPERTIES

    ## @{
    #
    ## @brief Built-in icon path.
    #
    #  @exception N/A
    #
    #  @return str - Absolute path.
    def builtInIconPath(self):

        return self._builtInIconPath

    #
    ## @brief Package icon path.
    #
    #  @exception N/A
    #
    #  @return str - Absolute path.
    def packageIconPath(self):

        return self._packageIconPath

    #
    ## @}

    # ------------------------------------------------------------------------------------------------
    # PUBLIC METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Get absolute path of the given icon file.
    #
    #  Method first checks whether given fileName is a file, then checks local package and then
    #  checks built-in icon location for in order to retrieve the icon.
    #
    #  @param fileName [ str  | None | in  ] - Absolute path or name of the icon file.
    #  @param useNA    [ bool | True | in  ] - Use "Not Applicable" icon if icon with fileName doesn't exist.
    #
    #  @exception N/A
    #
    #  @return str  - Absolute path of the icon file.
    #  @return None - If icon file doesn't exist.
    def getFile(self, fileName, useNA=True):

        if not fileName and useNA:
            fileName = CommonIcon.kNA

        if not os.path.splitext(fileName)[1]:
            fileName = '{}.{}'.format(fileName, Icon.ICON_FILE_EXTENSION)

        if os.path.isfile(fileName):
            return fileName

        icon = mFileSystem.directoryLib.Directory.join(self._packageIconPath, self._colorScheme, fileName)
        if os.path.isfile(icon):
            return icon

        icon = mFileSystem.directoryLib.Directory.join(self._builtInIconPath, self._colorScheme, fileName)

        if os.path.isfile(icon):
            return icon

        return None

    #
    ## @brief Create and return an QIcon instance for the given icon file.
    #
    #  Method first checks whether given fileName is a file, then checks local package and then
    #  checks built-in icon location in order to retrieve the icon.
    #
    #  @param fileName [ str  | None | in  ] - Absolute path or name of the icon file.
    #  @param useNA    [ bool | True | in  ] - Use "Not Applicable" icon if icon with fileName doesn't exist.
    #
    #  @exception N/A
    #
    #  @return QIcon - QIcon instance.
    def createIcon(self, fileName, useNA=True):

        iconFile = self.getFile(fileName, useNA)
        if iconFile:
            return QtGui.QIcon(iconFile)

        return QtGui.QIcon()

    #
    ## @brief Create and return a QPixmap instance for the given icon file.
    #
    #  Method first checks whether given fileName is a file, then checks local package and then
    #  checks built-in icon location in order to retrieve the icon.
    #
    #  @param fileName [ str  | None | in  ] - Absolute path or name of the icon file.
    #  @param useNA    [ bool | True | in  ] - Use "Not Applicable" icon if icon with fileName doesn't exist.
    #
    #  @exception N/A
    #
    #  @return QPixmap - QPixmap instance.
    def createPixmap(self, fileName, useNA=True):

        iconFile = self.getFile(fileName, useNA)

        if iconFile:
            return QtWidgets.QPixmap(iconFile)

        return QtWidgets.QPixmap()

    #
    ## @brief Create QIcon instance for the given file's extension.
    #
    #  Method first checks whether given fileName is a file, then checks local package and then
    #  checks built-in icon location in order to retrieve the icon.
    #
    #  @param fileName [ str  | None | in  ] - Absolute path or name of the icon file.
    #  @param useNA    [ bool | True | in  ] - Use "Not Applicable" icon if icon with fileName doesn't exist.
    #
    #  @exception N/A
    #
    #  @return QIcon - QIcon instance.
    def createIconForFileExtension(self, fileName, useNA=True):

        extension = os.path.splitext(fileName)[1]
        if not extension:
            extension = 'file'

        if extension.startswith('.'):
            extension = extension[1:]

        return self.createIcon('fileExt{}.png'.format(extension.upper()), useNA)

    #
    ## @brief Create QPixmap instance for the given file's extension.
    #
    #  Method first checks whether given fileName is a file, then checks local package and then
    #  checks built-in icon location in order to retrieve the icon.
    #
    #  @param fileName [ str  | None | in  ] - Absolute path or name of the icon file.
    #  @param useNA    [ bool | True | in  ] - Use "Not Applicable" icon if icon with fileName doesn't exist.
    #
    #  @exception N/A
    #
    #  @return None - None.
    def createPixmapForFileExtension(self, fileName, useNA=True):

        extension = os.path.splitext(fileName)[1]
        if not extension:
            extension = 'file'

        if extension.startswith('.'):
            extension = extension[1:]

        return self.createPixmap('fileExt{}.png'.format(extension.upper()), useNA)

    #
    ## @brief Create and return an QIcon instance for the given platform.
    #
    #  If platformIcon argument is not provided, current platform will be used.
    #
    #  @param platformIcon [ enum | None | in  ] - Platform icon from mQtWidgets.iconLib.Platform enum class.
    #
    #  @exception N/A
    #
    #  @return QIcon - QIcon instance.
    def createPlatformIcon(self, platformIcon=None):

        if not platformIcon:
            platformIcon = PlatformIcon.getValueFromAttributeName(mCore.platformLib.Platform.system(), removeK=True)

        iconFile = self.getFile(platformIcon)
        if iconFile:
            return QtGui.QIcon(iconFile)

        return QtGui.QIcon()

    #
    ## @brief Create and return an QPixmap instance for the given platform.
    #
    #  If platformIcon argument is not provided, current platform will be used.
    #
    #  @param platformIcon [ enum | None | in  ] - Platform icon from mQtWidgets.iconLib.Platform enum class.
    #
    #  @exception N/A
    #
    #  @return QPixmap - QPixmap instance.
    def createPlatformPixmap(self, platformIcon=None):

        if not platformIcon:
            platformIcon = PlatformIcon.getValueFromAttributeName(mCore.platformLib.Platform.system(), removeK=True)

        iconFile = self.getFile(platformIcon)
        if iconFile:
            return QtGui.QPixmap(iconFile)

        return QtGui.QPixmap()