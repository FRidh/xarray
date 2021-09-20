from xarray.backends.plugins import get_backend, list_engines

def test_get_backend__engine():
    """Test passing in a a backend name (engine) gets us an instance of the corresponding backend."""
    engine = "netcdf4"
    engines = list_engines()
    backend = get_backend(engine)
    assert backend == engines[engine]


def test_get_backend__backend():
    """Test passing in a backend directly gets us an instance of that backend."""
    engine = "netcdf4"
    given_backend = list_engines()["netcdf4"].__class__
    assert type(given_backend()) is type(get_backend(given_backend))
