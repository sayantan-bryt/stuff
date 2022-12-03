package main

type document struct {
    Title string `xml:"title"`
    URL   string `xml:"url"`
    Text  string `xml:"abstract"`
    ID    int
}

type index map[string][]int
