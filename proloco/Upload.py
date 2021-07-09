#!/usr/bin/env python
"""
Flask application that receives uploaded content from browser

"""
import sys
import os
import tempfile
import flask
# Python2
# import StringIO
from io import StringIO
from werkzeug.utils import secure_filename

# whitelist of file extensions
from proloco.flask_upload_files import allowed_file, app

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


class Upload:

    def handle_oserror(oserror):

        response = flask.jsonify({"message":StringIO(str(oserror)).getvalue()})
        response.status_code = 500
        return response

    def allowed_file(filename):

        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def entry_point(self):

        return flask.render_template('master.xhtml',  tempdir=tempfile.gettempdir())


    def flask(self):
        """Handle the front-page."""
        return flask.render_template('master.xhtml',  tempdir=tempfile.gettempdir())

    def upload_form(self):

        return flask.render_template('upload_form.html')

    def allowed_file(filename):
        """ whitelists file extensions for security reasons """
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def single_upload_chunked(filename):
        app.config['CHUNK_SIZE'] = 4096
        chunk_size = app.config['CHUNK_SIZE']
        if "Content-Length" not in flask.request.headers:
            add_flash_message("did not sense Content-Length in headers")
            return flask.redirect(flask.url_for("upload_form"))

        if filename is None or filename == '':
            add_flash_message("did not sense filename in form action")
            return flask.redirect(flask.url_for("upload_form"))

        if not allowed_file(filename):
            add_flash_message("not going to process file with extension " + filename)
            return flask.redirect(flask.url_for("upload_form"))

        print("Total Content-Length: " + flask.request.headers['Content-Length'])
        fileFullPath = os.path.join(app.config['UPLOAD_FOLDER'], filename)


        try:
            with open(fileFullPath, "wb") as f:
                reached_end = False
                while not reached_end:
                    chunk = flask.request.stream.read(chunk_size)
                    if len(chunk) == 0:
                        reached_end = True
                    else:
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        # the idea behind this chunked upload is that large content could be persisted
                        # somewhere besides the container: S3, NFS, etc...
                        # So we use a container with minimal mem/disk, that can handle large files
                        #
                        # f.write(chunk)
                        # f.flush()
                        # print("wrote chunk of {}".format(len(chunk)))
        except OSError as e:
            add_flash_message("ERROR writing file " + filename + " to disk: " + StringIO(str(e)).getvalue())
            return flask.redirect(flask.url_for("upload_form"))

        print("")
        add_flash_message("SUCCESS uploading single file: " + filename)
        return flask.redirect(flask.url_for("upload_form"))

def add_flash_message(msg):
    """Provides message to end user in browser"""
    print(msg)
    flask.flash(msg)
