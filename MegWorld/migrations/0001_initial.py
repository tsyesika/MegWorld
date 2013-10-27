# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Section'
        db.create_table(u'MegWorld_section', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('posted', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'MegWorld', ['Section'])

        # Adding model 'Page'
        db.create_table(u'MegWorld_page', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'MegWorld', ['Page'])

        # Adding M2M table for field sections on 'Page'
        m2m_table_name = db.shorten_name(u'MegWorld_page_sections')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('page', models.ForeignKey(orm[u'MegWorld.page'], null=False)),
            ('section', models.ForeignKey(orm[u'MegWorld.section'], null=False))
        ))
        db.create_unique(m2m_table_name, ['page_id', 'section_id'])

        # Adding model 'NewsItem'
        db.create_table(u'MegWorld_newsitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('posted', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'MegWorld', ['NewsItem'])

        # Adding model 'User'
        db.create_table(u'MegWorld_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('realname', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('ident', self.gf('django.db.models.fields.CharField')(max_length=75)),
        ))
        db.send_create_signal(u'MegWorld', ['User'])

        # Adding model 'ServerStatus'
        db.create_table(u'MegWorld_serverstatus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('server', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('ssl', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ipv6', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('online', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'MegWorld', ['ServerStatus'])

        # Adding model 'Comment'
        db.create_table(u'MegWorld_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('poster', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MegWorld.User'])),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'MegWorld', ['Comment'])

        # Adding model 'Status'
        db.create_table(u'MegWorld_status', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
        ))
        db.send_create_signal(u'MegWorld', ['Status'])

        # Adding model 'Ticket'
        db.create_table(u'MegWorld_ticket', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MegWorld.Status'], null=True, blank=True)),
            ('reporter', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='reporter', null=True, to=orm['MegWorld.User'])),
            ('posted', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('assigned', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='assigned', null=True, to=orm['MegWorld.User'])),
        ))
        db.send_create_signal(u'MegWorld', ['Ticket'])

        # Adding M2M table for field comments on 'Ticket'
        m2m_table_name = db.shorten_name(u'MegWorld_ticket_comments')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ticket', models.ForeignKey(orm[u'MegWorld.ticket'], null=False)),
            ('comment', models.ForeignKey(orm[u'MegWorld.comment'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ticket_id', 'comment_id'])


    def backwards(self, orm):
        # Deleting model 'Section'
        db.delete_table(u'MegWorld_section')

        # Deleting model 'Page'
        db.delete_table(u'MegWorld_page')

        # Removing M2M table for field sections on 'Page'
        db.delete_table(db.shorten_name(u'MegWorld_page_sections'))

        # Deleting model 'NewsItem'
        db.delete_table(u'MegWorld_newsitem')

        # Deleting model 'User'
        db.delete_table(u'MegWorld_user')

        # Deleting model 'ServerStatus'
        db.delete_table(u'MegWorld_serverstatus')

        # Deleting model 'Comment'
        db.delete_table(u'MegWorld_comment')

        # Deleting model 'Status'
        db.delete_table(u'MegWorld_status')

        # Deleting model 'Ticket'
        db.delete_table(u'MegWorld_ticket')

        # Removing M2M table for field comments on 'Ticket'
        db.delete_table(db.shorten_name(u'MegWorld_ticket_comments'))


    models = {
        u'MegWorld.comment': {
            'Meta': {'object_name': 'Comment'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poster': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MegWorld.User']"})
        },
        u'MegWorld.newsitem': {
            'Meta': {'object_name': 'NewsItem'},
            'body': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posted': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'MegWorld.page': {
            'Meta': {'object_name': 'Page'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sections': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['MegWorld.Section']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'MegWorld.section': {
            'Meta': {'object_name': 'Section'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'body': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'posted': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'MegWorld.serverstatus': {
            'Meta': {'object_name': 'ServerStatus'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ipv6': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'online': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'server': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'ssl': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'MegWorld.status': {
            'Meta': {'object_name': 'Status'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        u'MegWorld.ticket': {
            'Meta': {'object_name': 'Ticket'},
            'assigned': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'assigned'", 'null': 'True', 'to': u"orm['MegWorld.User']"}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'comments': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['MegWorld.Comment']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posted': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'reporter': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'reporter'", 'null': 'True', 'to': u"orm['MegWorld.User']"}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MegWorld.Status']", 'null': 'True', 'blank': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'MegWorld.user': {
            'Meta': {'object_name': 'User'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ident': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'realname': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['MegWorld']