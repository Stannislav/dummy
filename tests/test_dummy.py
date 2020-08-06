import dummy


class TestDummy:
    def test_hello(self):
        dummy.hello()

    def test_get_message(self):
        message = dummy.get_message()
        assert type(message) == str
        assert len(message) > 0
