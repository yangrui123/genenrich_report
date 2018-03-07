import sys,os
cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cwd,'../'))

from genenrich_report.report.report import report


def test_report():
    report_dict = {'templtJson': "data/TempltRenderParms.json", 'template':'/home/testData/geneEnrich_report/enrich_template.md', 'resultsDirectory':'data/'}
    report(report_dict)


if __name__ == '__main__':
    test_report()
