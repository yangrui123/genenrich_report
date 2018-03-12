#! /usr/bin/env python

import sys
import os
try:
    import config
except:
    pass

from jbiot import log
from jbiot import jbiotWorker

cwd = os.path.dirname(os.path.abspath(__file__))
arnge = os.path.join(cwd, 'enrich_arrange.py') 
if not os.path.exists(arnge):
    arnge = "/opt/enrich_arrange.py"


def arrange(parms):
    func = parms['func'] 
    go = parms['go']
    kegg = parms['kegg']
    cmd = "%s %s %s %s"%(arnge, func, go, kegg) 
    log.run('arranger', cmd)  
   

class ArngeWorker(jbiotWorker):
    def handle_task(self, key, params):
        self.execute(arrange, params) 
