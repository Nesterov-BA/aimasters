def get_df_info(df, *args, **kwargs):
    '''
    docstring example:

    Выводит инфу о колонках датафрейма в виде датафрейма

    df: исходный датафрейм
    ...
    
    returns: pd.DataFrame с инфой

    '''
    import pandas as pd
    import numpy as np
    cols = ["dtype",	"nunique",	"example_1",	"example_2",	"zero",	"nan",	"empty_str",	"vc_max",	"trash_score"]
    output = pd.DataFrame(columns=cols)
    ind = df.columns
    types = df.dtypes
    output["dtype"] = types
    output.index = ind
    #in each column find number of unique values
    output["nunique"] = df.nunique()
    #in each column find number of zeros
    output["zero"] = np.trunc(1000*df.isin([0]).sum()/len(df))/1000
    #in each column find number of nans divided by number of rows
    #truncate to 3 decimal places
    output["empty_str"] = np.trunc(1000*df.isin(['']).sum()/len(df))/1000
    output["nan"] = np.trunc(1000*df.isna().sum()/len(df))/1000
    output["vc_max"] = np.trunc(1000*df.apply(lambda x: x.value_counts().max()/len(df)))/1000
    output["trash_score"] = output["zero"] + output["nan"] + output["empty_str"]
    output["trash_score"]=output["trash_score"].replace(0, "-1")
    output["zero"]=output["zero"].replace(0, "-1")
    output["nan"]=output["nan"].replace(0, "-1")
    output["empty_str"]=output["empty_str"].replace(0, "-1")
    #generate two random numbers from 0 to len(df)

    
    output["example_1"] = df.apply(lambda x: x.iloc[0])
    output["example_2"] = df.apply(lambda x: x.iloc[1])
    return output

def plot_density(df, hue = None, cols=None):
    '''
    Рисует распределения колонок cols

    cols: отрисовываемые колонки. Если None, то рисуем df.columns (кроме hue)

    ...

    '''
    try:
        import seaborn as sns
    except ImportError:
        raise ImportError("Please install seaborn using: pip install seaborn")
    import matplotlib.pyplot as plt
    import numpy as np
    # your code here
    if cols is None:
        cols = df.columns
    cols = [col for col in cols if col != hue]
    for column in cols:
        if df.dtypes[column] == 'int64' or df.dtypes[column] == 'float64':
            fig, ax = plt.subplots(1, 2)
            #create a title for the plot
            plt.suptitle(column)
            #drop zero values
            # df = df[df[column] != 0]
            #drop nan values
            df = df[df[column] != np.inf]
            if len(df[column]) > 200:
                df = df.sample(200)
            sns.histplot(data=df, x=column, hue=hue, ax=ax[0])
            sns.boxenplot(data=df, y=column, hue=hue, ax=ax[1], showfliers=False)
        elif df[column].nunique() < 20:
            plt.figure()
            plt.suptitle(column)

            sns.countplot(data=df, x=column, hue=hue)
        
    pass