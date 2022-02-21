from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import os

mod = "mod4"
terminal = guess_terminal()
browser = "brave --disable-extensions --process-per-site --force-device-scale-factor=1.5"
screenshot = "import -window root screenshot.jpg"
spotify = "spotify --disable-extensions --process-per-site --force-device-scale-factor=1.5"
rofi = "rofi -show drun"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "j", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "k", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "l", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "j", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "k", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "l", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn(browser), desc="browser"),
    Key([], "Print", lazy.spawn(screenshot), desc="screenshot"),
    Key([mod], "s", lazy.spawn(spotify), desc="spotify"),
    Key([mod], "t", lazy.spawn(rofi), desc="rofi"),
    
    # Volume keys control
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),

    # Brightness keys control
    #Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    #Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

groups = []

group_names = ["1", "2", "3", "4", "5",]
group_labels = ["", "", "", "", "",]
group_layouts = ["max", "monadtall", "columns", "max", "max",]



for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layout_theme = {"border_width": 2,
                "margin": 8,
                "border_focus": "1f1922",
                "border_normal": "1f1922"
                }


layouts = [
    #layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.Tile(shift_windows=True, **layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    #layout.Stack(num_stacks=2),
    layout.RatioTile(**layout_theme),
    #layout.TreeTab(),
]

# COLORS FOR THE BAR
colors = [
    ["612F80", "#612F80"],  # ACTIVE WORKSPACES 0
    ["#6A6A6A", "#6A6A6A"],  # INACTIVE WORKSPACES 1
    ["#CFCFCF", "#CFCFCF"],  # background lighter 2
    ["#FF8080", "#FF8080"],  # red 3
    ["#97D59B", "#97D59B"],  # green 4
    ["#FFFE80", "#FFFE80"],  # yellow 5
    ["#80D1FF", "#80D1FF"],  # blue 6
    ["#C780FF", "#C780FF"],  # magenta 7
    ["#80FFE4", "#80FFE4"],  # cyan 8
    ["#D5D5D5", "#D5D5D5"],  # white 9
    ["#4c566a", "#4c566a"],  # grey 10
    ["#d08770", "#d08770"],  # orange 11
    ["#8fbcbb", "#8fbcbb"],  # super cyan12
    ["#181E23", "#0E131A"],  # super blue 13
    ["#1f1922", "#1f1922"],  # super dark background 14
]

widget_defaults = dict(
    font="consolas bold",
    fontsize=16,
    padding=5,
    background=colors[14],
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[14],
                        background = colors[14]
                        ),
                widget.CurrentLayout(font="consolas bold",
                        fontsize = 16,
                        margin_y = 0,
                        margin_x = 0,
                        padding_y = 0,
                        padding_x = 0,
                        borderwidth = 0,
                        active = colors[0],
                        rounded = True,
                        highlight_color = colors[1],
                        this_screen_border = colors[1],
                        this_current_screen_border = colors[2],
                        foreground = colors[2],
                        background = colors[10]
                        ),
                widget.GroupBox(font="consolas bold",
                        fontsize = 40,
                        margin_y = 1,
                        margin_x = 5,
                        padding_y = 1,
                        padding_x = 5,
                        borderwidth = 10,
                        disable_drag = True,
                        active = colors[0],
                        inactive = colors[1],
                        rounded = True,
                        highlight_method = "block",
                        highlight_color = colors[1],
                        this_screen_border = colors[1],
                        this_current_screen_border = colors[2],
                        foreground = colors[1],
                        background = colors[14]
                        ),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                #widget.TextBox("default config", name="default"),
                #widget.TextBox("Arch", foreground="#d75f5f"),
                widget.Systray(),
                widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[14],
                        background = colors[14]
                        ),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                #widget.QuickExit(),
                widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[14],
                        background = colors[14]
                        ),
            ],
            24,
            #border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            #border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

cmd = [
        "setxkbmap latam",
        "feh --bg-fill /wallpaper/directory",
        "picom &",

]

for x in cmd:
    os.system(x)
