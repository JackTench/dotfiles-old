-- Jack Tench 2023
-- Lua file to install plugins using the lazy neovim package manager.

return {

  -- Install folke's experimental UI plugin.
  -- TODO: Clean this up.
  {
    "folke/noice.nvim",
    event = "VeryLazy",
    opts = {
    },
    dependencies = {
      "MunifTanjim/nui.nvim",
      "rcarriga/nvim-notify",
    }
  },
  
  -- Install dracula vim theme. Fork by Mofiqul.
  {
    "Mofiqul/dracula.nvim",
    priority = 1000,
    config = function()
      vim.cmd("colorscheme dracula")
    end,
  },

  -- Install LuaLine.
  {
    "nvim-lualine/lualine.nvim",
    dependencies = {
      "nvim-tree/nvim-web-devicons"
    },
    config = function()
      require("lualine").setup({
        icons_enabled = true,
        theme = "dracula-nvim",
      })
    end,
  },

  -- Install ScrollView for a scroll bar.
  "dstein64/nvim-scrollview",

  -- Install a file tree.
  {
    "nvim-tree/nvim-tree.lua",
    version = "*",
    lazy = false,
    dependencies = {
      "nvim-tree/nvim-web-devicons",
    },
    config = function()
      require("nvim-tree").setup {}
    end,
  },

  -- Install comment plugin.
  "numToStr/Comment.nvim",

  -- Install keybind viewer.
  -- TODO: Clean this up. This is the install code from the github page.
  {
    "folke/which-key.nvim",
    event = "VeryLazy",
    init = function()
      vim.o.timeout = true
      vim.o.timeoutlen = 300
    end,
    opts = {},
  },

  -- Install LSP plugins.
  "williamboman/mason.nvim",
  "williamboman/mason-lspconfig.nvim",
  "neovim/nvim-lspconfig",

  -- Syntax highlighting.
  {
    "nvim-treesitter/nvim-treesitter",
    build = ':TSUpdate',
  },

}
