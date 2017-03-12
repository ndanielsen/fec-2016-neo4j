"""
Load candidate data into a local instance of neo4j

Combine cn.txt with the headerfile to make for more understandable ETL

Nathan @nate_somewhere
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



from app.models import Candidate
from py2neo import Graph
from py2neo import Relationship
graph = Graph("http://localhost:7474/db/fecdata", password="smarttrip")

header_file = os.path.join('data', 'headers', 'cn_header_file.csv')
data_file = os.path.join('data', 'cn.txt')


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

            zipcode = Zipcode()
            zipcode.ZIPCODE = data.CAND_ZIP
            graph.push(zipcode)

            city = City()
            city.CITY = data.CAND_CITY
            graph.push(city)

            status = Status()
            status.STATUS = data.CAND_STATUS
            graph.push(status)

            party = Party()
            party.PARTY = data.CAND_PTY_AFFILIATION
            graph.push(party)

            year = ElectionYear()
            year.YEAR = data.CAND_ELECTION_YR
            graph.push(year)

            state = State()
            state.STATE = data.CAND_OFFICE_ST
            graph.push(state)

            office = Office()
            office.OFFICE = data.CAND_OFFICE
            graph.push(office)

            district = District()
            district.DISTRICT = data.CAND_OFFICE_DISTRICT
            graph.push(district)



            cand = Candidate()
            cand.CAND_ID = data.CAND_ID
            cand.CAND_NAME = data.CAND_NAME
            # cand.CAND_PTY_AFFILIATION = data.CAND_PTY_AFFILIATION

            # cand.CAND_OFFICE_ST = data.CAND_OFFICE_ST
            # cand.CAND_OFFICE = data.CAND_OFFICE
            # cand.CAND_OFFICE_DISTRICT = data.CAND_OFFICE_DISTRICT
            cand.CAND_ICI = data.CAND_ICI

            cand.CAND_PCC = data.CAND_PCC
            cand.CAND_ST1 = data.CAND_ST1
            cand.CAND_ST2 = data.CAND_ST2

            cand.CAND_PTY_AFFILIATION.add(party)
            cand.CAND_ELECTION_YR.add(year)
            cand.CAND_OFFICE_ST.add(state)
            cand.CAND_STATUS.add(status)
            cand.CAND_CITY.add(city)
            cand.CAND_ZIP.add(zipcode)

            cand.CAND_OFFICE_DISTRICT.add(district)
            cand.CAND_OFFICE.add(office)



            graph.push(cand)
