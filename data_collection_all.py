from urllib.request import urlopen
from json import loads
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)



""" Data Functions """

def admissions(unitid=None):
    base_url = "https://educationdata.urban.org/api/v1/college-university/ipeds/admissions-enrollment/summaries"
    admissions_data = None

    variables = ['number_applied', 'number_admitted', 'number_enrolled_total', 'number_enrolled_ft',
                 'number_enrolled_pt']
    for variable in variables:
        url = f"{base_url}?var={variable}&stat=sum&by=unitid&unitid={unitid}"

        response = urlopen(url)
        data = loads(response.read())

        df = pd.DataFrame(data['results'])
        df = df[['year', variable]]

        if admissions_data is None:
            admissions_data = df
        else:
            admissions_data = pd.merge(admissions_data, df, on='year', how='outer')

    return admissions_data

# admissions_data = admissions(unitid=169798)
# print(admissions_data)

def tuition_fees(unitid=None)-> pd.DataFrame:
    base_url = "https://educationdata.urban.org/api/v1/college-university/ipeds/academic-year-tuition/summaries"
    tuition_data = None

    variables = ['tuition_fees_ft', 'tuition_ft', 'fees_ft']
    for variable in variables:
        url = f"{base_url}?var={variable}&stat=avg&by=unitid&unitid={unitid}"

        response = urlopen(url)
        data = loads(response.read())

        df = pd.DataFrame(data['results'])
        df = df[['year', variable]]

        if tuition_data is None:
            tuition_data = df
        else:
            tuition_data = pd.merge(tuition_data, df, on='year', how='outer')

    return round(tuition_data, 2)

# tuition_data = tuition_fees()
# print(tuition_data)

def enrollment(unitid=None)-> pd.DataFrame:
    base_url = "https://educationdata.urban.org/api/v1/college-university/ipeds/fall-enrollment/race/summaries"
    enrollment_data = None

    dynamic_key = f'{unitid}_unitid'

    column_mapping = {
        '1_sex': 'Male',
        '2_sex': 'Female',
        '99_sex': 'Total',
        '1_race': 'White',
        '2_race': 'Black',
        '3_race': 'Hispanic',
        '4_race': 'Asian',
        '5_race': 'American Indian or Alaska Native',
        '6_race': 'Native Hawaiian or other Pacific Islander',
        '7_race': 'Two or more races',
        '8_race': 'Nonresident alien',
        '9_race': 'Unknown',
        '20_race': 'Other',
        '99_race': 'Total',
        dynamic_key: 'Total Enrollment',
        '1_level_of_study': 'Undergraduate',
        '2_level_of_study': 'Graduate',
        '99_level_of_study': 'Total UG and G',
        '1_ftpt': 'Full-time',
        '2_ftpt': 'Part-time',
        '99_ftpt': 'Total FT and PT'
    }

    variables = ['enrollment_fall']
    groups = ['unitid', 'sex', 'race', 'level_of_study', 'ftpt']

    for variable in variables:

        for group in groups:

            url = f"{base_url}?var={variable}&stat=avg&by={group}&unitid={unitid}"

            response = urlopen(url)
            data = loads(response.read())

            df = pd.DataFrame(data['results'])

            df = df[['year', group, variable]]

            df_pivot = df.pivot(index='year', columns=group, values=variable).reset_index()

            df_pivot.columns = ['year'] + [f'{col}_{group}' if col != 'year' else col for col in df_pivot.columns[1:]]

            if enrollment_data is None:
                enrollment_data = df_pivot
            else:
                enrollment_data = pd.merge(enrollment_data, df_pivot, on='year', how='outer')

    enrollment_data = enrollment_data.rename(columns=column_mapping)

    if '4_level_of_study' in enrollment_data.columns:
        enrollment_data = enrollment_data.drop(columns=['4_level_of_study'])

    return round(enrollment_data, 2)

# enrollment_data = enrollment(unitid=169248)
# print(enrollment_data)

def retention(unitid=None)-> pd.DataFrame:
    base_url = "https://educationdata.urban.org/api/v1/college-university/ipeds/fall-retention/summaries"
    retention_data = None

    variables = ['retention_rate', 'returning_students', 'prev_cohort']
    for variable in variables:
        url = f"{base_url}?var={variable}&stat=avg&by=unitid&unitid={unitid}"

        response = urlopen(url)
        data = loads(response.read())

        df = pd.DataFrame(data['results'])
        df = df[['year', variable]]

        if retention_data is None:
            retention_data = df
        else:
            retention_data = pd.merge(retention_data, df, on='year', how='outer')

    return round(retention_data, 2)

# retention_data = retention()
# print(retention_data)

def fin_ops(unitid=None)-> pd.DataFrame:
    base_url = "https://educationdata.urban.org/api/v1/college-university/ipeds/finance/summaries"
    financial_data = None

    variables = ['rev_tuition_fees_gross', 'sch_allowances_tuition_fees', 'rev_tuition_fees_net',
                 'rev_operating', 'rev_nonoperating', 'rev_total_current', 'sch_pell_grant',
                 'exp_instruc_total', 'exp_instruc_salaries']

    for variable in variables:
        url = f"{base_url}?var={variable}&stat=avg&by=unitid&unitid={unitid}"

        response = urlopen(url)
        data = loads(response.read())

        df = pd.DataFrame(data['results'])
        df = df[['year', variable]]

        if financial_data is None:
            financial_data = df
        else:
            financial_data = pd.merge(financial_data, df, on='year', how='outer')

    return round(financial_data, 2)

# financial_data = fin_ops()
# print(financial_data)

def fin_balance_sheet(unitid:int=169798):
    ...


""" Plot Functions """

def admissions_plots(admissions_data:pd.DataFrame):
    plt.figure(figsize=(12, 8))

    plt.plot(admissions_data['year'], admissions_data['number_applied'], label='Number Applied', marker='o')
    plt.plot(admissions_data['year'], admissions_data['number_admitted'], label='Number Admitted', marker='o')
    plt.plot(admissions_data['year'], admissions_data['number_enrolled_ft'], label='Number Enrolled Full-Time',
             marker='o')
    plt.plot(admissions_data['year'], admissions_data['number_enrolled_pt'], label='Number Enrolled Part-Time',
             marker='o')

    plt.title('EMU Applications & Admissions Over Time')
    plt.xlabel('Year')
    plt.ylabel('Number of Students')

    plt.legend()
    plt.grid(True)
    plt.show()

# admissions_data = admissions(unitid=169798)
# admissions_plots(admissions_data)

def enrollment_plots(enrollment_data:pd.DataFrame, unitid:int=169798):

    university_name = None
    for name, id in MASU.items():
        if id == unitid:
            university_name = name
            break

    if university_name is None:
        university_name = "Unknown University"

    # Plot 1: Enrollment, by Sex
    plt.figure(figsize=(10, 6))
    plt.plot(enrollment_data['year'], enrollment_data['Male'], label='Male', marker='o')
    plt.plot(enrollment_data['year'], enrollment_data['Female'], label='Female', marker='o')
    plt.plot(enrollment_data['year'], enrollment_data['Total Enrollment'], label='Total Enrollment', marker='o')
    plt.title(f'{university_name} Enrollment Over Time')
    plt.xlabel('Year')
    plt.ylabel('Number of Students')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot 2: Enrollment, by Level of Study
    plt.figure(figsize=(10, 6))
    plt.plot(enrollment_data['year'], enrollment_data['Undergraduate'], label='Undergraduate', marker='o')
    plt.plot(enrollment_data['year'], enrollment_data['Graduate'], label='Graduate', marker='o')
    plt.plot(enrollment_data['year'], enrollment_data['Total Enrollment'], label='Total Enrollment', marker='o')
    plt.title(f'{university_name} UG/G Enrollment Over Time')
    plt.xlabel('Year')
    plt.ylabel('Number of Students')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot 3: Enrollment, by Full-time/Part-time Status
    plt.figure(figsize=(10, 6))
    plt.plot(enrollment_data['year'], enrollment_data['Full-time'], label='Full-time', marker='o')
    plt.plot(enrollment_data['year'], enrollment_data['Part-time'], label='Part-time', marker='o')
    plt.plot(enrollment_data['year'], enrollment_data['Total Enrollment'], label='Total Enrollment', marker='o')
    plt.title(f'{university_name} Enrollment Over Time, by Full-time/Part-time Status')
    plt.xlabel('Year')
    plt.ylabel('Number of Students')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot 4: Enrollment by Race/Ethnicity
    plt.figure(figsize=(12, 8))
    plt.plot(enrollment_data['year'], enrollment_data['White'], label='White', marker='o')
    plt.plot(enrollment_data['year'], enrollment_data['Asian'], label='Asian', marker='o')
    plt.plot(enrollment_data['year'], enrollment_data['American Indian or Alaska Native'],
             label='American Indian or Alaska Native', marker='o')
    plt.plot(enrollment_data['year'], enrollment_data['Black'], label='Black', marker='o')
    plt.plot(enrollment_data['year'], enrollment_data['Hispanic'], label='Hispanic', marker='o')
    plt.plot(enrollment_data['year'], enrollment_data['Total Enrollment'], label='Total Enrollment', marker='o')
    plt.title(f'{university_name} Enrollment Over Time, By Race/Ethnicity')
    plt.xlabel('Year')
    plt.ylabel('Number of Students')
    plt.legend()
    plt.grid(True)
    plt.show()

# enrollment_data = enrollment(unitid=169798)
# enrollment_plots(enrollment_data)

