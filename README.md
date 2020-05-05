# ProgImage
ProgImage is a specialised service exposing an API that offers image storage, retrieval and manipulation. 

## Build and run

To run the ProgImage server locally, first create a PostgreSQL database and a virtual env for it. Activate the virtualenv and export the following environment variables (or put them in the `bin/postactivate` file in the virtualenv folder):

    export DJANGO_SECRET_KEY="generate-a-secret-key-here"
    export PG_DB_NAME="progimage"
    export PG_USER="your_db_user"
    export PG_PASS="your_db_pass"
    export PG_HOST="localhost"

Next, install the requirements with `pip install -Ur requirements/dev.txt` 

Next, create the DB schema and apply migrations, all with one command: `./mange.py migrate`

Optionally, tou can run the test suite with: `./manage.py test`

Finally, start the web server: `./manage.py runserver`

## API documentation

The service exposes end-points to upload an image and get a uniqe identifier for it; to list all images; and to get a specific image by its unique identifier. 

The API can be explored by pointing a browser to `http://localhost:8000/`

### Store a new image

To store a new image (e.g. from a file called `img.jpg`), make a POST request to the `/images/` endpoint, like this:

    $ curl --request POST -F raw_image=@img.jpg localhost:8000/images/

This returns a JSON document with the unique identifier of the image, plus direct links to download, e.g.: 

    {
      "uuid":"fMTvugHtB6i4k2josBuSXK",
      "raw_image": {
        "thumbnail":"http://localhost:8000/media/__sized__/image_data/img_GV9JEPt-thumbnail-100x100-70.jpg",
        "medium_square_crop":"http://localhost:8000/media/__sized__/image_data/img_GV9JEPt-crop-c0-5__0-5-400x400-70.jpg",
        "full_size":"http://localhost:8000/media/image_data/img_GV9JEPt.jpg",
        "small_square_crop":"http://localhost:8000/media/__sized__/image_data/img_GV9JEPt-crop-c0-5__0-5-50x50-70.jpg"
      }
    }

### List existing images

To get a list of the currently stored images, send a GET request to the `/images/` endpoint:

    $ curl localhost:8000/images/

This returns a JSON list of documents, similar to the above, describing each stored image and its unique identifier. 

### Retreiving an image by identifier

You can get the links for a specific image if you know its unique identifier by a simple GET request like:

    $ curl localhost:8000/images/fMTvugHtB6i4k2josBuSXK/

You can then follow the `full_size` link to download the original image. 
