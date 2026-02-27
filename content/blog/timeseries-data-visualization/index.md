---
title: "Visualize time series data"
date: 2021-06-08
summary: "Reusable Python code for visualizing time series data from SCADA systems using Matplotlib."
categories:
  - Code Archive
tags:
  - visualization
  - personal tool
---

## Time series data

I need to work a lot with data from SCADA system. They are usually time series data. I just want to use this place as a archive to store the code I use to visualize the time series data.

## Code

```python

def date_selection(S_date, E_date, df_merge):
    '''
    select the dataset based on the time range.
    '''
    merge_s = df_merge.loc[(df_merge['Time']>=S_date)&
                           (df_merge['Time']<=E_date)].copy()
    return merge_s


def single_ts(ax, x_data, y_data, y_lable,
              y_legend = None,
              y_lim = None,
              color = None):
    '''
    plot the x and y data on a given axis
    add y range if given
    possible to have multiple lines.

    x_data: iterable, the x values, usually timestamps.

    y_data: list, each item in list contains a seperate dataset

    y_lable: string, the y axis lable

    y_legend: list, the length should be equal to y_data

    y_lim: list, the length is 2.

    color: list, containtsing the colors for each line

    '''
    for i, data in enumerate(y_data):

        if color and color[i]!=None:
            ax.plot(x_data, data, color = color[i])
        else:
            ax.plot(x_data, data )

    if y_legend:
        ax.legend(y_legend)

    if y_lim:
        ax.set_ylim(y_lim[0], y_lim[1])

    ax.set_ylabel(y_lable, fontsize=40)


def draw_ts_figure(data,
                   y_col,
                   y_lables,
                   y_col_legends,
                   color_dict = None,
                   y_lim_dict = None,
                   S_date=None,
                   E_date = None,
                   Ticks = None):
    '''
    To plot a figure with multiple axis

    data: dataframe

    y_col: list, the component in the list can also be a list,
           ex. ['aa', ['bb', 'cc'], dd]

    y_lables: list, the y lable name for each subplot

    y_col_legends: dict, key is the component in y_col

    color_dict: dict

    y_lim_dict: dict

    S_date: pd.Timestamp

    E_date: pd.Timestamp

    Ticks: list that holds pd.Timestamp

    '''

    # date interval selection
    if S_date and E_date:
        S = date_selection(S_date, E_date, data)
    else:
        S = data.copy()

    # number of axis shown in the figure
    num_ax = len(y_col)

    if len(y_lables) != num_ax:
        raise ValueError('The length of lables do not match')


    # initiate the picture settings
    fig, axs = plt.subplots(num_ax,1)
    fig.set_size_inches(w=(48),h=(40))
    plt.rcParams["font.family"] = "Times New Roman"
    plt.subplots_adjust(left=0.05, right=0.95, top=0.98,
                        bottom=0.1, hspace = 0.005)

    # iterate and draw subplots
    for i, ax in enumerate (axs.reshape(-1)):

        # convert y_col[i] to a list.
        if isinstance(y_col[i], list):
            cols = y_col[i]
        else:
            cols = [y_col[i]]


        # make a list to contain the columne data
        cols_data = [S[col] for col in cols]


        # make a list to contain the legend information
        legends_list = []
        for col in cols:
            if col in y_col_legends.keys():
                legends_list.append(y_col_legends[col])
            else:
                legends_list.append(None)

        # make a list to contain the color information
        if color_dict:
            color_list = []
            for col in cols:
                if col in color_dict.keys():
                    legends_list.append(color_dict[col])
                else:
                    legends_list.append(None)
        else:
            color_list = [None]*len(cols)


        # process to give a min and max value of y_lim
        if y_lim_dict:
            lim_list = []
            for col in cols:
                if col in y_lim_dict.keys():
                    lim_list = lim_list + y_lim_dict[col]
            if len(lim_list) > 0:
                y_lim = [min(lim_list), max(lim_list)]
            else:
                y_lim = None
        else:
            y_lim = None


        # draw the axis
        single_ts(ax, S['Time'], cols_data, y_lables[i],
                  y_legend =legends_list,
                  y_lim = y_lim,
                  color = color_list)

        # set xlable and ticks
        ax.set_xlim(S_date, E_date)
        if Ticks:
            ax.set_xticks(Ticks)
        ax.tick_params(axis='both', which='major', labelsize=40, right = True)
        ax.grid(axis = 'both', which = 'major')
        ax.grid(axis='x', which = 'minor')

        # if the last picture
        if i!= num_ax - 1:
            ax.set_xticklabels([])

    # save the picture
    name_string = ('4weeks_' +
              S_date.strftime('%y%m%d') +
              '-' + E_date.strftime('%y%m%d')
              + '.png')

    plt.savefig(name_string, format = 'png')
    print ('export: ' + name_string)
    plt.close()
```

## To use the code

```python
#%% Examples about how to use it to draw figures

y_cols = [['Signal_7', 'Signal_19'],
          'Signal_18',
          'Signal_6',
          'Signal_3']

y_lables= ['dp nät (bar',
           'tryck (bar)',
           'retur tryck (bar)',
           'fram tryck (bar)']

y_col_legends = {'Signal_7' : 'dp Sågvägen',
                 'Signal_19': 'dp Montaget',
                 'Signal_18': 'fram tryck dp Montaget'}


weeks = 4
S_date = pd.Timestamp(2021,2,1)
E_date = S_date + pd.Timedelta(weeks, unit='W')
Ticks = [S_date + pd.Timedelta(xx, unit='W') for xx in range(0,weeks)]
minor_ticks = [S_date + pd.Timedelta(xx, unit='day') for xx in range(0,weeks*7)]


draw_ts_figure(df_plc,
               y_cols,
               y_lables,
               y_col_legends,
               S_date=S_date,
               E_date = E_date,
               Ticks = Ticks)

```
