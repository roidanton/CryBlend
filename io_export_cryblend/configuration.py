#------------------------------------------------------------------------------
# Name:        configuration.py
# Purpose:     Storing CryBlend configuration settings
#
# Author:      Mikołaj Milej
#
# Created:     02/10/2013
# Copyright:   (c) Mikołaj Milej 2013
# Licence:     GPLv2+
#------------------------------------------------------------------------------

# <pep8-80 compliant>


import bpy
from io_export_cryblend.outPipe import cbPrint
import os
import pickle


class __Configuration:
    __CONFIG_PATH = bpy.utils.user_resource('CONFIG',
                                            path='scripts',
                                            create=True)
    __CONFIG_FILENAME = 'cryblend.cfg'
    __CONFIG_FILEPATH = os.path.join(__CONFIG_PATH, __CONFIG_FILENAME)
    __DEFAULT_CONFIGURATION = {'RC_LOCATION': r'',
                              'RC_FOR_TEXTURES_CONVERSION': r'',
                              'TEXTURES_DIR': r''}

    def __init__(self):
        self.__CONFIG = self.__load({})

    @property
    def rc_path(self):
        return self.__CONFIG['RC_LOCATION']

    @rc_path.setter
    def rc_path(self, value):
        self.__CONFIG['RC_LOCATION'] = value

    @property
    def rc_for_texture_conversion_path(self):
        if (not self.__CONFIG['RC_FOR_TEXTURES_CONVERSION']):
            return self.rc_path

        return self.__CONFIG['RC_FOR_TEXTURES_CONVERSION']

    @rc_for_texture_conversion_path.setter
    def rc_for_texture_conversion_path(self, value):
        self.__CONFIG['RC_FOR_TEXTURES_CONVERSION'] = value

    @property
    def textures_directory(self):
        return self.__CONFIG['TEXTURES_DIR']

    @textures_directory.setter
    def textures_directory(self, value):
        self.__CONFIG['TEXTURES_DIR'] = value

    def save(self):
        cbPrint("Saving configuration file.", 'debug')

        if os.path.isdir(self.__CONFIG_PATH):
            try:
                with open(self.__CONFIG_FILEPATH, 'wb') as f:
                    pickle.dump(self.__CONFIG, f, -1)
                    cbPrint("Configuration file saved.")

                cbPrint('Saved %s' % self.__CONFIG_FILEPATH)

            except:
                cbPrint("[IO] can not write: %s" % self.__CONFIG_FILEPATH,
                        'error')

        else:
            cbPrint("Configuration file path is missing %s"
                    % self.__CONFIG_PATH,
                    'error')

    def __load(self, current_configuration):
        new_configuration = {}
        new_configuration.update(self.__DEFAULT_CONFIGURATION)
        new_configuration.update(current_configuration)

        if os.path.isfile(self.__CONFIG_FILEPATH):
            try:
                with open(self.__CONFIG_FILEPATH, 'rb') as f:
                    new_configuration.update(pickle.load(f))
                    cbPrint('Configuration file loaded.')
            except:
                cbPrint("[IO] can not read: %s" % self.__CONFIG_FILEPATH,
                        'error')

        return new_configuration


Configuration = __Configuration()
