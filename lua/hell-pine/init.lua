-- Hell Pine for Neovim: a darker, higher-contrast take on Rosé Pine, the same theme as the VS Code one.
local M = {}

M.config = {
	transparent = false, -- leave the background to the terminal (for a translucent window)
	italic = true, -- comments, library functions, quotes
	bold = true, -- annotations, headings, the mode in the status line
	dim_inactive = false, -- darken windows without the cursor
	-- styles = { comments = { italic = true }, keywords = {}, functions = {}, ... } overrides per group kind
	styles = {},
	-- on_highlights = function(hl, c) hl.Normal = { fg = c.text } end, to change any group after the theme set it
	on_highlights = nil,
}

function M.setup(opts)
	M.config = vim.tbl_deep_extend("force", M.config, opts or {})
end

function M.palette()
	return require("hell-pine.palette")
end

function M.load()
	if vim.g.colors_name then
		vim.cmd("hi clear")
	end
	if vim.fn.exists("syntax_on") == 1 then
		vim.cmd("syntax reset")
	end
	vim.o.termguicolors = true
	vim.o.background = "dark"
	vim.g.colors_name = "hell-pine"
	local c = M.palette()
	local groups = require("hell-pine.highlights").groups(c, M.config)
	if M.config.on_highlights then
		M.config.on_highlights(groups, c)
	end
	for name, spec in pairs(groups) do
		vim.api.nvim_set_hl(0, name, spec)
	end
	local term = {
		c.black, c.love, c.pine, c.gold, c.foam, c.iris, c.rose, c.text,
		c.subtle, c.love, c.pine, c.gold, c.foam, c.iris, c.rose, c.text,
	}
	for i, colour in ipairs(term) do
		vim.g["terminal_color_" .. (i - 1)] = colour
	end
end

return M
