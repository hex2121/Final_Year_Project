import pandas as pd


class ExcelUtilities:

    # datavalidiation function
    def verify_excel_column_name(self, excel, column_lst: list):
        """
        return 1 if all the column in excel and column list are same here order are not considered
        :param excel: DataFrame
        :param column_lst: list
        :return: flag return integer 1 if all columns are same between excel and column list and
                if column are missing or extra then it returns name of missing and extra column

        """
        flag = ''

        if set(column_lst) == set(excel.columns):
            flag = 1
        else:
            missing_column = set(column_lst) - set(excel.columns)
            extra_column = set(excel.columns) - set(column_lst)

            if len(missing_column)>0:
                flag = f'missing column: {missing_column}'
            elif len(extra_column)>0:
                flag = flag + f'extra column: {extra_column}'

        return flag

    def verify_no_null_values(self, excel, column_lst: list):

        flag =1
        column_name_with_null_values = list()

        for i in column_lst:

            if excel[i].isna().sum()>0:
                flag = 0
                column_name_with_null_values.append(i)

        if flag==1:
            return flag

        else:
            return f'Column that contains null values -- {column_name_with_null_values}'

    def verify_excel_column_datatype(self, excel, column_lst: list):
        pass

    def verify_excel_column_contains_unique_value(self, excel, column_lst: list):

        col_lst_with_duplicate_value = []
        for i in column_lst:

            if excel[i].is_unique == False:
                col_lst_with_duplicate_value.append(i)

        if len(col_lst_with_duplicate_value) > 0:
            return col_lst_with_duplicate_value

        else:
            return 1

    def datetime_to_str(self, date, date_format="%m/%d/%Y"):
        return date.strftime(date_format)