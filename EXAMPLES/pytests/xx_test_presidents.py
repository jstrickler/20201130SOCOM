from president import President


def test_president_one_is_gw():
    p = President(1)
    assert p.first_name == 'George'
    assert p.last_name == 'Washington'



