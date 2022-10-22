name=rest-api
image=golang:alpine3.16

d_run:
	@docker run -it --rm -v $(shell pwd):/app --workdir /app --name $(name) -p 8000:80 $(image)  sh

d_exec:
	@docker exec -it $(name) sh

test_cvg:
	@CGO_ENABLED=0 GO111MODULE=on go test ./... -v -coverpkg=./... -coverprofile=coverage.out

test_html:
	@go tool cover -html=coverage.out

test:
	@CGO_ENABLED=0 GO111MODULE=on go test ./...

build:
	@go build -o /go/bin . && \
	go install
