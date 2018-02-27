import os
import config
from jbiot import log
import json


def arrange(parms):
    targetDir = parms['targetDir']
    goDir = os.path.join(targetDir, 'enrich/GO')
    keggDir = os.path.join(targetDir, 'enrich/KEGG')
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


def genTempltRendrParms(targetDir, func_pngs, go_pngs, kegg_pngs):
    out_dict = {}
    out_dict['func_pngs'] = func_pngs
    out_dict['go_pngs'] = go_pngs
    out_dict['kegg_pngs'] = kegg_pngs
    outfile = os.path.join(targetDir, "TempltRenderParms.json")
    fwp = open(outfile, 'w')
    fwp.write(json.dumps(out_dict))
    fwp.close()
    return outfile 


if __name__ == '__main__':
    import sys
    targetDir = sys.argv[1]
    func = sys.argv[2]
    go = sys.argv[3]
    kegg = sys.argv[4]    
    parms = {}
    parms['targetDir'] = targetDir
    parms['func'] = func
    parms['go'] = go
    parms['kegg'] = kegg
    arrange(parms)
