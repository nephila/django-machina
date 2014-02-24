# -*- coding: utf-8 -*-

# Standard library imports
from __future__ import unicode_literals

# Third party imports
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

# Local application / specific library imports
from machina.core.compat import AUTH_USER_MODEL
from machina.core.loading import get_class

ForumReadTrackManager = get_class('tracking.managers', 'ForumReadTrackManager')


@python_2_unicode_compatible
class AbstractForumReadTrack(models.Model):
    """
    Represents a track which records which forums have been read by a given user.
    """
    user = models.ForeignKey(AUTH_USER_MODEL, related_name='forum_tracks', verbose_name=_('User'))
    forum = models.ForeignKey('forum.Forum', verbose_name=_('Forum'), related_name='tracks')
    mark_time = models.DateTimeField(auto_now=True)

    objects = ForumReadTrackManager()

    class Meta:
        abstract = True
        unique_together = ['user', 'forum', ]
        verbose_name = _('Forum track')
        verbose_name_plural = _('Forum tracks')
        app_label = 'tracking'

    def __str__(self):
        return '{} - {}'.format(self.user, self.forum)


@python_2_unicode_compatible
class AbstractTopicReadTrack(models.Model):
    """
    Represents a track which records which topics have been read by a given user.
    """
    user = models.ForeignKey(AUTH_USER_MODEL, related_name='topic_tracks', verbose_name=_('User'))
    topic = models.ForeignKey('conversation.Topic', verbose_name=_('Topic'), related_name='tracks')
    mark_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        unique_together = ['user', 'topic', ]
        verbose_name = _('Topic track')
        verbose_name_plural = _('Topic tracks')
        app_label = 'tracking'

    def __str__(self):
        return '{} - {}'.format(self.user, self.topic)
