#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Volume(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "sound"
        self.help = "Volume"
        self.label = "Volume"
        self.color = "67:160:17:150"
        self.ports = [{"type":"mosaicode_lib_c_base.extensions.ports.float",
                       "name":"output0",
                       "conn_type":"Output",
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
float_callback * $port[output0]$;
int $port[output0]$_size = 0;
mscsound_volume_t  *$label$_$id$;
"""
        self.codes["execution"] = \
"""
for(int i=0 ; i < $port[output0]$_size ; i++){
    // Call the stored functions
    (*($port[output0]$[i]))(*($label$_$id$->output0));
}
"""

        self.codes["setup"] = \
"""
    $label$_$id$ = mscsound_create_volume(\"Volume: \");
    gtk_fixed_put(GTK_FIXED(fixed_layout), $label$_$id$->widget, $prop[x]$, $prop[y]$);
"""
