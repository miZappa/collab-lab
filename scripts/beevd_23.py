"""Exponential smoothing forecast."""
def exponential_smoothing(xs, alpha=0.3):
    result = [xs[0]]
    for x in xs[1:]:
        result.append(round(alpha * x + (1 - alpha) * result[-1], 4))
    return result
if __name__ == "__main__":
    data = [10, 12, 13, 12, 15]
    print(exponential_smoothing(data))
