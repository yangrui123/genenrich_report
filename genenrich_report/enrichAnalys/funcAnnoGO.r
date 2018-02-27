library(clusterProfiler)
library(Cairo)
library(org.Hs.eg.db)

args = commandArgs(T)
filename = args[1]
prefix = args[2]
dt = read.table(filename, sep='\t', header=T, fill=TRUE)
x = bitr(dt$Gene, fromType="SYMBOL", toType="ENTREZID", OrgDb="org.Hs.eg.db")
outs = c()
# CC
ggo = groupGO(gene=x$ENTREZID, OrgDb=org.Hs.eg.db, ont = 'CC', level=3, readable=TRUE)
out = paste(prefix,"go.CC.bar.func.png",sep='.')
Cairo(file=out,type="png",units="in",bg="white",width=12, height=6, pointsize=12, dpi=300)
if (typeof(ggo)!='NULL'){
print(barplot(ggo, drop=TRUE, showCategory=12))
outs = c(outs, out)
dev.off()
}
# MF
ggo = groupGO(gene=x$ENTREZID, OrgDb=org.Hs.eg.db, ont = 'MF', level=3, readable=TRUE)
if(typeof(ggo)!='NULL'){
out = paste(prefix,"go.MF.bar.func.png",sep='.')
Cairo(file=out,type="png",units="in",bg="white",width=12, height=6, pointsize=12, dpi=300)
print(barplot(ggo, drop=TRUE, showCategory=12))
outs = c(outs, out)
dev.off()
}
# BP
ggo = groupGO(gene=x$ENTREZID, OrgDb=org.Hs.eg.db, ont = 'BP', level=3, readable=TRUE)
if(typeof(ggo)!='NULL'){
out = paste(prefix,"go.BP.bar.func.png",sep='.')
Cairo(file=out,type="png",units="in",bg="white",width=12, height=6, pointsize=12, dpi=300)
print(barplot(ggo, drop=TRUE, showCategory=12))
outs = c(outs, out)
dev.off()
}
write.table(outs,paste(prefix, "func.go.txt", sep='.'),row.names = F,quote = F,col.names = F, sep="\t")


