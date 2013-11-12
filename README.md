## Python Bottle Framework Scaffold for Google App Engine

A scaffold for building Python applications on Google App Engine with the
[Bottle micro framework](http://bottlepy.org) version 0.11.6

This scaffold is targeted at web applications, but can easily be
modified for other use cases.  A directory structure is included:

* code that runs on the server is under server/ and includes a MVC structure
  that separates controllers, models, and views into subdirectories.
* code that runs in the browser is under client/ and includes images and
  scripts. Add you favorite client side framework here.

See our other [Google Cloud Platform github
repos](https://github.com/GoogleCloudPlatform) for sample applications and
scaffolding for other python frameworks and use cases.

## Run Locally
1. Install the [App Engine Python SDK](https://developers.google.com/appengine/downloads).
See the README file for directions. You'll need python 2.7 and [pip 1.4 or later](http://www.pip-installer.org/en/latest/installing.html) installed too.

2. Clone this repo with

   ```
   git clone <project URL>
   ```
3. Install dependencies in the project's server/lib directory - App Engine
   can only import libraries from inside your project directory.

   ```
   cd <project_directory>
   pip install -r requirements.txt -t server/lib
   ```
4. Run this project locally from the command line:

   ```
   dev_appserver.py <projectDirectory>
   ```

See the output in your browser at [http://localhost:8080/RESOURCE_NAME/1](http://localhost:8080/RESOURCE_NAME/1)

See [the development server documentation](https://developers.google.com/appengine/docs/python/tools/devserver)
for options when running dev_appserver.

## Deploy
To deploy the application:

1. Use the [Admin Console](https://appengine.google.com) to create an app and
   get the project/app id. (App id and project id are identical)
1. [Deploy the
   application](https://developers.google.com/appengine/docs/python/tools/uploadinganapp) with

```
appcfg.py -A <your-project-id> --oauth2 update <projectDirectory>
```
or use the App Engine Launcher.
1. Congratulations! Your application is now live at your-project-id.appspot.com

## Next Steps
This scaffold includes TODO markers you can search for to determine some of the
basic areas you will want to customize.

### Relational Databases and Datastore
To add persistence to your models, use
[NDB](https://developers.google.com/appengine/docs/python/ndb/) for
scale.  Consider
[CloudSQL](https://developers.google.com/appengine/docs/python/cloud-sql) if you need a
relational database.

### Installing Libraries
See the [Third party
libraries](https://developers.google.com/appengine/docs/python/tools/libraries27)
page for libraries that are already included in the SDK.  To include SDK
libraries, add them in your app.yaml file. Other than libraries included in
the SDK, only pure python libraries may be added to an App Engine project.

### Feedback
Star this repo if you found it useful. Use the github issue tracker to give
feedback on this repo and to ask for scaffolds for other use cases.

## Contributing changes
See [CONTRIB.md](CONTRIB.md)

## Licensing
See [LICENSE](LICENSE)

## Author
Logan Henriquez
