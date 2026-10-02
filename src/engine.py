"""改名系统 - 带6个bug"""
from dataclasses import dataclass, field
import time

@dataclass
class Player:
    pid: str
    name: str
    level: int
    vip: int
    name_history: list

class RenameSystem:
    def __init__(self):
        self.players: dict[str, Player] = {}
        self.used_names = set()
        self.last_rename = {}

    def can_rename(self, pid, new_name):
        p = self.players[pid]
        # bug1: 不检查敏感词
        if new_name in self.used_names:
            return False
        # bug2: 固定冷却
        if pid in self.last_rename and time.time() - self.last_rename[pid] < 604800:
            return False
        # bug4: 不检查等级
        return True

    def rename(self, pid, new_name):
        p = self.players[pid]
        old = p.name
        p.name = new_name
        self.used_names.add(new_name)
        # bug3: 不记录历史
        self.last_rename[pid] = time.time()
        # bug5: 不同步好友/公会
        return True

    def validate_name(self, name):
        # bug6: 只检查空格
        return " " not in name
