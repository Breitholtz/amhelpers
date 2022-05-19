from amhelpers import amhelpers

def test_create_object_from_dict_1():
    import collections
    expected = collections.Counter()
    d = {'type': 'collections.Counter'}
    actual = amhelpers.create_object_from_dict(d)
    assert actual == expected

def test_create_object_from_dict_2():
    from datetime import timedelta
    expected = timedelta(
        days=100,
        hours=8,
        minutes=5,
        seconds=27,
    )
    d = {'type': 'datetime.timedelta', 'days': 100, 'seconds': 27}
    default_kwargs = {'days': 50, 'hours': 8, 'minutes': 5, 'seconds': 12}
    actual = amhelpers.create_object_from_dict(d, **default_kwargs)
    assert actual == expected
    