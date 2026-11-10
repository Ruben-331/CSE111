import names


def test_make_full_name():
    assert names.make_full_name("Anna", "Smith") == "Smith; Anna"
    assert names.make_full_name("George", "Washington") == "Washington; George"
    assert names.make_full_name("Ava", "Smith-Jones") == "Smith-Jones; Ava"


def test_extract_family_name():
    assert names.extract_family_name("Brown; Sally") == "Brown"
    assert names.extract_family_name("Washington; George") == "Washington"
    assert names.extract_family_name("Smith-Jones; Ava") == "Smith-Jones"

def test_extract_given_name():
    assert names.extract_given_name("Brown; Sally") == "Sally"
    assert names.extract_given_name("Washington; George") == "George"
    assert names.extract_given_name("Smith-Jones; Ava") == "Ava"
    