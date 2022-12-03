package main

var stopwords = map[string]struct{}{ // I wish Go had built-in sets.
  "a": {}, "and": {}, "be": {}, "have": {}, "i": {},
  "in": {}, "of": {}, "that": {}, "the": {}, "to": {},
}
