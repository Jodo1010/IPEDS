from urllib.request import urlopen
from json import loads

import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


""" Data Functions by Year """

def directory(unitid=None, year=2022):
    base_url = f"https://educationdata.urban.org/api/v1/college-university/ipeds/directory/{year}"

    response = urlopen(base_url)
    data = loads(response.read())

    df = pd.json_normalize(data['results'])

    df_unitid = df[df['unitid'] == unitid]

    df_unitid_short = df_unitid[
        ['year', 'unitid', 'fips', 'inst_name', 'address', 'state_abbr', 'zip', 'phone_number', 'city', 'county_name',
         'url_school', 'urban_centric_locale', 'region', 'chief_admin_name', 'chief_admin_title', 'degree_granting',
         'inst_control', 'institution_level', 'inst_size', 'hbcu', 'land_grant', 'title_iv_indicator', 'cc_basic_2000',
         'cc_basic_2015', 'cc_basic_2018', 'cc_basic_2021']]

    return df_unitid_short  # df_unitid

# inst_data = directory(unitid=169798, year=2022)
# print(inst_data)

def admissions_yearly(unitid=None, years=[2020]):

    all_admin_data = []
    for year in years:
        base_url = f"https://educationdata.urban.org/api/v1/college-university/ipeds/institutional-characteristics/{year}"

        response = urlopen(base_url)
        data = loads(response.read())

        df = pd.json_normalize(data['results'])

        df_unitid_year = df[(df['unitid'] == unitid) & (df['year'] == year)]

        all_admin_data.append(df_unitid_year)

        result = pd.concat(all_admin_data, ignore_index=True)

    return result

# admin_data = admissions_yearly(unitid=169798, years=[2018, 2019])
# print(admin_data)

def admission_reqs_yearly(unitid=None, years=[2020]):

    all_reqs_data = []

    for year in years:

        base_url = f"https://educationdata.urban.org/api/v1/college-university/ipeds/admissions-requirements/{year}"

        response = urlopen(base_url)
        data = loads(response.read())

        df = pd.json_normalize(data['results'])

        df_unitid_year = df[(df['unitid'] == unitid) & (df['year'] == year)]

        all_reqs_data.append(df_unitid_year)

        result = pd.concat(all_reqs_data, ignore_index=True)

    return result

# admin_reqs= admission_reqs_yearly(unitid=169798, years=[2018,2019])
# print(admin_reqs)

def tuition_fees_yearly(unitid=None, years=[2020]):

    all_tuition_data = []

    for year in years:
        base_url = f"https://educationdata.urban.org/api/v1/college-university/ipeds/academic-year-tuition/{year}"

        response = urlopen(base_url)
        data = loads(response.read())

        df = pd.json_normalize(data['results'])

        df_unitid_year = df[(df['unitid'] == unitid) & (df['year'] == year)]

        all_tuition_data.append(df_unitid_year)

        result = pd.concat(all_tuition_data, ignore_index=True)

    return result

# tuition = tuition_fees_yearly(unitid=169798, years=[2018, 2019])
# print(tuition)

def fte_yearly(unitid=None, years=[2020], level_of_study=1):

    all_fte_data = []

    for year in years:
        base_url = f"https://educationdata.urban.org/api/v1/college-university/ipeds/enrollment-full-time-equivalent/{year}/{level_of_study}/"

        response = urlopen(base_url)
        data = loads(response.read())

        df = pd.json_normalize(data['results'])

        df_unitid_year = df[(df['unitid'] == unitid) & (df['year'] == year)]

        all_fte_data.append(df_unitid_year)

        result = pd.concat(all_fte_data, ignore_index=True)

    return result

# fte = fte_yearly(unitid=169798, years=[2018,2019])
# print(fte)

def retention_yearly(unitid=None, years=[2020]):

    all_retention_data = []

    for year in years:
        base_url = f"https://educationdata.urban.org/api/v1/college-university/ipeds/fall-retention/{year}/"

        response = urlopen(base_url)
        data = loads(response.read())

        df = pd.DataFrame(data)
        df = pd.json_normalize(data['results'])

        df_unitid_year = df[(df['unitid'] == unitid) & (df['year'] == year)]

        all_retention_data.append(df_unitid_year)

        result = pd.concat(all_retention_data, ignore_index=True)

    return result

# retention = retention_yearly(unitid=169798, years=[2015,2016])
# print(retention)

def finance_yearly(unitid=None, years=[2017]):
    '''1979, 1983-2017 are available'''

    all_fin_data = []

    for year in years:
        base_url = f"https://educationdata.urban.org/api/v1/college-university/ipeds/finance/{year}/"

        response = urlopen(base_url)
        data = loads(response.read())

        df = pd.DataFrame(data)
        df = pd.json_normalize(data['results'])

        df_unitid_year = df[(df['unitid'] == unitid) & (df['year'] == year)]

        all_fin_data.append(df_unitid_year)

        result = pd.concat(all_fin_data, ignore_index=True)

    return result

# finance = finance_yearly(unitid=169798, years=[2016,2017])
# print(finance)

def libraries_yearly(unitid=None, years=[2020]):
    '''2013-2020 are available'''

    all_lib_data = []

    for year in years:
        base_url = f"https://educationdata.urban.org/api/v1/college-university/ipeds/academic-libraries/{year}/"

        response = urlopen(base_url)
        data = loads(response.read())

        df = pd.json_normalize(data['results'])

        df_unitid_year = df[(df['unitid'] == unitid) & (df['year'] == year)]

        all_lib_data.append(df_unitid_year)

        result = pd.concat(all_lib_data, ignore_index=True)

    return result

# lib = libraries_yearly(unitid=169798, years=[2018,2020])
# print(lib)

