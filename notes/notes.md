
```
Q2. Create a proposal that outlines how you would a) structure the database and
validate data inputed by users, and b) design a simple workflow to achieve your
objective. You may also include other considerations, for example, on how you
would customise the UI/UX to suit your target audience or differentiate the app
from similar offerings.
```


# A) Structure the database, validate data inputted by users
---

## Decision on the type and design of database

1. Understand the entities involved
2. The schema is designed based on the relationship between the entities
3. Identity the type of data. (For eg; Postgres DB allows us to have JSON as a data type)
4. Identity the size of data. The data size and the relationship also matters
   when choosing the type of database
    * If the data is too large, we need NoSQL databases
    * otherwise we can use Relational Databases
5. Choices for design and implementation -
    * RDBMS - Build initial logical schema, and normalize the same before
      implementing the structure in a database
    * NoSQL - Joins are expensive across data sets. Might be better to
      replicate the data in the documents
6. Make sure of the data types

## Validation

For any user input, following are the primary validations need to be performed
* Data type
* Range and constraint
* Code and cross-reference
* Structured
* Consistency

# B) Workflow
---

* Understand the entities in play
* Design a draft for database schema for the relationships between the entities
* Validate its normalized else refactor the design
* Build the ORM for the database
* Build the APIs for accessing the DB using the ORM
* Secure the APIs with authentication and authorization
* Build a simple frontend.
* Make sure to have proper field validations in the input fields to ensure
  validation is done on client side
* The input type for the fields should adhere to the column types chosen for the Database
* Instead of all text fields, drop down lists can be used whenever the domain
  of accepted values is already known
* The frontend should have any and all data necessary for the user's context,
  but nothing more and nothing less
