'''
Module for approximating sqrt.
'''
def sqrt2(x):
    s = 1.
    kmax = 100
    tal = 1.e-14
    for k in range(kmax):
        print "Before iteration %s, s = %20.15f" % (k,s)
        s0 = s
        s = 0.5 * (s + x/s)
        delta_s = s - s0
        if abs(delta_s / x) < tal:
            break
    print "After %s iterations, s = %20.15f" % (k+1,s)
