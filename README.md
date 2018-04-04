# Decompress Snappy format

Decompress [Snappy format](https://google.github.io/snappy/) using [this](https://github.com/andrix/python-snappy) python library

Read all files in `/data/in/files/**/*` (regardless of extensions and how deeply they are nested), parse with  and write to corresponding (folder hierarchy is kept) locations in `/data/out/files`


# Configuration
```
{
    "definition": {
        "component": "pocin.processor-decompress-snappy"
    }
}


```

## Run locally

```

docker-compose run --rm dev
```

## Run tests
	

```
make test
# after dev session is finished to clean up containers..
make clean 
```
