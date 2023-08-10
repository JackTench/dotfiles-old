-- Jack Tench 2023
-- Options and preferences for neovim, but in lua.

-- TODO: Document or comment this mess.

local opt = vim.opt

opt.mouse = 'a'
opt.clipboard = 'unnamedplus'

opt.number = true
opt.relativenumber = false
opt.termguicolors = true
opt.ignorecase = true
opt.showmatch = true

opt.expandtab = true
opt.shiftwidth = 2
opt.tabstop = 2
opt.smartindent = true


