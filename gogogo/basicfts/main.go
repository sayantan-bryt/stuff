package main

import (
	"fmt"
	"time"
)

func main() {
    path := "./enwiki-latest-abstract1.xml"
    fmt.Printf("Considering path: %v\n", path)

    // loading the xml doc
    prev_ts := time.Now().UnixNano()
    fmt.Printf("Starting to parse...\n")
    docs, err := loadDocuments(path)
    fmt.Printf("Finished parsing: %vs\n", float64(time.Now().UnixNano() - prev_ts) * 1e-9)
    if err != nil {
        fmt.Printf("Error occured %v\n", err)
    }
    search_term := "cat"
    var searched_docs []document

    // Basic String search
    fmt.Printf("Basic Search...\n")
    prev_ts = time.Now().UnixNano()
    searched_docs = searchBasic(docs, search_term)
    fmt.Printf("Search finished for `%v`: %vs\n", search_term, float64(time.Now().UnixNano() - prev_ts) * 1e-9)
    fmt.Printf("Number of doc: %v\n", len(searched_docs))

    // Regex Search
    fmt.Printf("Regex Search...\n")
    prev_ts = time.Now().UnixNano()
    searched_docs = searchReg(docs, search_term)
    fmt.Printf("Search finished for `%v`: %vs\n", search_term, float64(time.Now().UnixNano() - prev_ts) * 1e-9)
    fmt.Printf("Number of doc: %v\n", len(searched_docs))

    // Inverted Index Search
    fmt.Printf("Starting to build Index...\n")
    idx := make(index)
    idx.add(docs)
    fmt.Printf("Finished building index: %vs\n", float64(time.Now().UnixNano() - prev_ts) * 1e-9)
    fmt.Printf("Index len: %v\n", len(idx))
    fmt.Printf("Inverted Index Search...\n")

    prev_ts = time.Now().UnixNano()
    searched_indexes := idx.search(search_term)
    fmt.Printf("Search for `%v` took: %vs\n", search_term, float64(time.Now().UnixNano() - prev_ts) * 1e-9)
    fmt.Printf("Number of doc: %v\n", len(searched_indexes))

    search_term = "Small wild cat"
    prev_ts = time.Now().UnixNano()
    searched_indexes = idx.search(search_term)
    fmt.Printf("Search for `%v` took: %vs\n", search_term, float64(time.Now().UnixNano() - prev_ts) * 1e-9)
    fmt.Printf("Search indices for `%v`: %vs\n", search_term, searched_indexes)
    for _, idx := range searched_indexes {
        fmt.Println(docs[idx])
    }
}
