package main

import (
	"log"

	"github.com/creepysta/stuff/gogogo/rest-api/api"
)

func main() {
  log.SetPrefix("rest-api")
  api.Routes().Run("0.0.0.0:80")
}
