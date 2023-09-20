# docker-1984-tweet-generator

<!-- omit in toc -->
## Table of Contents

- [docker-1984-tweet-generator](#docker-1984-tweet-generator)
  - [Command Reference](#command-reference)
    - [1. Build the Image](#1-build-the-image)
    - [2. Run the Container](#2-run-the-container)
    - [3. Access via Browser](#3-access-via-browser)

## Command Reference

### 1. Build the Image

```bash
docker build -t docker-tweet-generator .
```

### 2. Run the Container

```bash
docker run -p 5001:3000 --rm --name tweet-generator-container docker-tweet-generator
```

### 3. Access via Browser

http://localhost:5001
