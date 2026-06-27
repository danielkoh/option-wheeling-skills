import math
from bsm import price, greeks, implied_vol

# S=100, K=100, T=0.25y, r=4%, sigma=20%, q=0
ARGS = dict(S=100.0, K=100.0, T=0.25, r=0.04, sigma=0.20, q=0.0)


def test_put_call_parity():
    c = price(right="call", **ARGS)
    p = price(right="put", **ARGS)
    lhs = c - p
    rhs = ARGS["S"] * math.exp(-ARGS["q"] * ARGS["T"]) - ARGS["K"] * math.exp(-ARGS["r"] * ARGS["T"])
    assert abs(lhs - rhs) < 1e-9


def test_price_increases_with_vol():
    low = price(right="call", **{**ARGS, "sigma": 0.10})
    high = price(right="call", **{**ARGS, "sigma": 0.40})
    assert high > low > 0


def test_right_aliases_match():
    assert price(right="c", **ARGS) == price(right="CALL", **ARGS)
    assert price(right="p", **ARGS) == price(right="Put", **ARGS)


def test_greeks_signs_and_ranges():
    gc = greeks(right="call", **ARGS)
    gp = greeks(right="put", **ARGS)
    assert 0.0 < gc["delta"] < 1.0
    assert -1.0 < gp["delta"] < 0.0
    assert gc["gamma"] > 0 and gp["gamma"] > 0
    assert gc["vega"] > 0 and gp["vega"] > 0
    # call theta is typically negative for these params
    assert gc["theta"] < 0


def test_implied_vol_roundtrips():
    target = price(right="call", **ARGS)
    iv = implied_vol(target, S=100.0, K=100.0, T=0.25, r=0.04, right="call", q=0.0)
    assert abs(iv - 0.20) < 1e-4
