-- lualine: require("lualine").setup({ options = { theme = "hell-pine" } })
local c = require("hell-pine.palette")
local cfg = require("hell-pine").config
local bg = cfg.transparent and "NONE" or c.crust
local function mode(colour)
	return {
		a = { fg = c.base, bg = colour, gui = "bold" },
		b = { fg = colour, bg = c.overlay },
		c = { fg = c.subtle, bg = bg },
	}
end
return {
	normal = mode(c.rose),
	insert = mode(c.foam),
	visual = mode(c.iris),
	replace = mode(c.love),
	command = mode(c.gold),
	terminal = mode(c.pine),
	inactive = {
		a = { fg = c.muted, bg = bg },
		b = { fg = c.muted, bg = bg },
		c = { fg = c.muted, bg = bg },
	},
}
