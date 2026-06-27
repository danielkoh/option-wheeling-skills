"""Self-contained Black-Scholes-Merton reference implementation (MIT, stdlib-only).

Conventions (match the options-math skill):
  T in years; sigma, r, q annualized; r continuously-compounded; q dividend yield;
  vega per 1.00 vol (not per 1%); theta per year.

This is a compact reference for verifying the skill's formulas — not a production engine.
"""
from __future__ import annotations
import math

_CALL = {"c", "call"}
_PUT = {"p", "put"}


def _norm_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def _norm_pdf(x: float) -> float:
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def _d1_d2(S, K, T, r, sigma, q):
    vol_t = sigma * math.sqrt(T)
    d1 = (math.log(S / K) + (r - q + 0.5 * sigma * sigma) * T) / vol_t
    return d1, d1 - vol_t


def _norm_right(right: str) -> str:
    r = right.strip().lower()
    if r in _CALL:
        return "call"
    if r in _PUT:
        return "put"
    raise ValueError(f"right must be call/c or put/p, got {right!r}")


def price(S, K, T, r, sigma, right, q=0.0) -> float:
    side = _norm_right(right)
    d1, d2 = _d1_d2(S, K, T, r, sigma, q)
    df_q, df_r = math.exp(-q * T), math.exp(-r * T)
    if side == "call":
        return S * df_q * _norm_cdf(d1) - K * df_r * _norm_cdf(d2)
    return K * df_r * _norm_cdf(-d2) - S * df_q * _norm_cdf(-d1)


def greeks(S, K, T, r, sigma, right, q=0.0) -> dict:
    side = _norm_right(right)
    d1, d2 = _d1_d2(S, K, T, r, sigma, q)
    df_q, df_r = math.exp(-q * T), math.exp(-r * T)
    pdf_d1 = _norm_pdf(d1)
    gamma = df_q * pdf_d1 / (S * sigma * math.sqrt(T))
    vega = S * df_q * pdf_d1 * math.sqrt(T)  # per 1.00 vol
    if side == "call":
        delta = df_q * _norm_cdf(d1)
        theta = (
            -(S * df_q * pdf_d1 * sigma) / (2 * math.sqrt(T))
            - r * K * df_r * _norm_cdf(d2)
            + q * S * df_q * _norm_cdf(d1)
        )
        rho = K * T * df_r * _norm_cdf(d2)
    else:
        delta = -df_q * _norm_cdf(-d1)
        theta = (
            -(S * df_q * pdf_d1 * sigma) / (2 * math.sqrt(T))
            + r * K * df_r * _norm_cdf(-d2)
            - q * S * df_q * _norm_cdf(-d1)
        )
        rho = -K * T * df_r * _norm_cdf(-d2)
    return {
        "price": price(S, K, T, r, sigma, side, q),
        "delta": delta,
        "gamma": gamma,
        "vega": vega,    # per 1.00 vol
        "theta": theta,  # per year
        "rho": rho,
    }


def implied_vol(target_price, S, K, T, r, right, q=0.0, lo=1e-6, hi=5.0, tol=1e-8, max_iter=200) -> float:
    """Solve sigma by bisection so price() matches target_price."""
    side = _norm_right(right)
    for _ in range(max_iter):
        mid = 0.5 * (lo + hi)
        diff = price(S, K, T, r, mid, side, q) - target_price
        if abs(diff) < tol:
            return mid
        # price is monotonically increasing in sigma
        if diff > 0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)
