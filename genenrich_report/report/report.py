#! /usr/bin/env python

try:
    from config import render
    from config import md2html
except:
    render = 'render.py'
    md2html = 'md2html.py'

from jbiot import log
import os
from jbiot import jbiotWorker


def get_templt(remotefile):
    home = os.environ["HOME"]
    localfile = remotefile.split("/")[-1]
    cmd = "wget %s -P %s/.templates " % (home,remotefile)

    localfile1 = os.path.join(home,".templates",localfile)
    localfile2 = os.path.join("~",".templates",localfile)
    if os.path.exists(localfile1):
        return localfile1
    os.system(cmd)
    return localfile1


def report(parms):
    ijson = parms['templtJson']
    enrichTemplt = parms['template']
    if enrichTemplt.startswith("http://"):
        enrichTemplt =get_templt(enrichTemplt)

    try:
        targetDir = parms['resultsDirectory']
    except:
        targetDir = './'
    out = os.path.join(targetDir,"geneEnrich_report.md")
    cmd = "%s -t %s -j %s -o %s" %(render, enrichTemplt, ijson, out)
    log.run("generating cancer drug report templete", cmd)
    cmd = "%s %s"%(md2html, out)
    log.run("generating mapping report", cmd)


class ReportWorker(jbiotWorker):
    def handle_task(self, key, params):
        self.execute(report, params)
