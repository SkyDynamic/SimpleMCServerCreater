from qfluentwidgets import ScrollArea

from ...utils.properties_handler import Properties

default_config = {
    "enable-jmx-monitoring": "false",
    "rcon.port": 25575,
    "rcon.password": "",
    "level-seed": "",
    "gamemode": "survival",
    "enable-command-block": "false",
    "enable-query": "false",
    "generator-settings": {},
    "enforce-secure-profile": "true",
    "level-name": "world",
    "motd": "A Minecraft Server",
    "query.port": 25565,
    "pvp": "true",
    "generate-structures": "true",
    "max-chained-neighbor-updates": 1000000,
    "difficulty": "easy",
    "network-compression-threshold": 256,
    "max-tick-time": 60000,
    "require-resource-pack": "false",
    "use-native-transport": "true",
    "max-players": 20,
    "online-mode": "true",
    "enable-status": "true",
    "allow-flight": "false",
    "initial-disabled-packs": "",
    "broadcast-rcon-to-ops": "true",
    "view-distance": 10,
    "server-ip": "",
    "resource-pack-prompt": "",
    "allow-nether": "true",
    "server-port": 25565,
    "enable-rcon": "false",
    "sync-chunk-writes": "true",
    "op-permission-level": 4,
    "prevent-proxy-connections": "false",
    "hide-online-players": "false",
    "resource-pack": "",
    "entity-broadcast-range-percentage": 100,
    "simulation-distance": 10,
    "player-idle-timeout": "",
    "force-gamemode": "false",
    "rate-limit": "",
    "hardcore": "false",
    "white-list": "false",
    "broadcast-console-to-ops": "true",
    "spawn-npcs": "true",
    "spawn-animals": "true",
    "log-ips": "true",
    "function-permission-level": 2,
    "initial-enabled-packs": "vanilla",
    "level-type": "minecraft:normal",
    "text-filtering-config": "",
    "spawn-monsters": "true",
    "enforce-whitelist": "false",
    "spawn-protection": 16,
    "resource-pack-sha1": "",
    "max-world-size": 29999984
}

class GameConfigPage(ScrollArea):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setObjectName("server_config_page")
        ...
