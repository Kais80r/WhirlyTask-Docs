# Appearance

Use **Menu > Dark Mode** to switch the main application and editor between dark and light appearance. The graph editor's theme control uses the same application preference.

The preference is stored separately from sequence content. Changing the theme does not create a named Library item or export a sequence file.

The native main window, Library, routine settings dialogs, menus, and graph editor follow the chosen palette. Windows-managed file dialogs and other system surfaces can also depend on Windows appearance settings.

If a window seems to retain an old color after a switch, close and reopen that window. For a reproducible remaining color problem, note the window/control and whether it followed a tab change, selection change, or theme switch.

Changing appearance does not invert your reference images or make Pixel matching tolerant of another application's theme. A dark/light change in the target application can change the pixels that recognition sees.

See [Smart And Pixel Image Recognition](../Recognition/Images.md) and [Editors And Saving](Editors-And-Saving.md).
