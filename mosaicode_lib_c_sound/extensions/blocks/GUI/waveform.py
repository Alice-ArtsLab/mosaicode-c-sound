#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Waveform(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "sound"
        self.help = "Waveform"
        self.label = "waveform"
        self.color = "67:160:17:150"
        self.group = "GUI"
        self.ports = [{"type":"mosaicode_lib_c_sound.extensions.ports.sound",
                       "name":"input0",
                       "conn_type":"Input",
                       "label":"Sound value"}]
        self.properties = [{"name": "x",
                            "label": "X",
                            "type": MOSAICODE_INT,
                            "value": "0"
                            },
                            {"name": "y",
                            "label": "Y",
                            "type": MOSAICODE_INT,
                            "value": "0"},
                            {"name": "width",
                            "label": "Width",
                            "type": MOSAICODE_FLOAT,
                            "lower": 0,
                            "upper": 2147483647,
                            "step": 1,
                            "value": 200},
                           {"name": "height",
                            "label": "Height",
                            "type": MOSAICODE_FLOAT,
                            "lower": 0,
                            "upper": 2147483647,
                            "step": 1,
                            "value": 200}]
        self.codes["declaration"] = "mscsound_waveform_t *$label$_$id$;\n"
        self.codes["execution"] = "$label$_$id$->process(&$label$_$id$);\n"
        self.codes["setup"] = \
"""
    $label$_$id$ = mscsound_create_waveform($prop[width]$, $prop[height]$, FRAMES_PER_BUFFER);
    gtk_fixed_put(GTK_FIXED(fixed_layout), $label$_$id$->widget, $prop[x]$, $prop[y]$);
"""
