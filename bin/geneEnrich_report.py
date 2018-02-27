#!/bin/python2.7
# coding:utf-8
__author__ = 'yangrui'

import sys, os
cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cwd,'../'))
arrange = os.path.join(cwd, '../genenrich_report/arranger/arrange.py')

from genenrich_report.enrichAnalys.enrich import enrich
from genenrich_report.report.report import report
from genenrich_report import config
from jbiot import log
import yaml
import json


def enrichAnalysis(parms):
    enrichFiles = parms['enrichFiles']
    for enrichFile, prefix in enrichFiles:
        tmp = {'enrichFile':enrichFile, 'prefix':prefix}
        out_dict = enrich(tmp)
    out_dict['targetDir'] = parms['resultsDirectory']
    return out_dict


def arngeReport(parms):
    targetDir = parms['targetDir']
    cmd = "python %s %s %s %s %s"%(arrange, targetDir, parms['func'], parms['go'], parms['kegg'])
    log.run('arranger',cmd)
    report_dict = {'templt':os.path.join(targetDir, "TempltRenderParms.json"), 'targetDir':targetDir}
    report(report_dict)


if __name__ == '__main__':
    usage = '''
Usage:
    geneEnrich_report.py [-h | --help]
    geneEnrich_report.py -c <parameters>

Options:
    -h --help
    -c parms --parameter=parms      parameters 
'''
    from docopt import docopt
    args = docopt(usage)
    parmYaml = args['--parameter']
    parms = yaml.load(open(parmYaml))
    parms = enrichAnalysis(parms)
    arngeReport(parms)

