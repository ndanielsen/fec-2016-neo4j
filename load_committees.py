"""
Load candidate data into a local instance of neo4j

Combine cn.txt with the headerfile to make for more understandable ETL

Nathan @nate_somewhere
2017-03-12
"""

import os
import csv
from collections import namedtuple
from app.models import Candidate
from app.models import Zipcode
from app.models import City
from app.models import Status
from app.models import Party
from app.models import ElectionYear
from app.models import State
from app.models import District
from app.models import Office
from app.models import Committee

from py2neo import Graph
from py2neo import Relationship
graph = Graph("http://localhost:7474/db/fecdata", password="smarttrip")

header_file = os.path.join('data', 'headers', 'cm_header_file.csv')
data_file = os.path.join('data', 'cm.txt')


if __name__ == '__main__':

    with open(header_file, 'r') as header_file:
        data = header_file.read()
        # data = csv.reader(header_file)
        header = data.strip().replace('\n', '')

    with open(data_file, mode="r") as infile:
        reader = csv.reader(infile, delimiter='|')
        # print(list(reader))
        Data = namedtuple("Data", header)  # get names from column headers
        for data in map(Data._make, reader):

            comm = Committee()

            comm.CMTE_ID = data.CMTE_ID
            comm.CMTE_NM = data.CMTE_NM
            comm.TRES_NM = data.TRES_NM   # Treasures name
            comm.CMTE_ST1 = data.CMTE_ST1
            comm.CMTE_ST2 = data.CMTE_ST2
            comm.CMTE_DSGN = data.CMTE_DSGN
            comm.CMTE_TP = data.CMTE_TP
            comm.CMTE_FILING_FREQ = data.CMTE_FILING_FREQ
            comm.ORG_TP = data.ORG_TP
            comm.CONNECTED_ORG_NM = data.CONNECTED_ORG_NM

            cand = Candidate.select(graph, data.CAND_ID).first()

            if not cand:
                cand = Candidate()
                cand.CAND_ID = data.CAND_ID
                graph.push(cand)

            # add edge
            comm.CAND_ID.add(cand)

            zipcode = Zipcode.select(graph, data.CMTE_ZIP).first()
            if not zipcode:
                zipcode = Zipcode()
                zipcode.ZIPCODE = data.CMTE_ZIP
                graph.push(zipcode)
            # add edge
            comm.CMTE_ZIP.add(zipcode)

            city = City.select(graph, data.CMTE_CITY).first()
            if not city:
                city = City()
                city.CITY = data.CMTE_CITY
                graph.push(city)
            # add edge
            comm.CMTE_CITY.add(city)

            party = Party.select(graph, data.CMTE_PTY_AFFILIATION).first()
            if not party:
                party = Party()
                party.PARTY = data.CMTE_PTY_AFFILIATION
                graph.push(party)
            # add edge
            comm.CMTE_PTY_AFFILIATION.add(party)

            state = State.select(graph, data.CMTE_ST ).first()
            if not state:
                state = State()
                state.STATE = data.CMTE_ST
                graph.push(state)
                # add edge
            comm.CMTE_ST.add(state)

            # Commit it all
            graph.push(comm)
