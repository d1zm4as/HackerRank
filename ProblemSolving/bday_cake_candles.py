def birthdayCakeCandles(candles):
    a = max(candles)
    v_max = 0
    for x in candles:
        if x == a:
            v_max += 1
    return v_max
