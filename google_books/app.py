import web


url_app = (
    "/","aplicacion.index.Index"
)

app = web.application(url_app, globals()) 


if __name__ == "__main__":
    app.run()