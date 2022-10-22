package api

import (
	"github.com/gin-gonic/gin"
)

func Routes() (*gin.Engine) {
  router := gin.Default()
  router.GET("/", hello)
  router.GET("/albums", getAlbums)
  router.GET("/albums/:id", getAlbumByID)
  router.POST("/albums", postAlbums)

  return router
}
