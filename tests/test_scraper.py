from scraper import slugify


def test_slugify_basic():
    assert slugify("https://ladder7.in/about") == "ladder7_in_about"


def test_slugify_root_domain():
    assert slugify("https://example.com") == "example_com"


def test_slugify_trailing_slash():
    assert slugify("https://example.com/") == "example_com"


def test_slugify_empty_falls_back():
    assert slugify("") == "page"
