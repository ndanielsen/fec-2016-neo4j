"""
Neo4j models for FEC Data

Nathan @nate_somewhere
2017-03-12
"""

from py2neo.ogm import GraphObject
from py2neo.ogm import Property
from py2neo.ogm import RelatedTo
from py2neo.ogm import RelatedFrom


class Candidate(GraphObject):
    __primarykey__ = "CAND_ID"

    CAND_ID = Property()
    CAND_NAME = Property()

    CAND_ICI = Property()

    CAND_PCC = Property()
    CAND_ST1 = Property()
    CAND_ST2 = Property()

    CAND_PTY_AFFILIATION = RelatedTo("Party")
    CAND_ELECTION_YR = RelatedTo("ElectionYear")
    CAND_STATUS = RelatedTo("Status")
    CAND_CITY = RelatedTo("City")
    CAND_ZIP = RelatedTo("Zipcode")
    CAND_OFFICE_ST = RelatedTo("State")
    CAND_OFFICE = RelatedTo("Office")
    CAND_OFFICE_DISTRICT = RelatedTo("District")



class Zipcode(GraphObject):
    __primarykey__ = "ZIPCODE"
    ZIPCODE = Property()
    CAND_ZIP = RelatedFrom("Candidate", "CAND_ZIP")

class City(GraphObject):
    __primarykey__ = "CITY"
    CITY = Property()
    CAND_CITY = RelatedFrom("Candidate", "CITY")

class State(GraphObject):
    __primarykey__ = "STATE"

    STATE = Property()
    CAND_OFFICE_ST = RelatedFrom("Candidate", "STATE")


class Status(GraphObject):
    __primarykey__ = "STATUS"

    STATUS = Property()
    CAND_STATUS = RelatedFrom("Candidate", "STATUS")


class Party(GraphObject):
    __primarykey__ = "PARTY"

    PARTY = Property()
    CAND_PTY_AFFILIATION = RelatedFrom("Candidate", "PARTY")


class ElectionYear(GraphObject):
    __primarykey__ = "YEAR"

    YEAR = Property()
    CAND_ELECTION_YR = RelatedFrom("Candidate", "YEAR")

class District(GraphObject):
    __primarykey__ = "DISTRICT"

    DISTRICT = Property()
    CAND_OFFICE_DISTRICT = RelatedFrom("Candidate", "DISTRICT")

class Office(GraphObject):
    __primarykey__ = "OFFICE"

    OFFICE = Property()
    CAND_OFFICE = RelatedFrom("Candidate", "OFFICE")
