#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Playback(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "sound"
        self.help = "Playback"
        self.label = "Playback"
        self.color = "50:150:250:150"
        self.ports = [{"type":"mosaicode_lib_c_base.extensions.ports.string",
                       "name":"filename",
                       "conn_type":"Input",
                       "label":"Filename"},
                      {"type":"mosaicode_lib_c_base.extensions.ports.string",
                       "name":"loop",
                       "conn_type":"Input",
                       "label":"Loop"},
                       {"type":"mosaicode_lib_c_base.extensions.ports.integer",
                        "name":"fileFrames",
                        "conn_type":"Output",
                        "label":"File Frames"},
                       {"type":"mosaicode_lib_c_base.extensions.ports.integer",
                        "name":"readCount",
                        "conn_type":"Input",
                        "label":"Read Count"},
                       {"type":"mosaicode_lib_c_base.extensions.ports.integer",
                        "name":"readCountOutPut",
                        "conn_type":"Output",
                        "label":"Read Count"},
                       {"type":"mosaicode_lib_c_sound.extensions.ports.sound",
                        "name":"output0",
                        "conn_type":"Output",
                        "label":"Sound (Mono/Left)"},
                       {"type":"mosaicode_lib_c_sound.extensions.ports.sound",
                        "name":"output1",
                        "conn_type":"Output",
                        "label":"Sound (Right)"}]

        self.properties = [{"name": "filename",
                            "label": "Filename",
                            "type": MOSAICODE_OPEN_FILE},
                           {"name": "loop",
                            "label": "Loop",
                            "type": MOSAICODE_COMBO,
                            "values": ["yes", "no"],
                            "value": "no"},
                            {"name": "paused",
                             "label": "Paused",
                             "type": MOSAICODE_COMBO,
                             "values": ["yes","no"],
                             "value": "no"},
                            {"name": "readCount",
                             "label": "Read Count",
                             "type": MOSAICODE_INT,
                             "lower": 0,
                             "upper": 2147483647,
                             "step": 256,
                             "value": 0}]

        self.group = "Sound Sources"
        self.codes["function_declaration"] = ""
        self.codes["declaration"] = "mscsound_playback_t *$label$_$id$;\n"
        self.codes["declaration"] += "void $port[fileFrames]$(int value);\n";
        self.codes["declaration"] += "void $port[readCountOutPut]$(int value);\n";

        self.codes["function"] = \
"""
void $port[fileFrames]$(int value){
    $label$_$id$->fileFrames = value;
}

void $port[readCountOutPut]$(int value){
    $label$_$id$->readCount = value;
}
"""
        self.codes["execution"] = "$label$_$id$->process(&$label$_$id$);\n"
        self.codes["setup"] = "$label$_$id$ = mscsound_create_playback" + \
            "(\"$prop[filename]$\",FRAMES_PER_BUFFER);\n" + \
            "strcpy(*($label$_$id$->loop), \"$prop[loop]$\");\n" + \
            "strcpy(*($label$_$id$->paused), \"$prop[paused]$\");\n" + \
            "$label$_$id$->readCount = $prop[readCount]$;\n"
