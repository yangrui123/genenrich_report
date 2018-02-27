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
# MF
ego = enrichGO(gene = x$ENTREZID,OrgDb = org.Hs.eg.db,ont = 'MF',pAdjustMethod = 'BH',pvalueCutoff = 0.01,qvalueCutoff = 0.05)
print(as.data.frame(ego))
if(tryCatch(plotGOgraph(ego), error=function(err){0})){
out1 = paste(prefix,"go.MF.net.enrich.png",sep='.')
Cairo(file=out1,type="png",units="in",bg="white",width=12, height=6, pointsize=12, dpi=300)
plotGOgraph(ego)
dev.off()}
# dotplot
if(typeof(ego)!='NULL'){
out2 = paste(prefix,"go.MF.dot.enrich.png",sep='.')
Cairo(file=out2,type="png",units="in",bg="white",width=12, height=6, pointsize=12, dpi=300)
dotplot(ego,showCategory=30)
dev.off()
outs = c(outs,out1,out2)
}
print(outs)
write.table(outs,paste(prefix, "enrich.go.txt", sep='.'),row.names = F,quote = F,col.names = F, sep="\t")




