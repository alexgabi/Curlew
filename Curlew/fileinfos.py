# -*- coding: utf-8 -*-

# Curlew - Easy to use multimedia converter
#
# Copyright (C) 2012-2014 Fayssal Chamekh <chamfay@gmail.com>
#
# Released under terms on waqf public license.
#
# Curlew is free software; you can redistribute it and/or modify it 
# under the terms of the latest version waqf public license as published by 
# ojuba.org.
#
# Curlew is distributed in the hope that it will be useful, but WITHOUT 
# ANY WARRANTY; without even the implied warranty 
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#        
# The latest version of the license can be found on:
# http://www.ojuba.org/wiki/doku.php/waqf/license

from gi.repository import Gtk, Pango
from subprocess import check_output

class FileInfos(Gtk.Dialog):
    def __init__(self, prnt, file_name):
        Gtk.Dialog.__init__(self, parent=prnt)
        self.set_title(_("File informations"))
        self.set_size_request(580, 450)
        self.set_border_width(6)
        
        txt_info = Gtk.TextView()
        txt_info.set_editable(False)
        txt_info.set_cursor_visible(False)
        txt_info.set_border_width(8)
        
        scroll = Gtk.ScrolledWindow()
        scroll.set_shadow_type(Gtk.ShadowType.IN)
        scroll.add(txt_info)
        self.vbox.pack_start(scroll, True, True, 0)
        
        self.add_button(Gtk.STOCK_CLOSE, Gtk.ResponseType.CLOSE)
        
        font_desc = Pango.FontDescription('Monospace')
        txt_info.override_font(font_desc)
        
        txt_buffer = Gtk.TextBuffer()
        txt_info.set_buffer(txt_buffer)
        
        # Show info        
        buf = check_output('mediainfo "{}"'.format(file_name), shell=True)
        txt_buffer.set_text(buf.strip())
        
    
    
    def show_dialog(self):
        self.show_all()
        self.run()
        self.destroy()