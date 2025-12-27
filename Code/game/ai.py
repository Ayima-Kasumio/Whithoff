"""
AI for Whithoff variant using Sprague-Grundy (mex) computation.
Provides compute_sg(maxA, maxB, regle) and choose_move(regle, nb_A, nb_B).
"""

from typing import List, Tuple


def mex(s: set) -> int:
    """Minimum excludant of a set of non-negative integers."""
    m = 0
    while m in s:
        m += 1
    return m


def compute_sg(maxA: int, maxB: int, regle: List[int]):
    """Compute Sprague-Grundy table SG[a][b] for 0..maxA and 0..maxB.

    SG[a][b] = mex of reachable SG values after any legal move:
      - remove n from A only (if a>=n)
      - remove n from B only (if b>=n)
      - remove n from both A and B (if a>=n and b>=n)
    """
    # Ensure regle is a list of positive integers
    reg = sorted(set([n for n in regle if n > 0]))
    SG = [[0] * (maxB + 1) for _ in range(maxA + 1)]

    for a in range(maxA + 1):
        for b in range(maxB + 1):
            reachable = set()
            for n in reg:
                if a >= n:
                    reachable.add(SG[a - n][b])
                if b >= n:
                    reachable.add(SG[a][b - n])
                if a >= n and b >= n:
                    reachable.add(SG[a - n][b - n])
            SG[a][b] = mex(reachable)
    return SG


def choose_move(regle: List[int], nb_A: int, nb_B: int) -> Tuple[int, int]:
    """Choose a move (cA, cB) for the computer. If a winning move exists,
    return a move that leads to a position with SG==0. Otherwise return a
    reasonable fallback legal move, or (0,0) if no move is possible.
    """
    # Filter and sort rules
    reg = sorted(set([n for n in regle if n > 0]))
    if not reg:
        return 0, 0

    # Quick check: is there any legal move at all?
    any_legal = any((nb_A >= n) or (nb_B >= n) or (nb_A >= n and nb_B >= n) for n in reg)
    if not any_legal:
        return 0, 0

    SG = compute_sg(nb_A, nb_B, reg)
    if SG[nb_A][nb_B] == 0:
        # Already a P-position: no forced win. Return a fallback legal move.
        for n in reg:
            if nb_A >= n:
                return n, 0
            if nb_B >= n:
                return 0, n
            if nb_A >= n and nb_B >= n:
                return n, n
        return 0, 0

    # Find a move that moves to an SG == 0 position
    for n in reg:
        if nb_A >= n and SG[nb_A - n][nb_B] == 0:
            return n, 0
        if nb_B >= n and SG[nb_A][nb_B - n] == 0:
            return 0, n
        if nb_A >= n and nb_B >= n and SG[nb_A - n][nb_B - n] == 0:
            return n, n

    # Fallback
    for n in reg:
        if nb_A >= n:
            return n, 0
        if nb_B >= n:
            return 0, n
        if nb_A >= n and nb_B >= n:
            return n, n
    return 0, 0


# If this module is run directly, a tiny self test
if __name__ == '__main__':
    # simple test rule
    reg = [1, 2, 3]
    for a in range(6):
        for b in range(6):
            SG = compute_sg(a, b, reg)
    print('AI module loaded')
