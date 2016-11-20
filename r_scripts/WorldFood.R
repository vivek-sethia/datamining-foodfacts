#load csv file
WorldFood <- read.csv("FoodWorld.csv", header = TRUE, stringsAsFactors = FALSE, sep = "\t")

#increase max print
options(max.print = 20000000)

#replace blank cells into NA
WorldFood[WorldFood == ""] <- NA

#count NA in dataset
sum(is.na(WorldFood))

#send output to a file
sink("countries.txt")
WorldFood$countries[grep("^[^en:]", WorldFood$countries)]
sink()

#replace a countries column to appropriate filling
WorldFood$countries[WorldFood$countries == "France"] <- "en:FR"
WorldFood$countries[WorldFood$countries == "france"] <- "en:FR"
WorldFood$countries[WorldFood$countries == "United Kingdom"] <- "en:GB"
WorldFood$countries[WorldFood$countries == "United States"] <- "en:US"
WorldFood$countries[WorldFood$countries == "US"] <- "en:US"
WorldFood$countries[WorldFood$countries == "Usa"] <- "en:US"
WorldFood$countries[WorldFood$countries == "USA"] <- "en:US"
WorldFood$countries[WorldFood$countries == "États-Unis"] <- "en:US"
WorldFood$countries[WorldFood$countries == "Australia"] <- "en:AU"
WorldFood$countries[WorldFood$countries == "Singapore"] <- "en:SI"
WorldFood$countries[WorldFood$countries == "中華民國"] <- "en:TW"
WorldFood$countries[WorldFood$countries == "España"] <- "en:ES"
WorldFood$countries[WorldFood$countries == "Germany"] <- "en:DE"
WorldFood$countries[WorldFood$countries == "Deutschland"] <- "en:DE"
WorldFood$countries[WorldFood$countries == "France,United Kingdom"] <- "en:FR, en:GB"
WorldFood$countries[WorldFood$countries == "Royaume-Uni,France"] <- "en:FR, en:GB"
WorldFood$countries[WorldFood$countries == "Switzerland"] <- "en:CH"
WorldFood$countries[WorldFood$countries == "Belgium"] <- "en:BE"
WorldFood$countries[WorldFood$countries == "Ireland"] <- "en:IE"
WorldFood$countries[WorldFood$countries == "Belgique,France,Pays-Bas,Royaume-Uni"] <- "en:BE, en:FR, en:NL, en:GB"
WorldFood$countries[WorldFood$countries == "Australie"] <- "en:AU"
WorldFood$countries[WorldFood$countries == "Nederland"] <- "en:NL"
WorldFood$countries[WorldFood$countries == "New Zealand"] <- "en:NZ"
WorldFood$countries[WorldFood$countries == "Canada"] <- "en:CA"
WorldFood$countries[WorldFood$countries == "Belgique"] <- "en:BE"
WorldFood$countries[WorldFood$countries == "الولايات المتحدة"] <- "en:US"
WorldFood$countries[WorldFood$countries == "Sénégal"] <- "en:SN"
WorldFood$countries[WorldFood$countries == "Senegal"] <- "en:SN"
WorldFood$countries[WorldFood$countries == "Allemagne,Belgique"] <- "en:DE, en:BE"
WorldFood$countries[WorldFood$countries == "Germany,United Kingdom,United States"] <- "en:DE, en:GB, en:US"
WorldFood$countries[WorldFood$countries == "Germany,Netherlands,Austria"] <- "en:DE, en:NL, en:AT"
WorldFood$countries[WorldFood$countries == "Suisse"] <- "en:CH"
WorldFood$countries[WorldFood$countries == "Denmark"] <- "en:DK"
WorldFood$countries[WorldFood$countries == "Poland"] <- "en:PL"
WorldFood$countries[WorldFood$countries == "France,Poland"] <- "en:FR, en:PL"
WorldFood$countries[WorldFood$countries == "Poland,United Kingdom"] <- "en:PL, en:GB"
WorldFood$countries[WorldFood$countries == "Canada,United States"] <- "en:CA, en:US"
WorldFood$countries[WorldFood$countries == "United Kingdom,France"] <- "en:GB, en:FR"
WorldFood$countries[WorldFood$countries == "United Arab Emirates"] <- "en:AE"
WorldFood$countries[WorldFood$countries == "France,Royaume-Uni"] <- "en:FR, en:GB"
WorldFood$countries[WorldFood$countries == "United states"] <- "en:US"
WorldFood$countries[WorldFood$countries == "Spanien,Denmark"] <- "en:ES, en:DK"
WorldFood$countries[WorldFood$countries == "Indonesia"] <- "en:ID"
WorldFood$countries[WorldFood$countries == "Россия"] <- "en:RU"
WorldFood$countries[WorldFood$countries == "Россия"] <- "en:RU"
WorldFood$countries[WorldFood$countries == "Portugal"] <- "en:PT"
WorldFood$countries[WorldFood$countries == "Italia"] <- "en:IT"
WorldFood$countries[WorldFood$countries == "Italie"] <- "en:IT"
WorldFood$countries[WorldFood$countries == "Turkey"] <- "en:TR"
WorldFood$countries[WorldFood$countries == "Österreich"] <- "en:AT"
WorldFood$countries[WorldFood$countries == "Germany,Australia"] <- "en:DE, en:AU"
WorldFood$countries[WorldFood$countries == "Australia,Germany"] <- "en:DE, en:AU"
WorldFood$countries[WorldFood$countries == "Germany,Switzerland"] <- "en:DE, en:CH"
WorldFood$countries[WorldFood$countries == "Allemagne,Suisse"] <- "en:DE, en:CH"
WorldFood$countries[WorldFood$countries == "Allemagne,suisse"] <- "en:DE, en:CH"
WorldFood$countries[WorldFood$countries == "Austria"] <- "en:AT"
WorldFood$countries[WorldFood$countries == "Brasil"] <- "en:BR"
WorldFood$countries[WorldFood$countries == "Belgique,France"] <- "en:BL, en:FR"
WorldFood$countries[WorldFood$countries == "Magyarország"] <- "en:HU"
WorldFood$countries[WorldFood$countries == "Espagne"] <- "en:ES"
WorldFood$countries[WorldFood$countries == "Guadeloupe"] <- "en:GP"
WorldFood$countries[WorldFood$countries == "Spanien"] <- "en:ES"
WorldFood$countries[WorldFood$countries == "La Réunion"] <- "en:RE"
WorldFood$countries[WorldFood$countries == "Netherlands"] <- "en:NL"
WorldFood$countries[WorldFood$countries == "Russia"] <- "en:RU"
WorldFood$countries[WorldFood$countries == "Burkina Faso"] <- "en:BF"
WorldFood$countries[WorldFood$countries == "Hong Kong"] <- "en:HK"
WorldFood$countries[WorldFood$countries == "Hong Kong,China"] <- "en:HK, en:CN"
WorldFood$countries[WorldFood$countries == "Lebanon"] <- "en:LB"


#wordcloud allergens
library(NLP)
library(tm)
library(SnowballC)
library(wordcloud)

wc_allergens <- Corpus(VectorSource(jeopQ$Question))
wc_allergens <- tm_map(wc_allergens, PlainTextDocument)
wc_allergens <- tm_map(wc_allergens, removePunctuation)
wc_allergens <- tm_map(wc_allergens, removeWords, stopwords('english'))
wordcloud(jeopCorpus, max.words = 100, random.order = FALSE)

