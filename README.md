RubyCheckOnSave Sublime Text 2 Plugin
=====================================

This simple plugin checks the syntax of ruby files when they're saved.

Installation
------------

**With the Package Control plugin:** The easiest way to install SublimeLinter is through Package Control, which can be found at this site: http://wbond.net/sublime_packages/package_control

Once you install Package Control, restart ST2 and bring up the Command Palette (`Command+Shift+P` on OS X, `Control+Shift+P` on Linux/Windows). Select "Package Control: Install Package", wait while Package Control fetches the latest package list, then select RubyCheckOnSave when the list appears. The advantage of using this method is that Package Control will automatically keep RubyCheckOnSave up to date with the latest version.

**Without Git:** Download the latest source from [GitHub](https://github.com/edgar/RubyCheckOnSave) and copy the RubyCheckOnSave folder to your Sublime Text 2 "Packages" directory.

**With Git:** Clone the repository in your Sublime Text 2 "Packages" directory:

    git clone git://github.com/edgar/RubyCheckOnSave.git


The "Packages" directory is located at:

* OS X:

        ~/Library/Application Support/Sublime Text 2/Packages/

* Linux:

        ~/.config/sublime-text-2/Packages/

* Windows:

        %APPDATA%/Sublime Text 2/Packages/


Configuration
-------------

There are a number of configuration options available to customize the behavior of RubyCheckOnSave. For the latest information on what options are available, select the menu item `Preferences->Package Settings->RubyCheckOnSave->Settings - Default`.

Do **NOT** edit the default RubyCheckOnSave settings. Your changes will be lost when RubyCheckOnSave is updated. ALWAYS edit the user RubyCheckOnSave settings by selecting `Preferences->Package Settings->SublimeLinter->Settings - User`.

 If you are using rvm or rbenv, you will probably have to specify the full path to the ruby you are using in the `ruby_check_on_save_cmd` setting.

### Per project

SublimeLinter supports per-project settings. This is useful if you work with several projects that requires different ruby interpreters. To edit your project settings, select the menu item `Project->Edit Project`. If there is no `settings` object at the top level, add one and then add the `ruby_check_on_save_cmd` setting, like this:


    {
        "folders":
          [
              {
                  "path": "/Users/edgar/sandboxes/repo"
              }
          ],
          "settings":
          {
              "ruby_check_on_save_cmd": "/Users/edgar/.rvm/rubies/ruby-1.9.3-p194/bin/ruby"
          }
    }
