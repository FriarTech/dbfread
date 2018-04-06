"""
Load content of a DBF file into a Pandas data frame.

The iter() is required because Pandas doesn't detect that the DBF
object is iterable.
"""
from dbfread import DBF
from pandas import DataFrame

dbf = DBF('files/people.dbf')
frame = DataFrame(iter(dbf))

print(frame)

"""
Alternate way to load content from a DBF file into a Pandas data frame.
"""

from dbfread import DBF
from pandas import DataFrame

dbf = DBF('files/people.dbf')
dbf.load()
frame = pd.DataFrame()
frame = frame.from_records(dbf.records)

print(frame)
