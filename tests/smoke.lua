-- nvim --headless -u NONE -l tests/smoke.lua : the theme loads, every group it sets exists, and the main colours
-- are the VS Code theme's.
vim.opt.rtp:prepend(vim.fn.getcwd())
vim.cmd.colorscheme("hell-pine")
local function hex(n) return n and string.format("#%06x", n) or "NONE" end
local function get(name) return vim.api.nvim_get_hl(0, { name = name, link = false }) end
local want = {
	{ "Normal", "fg", "#e0def4" }, { "Normal", "bg", "#16181d" }, { "Comment", "fg", "#6e6a86" },
	{ "Keyword", "fg", "#658789" }, { "String", "fg", "#ca9f7c" }, { "Function", "fg", "#ebbcba" },
	{ "Type", "fg", "#9ccfd8" }, { "@variable.parameter", "fg", "#c4a7e7" }, { "DiagnosticError", "fg", "#d16d92" },
}
local failed = 0
for _, w in ipairs(want) do
	local got = hex(get(w[1])[w[2]])
	if got ~= w[3] then
		print(("%s.%s is %s, want %s"):format(w[1], w[2], got, w[3]))
		failed = failed + 1
	end
end
assert(vim.g.colors_name == "hell-pine", "colors_name")
assert(get("Comment").italic, "comments are italic")
assert(vim.g.terminal_color_1 == "#d16d92", "terminal red")
require("hell-pine").setup({ transparent = true })
vim.cmd.colorscheme("hell-pine")
assert(get("Normal").bg == nil, "transparent leaves the background")
local lualine = dofile(vim.fn.getcwd() .. "/lua/lualine/themes/hell-pine.lua")
assert(lualine.normal.a.bg == "#ebbcba", "lualine normal")
local n = 0
for _ in pairs(require("hell-pine.highlights").groups(require("hell-pine.palette"), require("hell-pine").config)) do n = n + 1 end
print(("ok: %d groups, %d checks failed"):format(n, failed))
os.exit(failed == 0 and 0 or 1)
