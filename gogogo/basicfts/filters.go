package main

import (
	"strings"
	"unicode"

	snowballeng "github.com/kljensen/snowball/english"
)

func tokenizer(text string) []string {
  return strings.FieldsFunc(text, func(r rune) bool {
    return !unicode.IsLetter(r) && !unicode.IsNumber(r)
  })
}

func lowercaseFilter(tokens []string) []string {
  r := make([]string, len(tokens))
  for i, token := range tokens {
    r[i] = strings.ToLower(token)
  }
  return r
}

func stopwordFilter(tokens []string) []string {
  r := make([]string, 0, len(tokens))
  for _, token := range tokens {
    if _, ok := stopwords[token]; !ok {
      r = append(r, token)
    }
  }
  return r
}

func stemmerFilter(tokens []string) []string {
  r := make([]string, len(tokens))
  for i, token := range tokens {
    r[i] = snowballeng.Stem(token, false)
  }
  return r
}

func analyze(text string) []string {
  tokens := tokenizer(text)
  tokens = lowercaseFilter(tokens)
  tokens = stopwordFilter(tokens)
  tokens = stemmerFilter(tokens)
  return tokens
}
