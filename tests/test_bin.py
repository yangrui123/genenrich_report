import sys,os
cwd = os.path.dirname(os.path.abspath(__file__))
geneEnrich_report = os.path.join(cwd, '../bin/geneEnrich_report.py')

parms = 'parms.yaml'

def test_bin():
    cmd = 'python %s  -c %s'%(geneEnrich_report, parms)
    os.system(cmd)

if __name__ == '__main__':
    test_bin()
