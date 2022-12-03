package main

import (
	"regexp"
	"strings"
)


func searchBasic(docs []document, term string) []document {
  var r []document
  for _, doc := range docs {
    if strings.Contains(doc.Text, term) {
      r = append(r, doc)
    }
  }
  return r
}

func searchReg(docs []document, term string) []document {
  re := regexp.MustCompile(`(?i)\b` + term + `\b`) // Don't do this in production, it's a security risk. term needs to be sanitized.
  var r []document
  for _, doc := range docs {
    if re.MatchString(doc.Text) {
      r = append(r, doc)
    }
  }
  return r
}

func (idx index) search(text string) []int {
  var r []int
  for _, token := range analyze(text) {
    if ids, ok := idx[token]; ok {
      if r == nil {
        r = ids
      } else {
        r = intersection(r, ids)
      }
    } else {
      return nil
    }
  }
  return r
}
