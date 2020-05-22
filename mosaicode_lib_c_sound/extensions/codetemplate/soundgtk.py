#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mosaicode.model.codetemplate import CodeTemplate
from mosaicode.GUI.fieldtypes import *

class MosaicodeCSoundGtk(CodeTemplate):

    # ----------------------------------------------------------------------
    def __init__(self):
        CodeTemplate.__init__(self)
        self.name = "Mosaicode-Sound-Gtk"
        self.language = "c"
        self.command = "make && ./main\n"
        self.description = "mosaicode-c-sound-gtk"
        self.code_parts = ["declaration", "execution", "setup", "function"]
        self.properties = [{"name": "sample_rate",
                            "label": "Sample Rate",
                            "value": "44100",
                            "type": MOSAICODE_INT
                            },
                            {"name": "frame_per_buffer",
                            "label": "Frames Per Buffer",
                            "value": "256",
                            "type": MOSAICODE_INT
                            },
                            {"name": "title",
                            "label": "Title",
                            "value": "Title",
                            "type": MOSAICODE_STRING
                            },
                            {"name": "width",
                            "label": "Width",
                            "value": 800,
                            "type": MOSAICODE_INT
                            },
                            {"name": "height",
                            "label": "Height",
                            "value": 600,
                            "type": MOSAICODE_INT
                            }
                            ]

        self.files["callback.h"] = r"""
typedef void (*string_callback)(const char * value);
typedef void (*float_callback)(float value);
typedef void (*int_callback)(int value);
typedef void (*char_callback)(char value);
"""

        self.files["main.c"] = \
r"""
#include <mosaic-sound.h>
#include <portaudio.h>
#include <alsa/asoundlib.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <gtk/gtk.h>
#include <limits.h>
#include <time.h>
#include <math.h>

#define NUM_SECONDS 12
#define SAMPLE_RATE 44100
#define FRAMES_PER_BUFFER 256

GtkWidget * window;
GtkWidget * fixed_layout;
$code[declaration]$

void destroy(void){
   gtk_main_quit ();
}

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
    gtk_init(&argc, &argv);

    window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    gtk_window_set_title(GTK_WINDOW(window), "$prop[title]$");
    g_signal_connect(window, "destroy",G_CALLBACK(destroy), NULL);
    gtk_window_resize(GTK_WINDOW(window), $prop[width]$, $prop[height]$);

    fixed_layout = gtk_fixed_new();
    gtk_container_add(GTK_CONTAINER(window), fixed_layout);

    $code[setup]$
    $connections$

    void *stream = mscsound_inicialize(SAMPLE_RATE, FRAMES_PER_BUFFER);

    gtk_widget_show_all(window);
    gtk_main();

    mscsound_terminate(stream);

    return 0;
}
"""

        self.files["Makefile"] = \
r"""CC := gcc
CFLAGS := -g -Wall
LIBS := -lportaudio -lm `pkg-config --cflags --libs sndfile --libs gtk+-3.0`
LIB_FLAGS := -I/usr/include/mosaic/mosaic-sound -lmosaic-sound
TARGET := main

all: $(TARGET)

main: main.o
	$(CC) $(CFLAGS) $^ $(LIB_FLAGS) -o $@  $(LIBS)

main.o: main.c
	$(CC) $(CFLAGS) -c $< $(LIB_FLAGS) -o $@  $(LIBS)

"""


# -------------------------------------------------------------------------
