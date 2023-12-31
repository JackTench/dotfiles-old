-- Jack Tench 2023
-- Treesitter config.

require('nvim-treesitter.configs').setup {

  ensure_installed = {
    "vim",
    "vimdoc",
    "lua",
  },

  auto_install = true,
  highlight = { enable = true },
  indent = { enable = true },

}
