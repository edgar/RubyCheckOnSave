import sublime, sublime_plugin

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
        view.window().run_command("exec", {"cmd": [ruby, "-cw", view.file_name()]})