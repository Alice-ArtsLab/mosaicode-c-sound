#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Speaker class.
"""
from mosaicode.model.blockmodel import BlockModel

class Devices(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "sound"
        self.help = "Devices"
        self.label = "Devices"
        self.color = "50:150:250:150"
        self.ports = [{"type":"mosaicode_lib_c_base.extensions.ports.integer",
                       "name":"trigger",
                       "conn_type":"Input",
                       "label":"Integer Value"},
                      {"type":"mosaicode_lib_c_base.extensions.ports.string",
                       "name":"output1",
                       "conn_type":"Output",
                       "label":"String Value"}]
        self.group = "General"
        self.properties = [{"name": "trigger",
                             "label": "Trigger",
                             "type": MOSAICODE_COMBO,
                             "values": ["0","1"],
                             "value": "1"}]

        self.codes["declaration"] = \
"""
mscsound_device_list_t *$label$_$id$;

void $port[trigger]$(int value){
    if (! value) {

    } else {
        $label$_$id$->process(&$label$_$id$);
        $label$_$id$->show(&$label$_$id$);
    }
}

typedef void (*$label$_$id$_callback_t)(char* value);
$label$_$id$_callback_t* $port[output1]$;
int $port[output1]$_size = 0;

void $label$_$id$_callback(void * data){
    for(int i=0 ; i < $port[output1]$_size ; i++){
        // Call the stored functions
        (*($port[output1]$[i]))(*($label$_$id$->output1));
    }
}
"""

        self.codes["setup"] = \
"""
$label$_$id$ = mscsound_create_devices();
if ($prop[trigger]$) {
    $label$_$id$->process(&$label$_$id$);
    $label$_$id$->show(&$label$_$id$);
}
"""
