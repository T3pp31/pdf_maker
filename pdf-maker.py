from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
import reportlab.lib.units as unit
import reportlab.lib.pagesizes as pagesizes

pdfmetrics.registerFont(UnicodeCIDFont("HeiseiKakuGo-W5"))

pdf=canvas.Canvas("example.pdf",pagesize=pagesizes.A4)

title="好きな文字を入力"

for moji in title:　#pdfに一文字ずつtitleに書いた文字を出力する
    pdf.setFont("HeiseiKakuGo-W5",210*unit.mm)
    h=(297-210)/2*unit.mm

    pdf.drawString(0*unit.mm,h,moji)
    pdf.showPage()

pdf.save()
