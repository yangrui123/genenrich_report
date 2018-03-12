#! /usr/bin/env Rscript

library(clusterProfiler)
library(Cairo)
library(org.Hs.eg.db)

args = commandArgs(T)
filename = args[1]
prefix = args[2]
dt = read.table(filename, sep='\t', header=T, fill=TRUE)
x = bitr(dt$Gene, fromType="SYMBOL", toType="ENTREZID", OrgDb="org.Hs.eg.db")
outs = c()
# GO enrich analysis
# CC
ego = enrichGO(gene = x$ENTREZIP, OrgDb = org.Hs.eg.db,ont = "CC",pAdjustMethod = 'BH',pvalueCutoff = 0.01,qvalueCutoff = 0.05)
# network
if(tryCatch(plotGOgraph(ego), error=function(err){0})){
out1 = paste(prefix,"go.CC.net.enrich.png",sep='.')
Cairo(file=out1,type="png",units="in",bg="white",width=12, height=6, pointsize=12, dpi=300) ;
print(plotGOgraph(ego))
dev.off()
# dotplot
out2 = paste(prefix,"go.CC.dot.enrich.png",sep='.')
Cairo(file=out2,type="png",units="in",bg="white",width=12, height=6, pointsize=12, dpi=300)
print(dotplot(ego,showCategory=30))
dev.off()
outs = c(outs,out1,out2)
}
# MF
ego = enrichGO(gene = x$ENTREZID,OrgDb = org.Hs.eg.db,ont = 'MF',pAdjustMethod = 'BH',pvalueCutoff = 0.01,qvalueCutoff = 0.05)
if(tryCatch(plotGOgraph(ego), error=function(err){0})){
out1 = paste(prefix,"go.MF.net.enrich.png",sep='.')
Cairo(file=out1,type="png",units="in",bg="white",width=12, height=6, pointsize=12, dpi=300)
print(plotGOgraph(ego))
dev.off()
# dotplot
out2 = paste(prefix,"go.MF.dot.enrich.png",sep='.')
Cairo(file=out2,type="png",units="in",bg="white",width=12, height=6, pointsize=12, dpi=300)
print(dotplot(ego,showCategory=30))
dev.off()
outs = c(outs,out1,out2)
}
#BP
ego = enrichGO(gene = x$ENTREZID,OrgDb = org.Hs.eg.db,ont = 'BP',pAdjustMethod = 'BH',pvalueCutoff = 0.01,qvalueCutoff = 0.05)
if(tryCatch(plotGOgraph(ego), error=function(err){0})){
out1 = paste(prefix,"go.BP.net.enrich.png",sep='.')
Cairo(file=out1,type="png",units="in",bg="white",width=12, height=6, pointsize=12, dpi=300)
print(plotGOgraph(ego))
dev.off()
# dotplot
out2 = paste(prefix,"go.BP.dot.enrich.png",sep='.')
Cairo(file=out2,type="png",units="in",bg="white",width=12, height=6, pointsize=12, dpi=300)
print(dotplot(ego,showCategory=30))
dev.off()
outs = c(outs,out1,out2)
}
write.table(outs,paste(prefix, "enrich.go.txt", sep='.'),row.names = F,quote = F,col.names = F, sep="\t")








