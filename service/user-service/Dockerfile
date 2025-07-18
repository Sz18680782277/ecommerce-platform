FROM golang:1.22-alpine AS builder

ENV CGO_ENABLED=0 \
    GO111MODULE=on \
    GOPROXY=https://goproxy.cn,direct

WORKDIR /app

COPY . .

RUN go build -o main .

FROM scratch

WORKDIR /

COPY --from=builder /app/main .

ENTRYPOINT ["/main"]

