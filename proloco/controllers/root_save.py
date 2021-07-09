# -*- coding: utf-8 -*-
"""Main Controller"""
import requests
from tg import expose, flash, require, url, lurl
from tg import request, redirect, tmpl_context
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg.exceptions import HTTPFound
from tg import predicates
from proloco import model
from proloco.controllers.secure import SecureController
from proloco.flask_upload_files import allowed_file
from proloco.model import DBSession
from tgext.admin.tgadminconfig import BootstrapTGAdminConfig as TGAdminConfig
from tgext.admin.controller import AdminController

from proloco.lib.base import BaseController
from proloco.controllers.error import ErrorController
from proloco.Connect import Connect
import requests
import sys
import os
import tempfile
import flask
# Python2
# import StringIO
LLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
from io import StringIO
from werkzeug.utils import secure_filename
__all__ = ['RootController']

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
class RootController(BaseController):
    """
    The root controller for the proloco application.

    All the other controllers and WSGI applications should be mounted on this
    controller. For example::

        panel = ControlPanelController()
        another_app = AnotherWSGIApplication()

    Keep in mind that WSGI applications shouldn't be mounted directly: They
    must be wrapped around with :class:`tg.controllers.WSGIAppController`.

    """
    secc = SecureController()
    admin = AdminController(model, DBSession, config_type=TGAdminConfig)

    error = ErrorController()

    def _before(self, *args, **kw):
        tmpl_context.project_name = "proloco"

    @expose('proloco.templates.master')
    def index(self):
        """Handle the front-page."""
        return dict(page='master', pagina=Connect.body("", "index"), luogo="index")
    @expose('proloco.templates.about')
    def about(self):
        """Handle the 'about' page."""
        return dict(page='about')

    @expose('proloco.templates.environ')
    def environ(self):
        """This method showcases TG's access to the wsgi environment."""
        return dict(page='environ', environment=request.environ)

    @expose('proloco.templates.data')
    @expose('json')
    def data(self, **kw):
        """
        This method showcases how you can use the same controller
        for a data page and a display page.
        """
        return dict(page='data', params=kw)
    @expose('proloco.templates.index')
    @require(predicates.has_permission('manage', msg=l_('Only for managers')))
    def manage_permission_only(self, **kw):
        """Illustrate how a page for managers only works."""
        return dict(page='managers stuff')

    @expose('proloco.templates.index')
    @require(predicates.is_user('editor', msg=l_('Only for the editor')))
    def editor_user_only(self, **kw):
        """Illustrate how a page exclusive for the editor works."""
        return dict(page='editor stuff')

    @expose('proloco.templates.login')
    def login(self, came_from=lurl('/'), failure=None, login=''):
        """Start the user login."""
        if failure is not None:
            if failure == 'user-not-found':
                flash(_('User not found'), 'error')
            elif failure == 'invalid-password':
                flash(_('Invalid Password'), 'error')

        login_counter = request.environ.get('repoze.who.logins', 0)
        if failure is None and login_counter > 0:
            flash(_('Wrong credentials'), 'warning')

        return dict(page='login', login_counter=str(login_counter),
                    came_from=came_from, login=login)

    @expose()
    def post_login(self, came_from=lurl('/')):
        """
        Redirect the user to the initially requested page on successful
        authentication or redirect her back to the login page if login failed.

        """
        if not request.identity:
            login_counter = request.environ.get('repoze.who.logins', 0) + 1
            redirect('/login',
                     params=dict(came_from=came_from, __logins=login_counter))
        userid = request.identity['repoze.who.userid']
        flash(_('Welcome back, %s!') % userid)

        # Do not use tg.redirect with tg.url as it will add the mountpoint
        # of the application twice.
        return HTTPFound(location=came_from)

    @expose()
    def post_logout(self, came_from=lurl('/')):
        """
        Redirect the user to the initially requested page on logout and say
        goodbye as well.

        """
        flash(_('We hope to see you soon!'))
        return HTTPFound(location=came_from)

    @expose('proloco.templates.home')
    def home(self):
        return dict(page='home')

    @expose('proloco.templates.nav')
    def menu(self):
        return dict(page='nav', pagina=Connect.body("", "mugello"), luogo="sanpiero")

    @expose('proloco.templates.master')
    def mugello(self):
        """Handle the front-page."""
        return dict(page='master', pagina=Connect.body("", "mugello"), luogo="mugello")

    @expose('proloco.templates.master')
    def sanpiero(self):
        """Handle the front-page."""
        return dict(page='master', pagina=Connect.body("", "sanpiero"), luogo="sanpiero")

    @expose('proloco.templates.master')
    def chisiamo(self):
        """Handle the front-page."""
        return dict(page='master', pagina=Connect.body("", "chisiamo"), luogo="chisiamo")

    @expose('proloco.templates.nivo')
    def slide(self, luogo):
        """Handle the front-page."""
        return dict(page='nivo', luogo=luogo)

    @expose('proloco.templates.manifesta')
    def locura(self):
        """Handle the front-page."""
        return dict(page='manifesta', pagina=Connect.body("", "sanpiero"), manifestazione="locura")

    @expose('proloco.templates.manifesta')
    def mercanzie(self):
        """Handle the front-page."""
        return dict(page='manifesta', pagina=Connect.body("", "sanpiero"), manifestazione="mercanzie")

    @expose('proloco.templates.news-slider')
    def news(self):
        """Handle the front-page."""
        return dict(page='news-slider', pagina=Connect.body("", "sanpiero"), manifestazione="news")

    @expose('proloco.templates.news')
    def NEWS(self):
        """Handle the front-page."""
        return dict(page='news', pagina=Connect.body("", "sanpiero"), manifestazione="news")

    @expose('proloco.templates.news_one')
    def news_one(self, titolo,id):
        """Handle the front-page."""
        return dict(page='news_one', pagina=Connect.body("", "sanpiero"), titolo=titolo, id=id)

    @expose('proloco.templates.ins_menu')
    def ins_menu(self):
        """Handle the front-page."""
        return dict(page='ins_menu', pagina=Connect.body("", "sanpiero"))


    @expose('proloco.templates.upload')
    def upload(self):
        """Handle the front-page."""
        return dict(page='upload', pagina=Connect.body("", "sanpiero"))

    @expose('proloco.templates.upload_form')
    def upload_form(self):

        return dict(page='upload_form', pagina=Connect.body("", "sanpiero"))

    @expose()
    def save(self,filename):

        with open(filename, "wb") as f:
            reached_end = False
            while not reached_end:



                    sys.stdout.write(".")
                    sys.stdout.flush()
                    # the idea behind this chunked upload is that large content could be persisted
                    # somewhere besides the container: S3, NFS, etc...
                    # So we use a container with minimal mem/disk, that can handle large files
                    #
                    # f.write(chunk)
                    # f.flush()
                    # print("wrote chunk of {}".format(len(chunk)))




print("")




def add_flash_message(msg):
    """Provides message to end user in browser"""
    print(msg)
    flask.flash(msg)

# from console it is the standard '__main__', but from docker flask it is 'main'
if __name__ == "__main__" or __name__ == "main":

    # docker flask image
    if __name__ == "main":
        if not os.getenv("TEMP_DIR") is None:
            if os.path.isdir(os.getenv("TEMP_DIR")):
              print("Overriding tempdir for docker image")
              tempfile.tempdir = os.getenv("TEMP_DIR")
    print("tempdir: " + tempfile.gettempdir())

    # Below error if MAX_CONTENT_LENGTH is exceeded by upload
    # [error] 11#11: *1 readv() failed (104: Connection reset by peer) while reading upstream
    #app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100MB limit

    # secret key used for flask.flash messages


    # docker flask uwsgi starts itself


