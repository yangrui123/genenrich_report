#! /usr/bin/env python

from jbiot import log
from jbiot import jbiotWorker
import sys,os
cwd = os.path.dirname(os.path.abspath(__file__))
funcAnnoGO = os.path.join(cwd, 'funcAnnoGO.r')
if not os.path.exists(funcAnnoGO):
    funcAnnoGO = "/opt/funcAnnoGO.r"
enrichGO = os.path.join(cwd, 'enrichGO.r')
if not os.path.exists(enrichGO):
    enrichGO = "/opt/enrichGO.r"
enrichKEGG = os.path.join(cwd, 'enrichKEGG.r') 
if not os.path.exists(enrichKEGG):
    enrichKEGG = "/opt/enrichKEGG.r"


def enrich(parms):
    enrichFile = parms['enrichFile']
    prefix = parms['prefix']
    cmd = "%s %s %s"%(funcAnnoGO, enrichFile, prefix)
    log.run('func annotation', cmd)
    cmd = "%s %s %s"%(enrichGO, enrichFile, prefix)
    log.run('GO enrich analysis', cmd)
    cmd = "%s %s %s"%(enrichKEGG, enrichFile, prefix)
    log.run('KEGG enrich analysis', cmd)
    #func_outs = []
    #suffixs = ['go.CC.bar.func.png', 'go.MF.bar.func.png', 'go.BP.bar.func.png']
    #for item in suffixs:
     #   func_outs.append(prefix+'.'+item)
    #goEnrich_outs = []
    #suffixs = ['go.CC.net.enrich.png', 'go.MF.net.enrich.png', 'go.BP.net.enrich.png', 'go.CC.dot.enrich.png', 'go.MF.dot.enrich.png', 'go.BP.dot.enrich.png']
    #for item in suffixs:
    #    goEnrich_outs.append(prefix+'.'+item)
    #kegg_out = prefix+'.kegg.enrich.png'
    func = prefix+'.func.go.txt'
    go = prefix+'.enrich.go.txt'
    kegg = prefix+'.enrich.kegg.txt'
    out_dict = {'func':func, 'go':go, 'kegg':kegg}
    return out_dict


class EnrichWorker(jbiotWorker):
    def handle_task(self, key, params):
        self.execute(enrich, params)

