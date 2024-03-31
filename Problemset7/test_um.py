import um

def test_um_appears_once():
    assert um.count("hello, um, world") == 1

def test_um_not_appears():
    assert um.count("yummy") == 0

def test_um_case_insensitive():
    assert um.count("Um um uM UM") == 4
