import xlsxwriter

workbook = xlsxwriter.Workbook('hello.xlsx')

worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Hello...')
worksheet.write('B1', 'World')

workbook.close()
