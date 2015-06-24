def fit_diff(a, b):# a is the fit_finc and b is ydata
    z = np.zeros(b.size)
    for i in range(0, b.size-1):
        z[i] = (a[i]- b[i])/(b[i])
    return z
