"""Writes the terminal and tool themes in extras/ from lua/hell-pine/palette.lua, so every app gets the same colours.

    python3 scripts/extras.py
"""
import json, os, re

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
c = dict(re.findall(r'(\w+)\s*=\s*"(#[0-9a-fA-F]{6})"', open(os.path.join(HERE, "lua/hell-pine/palette.lua")).read()))
# The terminal's sixteen colours, as the VS Code theme sets them.
ansi = [c["black"], c["love"], c["pine"], c["gold"], c["foam"], c["iris"], c["rose"], c["text"]]
bright = [c["subtle"], c["love"], c["pine"], c["gold"], c["foam"], c["iris"], c["rose"], c["text"]]
NAMES = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]
HEADER = "Hell Pine, generated from lua/hell-pine/palette.lua by scripts/extras.py"


def write(path, text):
    full = os.path.join(HERE, "extras", path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w").write(text)
    print("wrote extras/" + path)


write("ghostty/hell-pine", f"# {HEADER}\n" + "".join(f"palette = {i}={col}\n" for i, col in enumerate(ansi + bright)) + f"""background = {c['crust']}
foreground = {c['text']}
cursor-color = {c['text']}
cursor-text = {c['base']}
selection-background = {c['hl_med']}
selection-foreground = {c['text']}
""")

write("wezterm/hell-pine.toml", f"""# {HEADER}
[colors]
foreground = "{c['text']}"
background = "{c['crust']}"
cursor_bg = "{c['text']}"
cursor_fg = "{c['base']}"
cursor_border = "{c['text']}"
selection_bg = "{c['hl_med']}"
selection_fg = "{c['text']}"
split = "{c['overlay']}"
ansi = [{', '.join(f'"{x}"' for x in ansi)}]
brights = [{', '.join(f'"{x}"' for x in bright)}]

[colors.tab_bar]
background = "{c['crust']}"

[colors.tab_bar.active_tab]
bg_color = "{c['overlay']}"
fg_color = "{c['text']}"

[colors.tab_bar.inactive_tab]
bg_color = "{c['crust']}"
fg_color = "{c['muted']}"

[metadata]
name = "Hell Pine"
origin_url = "https://github.com/abxengg/hell-pine.nvim"
""")

write("kitty/hell-pine.conf", f"# {HEADER}\nforeground {c['text']}\nbackground {c['crust']}\ncursor {c['text']}\ncursor_text_color {c['base']}\n"
      f"selection_foreground {c['text']}\nselection_background {c['hl_med']}\nactive_border_color {c['rose']}\ninactive_border_color {c['overlay']}\n"
      f"active_tab_foreground {c['text']}\nactive_tab_background {c['overlay']}\ninactive_tab_foreground {c['muted']}\ninactive_tab_background {c['crust']}\n"
      + "".join(f"color{i} {col}\n" for i, col in enumerate(ansi + bright)))

write("alacritty/hell-pine.toml", f"""# {HEADER}
[colors.primary]
background = "{c['crust']}"
foreground = "{c['text']}"

[colors.cursor]
text = "{c['base']}"
cursor = "{c['text']}"

[colors.selection]
text = "{c['text']}"
background = "{c['hl_med']}"

[colors.normal]
""" + "".join(f'{n} = "{x}"\n' for n, x in zip(NAMES, ansi)) + "\n[colors.bright]\n" + "".join(f'{n} = "{x}"\n' for n, x in zip(NAMES, bright)))

write("tmux/hell-pine.tmux", f"""# {HEADER}
# source-file /path/to/hell-pine.tmux   (in ~/.tmux.conf)
set -g status-style "fg={c['subtle']},bg=default"
set -g status-left-style "fg={c['rose']},bold"
set -g status-right-style "fg={c['muted']}"
set -g window-status-style "fg={c['muted']}"
set -g window-status-current-style "fg={c['rose']},bold"
set -g window-status-activity-style "fg={c['gold']}"
set -g window-status-bell-style "fg={c['love']},bold"
set -g pane-border-style "fg={c['overlay']}"
set -g pane-active-border-style "fg={c['rose']}"
set -g message-style "fg={c['text']},bg={c['overlay']}"
set -g message-command-style "fg={c['text']},bg={c['overlay']}"
set -g mode-style "fg={c['text']},bg={c['hl_med']}"
set -g display-panes-active-colour "{c['rose']}"
set -g display-panes-colour "{c['muted']}"
set -g clock-mode-colour "{c['rose']}"
""")

write("starship/hell-pine.toml", f"""# {HEADER}
# In starship.toml: palette = "hell_pine", then add this table. Styles can then say "bold rose", "foam" and so on.
[palettes.hell_pine]
""" + "".join(f'{k} = "{c[k]}"\n' for k in ["text", "subtle", "muted", "love", "gold", "rose", "pine", "foam", "iris", "overlay", "base"])
      + "".join(f'{n} = "{x}"\n' for n, x in zip(NAMES[1:7], ansi[1:7])))

btop = {
    "main_bg": "", "main_fg": c["text"], "title": c["text"], "hi_fg": c["rose"], "selected_bg": c["hl_med"], "selected_fg": c["text"],
    "inactive_fg": c["muted"], "graph_text": c["subtle"], "meter_bg": c["overlay"], "proc_misc": c["foam"], "cpu_box": c["pine"],
    "mem_box": c["foam"], "net_box": c["iris"], "proc_box": c["rose"], "div_line": c["overlay"], "temp_start": c["pine"], "temp_mid": c["gold"],
    "temp_end": c["love"], "cpu_start": c["pine"], "cpu_mid": c["foam"], "cpu_end": c["love"], "free_start": c["pine"], "free_mid": c["foam"],
    "free_end": c["foam"], "cached_start": c["iris"], "cached_mid": c["iris"], "cached_end": c["rose"], "available_start": c["gold"],
    "available_mid": c["gold"], "available_end": c["rose"], "used_start": c["rose"], "used_mid": c["love"], "used_end": c["love"],
    "download_start": c["pine"], "download_mid": c["foam"], "download_end": c["iris"], "upload_start": c["gold"], "upload_mid": c["rose"],
    "upload_end": c["love"], "process_start": c["pine"], "process_mid": c["gold"], "process_end": c["love"],
}
write("btop/hell-pine.theme", f"# {HEADER}\n" + "".join(f'theme[{k}]="{v}"\n' for k, v in btop.items()))

h = lambda k: c[k].lstrip("#")
write("fish/hell-pine.theme", f"""# name: 'Hell Pine'
# {HEADER}. Install: copy to ~/.config/fish/themes/, then: fish_config theme save "hell-pine"
fish_color_normal {h('text')}
fish_color_command {h('rose')}
fish_color_keyword {h('pine')}
fish_color_quote {h('gold')}
fish_color_redirection {h('iris')}
fish_color_end {h('subtle')}
fish_color_error {h('love')}
fish_color_param {h('text')}
fish_color_option {h('iris')}
fish_color_comment {h('muted')} --italics
fish_color_operator {h('subtle')}
fish_color_escape {h('rose')}
fish_color_autosuggestion {h('muted')}
fish_color_valid_path --underline
fish_color_selection --background={h('hl_med')}
fish_color_search_match --background={h('hl_med')}
fish_color_history_current --bold
fish_pager_color_progress {h('subtle')}
fish_pager_color_prefix {h('rose')} --bold
fish_pager_color_completion {h('text')}
fish_pager_color_description {h('muted')}
fish_pager_color_selected_background --background={h('hl_med')}
""")

zed_syntax = {
    "comment": {"color": c["muted"], "font_style": "italic"}, "comment.doc": {"color": c["muted"], "font_style": "italic"},
    "keyword": {"color": c["pine"]}, "string": {"color": c["gold"]}, "string.escape": {"color": c["rose"]},
    "string.regex": {"color": c["iris"]}, "number": {"color": c["rose"]}, "boolean": {"color": c["rose"]},
    "constant": {"color": c["pine"]}, "function": {"color": c["rose"]}, "type": {"color": c["foam"]},
    "constructor": {"color": c["foam"]}, "variable": {"color": c["text"]}, "variable.special": {"color": c["pine"]},
    "property": {"color": c["text"]}, "attribute": {"color": c["iris"], "font_weight": 700}, "tag": {"color": c["foam"]},
    "operator": {"color": c["subtle"]}, "punctuation": {"color": c["subtle"]}, "punctuation.bracket": {"color": c["subtle"]},
    "punctuation.delimiter": {"color": c["subtle"]}, "punctuation.special": {"color": c["pine"]}, "label": {"color": c["foam"]},
    "title": {"color": c["rose"], "font_weight": 700}, "link_text": {"color": c["foam"]}, "link_uri": {"color": c["iris"]},
    "emphasis": {"font_style": "italic"}, "emphasis.strong": {"font_weight": 700}, "text.literal": {"color": c["gold"]},
    "embedded": {"color": c["text"]}, "enum": {"color": c["foam"]}, "variant": {"color": c["pine"]}, "preproc": {"color": c["iris"]},
}
zed = {
    "$schema": "https://zed.dev/schema/themes/v0.2.0.json", "name": "Hell Pine", "author": "ABX",
    "themes": [{"name": "Hell Pine", "appearance": "dark", "style": {
        "background": c["crust"], "surface.background": c["base"], "elevated_surface.background": c["surface"],
        "editor.background": c["base"], "editor.foreground": c["text"], "editor.gutter.background": c["base"],
        "editor.active_line.background": c["hl_low"], "editor.line_number": c["line_nr"], "editor.active_line_number": c["text"],
        "editor.indent_guide": c["overlay"], "editor.indent_guide_active": c["muted"], "editor.document_highlight.read_background": c["hl_med"],
        "panel.background": c["crust"], "status_bar.background": c["crust"], "title_bar.background": c["crust"], "tab_bar.background": c["crust"],
        "tab.active_background": c["base"], "tab.inactive_background": c["crust"], "toolbar.background": c["base"],
        "border": c["overlay"], "border.variant": c["overlay"], "border.focused": c["muted"], "text": c["text"], "text.muted": c["subtle"],
        "text.placeholder": c["muted"], "text.accent": c["rose"], "icon": c["subtle"], "icon.accent": c["rose"],
        "element.background": c["overlay"], "element.hover": c["hl_med"], "element.selected": c["hl_med"], "ghost_element.hover": c["hl_low"],
        "ghost_element.selected": c["hl_med"], "scrollbar.thumb.background": c["hl_med"], "search.match_background": "#ca9f7c33",
        "terminal.background": c["crust"], "terminal.foreground": c["text"], "terminal.ansi.background": c["crust"],
        "error": c["love"], "warning": c["gold"], "info": c["foam"], "hint": c["subtle"], "success": c["pine"],
        "created": c["foam"], "modified": c["rose"], "deleted": c["love"], "conflict": c["gold"],
        "players": [{"cursor": c["text"], "selection": c["hl_med"], "background": c["rose"]}],
        "syntax": zed_syntax,
    }}],
}
for n, x, b in zip(NAMES, ansi, bright):
    zed["themes"][0]["style"][f"terminal.ansi.{n}"] = x
    zed["themes"][0]["style"][f"terminal.ansi.bright_{n}"] = b
write("zed/hell-pine.json", json.dumps(zed, indent=2) + "\n")
