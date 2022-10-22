package api

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"testing"

	"github.com/creepysta/stuff/gogogo/rest-api/api/db"
	"github.com/stretchr/testify/assert"
)

var hostName = "http://0.0.0.0:80"

func TestHello(t *testing.T) {
  resp, err := http.Get(hostName + "/")
  if err != nil {
    log.Fatal(err)
  }
  body, err := ioutil.ReadAll(resp.Body)
  if err != nil {
    log.Fatal(err)
  }
  var decodedBody string
  var _ = json.Unmarshal(body, &decodedBody)
  assert.Equal(t, 200, resp.StatusCode, "Successful get should return 200")
  assert.Equal(t, "Hey there Delilah!!", string(decodedBody), "Should return `Hey there Delilah!!`")
}


func TestGetAll(t *testing.T) {
  assert := assert.New(t)
  resp, err := http.Get(hostName + "/albums")
  if err != nil {
    log.Fatal(err)
  }
  body, err := ioutil.ReadAll(resp.Body)
  if err != nil {
    log.Fatal(err)
  }
  var decodedBody []db.Album
  dErr := json.Unmarshal(body, &decodedBody)
  if dErr != nil {
    log.Fatal(dErr)
  }
  assert.Equal(200, resp.StatusCode, "Successful get should return 200")
  assert.Equal(3, len(decodedBody), "Should equal 3 initially")
}

func TestGetByIdPass(t *testing.T) {
  assert := assert.New(t)
  id := 1
  endpoint := fmt.Sprintf(hostName + "/albums/%v", id)
  resp, err := http.Get(endpoint)
  if err != nil {
    log.Fatal(err)
  }
  body, err := ioutil.ReadAll(resp.Body)
  if err != nil {
    log.Fatal(err)
  }
  expected := db.Album{ID: "1", Title: "Blue Train", Artist: "John Coltrane", Price: 56.99}
  var decodedBody db.Album
  json.Unmarshal(body, &decodedBody)
  assert.Equal(200, resp.StatusCode, "Successful get should return 200")
  assert.Equal(decodedBody, expected, "Id 1 should match from db")
}

func TestGetByIdFail(t *testing.T) {
  assert := assert.New(t)
  id := 999
  endpoint := fmt.Sprintf(hostName + "/albums/%v", id)
  resp, err := http.Get(endpoint)
  if err != nil {
    log.Fatal(err)
  }
  body, err := ioutil.ReadAll(resp.Body)
  if err != nil {
    log.Fatal(err)
  }
  var decodedBody map[string]string
  dErr := json.Unmarshal(body, &decodedBody)
  if dErr != nil {
    log.Fatal(dErr)
  }
  expected := map[string]string{
    "message": "album not found",
  }
  assert.Equal(404, resp.StatusCode, "Fail get should return 404")
  assert.Equal(decodedBody, expected, "Should return `album not found`")
}

func TestPost(t *testing.T) {
  assert := assert.New(t)
  for i := 0; i < 10; i++ {
    id := 100 + i
    newAlbum := db.Album {
      ID     : fmt.Sprint(id),
      Title  : fmt.Sprintf("Test Title %v", i),
      Artist : fmt.Sprintf("Test Artist %v", i),
      Price  : float64(i * 10) + 0.99,
    }
    postBody, _ := json.Marshal(newAlbum)
    resBody := bytes.NewBuffer(postBody)
    resp, err := http.Post(hostName + "/albums", "application/json", resBody)
    if err != nil {
      log.Fatalf("An error occurred for POST: %v", err)
    }
    defer resp.Body.Close()
    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
      log.Fatalln(err)
    }
    var decodedBody db.Album
    pErr := json.Unmarshal(body, &decodedBody)
    if pErr != nil {
      log.Fatalln(pErr)
    }
    endpoint := fmt.Sprintf(hostName + "/albums/%v", id)
    gResp, gErr := http.Get(endpoint)
    if gErr != nil {
      log.Fatalln(gErr)
    }
    gBody, _ := ioutil.ReadAll(gResp.Body)
    var decodedGBody db.Album
    json.Unmarshal(gBody, &decodedGBody)
    assert.Equal(201, resp.StatusCode, "Successful post creation should return 201")
    assert.Equal(newAlbum, decodedGBody, "Created Element must match")
  }
}
