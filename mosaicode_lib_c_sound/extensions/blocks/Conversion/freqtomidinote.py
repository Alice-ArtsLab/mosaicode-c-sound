#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class FreqToMIDINote(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "sound"
        self.help = "Frequency Value to Convert MIDI Note"
        self.label = "Freq_to_MIDI_Note"
        self.color = "140:114:114:150"
        self.ports = [{"type":"mosaicode_lib_c_base.extensions.ports.float",
                       "name":"midi_note",
                       "conn_type":"Output",
                       "label":"MIDI Note value"},
                      {"type":"mosaicode_lib_c_base.extensions.ports.float",
                       "name":"freq",
                       "conn_type":"Input",
                       "label":"Frequency value"}]

        self.group = "Conversion"
        self.codes["declaration"] = \
"""
float_callback *$port[midi_note]$;
int $port[midi_note]$_size = 0;

void $port[freq]$(float value){
  for(int i=0 ; i < $port[midi_note]$_size ; i++){
    // Call the stored functions
    (*($port[midi_note]$[i]))(mscsound_midi_freq_to_midi_note(value));
  }
}
"""
