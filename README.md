# Hell Pine for Neovim

A darker, higher-contrast take on [Rosé Pine](https://rosepinetheme.com/), born inside tmux. This is the Neovim
port of the [Hell Pine VS Code theme](https://github.com/abxengg/hell-pine): the same colours, the same choices
(keywords pine, types foam, functions rose, strings gold, parameters iris, errors love, comments muted and italic),
and the same language-server colours.

It also carries matching themes for your terminal and tools in [`extras/`](extras): Ghostty, WezTerm, kitty,
Alacritty, tmux, Starship, btop, fish, Zed and fzf.

## Install

[lazy.nvim](https://github.com/folke/lazy.nvim):

```lua
{
    "abxengg/hell-pine.nvim",
    lazy = false,
    priority = 1000,
    config = function()
        require("hell-pine").setup({ transparent = false })
        vim.cmd.colorscheme("hell-pine")
    end,
}
```

Any other plugin manager works too: put the repository on the runtime path and run `:colorscheme hell-pine`.

## Options

```lua
require("hell-pine").setup({
    transparent = false,  -- leave the background to the terminal (for a translucent window)
    italic = true,        -- comments, library functions, quotes
    bold = true,          -- annotations, headings, the mode in the status line
    dim_inactive = false, -- darken windows without the cursor
    styles = {            -- per kind: comments, keywords, functions, strings, types, variables
        comments = { italic = true },
    },
    on_highlights = function(hl, c) -- change any group; c is the palette
        hl.CursorLineNr = { fg = c.rose, bold = true }
    end,
})
```

The palette is `require("hell-pine").palette()`.

## Status line

[lualine](https://github.com/nvim-lualine/lualine.nvim): `require("lualine").setup({ options = { theme = "hell-pine" } })`.

## Supported

Tree-sitter, language-server semantic tokens, diagnostics, and the plugins people use most: gitsigns, telescope,
which-key, lazy, mason, indent-blankline, nvim-tree, neo-tree, flash, fidget, noice, blink.cmp, nvim-cmp, mini,
trouble and nvim-dap. The terminal inside Neovim gets the same sixteen colours.

## Extras

| Tool | File | How |
|---|---|---|
| Ghostty | `extras/ghostty/hell-pine` | copy to `~/.config/ghostty/themes/hell-pine`, then `theme = hell-pine` |
| WezTerm | `extras/wezterm/hell-pine.toml` | copy to `~/.config/wezterm/colors/`, then `config.color_scheme = "Hell Pine"` |
| kitty | `extras/kitty/hell-pine.conf` | `include hell-pine.conf` in `kitty.conf` |
| Alacritty | `extras/alacritty/hell-pine.toml` | `[general] import = ["…/hell-pine.toml"]` |
| tmux | `extras/tmux/hell-pine.tmux` | `source-file …/hell-pine.tmux` in `~/.tmux.conf` |
| Starship | `extras/starship/hell-pine.toml` | add the table to `starship.toml`, then `palette = "hell_pine"` |
| btop | `extras/btop/hell-pine.theme` | copy to `~/.config/btop/themes/`, then `color_theme = "hell-pine"` |
| fish | `extras/fish/hell-pine.theme` | copy to `~/.config/fish/themes/`, then `fish_config theme save hell-pine` |
| Zed | `extras/zed/hell-pine.json` | copy to `~/.config/zed/themes/`, then pick Hell Pine |
| fzf | `extras/fzf/hell-pine.sh` | source it in `~/.zshrc` or `~/.bashrc` |

They are all made from `lua/hell-pine/palette.lua` by `python3 scripts/extras.py`; change the palette there and run
it again.

## Development

`nvim --headless -u NONE -l tests/smoke.lua` loads the theme and checks its main colours against the VS Code
theme. CI runs it on every push, and checks that `extras/` matches the palette.

## Licence

MIT, like the VS Code theme.
