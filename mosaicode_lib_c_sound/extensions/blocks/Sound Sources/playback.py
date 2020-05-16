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
        self.color = "228:242:73:150"
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
                        "name":"readCountOutput",
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
        self.codes["declaration"] = \
"""
mscsound_playback_t *$label$_$id$;

typedef void (*$label$_$id$_callback_t)(int value);
$label$_$id$_callback_t* $port[fileFrames]$;
int $port[fileFrames]$_size = 0;

$label$_$id$_callback_t* $port[readCountOutput]$;
int $port[readCountOutput]$_size = 0;

void $port[filename]$(char *value){
    strcpy(*($label$_$id$->filename), \"value\");
}

void $port[loop]$(char *value){
    strcpy(*($label$_$id$->loop), \"value\");
}

void $port[readCount]$(int value){
    *($label$_$id$->readCount) = value;
    for(int i=0 ; i < $port[readCountOutput]$_size ; i++){
        // Call the stored functions
        (*($port[readCountOutput]$[i]))(*($label$_$id$->readCount));
    }
}
"""
        self.codes["execution"] = \
"""
$label$_$id$->process(&$label$_$id$);
for(int i=0 ; i < $port[fileFrames]$_size ; i++){
    // Call the stored functions
    (*($port[fileFrames]$[i]))(*($label$_$id$->fileFrames));
}
"""


        self.codes["setup"] = \
"""$label$_$id$ = mscsound_create_playback
(\"$prop[filename]$\",FRAMES_PER_BUFFER);
strcpy(*($label$_$id$->loop), \"$prop[loop]$\");
strcpy(*($label$_$id$->paused), \"$prop[paused]$\");
*($label$_$id$->readCount) = $prop[readCount]$;
"""
