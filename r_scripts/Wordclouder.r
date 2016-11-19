library(tm)
library(SnowballC)
library(wordcloud)
library(RColorBrewer)
print("running")
food <- read.csv("en.openfoodfacts.org.products.csv", header=TRUE, sep="\t", stringsAsFactors=FALSE, encoding="UTF-8")
options(max.print=20000000)
print("read csv")

myCorpus <- Corpus(VectorSource(food$allergens))

dtm <- TermDocumentMatrix(myCorpus)
m <- as.matrix(dtm)
v <- sort(rowSums(m),decreasing=TRUE)
d <- data.frame(word = names(v),freq=v)
head(d, 10)

print("we here now")

set.seed(1234)
wordcloud(words = d$word, freq = d$freq, min.freq = 1,
          max.words=50, random.order=FALSE, rot.per=0.35, 
          colors=brewer.pal(8, "Dark2"))
print("done")


