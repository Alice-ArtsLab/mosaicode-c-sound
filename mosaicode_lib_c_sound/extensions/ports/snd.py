#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mosaicode.model.port import Port

class SND(Port):
    def __init__(self):
        self.code = '''$input$ = $output$;'''
        self.multiple = '''False'''
        self.language = '''c'''
        self.color = '''#6c960cf10cf1'''
        self.label = '''SND'''
        self.source = '''python'''
        self.type = '''mosaicode_lib_c_sound.extensions.ports.sound'''
        self.var_name = "block_$id$_$conn_type$$port_number$"
