import pandas as pd


def gen_data(seed):

    pd.np.random.seed(seed)
    idx = pd.date_range(start="2015-01-02", periods=10, freq="b")
    data = pd.np.random.randn(10, 3)
    df = pd.DataFrame(data, index=idx, columns=['A', 'B', 'C'])
    return df


if __name__ == "__main__":
    import mio
    params = mio.main_input("exampledata")
    df = gen_data(**params)
    mio.write_output(df, "example.csv")
