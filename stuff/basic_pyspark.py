# pros and cons of pyspark
# serializers in PySpark
#   Default - PickleSerializer uses Python's cPickle serializer,
#               - which can serialize nearly any Python object.
#           - Other serializers, like MarshalSerializer, support fewer datatypes
#               - can be faster.
#   sc = SparkContext('local', 'test', serializer=MarshalSerializer(), batchSize=2)
# Logical and Physical plan
# Logical :=
#           - Unresolved / Parsed
#           - Analyzed (without action, using catalog with the help of metastore)
#           - Optimized
# types of operations := transformations,
#                        actions (first, take, collect, count, reduce)
# df.persist(storage_level) := storage_level ->
#   MEMORY ONLY: This is the default persistence level, and it's used to save RDDs on the JVM as deserialized Java objects. In the event that the RDDs are too large to fit in memory, the partitions are not cached and must be recomputed as needed.
#   MEMORY AND DISK: On the JVM, the RDDs are saved as deserialized Java objects. In the event that memory is inadequate, partitions that do not fit in memory will be kept on disc, and data will be retrieved from the drive as needed.
#   MEMORY ONLY SER: The RDD is stored as One Byte per partition serialized Java Objects.
#   DISK ONLY: RDD partitions are only saved on disc.
#   OFF HEAP: This level is similar to MEMORY ONLY SER, except that the data is saved in off-heap memory.
# types of transformations := narrow (map, filter)
#                              wide (shuffle - reduceByKey, groupByKey)
# Pros of RDD
#   - Lazy Evaluation
#   - In-Memory Computation
#   - Immutability
#   - Fault Tolerance
#   - Partitioning
#   - Persistence - user can define where to persist `df.persist(storage_level)`
#   - Location-Stickiness
#   - Typed
#   - Coarse-Grained Operation: operate on entire dataset
#   - No Limitation
# Cons of RDD
#       No inbuilt optimization engine
#           := No catalyst optimizer and Tungsten execution engine
#       Handling structured data
#           := RDDs don’t infer the schema of the ingested data
#       Performance limitation
#           := Being in-memory JVM objects, RDDs involve the overhead of Garbage Collection and Java Serialization which are expensive when data grows.
#       Storage limitation
#           := RDDs degrade when there is not enough memory to store them.
#              Can also store partition of RDD on disk which exceeds RAM.
# #1 parse /etc/passwd
# #2 pivot()
# #3 unpivot() # not present in pyspark, requires stack
# #4 total number of unique words
#   count of consonants and vowels

# 1
from __future__ import annotations

import json
import re
import typing
from dataclasses import asdict, dataclass, fields

import pyspark

sc = pyspark.SparkContext()
spark = pyspark.sql.SparkSession(sc)


passwd_rdd = sc.textFile("/etc/passwd")


@dataclass(frozen=True)
class Line:
    prev: str
    modified: str
    status: str = "unchanged"

    def asdict(self):
        return asdict(self)


def fn(line: str) -> Line:
    """
    basic fn for creating the structure for subsequent `map` calls
    """
    return Line(prev=line, modified=line)


def fn1(line: Line) -> Line:
    """
    doubles any number present in a line
    """

    def op(n: int) -> int:
        return n * 2

    def rep(x: re.Match) -> str:
        val = x.groupdict()["num"]
        return str(op(int(val)))

    prev_line = line.modified
    mod_line = re.sub(r"(?P<num>\d+)", rep, prev_line)
    return Line(status="changed", prev=line.prev, modified=mod_line)


def fn2(line: Line) -> Line:
    """
    makes the user id info upper case
    """

    prev_line = line.modified
    splits = prev_line.split(":")
    try:
        splits[4] = splits[4].upper()
    except IndexError as ie:
        return Line(prev=line.prev, modified=prev_line)
    else:
        mod_line = ":".join(splits)
        return Line(status="changed", prev=line.prev, modified=mod_line)


passwd_res = passwd_rdd.map(fn).map(fn1).map(fn2)
passwd_res.foreach(
    lambda x: print(
        json.dumps(
            {name: getattr(x, name) for name, field in x.__dataclass_fields__.items()},
            indent=4,
        )
    )
)
# passwd_res.foreach(print)
# passwd_res.foreach(lambda x: print(asdict(x)))
# passwd_res.foreach(lambda x: print(x.asdict()))
# passwd_res.foreach(lambda x: print(json.dumps(asdict(x), indent=2)))

changed_rdd = passwd_res.filter(lambda x: x.status == "changed")
print(f"Changed Rows: {changed_rdd.count()}")
print(f"Unchanged Rows: {passwd_res.count() - changed_rdd.count()}")


# 2
data = [
    ("Banana", 1000, "USA"),
    ("Carrots", 1500, "USA"),
    ("Beans", 1600, "USA"),
    ("Orange", 2000, "USA"),
    ("Orange", 2000, "USA"),
    ("Banana", 400, "China"),
    ("Carrots", 1200, "China"),
    ("Beans", 1500, "China"),
    ("Orange", 4000, "China"),
    ("Banana", 2000, "Canada"),
    ("Carrots", 2000, "Canada"),
    ("Beans", 2000, "Mexico"),
]
columns = ["Product", "Amount", "Country"]

df = spark.createDataFrame(data=data, schema=columns)
df.printSchema()
df.show(truncate=False)

privot_df = df.groupBy("Product").pivot("Country").sum("Amount")
privot_df.printSchema()
privot_df.show(truncate=False)


# 3
from pyspark.sql.functions import expr

unpivot_expr = (
    "stack(3, 'Canada', Canada, 'China', China, 'Mexico', Mexico) as (Country, Total)"
)
unpivot_df = privot_df.select("Product", expr(unpivot_expr)).where("Total is not null")
unpivot_df.show(truncate=False)
unpivot_df.show()


# 4
import re

# 10000 words from https://www.lipsum.com/

lorem_rdd = sc.textFile("/tmp/lorem.txt")
lorem_rdd_p = (
    lorem_rdd.map(lambda line: line.split(" "))
    .flatMap(lambda line: line)
    .map(lambda line: re.sub(r"\W", "", line))
    .filter(len)
)

lorem_vowels = lorem_rdd_p.filter(
    lambda x: (len(x) > 1 and x[0] in ("a", "e", "i", "o", "u"))
)

## Without Empty
#       Unique words = 199
#       Total words = 10000
## With Empty
#       Unique words = 200
#       Total words = 10111

# Consonants = 7180. Vowels = 2820 # Skipping articles (len(x) > 1)
# Consonants = 7068. Vowels = 2932 # Without skipping

lorem_uniq = lorem_rdd_p.distinct()

print(f"Unique words = {lorem_uniq.count()}")
print(
    f"Consonants = {lorem_rdd_p.count() - lorem_vowels.count()}. "
    f"Vowels = {lorem_vowels.count()}"
)
print(f"Total words = {lorem_rdd_p.count()}")
