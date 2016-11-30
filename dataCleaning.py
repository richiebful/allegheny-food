import pandas
addr = pandas.read_csv("Allegheny_County_Address_Points.csv")
rest = pandas.read_csv("ACHDRestaurentData.csv")
print rest

import HTMLParser
h = HTMLParser.HTMLParser()
rest["Name"] = rest["Name"].apply(h.unescape)
rest["Municipality"] = rest["Municipality"].apply(h.unescape)

import numpy
#prep to split Street Address into Street Name and Street Type
rest = rest.rename(columns={'Street Name': 'Street Address'})
restLen = len(rest["Name"])
rest["Street Name"] = pandas.Series(numpy.random.randn(restLen), index=rest.index).astype("str")
rest["Street Type"] = pandas.Series(numpy.random.randn(restLen), index=rest.index).astype("str")

print addr["ST_TYPE"].unique()

import re

regexRepls = [("(\s(Dr|Drive)\s|Dr(ive)?$)", "DR"), ("(\sSt\s|St(\.|reet)?$)", "ST"),
              ("(\sRd\s|Rd.|(Road|Rd|RD)$)", "RD"), ("(Ave\s|Ave(nue)?$)", "AVE"), ("(Blvd|Boulevard)$", "BLVD"), ("(Boulevard|Blvd)\s", "BLVD"),
              ("(Highway|Hwy)", "HWY"), ("Pike$", "PIKE"), ("Way$", "WAY"), ("\sWay\s", "WAY"),  ("(Place|Pl)$", "PL"), ("(lane|Lane|Ln)$","LN"),
              ("(Village|Vlg)$", "VLG"), ("End$", "END"), ("(Point|Pt|PT)$", "PT"),
              ("Cir(cle)?$", "CIR"), ("(Center|Ctr)$", "CTR"),  ("(Court|Ct)$", "CT"), ("Sq(uare)?$", "SQ"), ("(Plaza|Plz|PLZ)$", "PLZ"),
              ("(Extension|Ext|EXT)$", "EXT"),("Run$", "RUN"), ("(Roadway|Rdwy|RDWY)$", "RDWY"), ("(Knoll|Knl|KNL)$", "KNL"),
              ("(Parkway|Pkwy)$", "PKWY"), ("(Terrace|Ter)$", "TER"), ("(Trail|Trl)$", "TRL"), ("Park$", "PARK"), ("(Island|IS|Is)", "IS"),
              ("(Commons|Cmns|CMNS)$", "CMNS"), ("(Manor|MNR|Mnr)$", "MNR"), ("(Hill|Hl|HL)$", "HL"), ("(View|VW|Vw)$", "VW"),
              ("(Crossing|Xing)$", "XING"),  ("(Mall|MALL)$", "MALL"), ("(Field|Fld)$", "FLD"), ("(Green|Grn)$", "GRN"),
              ("(Expressway|Expy)$", "EXPY"), ("(Alley|Aly)$", "ALY"), ("Row$", "ROW"), ("Walk$", "WALK"),("(Heights|Hts)$", "HTS"),
              ("(Crescent|Cres|Crest)$", "CRES"), ("Spur$", "SPUR"), ("Path$", "PATH"), ("Oval$", "OVAL"), ("(Estates|Ests)$", "ESTS"),
              ("(Ridge|Rdg|RDG)$", "RDG"), ("(Harbor|Hbr|HBR)$", "HBR"), ("(Trace|TRCE|Trce)$", "TRCE"), ("(Mews|MEWS)$", "MEWS") ]
replacements = []
for regex in regexRepls:
    replacements.append((re.compile(regex[0]), regex[1]))

def extractStreetType(s, repl):
    for r in repl:
        if r[0].search(s) != None:
            return r[1]
    print s
    return ""

rest["Street Name"] = rest["Street Address"].apply(extractStreetType, args=(replacements,))

strName = rest["Street Name"]
print strName.value_counts()
#print strName.where(strName == "")