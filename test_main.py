from main import Add

class TestAdd:
    def test_add_class(self):
        obj = Add(6, 2)
        assert obj.add_one() == 8
