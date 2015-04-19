import os


def simple_ret(df, scalar, monitoring=None):

    ret = df.pct_change() + 3
    if monitoring:
        filepath = os.path.join(monitoring, "example.png")
        ax = ret.plot()
        fig = ax.get_figure()
        fig.savefig(filepath)
    return ret


if __name__ == "__main__":
    import mio
    params = mio.main_input("example")
    ret = simple_ret(**params)
    mio.write_output(ret, "example.csv")
