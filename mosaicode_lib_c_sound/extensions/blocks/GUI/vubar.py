#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class VUBar(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "sound"
        self.help = "VUBar"
        self.label = "VUBar"
        self.color = "67:160:17:150"
        self.ports = [{"type":"mosaicode_lib_c_base.extensions.ports.float",
                       "name":"input0",
                       "conn_type":"Input",
                       "label":"Float value"}]
        self.properties = [{"name": "x",
                            "label": "X",
                            "type": MOSAICODE_INT,
                            "value": "0"
                            },
                            {"name": "y",
                            "label": "Y",
                            "type": MOSAICODE_INT,
                            "value": "0"
                            }]

        self.group = "GUI"
        self.codes["declaration"] = \
"""
mscsound_vubar_t *$label$_$id$;

void $port[input0]$(float value){
    *($label$_$id$->input0) = value;
}
"""
        self.codes["execution"] = "$label$_$id$->process(&$label$_$id$);\n"

        self.codes["setup"] = \
"""
    $label$_$id$ = mscsound_create_vubar();
    $label$_$id$->input0 = calloc(1, sizeof(float));
    gtk_fixed_put(GTK_FIXED(fixed_layout), $label$_$id$->widget, $prop[x]$, $prop[y]$);
"""
