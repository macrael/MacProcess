#!/usr/bin/env python3

import sublime
import sublime_plugin



class MakeItSlideCommand(sublime_plugin.TextCommand):
    def run(self, edit, **kwargs):
        print("HIIHIHIHI")
        # Check that the name under the thing is word to word edge
        sel = self.view.sel()
        print(sel)


