#import --------------------------------------------------------------------------------
import pandas as pd
import numpy as np
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


#read ----------------------------------------
header = ["age", "workclass", "fnlwgt", "education", "education-num", "marital-status",
          "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss",
          "hours-per-week", "native-country", "income"]
dataframe = pd.read_csv("/Users/edoardosarri/Library/Mobile Documents/com~apple~CloudDocs/UniFi/Tesi/codice/adult.csv",
                        header=None, names=header)
dataframe.to_csv("adult_hader.csv")


#operazioni preliminari ------------------------
dataframe.replace("?", np.nan, inplace=True)
dataframe.dropna(inplace=True)
dataframe.loc[dataframe["race"] != "White", "race"] = "Non-white"
totIstanze = dataframe.shape[0]


#funzioni ------------------------
def filtra(df,attributo,valore):
    return df.loc[df[attributo] == valore]

def filtraIncome(df):
    return df.loc[df["income"] == ">50K"]

def scriviPDF(testo,nomeFile):
    c = canvas.Canvas(nomeFile, pagesize=letter)
    width, height = letter
    lines = testo.split("\n")
    y = height - 100
    for line in lines:
        c.drawString(100, y, line)
        y -= 20  # Spazio tra le righe
    c.save()
    print("File {} creato con successo".format(nomeFile))


#genere -----------------------------
dfFemale = filtra(dataframe,"sex","Female")
dfFemaleIncome = filtraIncome(dfFemale)
totFemale = dfFemale.shape[0]
totFemaleIncome = dfFemaleIncome.shape[0]
probFemale = totFemaleIncome / totFemale
testoFemale = "- Istanze di genere femminile: {}\n".format(totFemale)
testoFemale += "- Istanze di genere femminile con income >50K$: {}\n".format(totFemaleIncome)
testoFemale += "- Probabilità per il genere femminile di avere un income >50K$: {}\n".format(probFemale)

dfMale = filtra(dataframe,"sex","Male")
dfMaleIncome = filtraIncome(dfMale)
totMale = dfMale.shape[0]
totMaleIncome = dfMaleIncome.shape[0]
probMale = totMaleIncome / totMale
testoMale = "- Istanze di genere maschile: {}\n".format(totMale)
testoMale += "- Istanze di genere maschile con income >50K$: {}\n".format(dfMaleIncome.shape[0])
testoMale += "- Probabilità per il genere maschile di avere un income >50K$: {}\n".format(probMale)

paritaStatisticaGenere = abs(probFemale-probMale)
diversoImpattoGenere = probFemale/probMale

testoGenere = "GENERE\n{}\n{}\n".format(testoFemale,testoMale)
testoGenere += "- Parità statistica: {}\n".format(paritaStatisticaGenere)
testoGenere += "- Diverso impatto: {}\n".format(diversoImpattoGenere)
scriviPDF(testoGenere, "risultati genere.pdf")


#razza -----------------------------
dfNonWhite = filtra(dataframe,"race","Non-white")
dfNonWhiteIncome = filtraIncome(dfNonWhite)
totNonWhite = dfNonWhite.shape[0]
totNonWhiteIncome = dfNonWhiteIncome.shape[0]
probNonWhite = totNonWhiteIncome / totNonWhite
testoNonWhite = "- Istanze di razza Non-white: {}\n".format(totNonWhite)
testoNonWhite += "- Istanze di razza Non-white con income >50K$: {}\n".format(totNonWhiteIncome)
testoNonWhite += "- Probabilità per la razza Non-white di avere un income >50K$: {}\n".format(probNonWhite)

dfWhite = filtra(dataframe,"race","White")
dfWhiteIncome = filtraIncome(dfWhite)
totWhite = dfWhite.shape[0]
totWhiteIncome = dfWhiteIncome.shape[0]
probWhite = totWhiteIncome / totWhite
testoWhite = "- Istanze di razza White: {}\n".format(totWhite)
testoWhite += "- Istanze di razza White con income >50K$: {}\n".format(totWhiteIncome)
testoWhite += "- Probabilità per la razza White di avere un income >50K$: {}\n".format(probWhite)

paritaStatisticaRazza = abs(probNonWhite-probWhite)
diversoImpattoRazza = probNonWhite/probWhite

testoRazza = "RAZZA\n{}\n{}\n".format(testoNonWhite,testoWhite)
testoRazza += "- Parità statistica: {}\n".format(paritaStatisticaRazza)
testoRazza += "- Diverso impatto: {}\n".format(diversoImpattoRazza)
scriviPDF(testoRazza, "risultati razza.pdf")