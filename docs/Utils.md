# Utils

## Chatbot
- Add env var OPENAI_API_KEY

## Coding

## Code Runner

## OJ Interactions

### Interface
- submit locally
- get the submission result
- submit officially

### Local Setup

- [Judge0](https://github.com/judge0/judge0/tree/master)

- [Run Judge0 locally](https://github.com/judge0/judge0/blob/master/CHANGELOG.md#with-http)

1. Install [Docker](https://docs.docker.com) and [Docker Compose](https://docs.docker.com/compose).
2. Download and extract the release archive:
```
wget https://github.com/judge0/judge0/releases/download/v1.13.0/judge0-v1.13.0.zip
unzip judge0-v1.13.0.zip
```

3. Run all services and wait a few seconds until everything is initialized:
```
cd judge0-v1.13.0
docker-compose up -d db redis
sleep 10s
docker-compose up -d
sleep 5s
```

4. Your instance of Judge0 CE v1.13.0 is now available at `http://localhost:2358`.

### Use Rapid API
- [Get the API Key](https://github.com/judge0/judge0?tab=readme-ov-file#get-started)
- Set env var RAPIDAPI_KEY='your key'
- Check if it's successsfully set: `echo $RAPIDAPI_KEY`

## Problems