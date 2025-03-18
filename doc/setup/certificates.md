# ssl und so

in `Frontend\frontend`
Are the files:
`localhost-key.pem` and `localhost.pem`.
They are untracked throug the `.gitignore`. And need to be created.

A `.env` has to be added too:

```.env
    HTTPS=true
    SSL_CRT_FILE=./localhost.pem
    SSL_KEY_FILE=./localhost-key.pem
```
