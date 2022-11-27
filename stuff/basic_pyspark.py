# pros and cons of pyspark
# serializers in PySpark
# types of operations := transformations,
#                        actions (first, take, collect, count, reduce)
# types of transformations := narrow (map, filter)
#                              wide (shuffle - reduceByKey, groupByKey)
# Pros of RDD
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
# #3 unpivot()

# 1
from __future__ import annotations

import json
import re
import typing
from dataclasses import asdict, dataclass, fields

import pyspark

sc = pyspark.SparkContext()
spark = pyspark.sql.SparkSession(sc)


rdd = sc.textFile("/etc/passwd")


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


res = rdd.map(fn).map(fn1).map(fn2)
res.foreach(
    lambda x: print(
        json.dumps(
            {name: getattr(x, name) for name, field in x.__dataclass_fields__.items()},
            indent=4,
        )
    )
)
# res.foreach(print)
# res.foreach(lambda x: print(asdict(x)))
# res.foreach(lambda x: print(x.asdict()))
# res.foreach(lambda x: print(json.dumps(asdict(x), indent=2)))

changed_rdd = res.filter(lambda x: x.status == "changed")
print(f"Changed Rows: {changed_rdd.count()}")
print(f"Unchanged Rows: {res.count() - changed_rdd.count()}")


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
