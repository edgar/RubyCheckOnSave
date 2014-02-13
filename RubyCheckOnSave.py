import sublime, sublime_plugin, subprocess

class RubyCheckOnSave(sublime_plugin.EventListener):
    def on_post_save(self, view):
        if view.file_name()[-3:] == '.rb':
            view.window().run_command("ruby_check_on_save", {"saving": True})

class RubyCheckOnSaveCommand(sublime_plugin.TextCommand):
    def run(self, edit, saving=False):
        view = self.view
        global_settings = sublime.load_settings(__name__ + '.sublime-settings')
        cmd_setting = 'ruby_check_on_save_cmd'
        ruby = view.settings().get(cmd_setting, global_settings.get(cmd_setting))
        args = [ruby, "-cw", "%s" % view.file_name()]
        child_process = subprocess.Popen(args, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
        cmd_output = child_process.communicate()[0]

        if child_process.returncode != 0:
            first_line = sorted(cmd_output.split('\n'), key=lambda line: "error" not in line and "mismatch" not in line)[0]
            _, line, error = first_line.split(':', 2)
            err_message = "Ruby syntax error at %(line)s line: %(error)s\n\n%(output)s" % { "line": line, "error": error, "output": cmd_output.replace(view.file_name() + ":", '') }
            sublime.error_message(err_message)
            view.window().run_command("goto_line", {"line": line} )
