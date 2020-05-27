#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mosaicode.model.port import Port

class MIDI(Port):
    def __init__(self):
        self.multiple = False
        self.type = "mosaicode_lib_c_sound.extensions.ports.midi"
        self.language = "c"
        self.color = "#F00"
        self.hint = "MIDI"
        self.code = \
"""
$output$ = realloc($output$, ($output$_size + 1 ) * sizeof(void *));
$output$[$output$_size] = &$input$;
$output$_size++;
"""
        self.var_name = "$block[label]$_$block[id]$_$port[name]$"
