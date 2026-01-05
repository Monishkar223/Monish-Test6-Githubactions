from main import Add

class TestAdd:
    def test_add_class(self):
        obj = Add(6, 2)
        assert obj.add_one() == 8
    def test_sub_class(self):
        obj = Add(6, 2)
        assert obj.sub_one() == 4
    def test_mul_class(self):
        obj = Add(6, 2)
        assert obj.mul_one() == 12
