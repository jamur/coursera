#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter, A4

def generate(filename, title, additional_info, car_make_sales, table_data):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(additional_info, styles["BodyText"])
  table_style = [('GRID', (0,0), (-1,-1), 1, colors.black),
                ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                ('ALIGN', (0,0), (-1,-1), 'CENTER')]
  report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
  empty_line = Spacer(1,20)
  
  # Definir o tamanho do gráfico com base na largura da página
  page_width, _ = A4  # Obter a largura da página
  chart_width = page_width / 2
  chart_height = chart_width
  
  report_pie = Pie(witdth=chart_width, height=chart_height)
  report_pie.data = []
  report_pie.labels = []
  for car_make in sorted(car_make_sales):
    report_pie.data.append(car_make_sales[car_make])
    report_pie.labels.append(car_make)
  report_chart = Drawing(chart_width, chart_height)
  report_chart.add(report_pie)
  report_chart.width = chart_width
  report_chart.height = chart_height
  report_pie.width = chart_width
  report_pie.height = chart_height

  report.build([report_title, empty_line, report_info,
                empty_line, empty_line, empty_line,
                report_chart,
                empty_line, empty_line, empty_line,
                report_table])
