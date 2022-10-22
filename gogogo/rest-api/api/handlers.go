package api

import (
	"net/http"

	"github.com/creepysta/stuff/gogogo/rest-api/api/db"
	"github.com/gin-gonic/gin"
)

// hello
func hello(c *gin.Context) {
    c.IndentedJSON(http.StatusOK, "Hey there Delilah!!")
}

// getAlbums responds with the list of all albums as JSON.
func getAlbums(c *gin.Context) {
    c.IndentedJSON(http.StatusOK, db.Albums)
}

// getAlbumByID locates the album whose ID value matches the id
// parameter sent by the client, then returns that album as a response.
func getAlbumByID(c *gin.Context) {
    id := c.Param("id")

    // Loop over the list of albums, looking for
    // an album whose ID value matches the parameter.
    for _, a := range db.Albums {
        if a.ID == id {
            c.IndentedJSON(http.StatusOK, a)
            return
        }
    }
    c.IndentedJSON(http.StatusNotFound, gin.H{"message": "album not found"})
}

// postAlbums adds an album from JSON received in the request body.
func postAlbums(c *gin.Context) {
    var newAlbum db.Album

    // Call BindJSON to bind the received JSON to
    // newAlbum.
    if err := c.BindJSON(&newAlbum); err != nil {
        return
    }

    // Add the new album to the slice.
    db.Albums = append(db.Albums, newAlbum)
    c.IndentedJSON(http.StatusCreated, newAlbum)
}


