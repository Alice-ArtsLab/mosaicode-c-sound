#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class ChannelShooterSplitter(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "sound"
        self.help = "Channel Shooter Splitter"
        self.label = "ChannelShooterSplitter"
        self.color = "50:150:250:150"
        self.ports = [{"type":"mosaicode_lib_c_sound.extensions.ports.sound",
                       "name":"input0",
                       "conn_type":"Input",
                       "label":"Sound Value"},
                      {"type":"mosaicode_lib_c_sound.extensions.ports.sound",
                       "name":"output0",
                       "conn_type":"Output",
                       "label":"Sound Value"}]

        self.properties = []

        self.group = "General"
        self.codes["function_declaration"] = ""
        self.codes["declaration"] = "mscsound_channelshootersplitter_t *$label$_$id$;\n"

        self.codes["function"] = ""
        self.codes["execution"] = "$label$_$id$->process(&$label$_$id$);\n"
        self.codes["setup"] = \
"""
$label$_$id$ = mscsound_create_channelshootersplitter(FRAMES_PER_BUFFER);
"""
