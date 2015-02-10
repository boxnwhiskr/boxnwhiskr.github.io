import pylab


def bnw_boxplot(*args, **kwargs):
    defaults = {}
    defaults['boxprops'] = dict(
        linewidth=pylab.rcParams['lines.linewidth'],
        color=pylab.rcParams['lines.color']
    )
    defaults['whiskerprops'] = dict(
        linestyle='--',
        linewidth=0.5,
        color=pylab.rcParams['lines.color']
    )
    defaults['capprops'] = dict(
        linewidth=pylab.rcParams['lines.linewidth'],
        color=pylab.rcParams['lines.color']
    )
    defaults['medianprops'] = dict(
        linewidth=pylab.rcParams['lines.linewidth'],
        color=pylab.rcParams['lines.color']
    )
    defaults['flierprops'] = dict(
        markeredgewidth=pylab.rcParams['lines.linewidth'],
        linewidth=pylab.rcParams['lines.linewidth'],
        color=pylab.rcParams['lines.color']
    )

    for k, v in defaults.items():
        if k in kwargs:
            kwargs[k].update(v)
        else:
            kwargs[k] = v

    return pylab.boxplot(*args, **kwargs)
