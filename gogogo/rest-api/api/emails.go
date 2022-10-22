package api

import (
	"fmt"
	"time"
)

func SendEmails(msg string, email string) {
  fmt.Printf("Sending Email to %v\n", email)
  time.Sleep(10 * time.Second)
  fmt.Printf("Email sent to %v\n", email)
  fmt.Printf("Message Content: \n%v\n", msg)
  WG.Done()
}
