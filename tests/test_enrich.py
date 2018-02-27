import sys,os
cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cwd,'../'))

from genenrich_report.enrichAnalys.enrich import enrich

enrichFile = 'data/whole.pop_protein.new.xls'
prefix = 'data/test'

def test_enrich():
    funcs,gos,kegg = enrich(enrichFile, prefix)


if __name__ == '__main__':
    test_enrich()
