#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mosaicode.model.codetemplate import CodeTemplate
from mosaicode.GUI.fieldtypes import *

class MosaicodeCSound(CodeTemplate):

    # ----------------------------------------------------------------------
    def __init__(self):
        CodeTemplate.__init__(self)
        self.name = "Mosaicode-Sound"
        self.language = "c"
        self.command = "make && ./main\n"
        self.description = "mosaicode-c-sound"
        self.code_parts = ["declaration", "execution", "setup"]
        self.properties = [{"name": "title",
                            "label": "Title",
                            "value": "Title",
                            "type": MOSAICODE_STRING
                            }
                           ]

        self.files["main.c"] = \
r"""
#include <mosaic-sound.h>
#include <portaudio.h>
#include <alsa/asoundlib.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <time.h>
#include <math.h>

#define NUM_SECONDS 12
#define SAMPLE_RATE 44100
#define FRAMES_PER_BUFFER 256

$code[declaration]$

static int mscsound_callback(const void *inputBuffer, void *outputBuffer,
                             unsigned long framesPerBuffer,
                             const PaStreamCallbackTimeInfo *timeInfo,
                             PaStreamCallbackFlags statusFlags,
                             void *userData) {
  float *in = (float *)inputBuffer;
  float *out = (float *)outputBuffer;

  (void)timeInfo; /* Prevent unused variable warnings. */
  (void)statusFlags;
  (void)userData;
  (void)in;
  (void)out;

  $code[execution]$

  return paContinue;
}

/*
 * This routine is called by mscsound when mscsound_callback is done.
 */
static void mscsound_finished(void *data) { printf("Stream Completed!\n"); }

/*******************************************************************/
int main(int argc, char *argv[]) {
  time_t t;

  /* Intializes random number generator */
  srand((unsigned) time(&t));

  $code[setup]$

  $connections$

  void *stream = mscsound_inicialize(SAMPLE_RATE, FRAMES_PER_BUFFER);

  printf("Playing until the Enter key is pressed.\n");
  getchar();

  mscsound_terminate(stream);

  return 0;
}
"""

        self.files["Makefile"] = \
r"""CC := gcc
CFLAGS := -g -Wall
LIBS := -lportaudio -lm `pkg-config --libs sndfile`
LIB_FLAGS := -I/usr/include/mosaic/mosaic-sound -lmosaic-sound
TARGET := main

all: $(TARGET)

main: main.o
	$(CC) $(CFLAGS) $^ $(LIB_FLAGS) -o $@  $(LIBS)

main.o: main.c
	$(CC) $(CFLAGS) -c $< $(LIB_FLAGS) -o $@  $(LIBS)"""

# -------------------------------------------------------------------------
