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
                       "name":"input0",
                       "conn_type":"Input",
                       "label":"Integer Value"},
                      {"type":"mosaicode_lib_c_base.extensions.ports.string",
                       "name":"output1",
                       "conn_type":"Output",
                       "label":"String Value"}]
        self.group = "General"
        self.codes["function_declaration"] = ""
        self.codes["declaration"] = "mscsound_device_list_t *$label$_$id$;\n" +\
                                    "void $port[input0]$(int value);\n"

        self.codes["function"] =  \
"""
void $port[input0]$(int value){
    if (! value) {

    } else {
        $label$_$id$->process(&$label$_$id$);
        $label$_$id$->show(&$label$_$id$);
    }
}
"""
        self.codes["execution"] = ""
        self.codes["setup"] = \
"""
$label$_$id$ = mscsound_create_devices();
$label$_$id$->process(&$label$_$id$);
$label$_$id$->show(&$label$_$id$);
"""
