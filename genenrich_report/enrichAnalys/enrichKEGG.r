#! /usr/bin/env Rscript
library(clusterProfiler)
library(Cairo)
library(org.Hs.eg.db)

args = commandArgs(T)
filename = args[1]
prefix = args[2]
dt = read.table(filename, sep='\t', header=T, fill=TRUE)
x = bitr(dt$Gene, fromType="SYMBOL", toType="ENTREZID", OrgDb="org.Hs.eg.db")
# KEGG enrich analysis
kk = enrichMKEGG(x$ENTREZID, organism = 'hsa',pvalueCutoff = 0.05,pAdjustMethod = 'BH',qvalueCutoff = 0.1)
out = ''
if(typeof(kk)!='NULL'){
y <- setReadable(kk, 'org.Hs.eg.db', keytype="ENTREZID")
out = paste(prefix,"kegg.enrich.png",sep='.')
Cairo(file=out,type="png",units="in",bg="white",width=12, height=6, pointsize=12, dpi=300)
print(dotplot(kk,showCategory=30))
dev.off()}
write.table(out,paste(prefix, "enrich.kegg.txt", sep='.'),row.names = F,quote = F,col.names = F, sep="\t")

