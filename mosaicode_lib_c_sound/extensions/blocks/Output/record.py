#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Record(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "sound"
        self.help = "Record"
        self.label = "Record"
        self.color = "50:150:250:150"
        self.ports = [{"type":"mosaicode_lib_c_sound.extensions.ports.sound",
                       "name":"input0",
                       "conn_type":"Input",
                       "label":"Sound Value"},
                      {"type":"mosaicode_lib_c_base.extensions.ports.string",
                       "name":"filename",
                       "conn_type":"Input",
                       "label":"Filename"},
                      {"type":"mosaicode_lib_c_base.extensions.ports.string",
                       "name":"paused",
                       "conn_type":"Input",
                       "label":"Paused"},
                      {"type":"mosaicode_lib_c_base.extensions.ports.string",
                       "name":"stop",
                       "conn_type":"Input",
                       "label":"Stop"}]

        self.properties = [{"name": "filename",
                            "label": "Filename",
                            "type": MOSAICODE_STRING,
                            "value": "/tmp/mosaicode-c-sound-record.wav"
                           },
                           {"name": "paused",
                            "label": "Paused",
                            "type": MOSAICODE_COMBO,
                            "values": ["yes", "no"],
                            "value": "no"
                            }]
        self.group = "Output"
        self.codes["declaration"] = \
"""
mscsound_record_t *$label$_$id$;

void $port[filename]$(char** value){
    $label$_$id$->filename = value;
}

void $port[paused]$(char** value){
    $label$_$id$->paused = value;
}
"""
        self.codes["execution"] = "$label$_$id$->process(&$label$_$id$);\n"
        self.codes["setup"] = "$label$_$id$ = mscsound_create_record(\"$prop[filename]$\", FRAMES_PER_BUFFER, SAMPLE_RATE);\n"
        self.codes["setup"] += "strcpy(*($label$_$id$->filename), \"$prop[filename]$\");\n"
        self.codes["setup"] += "strcpy(*($label$_$id$->paused), \"$prop[paused]$\");\n"
