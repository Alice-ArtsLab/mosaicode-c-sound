#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mosaicode.model.port import Port

class SOUND(Port):
    def __init__(self):
        self.multiple = False
        self.type = "mosaicode_lib_c_sound.extensions.ports.sound"
        self.language = "c"
        self.color = "#F00"
        self.hint = "SOUND"
        self.var_name = "$block[label]$_$block[id]$_$port[name]$"

        self.code = \
r"""
$output$ = (sound_callback *) realloc($output$, ($output$_size + 1 ) * sizeof(sound_callback));
$output$[$output$_size] = $input$;
$output$_size++;
"""
        self.var_name = "$port[name]$$block[id]$"
