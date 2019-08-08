#!/usr/bin/env python3

import sublime
import sublime_plugin


class CreateSliderCommand(sublime_plugin.TextCommand):
    def run(self, edit, rr_a, rr_b, variable_name):
        region_to_replace = sublime.Region(rr_a, rr_b)
        initial_value = self.view.substr(region_to_replace)

        self.view.replace(edit, region_to_replace, variable_name)

        var_def = 'float {} = {};'.format(variable_name, initial_value)
        self.insert_line_before_pattern(edit, var_def, r'// --/Fiddles--')

        slider_def = '  new SliderConfig("{}", {}, {}),'.format(variable_name, str(0), str(float(initial_value) * 10))
        self.insert_line_before_pattern(edit, slider_def, r'// --/Sliders')

    def insert_line_before_pattern(self, edit, new_line, pattern):
        match = self.view.find(pattern, 0, sublime.LITERAL)
        line = self.view.line(match)
        self.view.insert(edit, line.a, new_line + '\n')

class MakeItSlideCommand(sublime_plugin.TextCommand):
    region_to_replace = None

    def run(self, edit, **kwargs):
        # Check that the name under the thing is word to word edge
        selections = self.view.sel()
        for region in selections:
            variable = self.view.substr(region)
            self.region_to_replace = region
            self.view.window().show_input_panel('Global Name for :"{}": '.format(variable), '', self.create_slider, None, self.on_cancel)

    def on_cancel(self):
        region_to_replace = None

    def create_slider(self, new_name):
        # You can't pass values like regions and views into functions, so you have to break it down.
        args = {'rr_a': self.region_to_replace.a, 'rr_b': self.region_to_replace.b, 'variable_name': new_name}
        self.view.run_command('create_slider', args)
