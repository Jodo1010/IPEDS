import pandas as pd
from openpyxl import Workbook

from data_collection_yearly import (
    admissions_yearly,
    admission_reqs_yearly,
    tuition_fees_yearly,
    fte_yearly,
    retention_yearly,
    finance_yearly,
    libraries_yearly
)
from references_helper import Reference

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


def master_function_yearly(unitid=169798, years=[2020]):
    university_name = None

    if Reference.ALL:
        for name, info in Reference.ALL.items():
            # Now correctly access the nested dictionary to check the unitid
            if info.get('unitid') == unitid:
                university_name = name
                break

    file_name = f'ipeds_yearly_data_{university_name if university_name else unitid}.xlsx'

    # Create an Excel writer object
    with pd.ExcelWriter(file_name, engine='openpyxl') as writer:

        # Admissions Data
        try:
            admissions_data = admissions_yearly(unitid=unitid, years=years)
            admissions_data.to_excel(writer, sheet_name='Admissions', index=False)
        except Exception as e:
            print(f"Error retrieving admissions data: {e}")

        # Admission Requirements Data
        try:
            admission_reqs_data = admission_reqs_yearly(unitid=unitid, years=years)
            admission_reqs_data.to_excel(writer, sheet_name='Admission_Requirements', index=False)
        except Exception as e:
            print(f"Error retrieving admission requirements data: {e}")

        # Tuition and Fees Data
        try:
            tuition_data = tuition_fees_yearly(unitid=unitid, years=years)
            tuition_data.to_excel(writer, sheet_name='Tuition_Fees', index=False)
        except Exception as e:
            print(f"Error retrieving tuition data: {e}")

        # FTE Data
        try:
            fte_data = fte_yearly(unitid=unitid, years=years)
            fte_data.to_excel(writer, sheet_name='FTE', index=False)
        except Exception as e:
            print(f"Error retrieving FTE data: {e}")

        # Retention Data
        try:
            retention_data = retention_yearly(unitid=unitid, years=years)
            retention_data.to_excel(writer, sheet_name='Retention', index=False)
        except Exception as e:
            print(f"Error retrieving retention data: {e}")

        # Financial Operations Data
        try:
            finance_data = finance_yearly(unitid=unitid, years=years)
            finance_data.to_excel(writer, sheet_name='Financial_Operations', index=False)
        except Exception as e:
            print(f"Error retrieving financial operations data: {e}")

        # Libraries Data
        try:
            libraries_data = libraries_yearly(unitid=unitid, years=years)
            libraries_data.to_excel(writer, sheet_name='Libraries', index=False)
        except Exception as e:
            print(f"Error retrieving libraries data: {e}")


        workbook = writer.book


if __name__ == "__main__":

    """ Below is an example """ 

    Reference.load_institution_data()  # Load institution map

    master_function_yearly(unitid=169798, years=[2014, 2015, 2016])
