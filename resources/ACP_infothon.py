import json
from rdflib import Graph, URIRef, Literal, RDF, Namespace, BNode, XSD, RDFS

# prefixes
onzorg = Namespace('http://purl.org/ozo/onz-org#')
onzzorg = Namespace('http://purl.org/ozo/onz-zorg#')
onzpers = Namespace('http://purl.org/ozo/onz-pers#')
onzg = Namespace('http://purl.org/ozo/onz-g#')
onzfin = Namespace('http://purl.org/ozo/onz-fin#')
dummy = Namespace('http://data.dummyzorg.nl/')

g = Graph()

g.bind('onz-org', onzorg)
g.bind('onz-zorg', onzzorg)
g.bind('onz-g', onzg)
g.bind('onz-pers', onzpers)
g.bind('onz-fin', onzfin)
g.bind('dummy', dummy)

No = URIRef('http://purl.bioontology.org/ontology/SNOMEDCT/373067005')
Yes = URIRef('http://purl.bioontology.org/ontology/SNOMEDCT/373066001')

clienten = [	
    dummy.Client_N90748a30df984605a5fc54a9e7ead0ab,
    dummy.Client_N88b881bc725348ef9ec3ca3c4b3337e0,
    dummy.Client_N9a4c0312bd5d41e68833cc3b4c821685,
    dummy.Client_Nde9600a502f54c01b16350bb7d37fc12,
    dummy.Client_N77c82906c1a64fb2a81636883924b191,	
    dummy.Client_N6b25701dbfb64b6cb246ef7cf850514f,
    dummy.Client_N36710bf84e704db5be86845685118575,	
    dummy.Client_Nc35bbbd53bbf4b3daed9211c8d92e04c,
    dummy.Client_N74378397c54e4c7a805a2fa412d23846,
    dummy.Client_N117a73a791f04490a67b2ccd94443a73]

locaties = [
    dummy.Locatie_BG_Links,
    dummy.Locatie_BG_Rechts,
    dummy.Locatie_Begane_Grond,
    dummy.Locatie_De_Beuk_1,
    dummy.Locatie_De_Beuk_2,
    dummy.Locatie_Grotestraat_17,
    dummy.Locatie_Grotestraat_213,
    dummy.Locatie_Kelder,
    dummy.Locatie_Verdieping_2,
    dummy.Locatie_Vleugel_A]

decision_code_lookup = {
    'No CPR': No,
    'Full CPR': Yes,
    'Limited CPR': onzzorg.LimitedCPR
}

# Open the JSON file and load its content
with open('acp kik-v data all.json', 'r') as file:
    data = json.load(file)    

# print(data)
index = 0
for item in data:
    decision_code = item['#0']['content'][0]['items'][0]['data']['items'][0]['value']['value']
    decision_value = decision_code

    # Client en locatie URI's
    client_uri = clienten[index]
    locatie_uri = locaties[index]

    # ACP Proces
    proces_uri = URIRef(dummy + f"proces_{index}")
    time_stamp = BNode()
    g.add((proces_uri, RDF.type, onzzorg.ACPProces))
    g.add((proces_uri, onzg.hasTime, time_stamp))
    g.add((proces_uri, onzg.hasParticipant, client_uri))
    g.add((proces_uri, onzg.hasPerdurantLocation, locatie_uri))

    # CPR Information Object
    decision_uri = URIRef(dummy + f"decision_{index}")
    g.add((decision_uri, RDF.type, onzzorg.CPRInformationObject))
    g.add((decision_uri, RDFS.label, Literal(decision_value, datatype=XSD.string)))
    g.add((proces_uri, onzg.hasOutput, decision_uri))
    g.add((decision_uri, onzg.isAbout, client_uri))
    g.add((decision_uri, onzg.hasDataValue, Literal(decision_code, datatype=XSD.string)))
    if decision_code_lookup.get(decision_code):
        g.add((decision_uri, onzg.hasAssessmentValueResult, decision_code_lookup.get(decision_code)))
    else:
        print(f"No code found for {decision_code}")

    index += 1

g.serialize(destination='OpenEHR.ttl', format='turtle')
