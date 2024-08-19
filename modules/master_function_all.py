import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import Workbook
from openpyxl.drawing.image import Image
from io import BytesIO

from data_collection_all import admissions, tuition_fees, enrollment, retention, fin_ops
# from data_collection_all import MASU
from data_collection_yearly import directory
from references_helper import Reference



def master_function(unitid=169798):

    university_name = None
    for name, id in Reference.get_masu().items():
        if id == unitid:
            university_name = name
            break

    file_name = f'ipeds_data_{university_name if university_name else unitid}.xlsx'

    # Create an Excel writer object
    with pd.ExcelWriter(file_name, engine='openpyxl') as writer:

        directory_data = directory(unitid=unitid)
        directory_data.to_excel(writer, sheet_name='Directory', index=False)

        admissions_data = admissions(unitid=unitid)
        admissions_data.to_excel(writer, sheet_name='Admissions', index=False)

        tuition_data = tuition_fees(unitid=unitid)
        tuition_data.to_excel(writer, sheet_name='Tuition_Fees', index=False)

        enrollment_data = enrollment(unitid=unitid)
        enrollment_data.to_excel(writer, sheet_name='Enrollment', index=False)

        retention_data = retention(unitid=unitid)
        retention_data.to_excel(writer, sheet_name='Retention', index=False)

        financial_data = fin_ops(unitid=unitid)
        financial_data.to_excel(writer, sheet_name='Financial_Operations', index=False)

        workbook = writer.book



if __name__ == "__main__":
    master_function(unitid=169798)  # defaults to EMU
    # master_function(unitid=169248)  # Central Michigan University
    # master_function(unitid=171571)  # Oakland University

    # for university_name, unitid in MASU.items():
    #     master_function(unitid=unitid)