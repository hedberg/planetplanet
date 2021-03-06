##############################################################################
# Copyright (c) 2010 Hajime Nakagami <nakagami@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.
from django.conf.urls.defaults import *
from django.conf import settings
from feeds import RecentFeed, AtomRecentFeed
import os
feeds = {
    'rss.xml' : RecentFeed,
    'atom.xml' : AtomRecentFeed,
}

urlpatterns = patterns('',
    (r'^$', 'planetplanet.planet.views.index'),
    (r'^(.*\.xml)$', 'django.contrib.syndication.views.feed',
            {'feed_dict': feeds}),
)
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^css/(.*\.css)$', 'django.views.static.serve', {'document_root':os.path.join(os.getcwd(), 'static/planet/css')}),
        (r'^images/(.*)$', 'django.views.static.serve', {'document_root':os.path.join(os.getcwd(), 'static/planet/images')}),
    )
