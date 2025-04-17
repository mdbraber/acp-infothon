# Infothon 20-21 maart 2025

## Doel 
Reanimatiebeleid uit IKNL formulier bevragen met Semantic Web

## Door
Joost Holslag (RSO Zuid-Limburg), Marc Nieuwland en Joost Wildenberg (Zorginstituut), Evelien Vaags (CNIO Sensire) en onderzoeksteam (Jerry Fortuin, Maarten den Braber en Ilona Oude Nijhuis)

## Achtergrond / tools
- [openEHR Archetype Designer](https://tools.openehr.org). Archetype designer is de plek waar je een template maakt op basis van archetypes
- [OpenEHR NL Github repositories](https://github.com/openehr-nl)
- [ACP repository van openEHR-NL](https://github.com/openehr-nl/acp)
- [Joost Holslag (openEHR) Github repositories](http://github.com/joostholslag)
- [Better](https://www.better.care): invultool voor openEHR templates. Vertaalat data uit formulier naar openEHR schema. 
- [Clinical Knowledge Manager (CKM)](https://ckm.openehr.org/ckm/). Beheertool van openEHR archetypes. Centrale punt van de openEHR community voor o.a. afstemmen van consensus rondom archetypes.

![](screenshots/01%20-%20openEHR%20Clinical%20Knowledge%20Manager.png)
![](screenshots/02%20-%20openEHR%20archetype%20community%20discussion.png)

## Stappen

### 1. Invoer data - reanimatiebeleid op basis van IKNL formulier
- openEHR Template gevonden dat overeenkomt met het[IKNL-formulier](resources/Formulier_Uniform_vastleggen_proactieve_zorgplanning_richtlijn_Proactieve_Zorgplanning): [Advance Intervention Decisions](https://github.com/openehr-nl/ACP/blob/main/openEHR-EHR-COMPOSITION.care_plan.v0.adl)
- Op basis van het template een formulier gemaakt (Better). We gebruiken Better omdat je daarmee met een low-code omgeving het formulier kan maken

![](screenshots/03%20-%20openEHR%20Advanced%20Care%20Directive.png)
![](screenshots/04%20-%20openEHR%20Archetype%20designer.png)
![](screenshots/05%20-%20openEHR%20CPR%20decision%20attributes.png)
![](screenshots/06%20-%20openEHR%20CPR%20decision%data%details.png)

### 2. Vastlegging data - in openEHR op basis van archetype
- 7x een 'instance' van een reanimatie-beleid ingevoerd. De invoer van Better wordt opgeslagen in het openEHR Clinical Data Repository (gefaciliteerd door Better)

![](screenshots/07%20-%20openEHR%20input%20form.png)
![](screenshots/10%20-%20ACP%20Test%20KIK-V.png)

### 3. Overdracht data - naar RDF triple store
- [AQL / openEHR query](resources/acp%20kik-v%20query.aql) geschreven om de data uit Clinical Data Repository te extraheren
- Output van de de AQL / openEHR query is een [JSON bestand](resources/acp%20kik-v%20data%20all.json) conform openEHR structuur
- [Python script](resources/ACP_infothon.py) dat op basis output van openEHR 'vertaalt' naar Semantic web

![](screenshots/12%20-%20Semantic%20Web%20ACPInformationObject.png)

- JSON bestand gebruiken voor import naar de Triple Store / [GraphDB](http://graphdb.ontotext.com) (ontologie, KIK-V test data en gegenereerde TTL)

![](screenshots/13%20-%20Advanced%20Care%20Planning%20Process%20examples%201.png)
![](screenshots/14%20-%20Advanced%20Care%20Planning%20Process%20examples%202.png)
![](screenshots/15%20-%20Advanced%20Care%20Planning%20Process%20examples%203.png)

### 4. Bevragen data - op basis van Semantic Web
![](resources/acp%20kik-v%20query.aql)

- SPARQL query
  a. ‘van hoeveel personen / cliënten /patiënten binnen de organisatie is het reanimatiebeleid vastgelegd?’; en opmerkingen voor vervolgonderzoek: discussie over ‘onbekend’ queryen en wat dat betekent -> vervolgonderzoek?
  b. ‘wat is de datum van vastlegging van het reanimatiebeleid van de personen /cliënten /patiënten?’  Hiermee wordt bedoeld, de datum waarop de keuze-optie in het formulier voor het laatst gewijzigd is.
  c. Bonus (als de data-invoer zover is gekomen): ‘bij hoeveel personen /cliënten /patiënten binnen ouderenzorg/intramuraal is het reanimatiebeleid vastgelegd binnen 24 uur na opname?’  
  _Vraag b en c kun je ook beantwoorden (dat hebben we niet uitgevoerd) als je gebruik maakt van het expliciet veld Last Updated van het archetype  Advanced Intervention Decision gebruik_
  
![](screenshots/16%20-%20SPARQL%20query%20ACP.png)
