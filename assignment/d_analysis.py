
def gdp_top(data):
    """

    :param data: data
    :return: table with top 5 gdp per capita for each year
    """
    cords = data.groupby(["Year"])["Gdp per Capita"].nlargest().index.get_level_values(1).tolist()
    emissions_table = data.iloc[cords, [0, 1, 3, -1]].reset_index(drop=True)
    return emissions_table


def emissions_top(data):
    """

        :param data: data
        :return: table with top 5 emissions per capita for each year
        """
    cords = data.groupby(["Year"])["Emissions per Capita"].nlargest().index.get_level_values(1).tolist()
    emissions_table = data.iloc[cords, [0, 1, 5, 4]].reset_index(drop=True)
    return emissions_table


# Function that measures changes in emission per capita in last 10 years present in supplied dataframe
def emission_balance(data):
    """

        :param data: data
        :return: table with emissions change in recent 10 years
        """
    if len(data.Year.unique()) >= 10:
        years = [0, 0]
        years[0], years[1] = data.Year.unique()[-1], data.Year.unique()[-11]
        loss = data[data.Year.isin(years)]
        loss.loc[loss.Year.isin([years[1]]), ['Emissions per Capita']] \
            = loss[loss.Year.isin([years[1]])]['Emissions per Capita'].apply(lambda x: -x)
        r1 = loss.groupby(['Country Name'])["Emissions per Capita"].sum().nlargest()
        r2 = loss.groupby(['Country Name'])["Emissions per Capita"].sum().nsmallest()
        return [r1, r2]

    else:
        return "Data time interval too small"
