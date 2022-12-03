

local networking = require "networking"
local server = require "server"

networking.setup()
server.begin(80)
