import sys,os
cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cwd,'../'))

from genenrich_report.report.report import report

targetDir = 'data/'

def test_report():
    report_dict = {'templt':os.path.join(targetDir, "TempltRenderParms.json"), 'targetDir':targetDir}
    report(report_dict)


if __name__ == '__main__':
    test_report()
