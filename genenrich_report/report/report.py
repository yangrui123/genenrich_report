from config import render
import config
from jbiot import log
import os
from config import md2html

cwd = os.path.dirname(os.path.abspath(__file__))
enrichTemplt = os.path.join(cwd, 'enrich_template.md')


def report(parms):
    ijson = parms['templt']
    targetDir = parms['targetDir']
    out = os.path.join(targetDir,"geneEnrich_report.md")
    cmd = "python %s -t %s -j %s -o %s" %(render, enrichTemplt, ijson, out)
    log.run("generating cancer drug report templete", cmd)
    cmd = "python %s %s"%(md2html, out)
    log.run("generating mapping report", cmd)
