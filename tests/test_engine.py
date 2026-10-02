"""改名测试"""
import pytest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from src.engine import RenameSystem, Player

class TestRename:
    def test_sensitive_word(self):
        rs = RenameSystem()
        rs.players = {"p1": Player("p1","old",10,0,[])}
        assert not rs.can_rename("p1", "违禁词"), "敏感词未检查"

    def test_history_recorded(self):
        rs = RenameSystem()
        rs.players = {"p1": Player("p1","old",10,0,[])}
        rs.used_names = set()
        rs.rename("p1", "new")
        assert "old" in rs.players["p1"].name_history, "历史未记录"
