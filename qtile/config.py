# Jack Tench 2023
# qtile config file

# Import python libs.
import os
import subprocess

# Import qtile libs.
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
#from libqtile.utils import guess_terminal

# Import color scheme.
from cols import color

# Set mod key to alt.
mod = "mod1"

# Set default apps.
myTerm = "alacritty"
myRun = "rofi -show drun"
myText = "nvim"
myFile = "pcmanfm"

# Run script to handle starting the compositor and setting the wallpaper.
@hook.subscribe.startup
def autostart():
    home=os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

# Configure layout options.
layoutCfg = {
        "border_width": 4,
        "margin": 8,
        "border_focus": color["purple"],
        "border_normal": color["comment"]
}

# Configure bar widget options.
widget_defaults = dict(
        font = "sans",
        fontsize = 16,
        padding = 3,
)
extension_defaults = widget_defaults.copy()

# Create 4 workspaces.
groups = [Group(i) for i in "1234"]

# Define main keybinds.
keys = [

    # Reload qtile config. Ctrl + Alt + R
    Key([mod, "control"], "r", lazy.reload_config(), desc = "Reload qtile config."),
    
    # Quick launch keybinds.
    # Launch terminal. Alt + Enter
    Key([mod], "Return", lazy.spawn(myTerm), desc = "Open terminal."),
    # Launch rofi. Alt + Space
    Key([mod], "space", lazy.spawn(myRun), desc = "Open rofi."),
    # Launch neovim. Alt + T
    Key([mod], "t", lazy.spawn(myText), desc = "Open neovim."),
    # Launch pcmanfm. Alt + E
    Key([mod], "e", lazy.spawn(myFile), desc = "Open file manager."),

    # Navigation keybinds.
    # Close focused window. Alt + Q
    Key([mod], "q", lazy.window.kill(), desc = "Close focused window."),
    # Change layout. Alt + Tab
    Key([mod], "Tab", lazy.next_layout(), desc = "Change tiling layout."),
    # Navigate window focus. Alt + vim keys
    Key([mod], "h", lazy.layout.left(), desc = "Left"),
    Key([mod], "l", lazy.layout.right(), desc = "Right"),
    Key([mod], "j", lazy.layout.down(), desc = "Down"),
    Key([mod], "k", lazy.layout.up(), desc = "Up"),
    # Move windows between left/right columns or move up/down in the current stack. Alt + Shift + vim keys
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc = "Move left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc = "Move right."),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc = "Move down."),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc = "Move up."),

]

# Define workspace keybinds.
for i in groups:
    keys.extend(
            [

                # Change workspace. Alt + (1234)
                Key(
                    [mod],
                    i.name,
                    lazy.group[i.name].toscreen(),
                    desc = "Switch to workspace {}".format(i.name),
                ),

                # Move focused window to workspace. Alt + Shift + (1234)
                Key(
                    [mod, "shift"],
                    i.name,
                    lazy.window.togroup(i.name),
                    desc = "Move focused window to workspace {}".format(i.name),
                ),

            ]
            )

# Set tiling layouts.
layouts = [

    # Tall layout from XMonad. This is a master/stack config. Default layout.
    layout.MonadTall(**layoutCfg),
    # Spiral layout.
    layout.Spiral(**layoutCfg),
    # Columns layout. This one is disabled for now.
    #layout.Columns(**layoutCfg),

    # Full screen or monocle layout. Has no gaps.
    layout.Max(
        border_width = 0,
        margin = 0,
    ),

]

# Configure floating rules and keybinds.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start = lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start = lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]
floating_layout = layout.Floating(
    float_rules = [
        *layout.Floating.default_float_rules,
        Match(wm_class = "confirmreset"),
        Match(wm_class = "makebranch"),
        Match(wm_class = "maketag"),
        Match(wm_class = "ssh-askpass"),
        Match(title = "branchdialog"),
        Match(title = "pinentry"),
    ]
)

# Configure top bar.
screens = [
    Screen(
        top=bar.Bar(
            [

                # Workspace switcher.
                widget.GroupBox(
                    disable_drag = True,
                    highlight_method = 'block',
                    block_highlight_text_color = color["background"],
                    inactive = color["current-line"],
                    this_current_screen_border = color["pink"],
                ),

                # Display current tiling layout.
                widget.CurrentLayout(
                    fmt = 'layout: {}'
                ),

                # Spacer
                widget.Spacer(  length = bar.STRETCH,   ),

                # System tray.
                widget.Systray(),

                # Battery indicator.
                widget.Battery(),

                # Clock
                widget.Clock(
                    foreground = color["cyan"],
                ),

            ],
            # Bar options.
            40,
            border_color = color["background"],
            background = color["background"]
        ),
    ),
]

# Mainly default qtile stuff down here.
# TODO: Make this code nicer?
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"
