def hurdleRace(k, height):
    if k> max(height):
        return 0 
    return max(height)-k
