#!/bin/python2.7
# coding:utf-8
__author__ = 'yangrui'

import sys, os
cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(cwd,'../'))


from genenrich_report.enrichAnalys.enrich import enrich
from genenrich_report.report.report import report
from genenrich_report.arranger.arrange import arrange
try:
    from genenrich_report import config
except:
    pass
from jbiot import log
import yaml
import json
from jbiot import jbiotWorker


def enrichAnalysis(parms):
    enrichFiles = parms['enrichFiles']
    for prefix in enrichFiles:
        tmp = {'enrichFile':enrichFiles[prefix], 'prefix':prefix}
        out_dict = enrich(tmp)
    try:
        targetDir = parms['resultsDirectory']
    except:
        targetDir = './'
    out_dict['resultsDirectory'] = targetDir
    return out_dict


def arngeReport(parms):
    targetDir = parms['resultsDirectory']
    arrange(parms)
    report_dict = {'templtJson':os.path.join(targetDir, "TempltRenderParms.json"), 'template':parms['template'], 'resultsDirectory':targetDir}
    report(report_dict)


def main(parms):
    template = parms['enrich_template']
    parms = enrichAnalysis(parms)
    parms['template'] = template
    arngeReport(parms)


class EnrichWorker(jbiotWorker):
    def handle_task(self, key, params):
        self.execute(main, params)


if __name__ == '__main__':
    usage = '''
Usage:
    geneEnrich_report.py -c <parameters>

Options:
    -h --help
    -c,--parameter=parms      parameters with yaml format
'''
    from docopt import docopt
    args = docopt(usage)
    parmYaml = args['--parameter']
    parms = yaml.load(open(parmYaml))
    main(parms)

