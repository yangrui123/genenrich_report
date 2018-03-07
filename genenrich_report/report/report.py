try:
    from config import render, md2html
except:
    render = 'render.py'
    md2html = 'md2html.py'

from jbiot import log
import os
from jbiot import jbiotWorker

cwd = os.path.dirname(os.path.abspath(__file__))
enrichTemplt = os.path.join(cwd, 'enrich_template.md')


def report(parms):
    ijson = parms['templtJson']
    enrichTemplt = parms['template']
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
