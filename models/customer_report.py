from odoo import models

class CustomerProductReportXlsx(models.AbstractModel):
    _name = 'report.my_service.report_customer_product_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
        sheet = workbook.add_worksheet('Customer Products')
        bold = workbook.add_format({'bold': True})
        row = 0

        # Lägg till rubriker
        sheet.write(row, 0, 'Product', bold)
        sheet.write(row, 1, 'Quantity', bold)
        sheet.write(row, 2, 'Status', bold)
        sheet.write(row, 3, 'Location', bold)
        row += 1

        for partner in partners:
            for line in partner.order_line:
                sheet.write(row, 0, line.product_id.name)
                sheet.write(row, 1, line.product_uom_qty)
                sheet.write(row, 2, getattr(line.product_id, 'status', 'Unknown'))
                sheet.write(row, 3, getattr(line.product_id.location_id, 'name', 'Unknown'))
                row += 1
