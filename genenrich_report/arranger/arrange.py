import os
try:
    import config
except:
    pass
from jbiot import log
from jbiot import jbiotWorker
import json


def arrange(parms):
    try:
        targetDir = parms['resultsDirectory']
    except:
        targetDir = './'
    goDir = os.path.join(targetDir, 'report/enrichAnalysis/GO')
    keggDir = os.path.join(targetDir, 'report/enrichAnalysis/KEGG')
    if not os.path.exists(goDir):
        cmd = "mkdir -p %s"%goDir
        os.system(cmd)
    if not os.path.exists(keggDir):
        cmd = "mkdir -p %s"%keggDir
        os.system(cmd)
    funcFiles = open(parms['func'], 'r').readlines()
    funcs = []
    for item in funcFiles:
        item = item.strip('\n')
        cmd = "mv %s %s" %(item, goDir)
        os.system(cmd)
        funcs.append(os.path.join(goDir, item.split('/')[-1]))
    goFiles = open(parms['go'], 'r').readlines()
    gos = []
    for item in goFiles:
        item = item.strip('\n')
        cmd = "mv %s %s" %(item, goDir)
        os.system(cmd)
        gos.append(os.path.join(goDir, item.split('/')[-1]))
    keggFiles = open(parms['kegg'], 'r').readlines()
    keggs = []
    for item in keggFiles:
        item = item.strip('\n')
        cmd = "mv %s %s" %(item, keggDir)
        os.system(cmd)
        keggs.append(os.path.join(keggDir, item.split('/')[-1]))
    out_dict = {}
    out_dict['func_pngs'] = funcs
    out_dict['go_pngs'] = gos
    out_dict['kegg_pngs'] = keggs
    outfile = os.path.join(targetDir, "TempltRenderParms.json")
    fwp = open(outfile, 'w')
    fwp.write(json.dumps(out_dict))
    fwp.close()


class ArrangeWorker(jbiotWorker):
    def handle_task(self, key, params):
        self.execute(arrange, params)


if __name__ == '__main__':
    import sys
    targetDir = sys.argv[1]
    funcFile = sys.argv[2]
    goFile = sys.argv[3]
    keggFile = sys.argv[4]    
    parms = {}
    parms['resultsDirectory'] = targetDir
    parms['func'] = funcFile
    parms['go'] = goFile
    parms['kegg'] = keggFile
    arrange(parms)
