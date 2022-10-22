package main

import (
	"log"

	"github.com/creepysta/stuff/gogogo/rest-api/api"
)


func main() {
  api.WG.Add(1)
  go api.SendEmails("user called api", "sam@example.com")

  log.SetPrefix("rest-api")
  api.Routes().Run("0.0.0.0:80")

  api.WG.Wait()
}
