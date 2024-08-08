Usage
=====

.. doctest::

    >>> import geosub

    >>> geosub.lookup('US', '10001')
    SubdivisionHierarchy(code='US-NY', country_code='US', name='New York', ..., type='State')

    >>> geosub.lookup('CA', 'M5H 2N2')
    SubdivisionHierarchy(code='CA-ON', country_code='CA', name='Ontario', ..., type='Province')

    >>> geosub.lookup('FR', '75001')
    SubdivisionHierarchy(code='FR-11', country_code='FR', name='Aude', ..., type='Metropolitan department')

    >>> geosub.lookup('AU', '2000')
    SubdivisionHierarchy(code='AU-NSW', country_code='AU', name='New South Wales', ..., type='State')

    >>> geosub.lookup('GB', 'SW1A 1AA')
    SubdivisionHierarchy(code='GB-ENG', country_code='GB', name='England', ..., type='Country')

    >>> geosub.lookup('BR', '01000-000')
    SubdivisionHierarchy(code='BR-SP', country_code='BR', name='São Paulo', ..., type='State')

    >>> geosub.lookup('IN', '110001')
    SubdivisionHierarchy(code='IN-DL', country_code='IN', name='Delhi', ..., type='Union territory')

    >>> geosub.lookup('RU', '101000')
    SubdivisionHierarchy(code='RU-MOW', country_code='RU', name='Moskva', ..., type='Autonomous city')

    >>> geosub.lookup('JP', '100-0001')
    SubdivisionHierarchy(code='JP-40', country_code='JP', name='Fukuoka', ..., type='Prefecture')

    >>> geosub.lookup('DE', '10115')
    SubdivisionHierarchy(code='DE-BE', country_code='DE', name='Berlin', ..., type='Land')

If `lookup()` does not find a subdivision, it returns `None`.

It's important to handle this possibility in your code:

.. doctest::

    >>> print(geosub.lookup('XX', '99999'))
    None
