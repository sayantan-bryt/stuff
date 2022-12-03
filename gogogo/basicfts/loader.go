package main

import (
	"encoding/xml"
	"os"
)

func loadDocuments(path string) ([]document, error) {
  f, err := os.Open(path)
  if err != nil {
    return nil, err
  }
  defer f.Close()

  dec := xml.NewDecoder(f)
  dump := struct {
    Documents []document `xml:"doc"`
  }{}
  if err := dec.Decode(&dump); err != nil {
    return nil, err
  }
  docs := dump.Documents
  for i := range docs {
    docs[i].ID = i
  }
  return docs, nil
}

func (idx index) add(docs []document) {
  for _, doc := range docs {
    for _, token := range analyze(doc.Text) {
      ids := idx[token]
      if ids != nil && ids[len(ids)-1] == doc.ID {
        // Don't add same ID twice.
        continue
      }
      idx[token] = append(ids, doc.ID)
    }
  }
}
