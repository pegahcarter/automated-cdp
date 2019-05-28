# File to create initial CSV of CDP and actions
from py.cdp import CDP

cdp = CDP(price=100)
cdp.__dict__

cdp.releverage(10)

cdp.__dict__
