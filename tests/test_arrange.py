import sys,os
cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cwd, '../'))

try:
    from genenrich_report.arranger.arrange import arrange
except:
    pass

func = '/home/testData/geneEnrich_report/data/test.func.go.txt'
go = '/home/testData/geneEnrich_report/data/test.enrich.go.txt'
kegg = '/home/testData/geneEnrich_report/data/test.enrich.kegg.txt'


def test_arrange():
    parms = {}
    parms['func'] = func
    parms['go'] = go
    parms['kegg'] = kegg
    arrange(parms)


if __name__ == '__main__':
    test_arrange()
