import math

def dft(x):
    X = []
    N = len(x)
    for k in range(N):
        re = 0
        im = 0
        for n in range(N):
            c = 2 * math.pi * k * n / N
            re += x[n] * math.cos(c)
            im -= x[n] * math.sin(c)
        re = re / N
        im = im / N
        
        
        freq = k
        amp = math.sqrt(re*re + im*im)
        phase = math.atan2(im, re)
        
        X.append((re, im, freq, amp, phase));
        
    return X