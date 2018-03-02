import sys,os
cwd = os.path.dirname(os.path.abspath(__file__))
arrange = os.path.join(cwd, '../genenrich_report/arranger/arrange.py')
sys.path.append(os.path.join(cwd, '../'))

try:
    from genenrich_report import config
except:
    pass
from jbiot import log

targetDir = 'data/report/'
func = 'data/test.func.go.txt'
go = 'data/test.enrich.go.txt'
kegg = 'data/test.enrich.kegg.txt'


def test_arrange():
    parms = {}
    parms['targetDir'] = targetDir
    parms['func'] = func
    parms['go'] = go
    parms['kegg'] = kegg
    cmd = "python %s %s %s %s %s"%(arrange, targetDir, parms['func'], parms['go'], parms['kegg'])
    log.run('arranger',cmd)


if __name__ == '__main__':
    test_arrange()
