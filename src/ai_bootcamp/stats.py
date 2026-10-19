"""最基础的两个统计量——故意手写，不用 numpy。"""


def mean(xs: list[float]) -> float:
    """算术平均。空列表直接报错，别悄悄返回 0。"""
    if not xs:
        raise ValueError("mean() 需要非空序列")
    return sum(xs) / len(xs)


def var(xs: list[float]) -> float:
    """总体方差（除以 n，不是 n-1）。"""
    if not xs:
        raise ValueError("var() 需要非空序列")
    m = mean(xs)
    return sum((x - m) ** 2 for x in xs) / len(xs)
